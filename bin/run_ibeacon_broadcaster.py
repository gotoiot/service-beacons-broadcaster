from ibeacon.services import *

if __name__ == "__main__":
    print("Starting to run iBeacon Broadcaster")
    settings = ibeacon_get_settings()
    ibeacon_print_settings(**settings)
    ibeacon_start_broadcaster(**settings)