from ibeacon.services import *

if __name__ == "__main__":
    print("Stopping iBeacon Broadcaster")
    settings = ibeacon_get_settings()
    ibeacon_stop_broadcaster(**settings)