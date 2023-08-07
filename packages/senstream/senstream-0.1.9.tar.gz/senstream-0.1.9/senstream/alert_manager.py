import mysql.connector
import server_tool
from senstream.resensys import Resensys
from senstream.senspot import SenSpot
import pandas as pd

# 1. Handles alert management configurations
# 2. Change the activity status of a user of the alert service
# 3. Pull the current static alert levels for a given device
# 4. Set new static alert levels per device-quantity pair
# 5. Defines an "alert trigger" which automatically sends an alert when a user-defined condition is met
# 6. Specify who will be recieving alerts (emails and mobile numbers)
# 7. Sync alerts across systems (sites, senscope, and webportal)

class AlertManager(Resensys):
    def __init__(self,parent):
        super().__init__(parent.username, parent.password)
        self.conn = parent.conn

    # check the current alert levels for all devices
    def alerts(self,senspot=None,format="json"):
        
        cursor = self.conn.cursor()
        
        if senspot is not None:
            # parse the senspot object
            query = f"SELECT DeviceID1 as DID,SiteID1 as SID,Quantity1 as DataFormat,Quantity1Name as QuantityName,Offset1 as Offset,Coef1 as Coeff,ALARM_LL_1 as AlarmLow,WARNING_LL_1 as WarningLow,WARNING_HH_1 as WarningHigh,ALARM_HH_1 as AlarmHigh FROM {self.username}.AlertGen WHERE DeviceID1 = '{senspot.did}';"
            cursor.execute(query)
            senspot_alerts = cursor.fetchall()
            field_names = [i[0] for i in cursor.description]

            if senspot_alerts is not None:
                if format == "json":
                    alerts_dict = {}
                    for count,result in enumerate(alert_levels):
                        alerts_dict[str(count)] = {field_names[i]:result[i] for i in range(len(field_names))}
                    return alerts_dict
                elif format == "dataframe":
                    return pd.DataFrame(senspot_alerts,columns=field_names)
            else:
                print("Account not registered alert service user.")

        else:
            query = f"SELECT DeviceID1 as DID,SiteID1 as SID,Quantity1 as DataFormat,Quantity1Name as QuantityName,Offset1 as Offset,Coef1 as Coeff,ALARM_LL_1 as AlarmLow,WARNING_LL_1 as WarningLow,WARNING_HH_1 as WarningHigh,ALARM_HH_1 as AlarmHigh FROM {self.username}.AlertGen;"
            cursor.execute(query)
            alert_levels = cursor.fetchall()
            field_names = [i[0] for i in cursor.description]

            if alert_levels is not None:
                if format == "json":
                    alerts_dict = {}
                    for count,result in enumerate(alert_levels):
                        alerts_dict[str(count)] = {field_names[i]:result[i] for i in range(len(field_names))}
                    return alerts_dict
                elif format == "dataframe":
                    return pd.DataFrame(alert_levels,columns=field_names)
            else:
                print("Account not registered alert service user.")
    
    # handle registration of a user for the alert service
    def register(self):
        # check to see if the user is alread registered in active users
        cnx = mysql.connector.connect(user='tom',password='Manhattan44joke#',
                            host='resensys.net',use_pure=True)
        c = cnx.cursor()
        # define the query to the db
        query = f"SELECT AlertActivated FROM admin.ActiveUsers WHERE Username = '{self.username}';"
        c.execute(query)
        alerts_active = c.fetchall()[0][0]

        if alerts_active == 2:
            print("Account is already registered in the alert management system.")
        else:
            # add new user to admin.activeusers
            insert_new_alert_user = f"INSERT INTO `admin`.`ActiveUsers` (`Username`, `Password`, `DBName`, `AlertActivated`, `DBUID`, `DBPSSWD`, `UserCreationTime`) VALUES ('{self.username}', '{self.password}', '{self.username}', '2', '{self.password}', '{self.encoded_password}', '2020-11-20 12:00:00');"
            c.execute(insert_new_alert_user)
            cnx.commit()
            # then perform an insert_alert and update_quantitylist stored proceedures
        cnx.close()

    # handle the unregstering the user in the alert service
    def unregister(self):
        cnx = mysql.connector.connect(user='tom',password='Manhattan44joke#',
                            host='resensys.net',use_pure=True)
        c = cnx.cursor()
        remove_alert_user = f"DELETE FROM `admin`.`ActiveUsers` WHERE (`Username` = '{self.username}');"
        c.execute(remove_alert_user)
        cnx.commit()

    def updateAlert(self,dids,threshold_dict={}):
        return
        # update_command = UPDATE `Constellation`.`AlertGen` SET `WARNING_LL_1` = '7' WHERE (`idAlertGen` = '6188');

    # input an email address as a string to be added to database
    def addEmail(self,email):
        return
    
    # input a list of email addresses
    def updateEmail(self,email_list):
        return

    # input mobile number for recieving text message alerts
    def addMobile(self, mobile):
        return
    
    # input mobile numbers to recieve multiple messages at once
    def updateMobile(self,mobile_list):
        return

    
