import re
import pandas as pd
from datetime import datetime
from datetime import timedelta

SenScopeConfiguration = {
    'MAX_NUM_ACTIVE_USERS':  20,
    'MAX_ALERT_NUM':    1000,
    'MAX_MIN_ALERT':    0,
    'MAX_DEVICE_BUFFER_SIZE':  1000,
    'MAX_DATAPOINT_PER_SERIE': 4096,

    'COLOR_CODE_WHITE': 0,
    'COLOR_CODE_YELLOW':   1,
    'COLOR_CODE_RED': 2,


    'MAX_VECTOR_LEN':   10000,
    'DATA_FORMAT_TEMP': 3002,
    'DATA_FORMAT_VLT':  3003,
    'DATA_FORMAT_TILT_X':  2001,
    'DATA_FORMAT_TILT_Y':  2002,
    'DATA_FORMAT_TILT_Z':  2003,
    'DATA_FORMAT_STRAIN':  1,

    'DUR_1_HOUR':  1,
    'DUR_2_HOUR':  2,
    'DUR_6_HOUR':  6,
    'DUR_12_HOUR':  12,
    'STANDARD_1_HOUR': 3600,
    'NUM_HOUR_IN_A_DAY':  24,

    'DF_SENSOR_STRAIN_LOW_RATE': 1,
    'DF_SENSOR_TILT_XYZ': 2,
    'DF_SENSOR_TILT_X': 2001,
    'DF_SENSOR_TILT_Y': 2002,
    'DF_SENSOR_TILT_Z': 2003,
    'DF_SENSOR_VOLT_TEMP': 3,
    'DF_SENSOR_LQI': 3001,
    'DF_SENSOR_TEMP': 3002,
    'DF_SENSOR_VOLT': 3003,
    'DF_SENSOR_DISPLACEMENT_LOW_RATE': 5,
    'DF_SENSOR_DISPLACEMENT_LOW_RATE_1inch': 5001,
    'DF_SENSOR_DISPLACEMENT_LOW_RATE_2inch': 5002,
    'DF_SENSOR_DISPLACEMENT_LOW_RATE_4inch': 5003,
    'DF_SENSOR_MOISTURE_TEMP_PROBE': 6,
    'DF_SENSOR_MOISTURE_PROBE_LOW_RATE': 6001,
    'DF_SENSOR_TEMP_PROBE_LOW_RATE': 6002,
    'DF_E_TILT_Y_FORMAT': 7,
    'DF_DOUBLE_TEMP_INFO': 8,
    'DF_SENSOR_PADDING': 15,
    'DF_SENSOR_DOUBLE_TEMP_INFO1': 8001,
    'DF_SENSOR_DOUBLE_TEMP_INFO2': 8002,
    'DF_SENSOR_ACCELERATION_XYZ': 10,
    'DF_SENSOR_ACCELERATION_X': 10001,
    'DF_SENSOR_ACCELERATION_Y': 10002,
    'DF_SENSOR_ACCELERATION_Z': 10003,
    'DF_SENSOR_DISPLACEMENT_PEAK_INFO': 9,
    # I assign X100 for Async data
    'DF_SENSOR_DISPLACEMENT_PEAK_ASYNC_MAX': 9101,
    # I assign X100 for Async data
    'DF_SENSOR_DISPLACEMENT_PEAK_ASYNC_MIN': 9102,
    # I assign X100 for Async data
    'DF_SENSOR_DISPLACEMENT_PEAK_ASYNC_CURR': 9103,
    'DF_SENSOR_DISPLACEMENT_PEAK_MAX': 9001,
    'DF_SENSOR_DISPLACEMENT_PEAK_MIN': 9002,
    'DF_SENSOR_DISPLACEMENT_PEAK_CURR': 9003,
    'DF_SENSOR_MOTION_DETECTION': 11,
    'DF_SENSOR_MOTION_DETECTION_ASYNC': 11101,
    'DF_ACTUATION': 12,
    'DF_ACTUATION_ASYNC': 12101,
    'DF_SENSOR_GENERIC_DIFF_INP': 13,
    'DF_SENSOR_GENERIC_DIFF_INP_VALUE': 13001,  # 13 * 1000 + 1
    'DF_SENSOR_GENERIC_DIFF_INP_IA_GAIN': 13002,  # 13 * 1000 + 2
    'DF_REPEATER_INFO': 14,
    'DF_REPEATER_CHILD_NUM': 14001,  # 14 * 1000 + 1
    'DF_REPEATER_SYNC_WITH_SENIMAX': 14002,  # 14 * 1000 + 2
    'DF_REPEATER_XMIT_PERIOD_SEC': 14003,  # 14 * 1000 + 3

    'DF_SENSOR_VIBRATION_ASYNC_XYZ': 15,
    # DF_SENSOR_VIBRATION_ASYNC_XYZ * 1000 + 1
    'DF_SENSOR_VIBRATION_ASYNC_X': 15001,
    # DF_SENSOR_VIBRATION_ASYNC_XYZ * 1000 + 2
    'DF_SENSOR_VIBRATION_ASYNC_Y': 15002,
    # DF_SENSOR_VIBRATION_ASYNC_XYZ * 1000 + 3
    'DF_SENSOR_VIBRATION_ASYNC_Z': 15003,

    'DF_SENSOR_VIBRATION_REGULAR_XYZ': 16,
    # DF_SENSOR_VIBRATION_REGULAR_XYZ * 1000 + 1
    'DF_SENSOR_VIBRATION_REGULAR_X': 16001,
    # DF_SENSOR_VIBRATION_REGULAR_XYZ * 1000 + 2
    'DF_SENSOR_VIBRATION_REGULAR_Y': 16002,
    # DF_SENSOR_VIBRATION_REGULAR_XYZ * 1000 + 3
    'DF_SENSOR_VIBRATION_REGULAR_Z': 16003,
    # DF_SENSOR_VIBRATION_REGULAR_X + 100
    'DF_SENSOR_VIBRATION_REGULAR_BASE_X': 16101,
    # DF_SENSOR_VIBRATION_REGULAR_Y + 100
    'DF_SENSOR_VIBRATION_REGULAR_BASE_Y': 16102,
    # DF_SENSOR_VIBRATION_REGULAR_Z + 100
    'DF_SENSOR_VIBRATION_REGULAR_BASE_Z': 16103,
    # DF_SENSOR_VIBRATION_REGULAR_XYZ * 1000 + 100 + 1
    'DF_SENSOR_VIBRATION_REGULAR_THRESHOLD': 16101,
    # DF_SENSOR_VIBRATION_REGULAR_XYZ * 1000 + 100 + 2
    'DF_SENSOR_VIBRATION_REGULAR_INTERVAL': 16102,


    'DF_SENSOR_VIBRATION_EVENT_XYZ': 17,
    # DF_SENSOR_VIBRATION_EVENT_XYZ * 1000 + 1
    'DF_SENSOR_VIBRATION_EVENT_X': 17001,
    # DF_SENSOR_VIBRATION_EVENT_XYZ * 1000 + 2
    'DF_SENSOR_VIBRATION_EVENT_Y': 17002,
    # DF_SENSOR_VIBRATION_EVENT_XYZ * 1000 + 3
    'DF_SENSOR_VIBRATION_EVENT_Z': 17003,
    'DF_SENSOR_VIBRATION_EVENT_BASE_X': 17101,  # DF_SENSOR_VIBRATION_EVENT_X + 100
    'DF_SENSOR_VIBRATION_EVENT_BASE_Y': 17102,  # DF_SENSOR_VIBRATION_EVENT_Y + 100
    'DF_SENSOR_VIBRATION_EVENT_BASE_Z': 17103,  # DF_SENSOR_VIBRATION_EVENT_Z + 100

    'DF_DISPLACEMENT_3D_INFO': 18,
    'DF_DISPLACEMENT_3D_INFO_S1': 18001,  # DF_DISPLACEMENT_3D_INFO * 1000 + 1
    'DF_DISPLACEMENT_3D_INFO_S2': 18002,  # DF_DISPLACEMENT_3D_INFO * 1000 + 2
    'DF_DISPLACEMENT_3D_INFO_S3': 18003,  # DF_DISPLACEMENT_3D_INFO * 1000 + 3
    'DF_DISPLACEMENT_3D_INFO_S4': 18004,  # DF_DISPLACEMENT_3D_INFO * 1000 + 4
    'DF_DISPLACEMENT_3D_INFO_X': 18005,  # DF_DISPLACEMENT_3D_INFO * 1000 + 5
    'DF_DISPLACEMENT_3D_INFO_Y': 18006,  # DF_DISPLACEMENT_3D_INFO * 1000 + 6
    'DF_DISPLACEMENT_3D_INFO_Z': 18007,  # DF_DISPLACEMENT_3D_INFO * 1000 + 7
    'DF_DISPLACEMENT_3D_INFO_ANGL1': 18008,  # DF_DISPLACEMENT_3D_INFO * 1000 + 8
    'DF_DISPLACEMENT_3D_INFO_ANGL2': 18009,  # DF_DISPLACEMENT_3D_INFO * 1000 + 9
    'DF_DISPLACEMENT_3D_INFO_ANGL3': 18010,  # DF_DISPLACEMENT_3D_INFO * 1000 + 10
    'DF_DISPLACEMENT_3D_INFO_ANGL4': 18011,  # DF_DISPLACEMENT_3D_INFO * 1000 + 11
    'DF_DISPLACEMENT_3D_INFO_XX': 18012,  # DF_DISPLACEMENT_3D_INFO * 1000 + 12

    'DF_SENIMAX_STATUS_INFO': 22,
    'DF_SENIMAX_STATUS_INFO_TEMP': 22001,  # DF_SENIMAX_STATUS_INFO * 1000 + 1
    'DF_SENIMAX_STATUS_INFO_VOLT': 22002,  # DF_SENIMAX_STATUS_INFO * 1000 + 2
    'DF_SENIMAX_STATUS_INFO_RSSI': 22003,  # DF_SENIMAX_STATUS_INFO * 1000 + 3
    'DF_SENIMAX_STATUS_INFO_VRSN': 22004,  # DF_SENIMAX_STATUS_INFO * 1000 + 4
    'DF_SENIMAX_STATUS_INFO_VOLT_AUX': 22005,  # DF_SENIMAX_STATUS_INFO * 1000 + 5
    # DF_SENIMAX_STATUS_INFO * 1000 + 6
    'DF_SENIMAX_STATUS_INFO_CHARGE_CURR_1': 22006,
    # DF_SENIMAX_STATUS_INFO * 1000 + 7
    'DF_SENIMAX_STATUS_INFO_CHARGE_CURR_2': 22007,

    'DF_SENIMAX_STATUS_INFO_TX_INTERVAL': 22008,  # DF_SENIMAX_STATUS_INFO * 1000 + 8

    'DF_SENSOR_E_TILT_2D_XYZ': 23,
    'DF_SENSOR_E_TILT_2D_Pitch': 23001,
    'DF_SENSOR_E_TILT_2D_Roll': 23002,

    'DF_SENSOR_FORCE_BALANCE_VIBRATION_X': 24,
    'DF_SENSOR_FORCE_BALANCE_VIBRATION_Y': 25,
    'DF_SENSOR_FORCE_BALANCE_VIBRATION_Z': 26,

    # DF_SENSOR_FORCE_BALANCE_VIBRATION_X * 1000 + 100 + 1
    'DF_SENSOR_FORCE_BALANCE_X_AVERAGE_TIMEOFFSET': 24101,
    # DF_SENSOR_FORCE_BALANCE_VIBRATION_X * 1000 + 100 + 2
    'DF_SENSOR_FORCE_BALANCE_X_THRESHOLD_INTERVAL': 24102,
    # DF_SENSOR_FORCE_BALANCE_VIBRATION_Y * 1000 + 100 + 1
    'DF_SENSOR_FORCE_BALANCE_Y_AVERAGE_TIMEOFFSET': 25101,
    # DF_SENSOR_FORCE_BALANCE_VIBRATION_Y * 1000 + 100 + 2
    'DF_SENSOR_FORCE_BALANCE_Y_THRESHOLD_INTERVAL': 25102,
    # DF_SENSOR_FORCE_BALANCE_VIBRATION_Z * 1000 + 100 + 1
    'DF_SENSOR_FORCE_BALANCE_Z_AVERAGE_TIMEOFFSET': 26101,
    # DF_SENSOR_FORCE_BALANCE_VIBRATION_Z * 1000 + 100 + 2
    'DF_SENSOR_FORCE_BALANCE_Z_THRESHOLD_INTERVAL': 26102,

    'DF_SENSOR_HIGH_RATE_STRAIN': 27,

    'DF_SENSOR_GENERIC_SAMPLES': 28,

    # DF_SENSOR_GENERIC_SAMPLES * 1000 + DF_SENSOR_GENERIC_SUBTYPE_ANEMOMETER_1D * 100 + 1
    'DF_SENSOR_WIND_SPEED_1D': 28301,
    # DF_SENSOR_GENERIC_SAMPLES * 1000 + DF_SENSOR_GENERIC_SUBTYPE_ANEMOMETER_1D * 100 + 2
    'DF_SENSOR_WIND_DIRECTION_1D': 28302,

    # DF_SENSOR_GENERIC_SAMPLES * 1000 + DF_SENSOR_GENERIC_SUBTYPE_ANEMOMETER_3D * 100 + 0
    'DF_SENSOR_WIND_SPEED_3D': 28500,
    # DF_SENSOR_GENERIC_SAMPLES * 1000 + DF_SENSOR_GENERIC_SUBTYPE_ANEMOMETER_3D * 100 + 1
    'DF_SENSOR_WIND_AZIMUTH': 28501,
    # DF_SENSOR_GENERIC_SAMPLES * 1000 + DF_SENSOR_GENERIC_SUBTYPE_ANEMOMETER_3D * 100 + 2
    'DF_SENSOR_WIND_ELEVATION': 28502,
    # DF_SENSOR_GENERIC_SAMPLES * 1000 + DF_SENSOR_GENERIC_SUBTYPE_ANEMOMETER_3D * 100 + 3
    'DF_SENSORSOUND_SPEED': 28503,
    # DF_SENSOR_GENERIC_SAMPLES * 1000 + DF_SENSOR_GENERIC_SUBTYPE_ANEMOMETER_3D * 100 + 4
    'DF_SENSOR_AIR_TEMPERATURE': 28504,

    # DF_SENSOR_GENERIC_SAMPLES * 1000 + DF_SENSOR_GENERIC_SUBTYPE_VIBRATION_X * 100 + 0
    'DF_SENSOR_VIBRATION_3D_X': 28000,
    # DF_SENSOR_GENERIC_SAMPLES * 1000 + DF_SENSOR_GENERIC_SUBTYPE_VIBRATION_Y * 100 + 0
    'DF_SENSOR_VIBRATION_3D_Y': 28100,
    # DF_SENSOR_GENERIC_SAMPLES * 1000 + DF_SENSOR_GENERIC_SUBTYPE_VIBRATION_Z * 100 + 0
    'DF_SENSOR_VIBRATION_3D_Z': 28200,

    # DF_SENSOR_PADDING * 1000 + DF_SENSOR_GENERIC_SUBTYPE_ANEMOMETER_1D * 100 + 1
    'DF_SENSOR_WIND_SPEED_1D_NOTIF': 15101,
    # DF_SENSOR_PADDING * 1000 + DF_SENSOR_GENERIC_SUBTYPE_ANEMOMETER_1D * 100 + 2
    'DF_SENSOR_WIND_DIRECTION_1D_NOTIF': 15102,

    # DF_SENSOR_PADDING * 1000 + DF_SENSOR_GENERIC_SUBTYPE_ANEMOMETER_3D * 100 + 0
    'DF_SENSOR_WIND_SPEED_3D_NOTIF': 15500,
    # DF_SENSOR_PADDING * 1000 + DF_SENSOR_GENERIC_SUBTYPE_ANEMOMETER_3D * 100 + 1
    'DF_SENSOR_WIND_AZIMUTH_NOTIF': 15501,
    # DF_SENSOR_PADDING * 1000 + DF_SENSOR_GENERIC_SUBTYPE_ANEMOMETER_3D * 100 + 2
    'DF_SENSOR_WIND_ELEVATION_NOTIF': 15502,
    # DF_SENSOR_PADDING * 1000 + DF_SENSOR_GENERIC_SUBTYPE_ANEMOMETER_3D * 100 + 3
    'DF_SENSORSOUND_SPEED_NOTIF': 15503,
    # DF_SENSOR_PADDING * 1000 + DF_SENSOR_GENERIC_SUBTYPE_ANEMOMETER_3D * 100 + 4
    'DF_SENSOR_AIR_TEMPERATURE_NOTIF': 15504,

    # DF_SENSOR_PADDING * 1000 + DF_SENSOR_GENERIC_SUBTYPE_VIBRATION_X * 100 + 0
    'DF_SENSOR_VIBRATION_3D_X_NOTIF': 15000,
    # DF_SENSOR_PADDING * 1000 + DF_SENSOR_GENERIC_SUBTYPE_VIBRATION_Y * 100 + 0
    'DF_SENSOR_VIBRATION_3D_Y_NOTIF': 15100,
    # DF_SENSOR_PADDING * 1000 + DF_SENSOR_GENERIC_SUBTYPE_VIBRATION_Z * 100 + 0
    'DF_SENSOR_VIBRATION_3D_Z_NOTIF': 15200,

    # DF_SENSOR_GENERIC_SAMPLES * 1000 + DF_SENSOR_GENERIC_SUBTYPE_LR_REDUNDANT_STRAIN * 100 + 0
    'DF_SENSOR_LR_REDUNDANT_STRAIN_DIFFRENTIAL': 28600,
    # DF_SENSOR_GENERIC_SAMPLES * 1000 + DF_SENSOR_GENERIC_SUBTYPE_LR_REDUNDANT_STRAIN * 100 + 1
    'DF_SENSOR_LR_REDUNDANT_STRAIN_POSITIVE': 28601,
    # DF_SENSOR_GENERIC_SAMPLES * 1000 + DF_SENSOR_GENERIC_SUBTYPE_LR_REDUNDANT_STRAIN * 100 + 2
    'DF_SENSOR_LR_REDUNDANT_STRAIN_NEGATIVE': 28602,


    'MD_DEVICE_TYPE_SENSOR': 1,
    'MD_DEVICE_TYPE_ACTUATOR': 2,
    'ACTUATION_STARTED_ASYNC': 2,
    'ACTUATION_ENDED_ASYNC': 1,

    'SENSOR_DISPLACEMENT_IS_A_4_inch': 100,
    'SENSOR_DISPLACEMENT_IS_A_2_inch': 50,
    'SENSOR_DISPLACEMENT_IS_A_1_inch': 25,  # Not implemented for all sensors



    'PARSER_MODE_LIVE': 0,
    'PARSER_MODE_OFFLINE': 1,



    'DF_SENSOR_GENERIC_SUBTYPE_VIBRATION_X': 0,
    'DF_SENSOR_GENERIC_SUBTYPE_VIBRATION_Y': 1,
    'DF_SENSOR_GENERIC_SUBTYPE_VIBRATION_Z': 2,
    'DF_SENSOR_GENERIC_SUBTYPE_ANEMOMETER_1D': 3,
    'DF_SENSOR_GENERIC_SUBTYPE_ANEMOMETER_2D': 4,
    'DF_SENSOR_GENERIC_SUBTYPE_ANEMOMETER_3D': 5,

    'DF_SENSOR_GENERIC_SUBTYPE_LR_REDUNDANT_STRAIN': 6,

    'DF_INTERNAL_TEMP_FLIP_THRESHOLD': 175
}
# ------------------------Table: RegInfo.registration ---------------------
RegInfo_registration_columns = [
    "idRegistration",
    "DID",
    "DNAME",
    "DTYPE",
    "SID",
    "SNAME",
    "GROUPID",
    "M",
    "DATAFORMAT",
    "QUANTITYNAME",
    "UNIT",
    "NUMBERFORMAT",
    "NUMPRECISION",
    "DATETIMEFORMAT",
    "CALIBCOEF",
    "CALIBDOFF",
    "TEMPCALIBCOEF0",
    "TEMPCALIBCOEF1",
    "TEMPCALIBCOEF2",
    "TEMPCALIBCOEF3",
    "APPLYOPTIONALOFFSET",
    "SHOWABLE",
    "VERSION",
    "ALTUNIT",
    "AUCOEF",
    "AUDOFF"
]
RegInfo_registration_Index = {
    'DID': 1,
    'SID': 4,
    'SNAME': 5,
    'DataFormat': 8,
    'DTYPE': 28,
    'QuantityName': 9,
    'Unit': 10,
    'NumPrecision': 12,
    'CalibCOEF': 14,
    'CalibDOFF': 15,
}

# -----------------------Table: ActiveUsers Column Definition------------
ActiveUserIndex = {
    'Username': 1,
    'DBPass': 6,
    'AlertActivated': 4}
# ------------------------Table: Raw Data Table Definition------------
RawDataTableIndex = {
    'Time': 0,
    # 'SeqNum': 1,
    'Data': 1
    # 'Optional': 3
}
# -----------------------Table: Alert1D Column Definition------------
Alert1ColumnNumber = 46
Alert1DIndex = {
    'id': 0,
    'Status': 2,
    'AlertInterval': 3,
    'DID1': 4,
    'SID1': 5,
    'DATAFORMAT1': 6,
    'TempCoef': 10,
    'QUANTITYNAME1': 44,
    'W_L': 18,
    'W_H': 22,
    'A_L': 26,
    'A_H': 30,
    'Email1': 37,
    'Email2': 38,
    'Email3': 39,
    'Activated': 34,
    'LastModifDateTime': 35
}
# ---------------------Quantity List Column Definition -------------
QLColumnNumber = 24
QLIndex = {
    'DID': 1,
    'DNAME': 2,
    'SID': 3,
    'SNAME': 4,
    'DTYPE': 5,
    'DataFormat': 6,
    'QuantityName': 7,
    'Unit': 8,
    'NumPrecision': 10,
    'CalibCOEF': 11,
    'CalibDOFF': 12,
}
# ---------------------Temperature Calib Column Definition -------------
TCIndex = {
    'idTempCalib': 0,
    'DID': 1,
    'SID': 2,
    'DataFormat': 3,
    'Coef': 5
}
# -----------------------Table: Alert2D Column Definition------------
Alert2DIndex = {
    'Status': 0,
    'DID1': 1,
    'DNAME1': 2,
    'SID1': 3,
    'SNAME1': 4,
    'DATAFORMAT1': 5,
    'QUANTITYNAME1': 6,
    'COEF1': 7,
    'DOFF1': 8,
    'TEMPCOEF1': 9,
    'DID2': 10,
    'DNAME2': 11,
    'SID2': 12,
    'SNAME2': 13,
    'DATAFORMAT2': 14,
    'QUANTITYNAME2': 15,
    'COEF2': 16,
    'DOFF2': 17,
    'TEMPCOEF2': 18,
    'W1X': 19,
    'W1Y': 20,
    'W2X': 21,
    'W2Y': 22,
    'W3X': 23,
    'W3Y': 24,
    'W4X': 25,
    'W4Y': 26,
    'A1X': 27,
    'A1Y': 28,
    'A2X': 29,
    'A2Y': 30,
    'A3X': 31,
    'A3Y': 32,
    'A4X': 33,
    'A4Y': 34,
    'AlertInterval': 35,
    'Email1': 36,
    'Email2': 37,
    'Email3': 38,
    'Activated': 39,
    'id': 40
}
# ---------------Alarm Status---------------
AlertStatus = {
    'Normal': 0,
    'Warning': 1,
    'Alarm': 2,
    'Offline': 5
}

AlertStatusRev = {
    0: 'Normal',
    1: 'Warning',
    2: 'Alarm',
    5: 'Offline'
}

AlertStatusColorRev = {
    0: 'green',
    1: '#ffa31a',
    2: 'red'
}

AlertSubject = {
    0: 'Clear: ',
    1: 'Warning: ',
    2: 'Alarm: ',
    5: 'Offline: '
}

AlertSign = {
    0: ' =/= ',
    1: ' > ',
    2: ' >= ',
    3: ' <= ',
    4: ' < ',
}

MYSQL_Datetime_Formatter = "%Y-%m-%d %H:%M:%S"

def generate_data_query(deviceID, siteID, dataFormat, datetimeStart, datetimeEnd, coef, offset, temp_calib=[0,0,0,0], apply_temp_coef='False'):
    query = ""
    datetimePattern = re.compile(r'^[0-9]{4}-[0-9]{1,2}-[0-9]{1,2} [0-9]{1,2}:[0-9]{1,2}:[0-9]{1,2}')
    if datetimePattern.match(datetimeStart):
        datetimeStart=f"\'{datetimeStart}\'"
    if datetimePattern.match(datetimeEnd):
        datetimeEnd=f"\'{datetimeEnd}\'"
    # ------Assemble the Raw Data Table name and remove the "-" in the DID and SID-----
    tableNamePrefix = ("`Data_" + siteID + "`.`Data."
                        + deviceID + "."
                        + siteID + ".").replace("-", "")
    tableNameTemp = tableNamePrefix + \
        str(SenScopeConfiguration['DF_SENSOR_TEMP']) + "`"
    tableName1 = tableNamePrefix + str(dataFormat) + "`"
    # -----Date Time Picker----------
    # -------Query-------------------
    if (apply_temp_coef == 'True'):
        # query = (
        #     f"SELECT UNIX_TIMESTAMP(CONVERT_TZ(t1.Time, '+00:00', @@global.time_zone)) as Time, "
        #     f"({str(coef)})*" #Calib Coef
        #     f"(t1.Value" #Raw
        #     f"-({str(offset)})" #Calib Offset
        #     f"-({temp_calib[0]})" # Constant Temp Offset
        #     f"-({temp_calib[1]})*(IF(t2.value<={SenScopeConfiguration['DF_INTERNAL_TEMP_FLIP_THRESHOLD']},t2.value,(t2.value-256)))" #1st order Temp Calib
        #     # f"-({temp_calib[2]})*(POWER((IF(t2.value<={SenScopeConfiguration['DF_INTERNAL_TEMP_FLIP_THRESHOLD']},t2.value,(t2.value-256))),2))" #2nd order Temp Calib
        #     # f"-({temp_calib[3]})*(POWER((IF(t2.value<={SenScopeConfiguration['DF_INTERNAL_TEMP_FLIP_THRESHOLD']},t2.value,(t2.value-256))),3))" #3rd order Temp Calib
        #     f" as Calibrated "
        #     f"FROM {tableName1} as t1 LEFT JOIN {tableNameTemp} as t2 on t1.Time=t2.Time "
        #     f"WHERE t1.Time Between {datetimeStart} and {datetimeEnd} "
        #     f"order by UNIX_TIMESTAMP(t1.Time) asc;"
        if (int(dataFormat) == SenScopeConfiguration['DF_SENSOR_TEMP']):
            query = (
                f"SELECT UNIX_TIMESTAMP(CONVERT_TZ(t1.Time, '+00:00', @@global.time_zone)) as Time, IF(t1.Value<={SenScopeConfiguration['DF_INTERNAL_TEMP_FLIP_THRESHOLD']},t1.value,(t1.value-256)) as Temp "
                f"FROM {tableName1} as t1 WHERE Time Between {datetimeStart} and {datetimeEnd} "
                f"order by UNIX_TIMESTAMP(t1.Time) asc;"
            )
        else:
            query = (
                f"SELECT UNIX_TIMESTAMP(CONVERT_TZ(t1.Time, '+00:00', @@global.time_zone)) as Time, "
                f"t1.Value as Temp" #Raw
                f"FROM {tableName1} as t1 WHERE Time Between {datetimeStart} and {datetimeEnd} "
                f"order by UNIX_TIMESTAMP(t1.Time) asc;"
            )
    elif (int(dataFormat)//1000 == SenScopeConfiguration['DF_SENSOR_VIBRATION_EVENT_XYZ'] or
        int(dataFormat)//1000 == SenScopeConfiguration['DF_SENSOR_VIBRATION_REGULAR_XYZ'] or
        int(dataFormat)//1000 >= SenScopeConfiguration['DF_SENSOR_GENERIC_SAMPLES'] or
        int(dataFormat) == SenScopeConfiguration['DF_SENSOR_FORCE_BALANCE_VIBRATION_X'] or
        int(dataFormat) == SenScopeConfiguration['DF_SENSOR_FORCE_BALANCE_VIBRATION_X'] or
        int(dataFormat) == SenScopeConfiguration['DF_SENSOR_FORCE_BALANCE_VIBRATION_X'] or
        int(dataFormat) == SenScopeConfiguration['DF_SENSOR_HIGH_RATE_STRAIN']):
        query = (
            f"SELECT UNIX_TIMESTAMP(CONVERT_TZ(SUBTIME(t1.Time, Optional/1000), '+00:00', @@global.time_zone)) as Time, ({str(coef)})*(t1.Value-({str(offset)})) as Calibrated "
            f"FROM {tableName1} as t1 WHERE SUBTIME(t1.Time, (Optional div 1000)) Between {datetimeStart} and {datetimeEnd} "
            f"order by (UNIX_TIMESTAMP(t1.Time)*1000 - Optional) asc;"
        )
    elif (int(dataFormat) == SenScopeConfiguration['DF_SENSOR_TEMP']):
        query = (
            f"SELECT UNIX_TIMESTAMP(CONVERT_TZ(t1.Time, '+00:00', @@global.time_zone)) as Time, ({str(coef)})*((IF(t1.Value<={SenScopeConfiguration['DF_INTERNAL_TEMP_FLIP_THRESHOLD']},t1.value,(t1.value-256)))-({str(offset)})) as Calibrated "
            f"FROM {tableName1} as t1 WHERE Time Between {datetimeStart} and {datetimeEnd} "
            f"order by UNIX_TIMESTAMP(t1.Time) asc;"
        )
    else:
        query = (
            f"SELECT UNIX_TIMESTAMP(CONVERT_TZ(t1.Time, '+00:00', @@global.time_zone)) as Time, ({str(coef)})*(t1.Value-({str(offset)})) as Calibrated "
            f"FROM {tableName1} as t1 WHERE t1.Time Between {datetimeStart} and {datetimeEnd} "
            f"order by UNIX_TIMESTAMP(t1.Time) asc;"
        )
    return query

def print_debug_info(input_str):
    print(f"======================================\n"
          f"{input_str}\n"
          f"======================================\n")
# ---------------------Fxn: read data to dataframe with mysqlconnector lib --------------------------------------
# dbCursor: mysqlconnector database cursor object
# query: MySQL query in string
# return: pandas.DataFrame object
def read_cursor_to_DF_mysqlconnector(dbCursor, query):
    try:
        dbCursor.execute(query)
        data = dbCursor.fetchall()
        frame = pd.DataFrame(list(data))
        frame.columns = list(dbCursor.column_names)
    except Exception as e:
        frame = pd.DataFrame()
        print("========\n", str(e), "\n========\nQuery:\n",query,"\n")
    return frame

def read_cursor_to_DF_mysqlclient(dbCursor, query, add_column_name=0):
    try:
        dbCursor.execute(query)
        data = dbCursor.fetchall()
        frame = pd.DataFrame(list(data))
        # print(dbCursor.description)
        if add_column_name == 1:
            column_list = list()
            for column_name in dbCursor.description:
                column_list.append(list(column_name)[0])
            frame.columns = list(column_list)
        # End if add_column_name
    except Exception as e:
        frame = pd.DataFrame()
        print("========\n", str(e), "\n========\nQuery:\n",query,"\n")
    return frame
# ---------------------Fxn: Time to now --------------------------------------
# timestamp: time read from mysql table, already Datetime.Datetime format
# return: seconds

def utc_time_to_now_timedelta(timeStamp):
    if timeStamp is not None:
        # dateTimeIn = datetime.strptime(timeStamp,"%Y-%m-%d %H:%M:%S")
        dateTimeNow = datetime.utcnow()
        time_delta = dateTimeNow - timeStamp
    else:
        time_delta = timedelta(days=7000)
    return time_delta
