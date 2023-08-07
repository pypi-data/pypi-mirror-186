import mysql.connector
from senstream.resensys import Resensys
import pandas as pd
import requests
import os
import re
from datetime import datetime
from senstream.senscope import *


class ServerTool(Resensys):
    def __init__(self,parent):
        # if ('Windows' in platform.system()):
        #     self._configurationFilePath = "./conf.json"
        #     self._basedir = "./"
        # else:
        #     self._configurationFilePath = "/home/betta/AlertServ/conf.json"
        #     self._basedir = "/home/betta/AlertServ"

        # with open(self._configurationFilePath, 'r') as infile:
        #     self._configFile = json.load(infile)
        #     # print(self._configFile)

        # self._connInfoPort = self._configFile['DBPort']
        # self._connInfoHost = self._configFile['DBHost']
        # self._connInfoUsername = self._configFile['DBUsername']
        # self._connInfoPassword = self._configFile['DBPassword']
        # self._connInfoDBName = self._configFile['DBName']
        # self._connInfoLastCheckTime = self._configFile['lastTransmission']

        super().__init__(parent.username, parent.password)
        self.conn = parent.conn


        self.SIDre = re.compile("[0-9a-fA-F]{2}-[0-9a-fA-F]{2}")
    
    def _send_alert_message(self, emailAddr, subject, mailContent, imgName=[], imgDir=""):
        if imgName != []:
            return requests.post(
                "https://api.mailgun.net/v3/alert.resensys.com/messages",
                auth=("api", "eb236b2e3140053deda2ae9c6ce8f48f-f8b3d330-62ad6a31"),
                files=[("attachment", (imgName[0], open(imgName[0], 'rb'))),
                        ],
                data={"from": "Resensys Replication Server Alert <alert@alert.resensys.com>",
                        "to": emailAddr,
                        "subject": subject,
                        "text": mailContent
                        })
        else:
            return requests.post(
                "https://api.mailgun.net/v3/alert.resensys.com/messages",
                auth=("api", "eb236b2e3140053deda2ae9c6ce8f48f-f8b3d330-62ad6a31"),
                data={"from": "Resensys 1D-Alert Service <alert@alert.resensys.com>",
                        "to": emailAddr,
                        "subject": subject,
                        "text": mailContent
                        })
    # End Fxn

    def CheckActiveSeniMax(self):
        # self.conn = mysql.connector.connect(user=self._connInfoUsername, host=self._connInfoHost, password=self._connInfoPassword, port=self._connInfoPort)
        cursor = self.conn.cursor()
        cursor.execute(
            "SELECT DID,SID FROM `admin`.Info where DID like '00-00-%';")
        usrResultRows = cursor.fetchall()

        if (usrResultRows is not None):

            for usrRecord in usrResultRows:
                resultRows = []
                gatewayDID = str(usrRecord[0]).replace("-", "")
                gatewaySID = str(usrRecord[1]).replace("-", "")
                datetimeStart = "SUBTIME(UTC_TIMESTAMP(),\'500:00:00\')"
                datetimeEnd = "UTC_TIMESTAMP()"
                #print(gatewayDID, gatewaySID)
                query = f"SELECT * FROM `Data_{gatewaySID}`.`Data.{gatewayDID}.{gatewaySID}.3003` where Time between {datetimeStart} and {datetimeEnd} order by Time desc limit 10;"
                #print(query)
                gatewayActivated = False
                try:
                    cursor.execute(query)
                    resultRows = cursor.fetchall()
                except:
                    pass
                
                if (len(resultRows) > 0 ):
                    print(gatewayDID,"| Active | Last TX @ ", resultRows[0][0])
                else:
                    print(gatewayDID,"| OFFLINE")
        else:
            print("ERROR!!!!")
    
    def CheckReplicationActivity(self):
        self.conn = mysql.connector.connect(user='root', host='gamma-srvr.coxrusc9yue4.us-east-1.rds.amazonaws.com', password='31163116', port='3306')
        cursor = self.conn.cursor()
        server_running = True
        log_path = os.path.join(self._basedir, "Log/Replicate_Server_Log_file.txt")
        query = f"SHOW SLAVE STATUS;"
        try:
            result_DF = read_cursor_to_DF_mysqlconnector(cursor, query)

            
            whole_msg = result_DF.to_string()
            print(whole_msg)
            for row in result_DF.itertuples():
                slave_sql_running = getattr(row, "Slave_SQL_Running")
                slave_IO_running = getattr(row, "Slave_IO_Running")
                error_msg = getattr(row, 'Last_Error')
            if slave_sql_running == "No":
                server_running = False

        except Exception as e:
            print(str(e))

        if not server_running:
            print("Send Email")
            email_addr = ["wadesthomas1@gmail.com", "mehdi@resensys.com"]
            subject = "The replication server run into an error!"
            mail_content = (f"The error info:\n{error_msg}\n"
                            f"UTC Time: {datetime.utcnow().strftime('%Y-%m-%d %H:%M:%S')}\n") + whole_msg + "\n"
            self._send_alert_message(email_addr, subject, mail_content)

            log_info = (mail_content + "_________________________\n")
        else:
            log_info = (f"Replication server running\n"
                        f"UTC Time: {datetime.utcnow().strftime('%Y-%m-%d %H:%M:%S')}\n"
                        f"_________________________\n")
        
        with open(log_path, 'a') as outfile:
                outfile.write(log_info)
    #  End of Check replication server activity

    def ZeroSensors(self, SID, DID, DF, T_start_utc, T_end_utc):
        # self.conn = mysql.connector.connect(user=self._connInfoUsername, host=self._connInfoHost, password=self._connInfoPassword, port=self._connInfoPort)
        cursor = self.conn.cursor()
        query = generate_data_query(DID, SID, DF, T_start_utc, T_end_utc, 1, 0, 0)
        result_DF = read_cursor_to_DF_mysqlconnector(cursor, query)
        if result_DF.empty:
            avg = 0
        else:
            data_ser = result_DF.iloc[:, 1]
            avg = round(data_ser.mean())
        print("Average:", avg)

    def add_site_to_user(self, acc_name, SID, acc_pswd="", mode=0, extra_criterion=""):
        """
        Args:
            acc_name: string,
            SID: string, XX-XX
            acc_pswd: string
            mode: int, mode 0-> insert Info, update quantitylist, add alertGen
                       mode 1-> insert Info, update quantitylist
                       mode 2-> insert Info, add alertGen
                       mode 3-> insert Info only
        """
        if self.SIDre.match(SID):
            # self.conn = mysql.connector.connect(user=self._connInfoUsername, host=self._connInfoHost, password=self._connInfoPassword, port=self._connInfoPort)
            cursor = self.conn.cursor()
            if acc_pswd=="":
                query_prep = f"select * from `{acc_name}`.Accounts limit 1;"
                result_DF = read_cursor_to_DF_mysqlconnector(cursor, query_prep)
                if not result_DF.empty:
                    acc_pswd = result_DF.loc[0, 'Password']
            
            query = (f"insert ignore into `{acc_name}`.Accounts (UserName,SID,SIDName,AccountType,LastLogin,Enable,Password,Email1,Email2,Email3,AirUpdateEn,LastUpdate,DongleIncluded,latitude,longtitude)"
                    f" select '{acc_name}',SID,SIDName,'Standard','2000-01-01 00:00:00',1,'{acc_pswd}','','','',0,'2000-01-01 00:00:00',0,0,0 from admin.Accounts where SID ='{SID}';")
            query2 = (f"insert ignore into `{acc_name}`.Info select * from `admin`.Info where `STT`=1 and SID='{SID}';")

            #print(query, "\n", query2)

            cursor.execute(query)
            print("Number of rows affected by statement : {}".format(cursor._rowcount))
            cursor.execute(query2)
            print("Number of rows affected by statement : {}".format(cursor._rowcount))
            cursor.commit()
            if mode != 2 and mode != 3:
                self.update_quantitylist(acc_name, "admin", SID=SID)
            if mode != 1 and mode != 3:
                self.insert_alert(acc_name, "admin", SID=SID)

    def update_quantitylist(self, acc_name, src_acc_name, SID="", extra_filter="", dbHandler=None):
        i = 1
        if self.SIDre.match(SID):
            extra_filter += f" and inf.SID='{SID}'"
        elif SID != "":
            print("Invalid SID!")
            return 1
        if dbHandler is None:
            # self.conn = mysql.connector.connect(user=self._connInfoUsername, host=self._connInfoHost, password=self._connInfoPassword, port=self._connInfoPort)
            cursor = self.conn.cursor()
        while i <= 10:
            query = (f"INSERT ignore INTO `{acc_name}`.`QuantityList`"
                     f"(`DID`,`DNAME`,`SID`,`SNAME`,`DTYPE`,`DATAFORMAT`,`QUANTITYNAME`,`UNIT`,`NUMBERFORMAT`,`NUMPRECISION`,`CALIBCOEF`,`CALIBDOFF`,`CALIBTEMPCOEF`,`SAMPLINGINTERVAL`,`THRLL`,`THRL`,`THRH`,`THRHH`,`DATETIMEFORMAT`,`SHOWTHR`,`APPLYOPTIONALOFFSET`,`EVENTDETTHR`,`ACTIVE`) "
                     f"select inf.`DID`,inf.`TTL`,inf.`SID`,acc.`SIDName`,inf.`TYP`,qtmp.`DATAFORMAT`,"
                     f"qtmp.`QUANTITYNAME`,qtmp.`UNIT`,qtmp.`NUMBERFORMAT`,qtmp.`NUMPRECISION`,inf.COF{i},inf.DOF{i},qtmp.`CALIBTEMPCOEF`,qtmp.`SAMPLINGINTERVAL`,qtmp.`THRLL`,qtmp.`THRL`,"
                     f"qtmp.`THRH`,qtmp.`THRHH`,qtmp.`DATETIMEFORMAT`,qtmp.`SHOWTHR`,qtmp.`APPLYOPTIONALOFFSET`,qtmp.`EVENTDETTHR`,qtmp.`Active` "
                     f"from `{src_acc_name}`.`Info` as inf inner join `Templates`.`Quantity_TMP` as qtmp inner join `{acc_name}`.Accounts as acc "
                     f"on acc.SID=inf.SID and TRIM(LEADING '0' FROM inf.M{i}) = qtmp.DATAFORMAT and inf.`STT`=1 {extra_filter} order by inf.`SID`, inf.`DID` asc;")
            cursor.execute(query)
            i = i+1
        
        self.conn.commit()

    def insert_alert(self, acc_name, src_acc_name, SID="", extra_filter="", dbHandler=None):
        i = 1
        if self.SIDre.match(SID):
            extra_filter += f" and inf.SID='{SID}'"
        elif SID != "":
            print("Invalid SID!")
            return 1
        if dbHandler is None:
            # self.conn = mysql.connector.connect(user=self._connInfoUsername, host=self._connInfoHost, password=self._connInfoPassword, port=self._connInfoPort)
            cursor = self.conn.cursor()
        while i <= 10:
            query = (f"INSERT ignore INTO `{acc_name}`.`AlertGen` "
                    f"(`AlertType`,"
                    f"`AlertStatus`,"
                    f"`AlertInterval`,"
                    f"`DeviceID1`,"
                    f"`SiteID1`,"
                    f"`Quantity1`,"
                    f"`Offset1`,"
                    f"`Coef1`,"
                    f"`TempOffset1`,"
                    f"`TempCoef1`,"
                    f"`WARNING_LL_1`,`WARNING_LL_2`,`WARNING_HL_1`,`WARNING_HL_2`,`WARNING_HH_1`,`WARNING_HH_2`,`WARNING_LH_1`,`WARNING_LH_2`,"
                    f"`ALARM_LL_1`,`ALARM_LL_2`,`ALARM_HL_1`,`ALARM_HL_2`,`ALARM_HH_1`,`ALARM_HH_2`,`ALARM_LH_1`,`ALARM_LH_2`,"
                    f"`Activated`,`Quantity1Name`)"
                    f"SELECT 1,0,'12:00:00',inf.`DID`,inf.`SID`,qtmp.`DATAFORMAT`,inf.`DOF{i}`,inf.`COF{i}`,0,qtmp.`CALIBTEMPCOEF`, "
                    f"qtmp.`THRL`,qtmp.`THRL`,qtmp.`THRL`,qtmp.`THRL`, "
                    f"qtmp.`THRH`,qtmp.`THRH`,qtmp.`THRH`,qtmp.`THRH`, "
                    f"qtmp.`THRLL`,qtmp.`THRLL`,qtmp.`THRLL`,qtmp.`THRLL`, "
                    f"qtmp.`THRHH`,qtmp.`THRHH`,qtmp.`THRHH`,qtmp.`THRHH`, "
                    f"qtmp.`SHOWTHR`,qtmp.`QUANTITYNAME`"
                    f"from `{src_acc_name}`.`Info` as inf inner join `Templates`.`Quantity_TMP` as qtmp inner join `{acc_name}`.`Accounts` as acc "
                    f"on acc.SID = inf.SID and TRIM(LEADING '0' FROM inf.M{i}) = qtmp.DATAFORMAT and inf.`STT`=1 {extra_filter} order by inf.`SID`, inf.`DID` asc;")
            cursor.execute(query)
            i = i+1
        self.conn.commit()

    def insert_into_new_registration(self, acc_name, src_acc_name, SID="", extra_filter="", dbHandler=None):
        i = 1
        if self.SIDre.match(SID):
            extra_filter += f" and inf.SID='{SID}'"
        elif SID != "":
            print("Invalid SID!")
            return 1
        if dbHandler is None:
            # self.conn = mysql.connector.connect(user=self._connInfoUsername, host=self._connInfoHost, password=self._connInfoPassword, port=self._connInfoPort)
            cursor = self.conn.cursor()
        while i <= 10:
            query = (f"INSERT ignore INTO `RegInfo`.`registration`"
                f"(`DID`,`DNAME`,`SID`,`SNAME`,"
                f"`DTYPE`,`DATAFORMAT`,`QUANTITYNAME`,`UNIT`,"
                f"`NUMBERFORMAT`,`NUMPRECISION`,`CALIBCOEF`,`CALIBDOFF`,"
                f"`TEMPCALIBCOEF0`,`DATETIMEFORMAT`,`APPLYTEMPCOMP`,`SHOWABLE`,"
                f"`M`,`VERSION`)"
                f"select inf.`DID`,inf.`TTL`,inf.`SID`,acc.`SIDName`,"
                f"inf.`TYP`,qtmp.`DATAFORMAT`,qtmp.`NAME`,qtmp.`UNIT`,"
                f"qtmp.`Precision`,qtmp.`NUMPRECISION`,inf.`COF{i}`,inf.`DOF{i}`,"
                f"0,qtmp.`DATETIMEFORMAT`,'False',qtmp.`SHOWABLE`,"
                f"{i},`Version`"
                f"from `{acc_name}`.`Info` as inf "
                f"inner join `RegInfo`.`quantityBank` as qtmp "
                f"inner join `{acc_name}`.Accounts as acc "
                f"on acc.SID=inf.SID and TRIM(LEADING '0' FROM inf.M{i}) = qtmp.DATAFORMAT and inf.`STT`=1 where 1=1 {extra_filter} order by inf.`SID`, inf.`DID`, qtmp.`Version` desc;")
            cursor.execute(query)
            i = i+1
        self.conn.commit()

    def schema_setup(self,line,dbHandler=None):
        if dbHandler is None:
            # self.conn = mysql.connector.connect(user=self._connInfoUsername, host=self._connInfoHost, password=self._connInfoPassword, port=self._connInfoPort)
            cursor = self.conn.cursor()
        create_schema = f"CREATE SCHEMA IF NOT EXISTS `Data_{line.replace('-','')}`"
        cursor.execute(create_schema)
        self.conn.commit()
        create_volt_table = f"CREATE TABLE IF NOT EXISTS `Data_{line.replace('-','')}`.`Data.0000{line.replace('-','')}.{line.replace('-','')}.3003` (  `Time` timestamp NOT NULL DEFAULT CURRENT_TIMESTAMP,   `SeqNo` tinyint(1) unsigned DEFAULT NULL,   `Value` int(4) DEFAULT NULL,   `Optional` int(4) DEFAULT NULL,   KEY `time_index` (`Time`) ) ENGINE=MyISAM DEFAULT CHARSET=latin1;"
        cursor.execute(create_volt_table)
        self.conn.commit()
        add_new_data = f"INSERT INTO `Data_{line.replace('-','')}`.`Data.0000{line.replace('-','')}.{line.replace('-','')}.3003` (`Time`, `SeqNo`, `Value`, `Optional`) VALUES ('2017-10-12 14:56:56',0,0,0);"
        cursor.execute(add_new_data)
        self.conn.commit()
        create_sensors_table = f"CREATE TABLE IF NOT EXISTS sensors.`Data_{line.replace('-','')}` like sensors.Data_0104"
        cursor.execute(create_sensors_table)
        self.conn.commit()
        insert_into_admin = f"insert into admin.Accounts (`UserName`,`SID`,`SIDName`,`AccountType`,`LastLogin`,`Enable`,`Password`,`LastUpdate`,`Email1`,`Email2`,`Email3`,`latitude`,`longtitude`) VALUES('admin','{line}','{line}','Administrator',UTC_TIMESTAMP(),1,'t5epHatrufuspeKU',UTC_TIMESTAMP(),'thomas.wade@resensys.com','','',0,0);"
        cursor.execute(insert_into_admin)
        self.conn.commit()
    
    def grant_user_privileges(self,acc_name,SID,SNAME="",dbHandler=None):
        if SNAME == "":
            SNAME = SID
        if dbHandler is None:
            # self.conn = mysql.connector.connect(user=self._connInfoUsername, host=self._connInfoHost, password=self._connInfoPassword, port=self._connInfoPort)
            cursor = self.conn.cursor()
        query = f"INSERT IGNORE INTO `RegInfo`.`privilege` (`Username`, `SID`, `SNAME`, `Enable`, `Privilege`) VALUES ('{acc_name}', '{SID}', '{SID}', '1', '1');"
        cursor.execute(query)
        self.conn.commit()
    

    def connect_to_DB_server(self, username="", host="", password="", port=""):
        if username =="":
            username = self._connInfoUsername
        if host == "":
            host = self._connInfoHost
        if password == "":
            password = self._connInfoPassword
        if port == "":
            port = self._connInfoPort
        self.conn = mysql.connector.connect(user=username, host=host, password=password, port=port)
        return self.conn