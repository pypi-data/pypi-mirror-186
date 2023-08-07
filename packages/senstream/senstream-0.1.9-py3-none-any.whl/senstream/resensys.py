import mysql.connector
import numpy as np
import pandas as pd
import math

# 1. Establish a remote connection to resensys.net using python environment
# 2. Encrypt the connection to resensys.net
# 3. Pull general data for all sensors/sites/routing parameters for a given account

class Resensys():

    def __init__(self,username,password):
        self.username = username
        self.password = password
        self.host = 'resensys.net'
        self.connect()
    
    def connect(self):
        # define ssh connection

        # decrypt user password
        self.password_encoding_generator()
        config = {  
            'user': self.username,
            'password': self.encoded_password,
            'host': self.host,
            'port': 3306,

            # Create SSL connection with the self-signed certificate
            'ssl_verify_cert': False,
        }

        # self.conn = mysql.connector.connect(user=self.username,password=self.encoded_password,host=self.host)
        self.conn = mysql.connector.connect(**config,use_pure=True)
        return self.conn
    
    def getCredentials(self):
        return self.username,self.password
    
    def password_encoding_generator(self):
        password_bytes = bytes(self.password, 'ascii')
        byte_list = []
        for byte in password_bytes:
            byte_list.append(byte)
        reverse_list = byte_list[::-1]
        # loop through every element of the reversed array
        for i in range(len(reverse_list)):
            new_byte = (int(math.pow(-1, i))*(i%10))
            reverse_list[i] += new_byte
        # decode the new array
        encoded_characters = []
        for j in range(len(reverse_list)):
            encoded_characters.append(chr(reverse_list[j]))
        self.encoded_password = ''.join(encoded_characters)

    def add_new_site(self,SID):
        self.serverTool.add_site_to_user(self, self.username, SID, acc_pswd="", mode=0, extra_criterion="")


class Sensors(Resensys):
    def __init__(self,parent):
        super().__init__(parent.username, parent.password)
        self.conn = parent.conn

    def getSensors(self,format="json",filter={}):
        # create a db cursor
        cursor = self.conn.cursor()
        # define the query to the db
        query = f"SELECT TTL,DID,SID,TYP,DES,STT FROM `{self.username}`.`Info`"
        cursor.execute(query)
        results = cursor.fetchall()
        # define resultant columns as list
        cols = ["Title","DID","SID","DeviceType","Description","Status"]

        if format == "json":
            devices_dict = {}
            for count,result in enumerate(results):
                devices_dict[str(count)] = {cols[i]:result[i] for i in range(len(cols))}
            return devices_dict
        elif format == "dataframe":
            return pd.DataFrame(results,columns=cols)

    def getSites(self,format="json",filter={},unique=False):
        # create a db cursor
        cursor = self.conn.cursor()
        # define the query to the db
        query = f"SELECT SIDName,SID FROM `{self.username}`.`Accounts`"
        cursor.execute(query)
        results = cursor.fetchall()
        # define resultant columns as list
        cols = ["SiteName","SID"]

        if unique:
            return pd.DataFrame(results,columns=cols).SID.unique()
        else:
            if format == "json":
                devices_dict = {}
                for count,result in enumerate(results):
                    devices_dict[str(count)] = {cols[i]:result[i] for i in range(len(cols))}
                return devices_dict
            elif format == "dataframe":
                return pd.DataFrame(results,columns=cols)

    def getTables(self,SID):
        # convert the SID XX-XX to xxxx
        sid = SID.replace('-','') 
        cursor = self.conn.cursor()
        query = ("SHOW TABLES FROM `Data_%s`"%(sid))
        cursor.execute(query)
        tables = cursor.fetchall()
        field_names = [i[0] for i in cursor.description]
        tables_df = pd.DataFrame(tables,columns=field_names)
        return tables_df

    def getRouting(self,format="json",filter={}):
        # get list of all sites
        sites = self.getSites(format="dataframe").SID.tolist()

        # create a bulk list of all tables in user sites
        combined_tables = []
        # loop through every site in sites
        for site in sites:
            site_tables = self.getTables(site)['Tables_in_Data_'+site.replace("-","")].tolist()
            combined_tables += site_tables

        volt_tables=[]
        # remove all but the volt tables
        for table in combined_tables:
            # get the dataformat
            df = table.split('.')[-1]
            did = table.split('.')[1][:4]
            sid = table.split('.')[2]
            # check if the data format is volt = 3003
            if df == '3003' and did != '0000':
                device_id = table.split('.')[1]
                device_id = '-'.join([device_id[i:i+2] for i in range(0, len(device_id), 2)])
                volt_tables.append((table,device_id,sid))
            
        # create a db cursor
        cursor = self.conn.cursor()
        local_addresses = []
        # define the query to the db
        for table in volt_tables:
            SID = table[2]
            query = ("SELECT `Optional` FROM `Data_%s`.`%s` ORDER BY Time DESC LIMIT 1"%(SID,table[0]))
            cursor.execute(query)
            optional = cursor.fetchall()
            local_address = int(optional[0][0]/1001)
            local_addresses.append((table[1],SID[:2]+"-"+SID[2:],local_address))
        
        la_df = pd.DataFrame(local_addresses,columns=['DID','SID','LocAddr'])
        return la_df