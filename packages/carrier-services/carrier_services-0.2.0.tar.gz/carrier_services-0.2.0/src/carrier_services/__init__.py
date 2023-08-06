from datetime import datetime

# Package version
__version__ = "0.2.0"

P44_CS_HEADERS = ["CHANGE_MODE", "ALLIANCE_ID", "ALLIANCE_POOL_ID", "TRADE_ID", "OI_SERVICE_ID",
                  "CARRIER_ID", "SERVICE_ID", "SERVICE", "DIRECTION", "FREQUENCY",
                  "START_DAY", "PORT_CODE", "ORDER", "TT", "LOCATION_TYPE",
                  "RELATED_IDS"]
RUN_TIME = datetime.now()
RUN_TIME_STR = RUN_TIME.strftime("%Y%m%d_%H%M%S")
