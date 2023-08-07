import mysql.connector
from senstream.resensys import Resensys
from datetime import datetime,timedelta
import pandas as pd

# 1. Handles all operations for remote configurations
# 2. Handles setting name of a site in a user account
# 3. Used to extract information about the health of the site (e.g. activity status, low battery, no charging, etc.)

class SeniMax(Resensys):
    def __init__(self):
        return
    
    # get the name of the site
    def siteName(self):
        return

    # set the site name to something else
    def siteName(self,name):
        return
    
    # return a summary of the status of the device
    def status(self):
        return

    def txInterval(self):
        return