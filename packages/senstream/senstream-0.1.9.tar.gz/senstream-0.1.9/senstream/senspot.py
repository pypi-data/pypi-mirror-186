import mysql.connector
from senstream.resensys import Resensys
from datetime import datetime,timedelta
import pandas as pd

# 1. Handles checking senspot credentials, info, calibrations
# 2. Handles checking the routing parameters
# 3. Contains some db helper function for handling dataformat to format name translation
# 4. timestream: Used to pull time series for a single SenSpot for different time periods
# 5. Sync calibration coefficients across systems (senscope and webportal); includes temperature compensation

class SenSpot(Resensys):

    def __init__(self,parent,did):
        super().__init__(parent.username, parent.password)
        self.conn = parent.conn
        self.did = did
    
    def getName(self):
        # create a db cursor
        cursor = self.conn.cursor()
        # define the query to the db
        query = f"SELECT TTL FROM `{self.username}`.`Info` WHERE `DID`='{self.did}'"
        cursor.execute(query)
        site = cursor.fetchall()[0][0]
        return site

    def getSite(self):
        # create a db cursor
        cursor = self.conn.cursor()
        # define the query to the db
        query = f"SELECT SID FROM `{self.username}`.`Info` WHERE `DID`='{self.did}'"
        cursor.execute(query)
        site = cursor.fetchall()[0][0]
        return site
    
    def getLocAddr(self):
        sid = self.getSite().replace("-","")
        table = "Data."+self.did.replace("-","")+"."+sid+".3003"
        # create a db cursor
        cursor = self.conn.cursor()
        # define the query to the db
        query = f"SELECT Optional FROM `Data_{sid}`.`{table}` ORDER BY Time DESC LIMIT 1"
        cursor.execute(query)
        la = int(cursor.fetchall()[0][0]/1001)
        return la
    
    def getQuantities(self,translate=True):
        cursor = self.conn.cursor()
        df_query = ("""SELECT TRIM(LEADING '0' FROM M1) AS M1,
                        TRIM(LEADING '0' FROM M2) AS M2,
                        TRIM(LEADING '0' FROM M3) AS M3,
                        TRIM(LEADING '0' FROM M4) AS M4,
                        TRIM(LEADING '0' FROM M5) AS M5,
                        TRIM(LEADING '0' FROM M6) AS M6,
                        TRIM(LEADING '0' FROM M7) AS M7,
                        TRIM(LEADING '0' FROM M8) AS M8,
                        TRIM(LEADING '0' FROM M9) AS M9,
                        TRIM(LEADING '0' FROM M10) AS M10
                        FROM `%s`.Info WHERE DID = '%s'""" % (self.username,self.did))
        cursor.execute(df_query)
        dataformats = cursor.fetchall()

        non_empty = []
        for i in range(len(dataformats[0])):
            if dataformats[0][i] != '':
                non_empty.append(dataformats[0][i])

        if translate:
            non_empty = [self.get_quantity_name(non_empty[i]) for i in range(len(non_empty))]
        return non_empty

    def get_quantity_name(self,dataformat):
        cnx = mysql.connector.connect(user='regUser',password='iZge8097^ds6',
                            host='resensys.net',use_pure=True)
        c = cnx.cursor()
        query = ("SELECT Name FROM `RegInfo`.`quantityBank` WHERE `DataFormat` ='%s'"%(dataformat))
        c.execute(query)
        quantity_name = c.fetchall()
        cnx.close()
        return quantity_name[0][0]

    def getDataFormat(self,df_name):
        cnx = mysql.connector.connect(user='regUser',password='iZge8097^ds6',
                            host='resensys.net',use_pure=True)
        c = cnx.cursor()
        query = ("SELECT DataFormat,Unit FROM `RegInfo`.`quantityBank` WHERE `Name` ='%s'"%(df_name))
        c.execute(query)
        quantity_name = c.fetchall()
        cnx.close()
        return quantity_name[0][0],quantity_name[0][1]

    def getCalibration(self,df_name=""):
        cursor = self.conn.cursor()
        df_query = ("""SELECT TRIM(LEADING '0' FROM M1) AS M1,
                        TRIM(LEADING '0' FROM M2) AS M2,
                        TRIM(LEADING '0' FROM M3) AS M3,
                        TRIM(LEADING '0' FROM M4) AS M4,
                        TRIM(LEADING '0' FROM M5) AS M5,
                        TRIM(LEADING '0' FROM M6) AS M6,
                        TRIM(LEADING '0' FROM M7) AS M7,
                        TRIM(LEADING '0' FROM M8) AS M8,
                        TRIM(LEADING '0' FROM M9) AS M9,
                        TRIM(LEADING '0' FROM M10) AS M10
                        FROM `%s`.`Info` WHERE DID = '%s'""" % (self.username,self.did))
        cursor.execute(df_query)
        dataformats = cursor.fetchall()[0]

        dataformat,unit = self.getDataFormat(df_name)

        index = 1
        for i in range(len(dataformats)):
            if dataformats[i] == dataformat:
                index = i+1

        coeff_col,offset_col = "COF"+str(index),"DOF"+str(index)
        coeff_query = f"SELECT `{coeff_col}`,`{offset_col}` FROM `{self.username}`.`Info` WHERE `DID` = '{self.did}'"
        cursor.execute(coeff_query)
        coeffs = cursor.fetchall()[0]

        return coeffs[0],coeffs[1],unit

    def getCoefficients(self):
        coefficients = {}
        quantities = self.getQuantities()
        for quantity in quantities:
            coeff,offset,unit = self.getCalibration(quantity)
            coefficients[str(quantity)] = {"coefficient":coeff,"offset":offset,"unit":unit}
        return coefficients

    def getDeviceInfo(self,properties=[]):
        device_info = {}
        if "Name" in properties:
            device_info["Name"] = self.getName()
        if "DID" in properties:
            device_info["DID"] = self.did
        if "SID" in properties:
            device_info["SID"] = self.getSite()
        if "LocAddr" in properties:
            device_info["LocAddr"] = self.getLocAddr()
        if "Quantities" in properties:
            device_info["Quantities"] = self.getCoefficients()
        if len(properties) == 0:
            device_info["Name"] = self.getName()
            device_info["DID"] = self.did
            device_info["SID"] = self.getSite()
            device_info["LocAddr"] = self.getLocAddr()
            device_info["Quantities"] = self.getCoefficients()
        return device_info

    def timeStream(self,df_name,time=[],t_s="",t_e="",calibrate=True):
        did = str(self.did).replace('-',"")
        sid = str(self.getSite()).replace('-',"")
        db = "Data_"+str(sid)
        DF,unit = self.getDataFormat(df_name)
        table = db+"."+"`Data."+did+"."+sid+"."+DF+"`"

        t_end = datetime.utcnow()
        t_start = t_end - timedelta(hours=24)

        # define options for time window
        if "1hour" in time:
            t_start = t_end - timedelta(hours=1)
        elif "2hour" in time:
            t_start = t_end - timedelta(hours=2)
        elif "6hour" in time:
            t_start = t_end - timedelta(hours=6)
        elif "12hour" in time:
            t_start = t_end - timedelta(hours=12)
        elif "24hour" in time or "1day" in time:
            t_start = t_end - timedelta(hours=24)
        elif "48hour" in time or "2day" in time:
            t_start = t_end - timedelta(hours=48)
        elif "1week" in time:
            t_start = t_end - timedelta(weeks=1)
        elif "2week" in time:
            t_start = t_end - timedelta(weeks=2)
        elif "4week" in time or "1month" in time:
            t_start = t_end - timedelta(weeks=4)
        elif "6month" in time:
            t_start = t_end - timedelta(months=6)
        elif "12month" in time or "1year" in time:
            t_start = t_end - timedelta(months=12)
        elif "2year" in time:
            t_start = t_end - timedelta(years=2)
        else:
            t_start = t_end - timedelta(hours=24)

        try:
            if "custom" in time:
                t_start,t_end = t_s,t_e
        except Exception as e:
            print("Please check that time = ['custom']")
        cursor = self.conn.cursor()

        query = ("SELECT * FROM %s WHERE (Time >= '%s' AND Time <= '%s')" % (table,t_start,t_end))
        # Execute SQL query
        cursor.execute(query)
        # Record all instances that match query to records
        records = cursor.fetchall()
        # Collect the name of each of the table fields
        field_names = [i[0] for i in cursor.description]
        # Convert the records to a dataframe and filter rows by start and end time
        data_df = pd.DataFrame(records,columns=field_names)
        
        # Set added time to a TimeDelta object
        data_df['Time Added'] = pd.to_timedelta(data_df['Optional'],'milli')
        data_df['Time'] = pd.to_datetime(data_df['Time'])
        # Subtract the retarded time from the base time
        data_df['Time'] = data_df['Time'] - data_df['Time Added']
        # Drop the temporary 'Time Added' feature from data_df
        data_df = data_df.drop('Time Added',axis=1)                   
        
        # apply flip threshold if internal temperature measurement
        if (DF == '3002'):
            for i in range(len(data_df)):
                temp = data_df.Value[i]
                if temp > 175:
                    data_df.Value[i] = temp-256

        # Apply coefficients to the filtered data
        if calibrate:
            coeff,offset,unit = self.getCalibration(df_name)
            data_df['Value'] = coeff*(data_df['Value']-offset)
        
        return data_df.iloc[:,[0,2]].drop_duplicates().reset_index(drop=True)
