# Simple BLE Sniffer
import bluetooth
import logging
from datetime import datetime
import time
import argparse

def sniff():
    nearbyDevices = bluetooth.discover_devices(lookup_names=True)
    #print("Found {} devices.".format(len(nearbyDevices)))

    for addr, name in nearbyDevices:
        #print("  {} - {}".format(addr, name))
        if name == targetDevice:
            found = True
            break
        else:
            found = False

    # Returns a datetime object containing the local date and time
    dateTime = datetime.now()

    if found:
        print(dateTime, ": ", targetDevice, " detected.")
        log.debug("%s detected", targetDevice)
    else:
        print(dateTime, ": ", targetDevice, " NOT detected.")
        log.debug("%s NOT detected", targetDevice) 

if __name__ == '__main__':
    argparser = argparse.ArgumentParser(
            description="Simple BLE Sniffer"
    )

    # Positional/Optional parameters
    argparser.add_argument('--interval', help="loop interval", type=int)
    argparser.add_argument('--iteration', help="number of iterations", type=int)

    # Parse the arguments
    args = argparser.parse_args()

    # set up logging
    logging.basicConfig(filename="bleSniffer.log", 
                        format='%(asctime)s %(message)s', 
                        filemode='a')   # append
    log = logging.getLogger();
    log.setLevel(logging.DEBUG)

    targetDevice = "Tatskie's iPhone"

    for i in range(args.iteration):    
        sniff()
        time.sleep(args.interval) # there are better ways
