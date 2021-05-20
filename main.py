
def _get_welcome_message():
    welcome_message = """\n
          /$$$$$$            /$$                    /$$$$$$      /$$$$$$$$
         /$$__  $$          | $$                   |_  $$_/     |__  $$__/
        | $$  \__/ /$$$$$$ /$$$$$$   /$$$$$$         | $$   /$$$$$$| $$   
        | $$ /$$$$/$$__  $|_  $$_/  /$$__  $$        | $$  /$$__  $| $$   
        | $$|_  $| $$  \ $$ | $$   | $$  \ $$        | $$ | $$  \ $| $$   
        | $$  \ $| $$  | $$ | $$ /$| $$  | $$        | $$ | $$  | $| $$   
        |  $$$$$$|  $$$$$$/ |  $$$$|  $$$$$$/       /$$$$$|  $$$$$$| $$   
         \______/ \______/   \___/  \______/       |______/\______/|__/   

                        SERVICE BEACONS BROADCASTER
                        ---------------------------

    * Run iBeacon broadcaster:
        docker-compose run beacons-broadcaster \\
            python bin/run_ibeacon_broadcaster.py \\
                --device hci0 --major 20 --minor 10 --power 200

    * Stop iBeacon broadcaster 
        docker-compose run beacons-broadcaster \\
            python bin/stop_ibeacon_broadcaster.py --device hci0

    """
    return welcome_message


if __name__ == "__main__":
    print(_get_welcome_message())
