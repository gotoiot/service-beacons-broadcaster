import os
import subprocess
import sys
import re
import getopt
import uuid

device = "hci0"
uuid = "E20A39F473F54BC4A12F17D1AD07A961"
major = 0
minor = 0
power = 200

def hexsplit(string):
    """ Split a hex string into 8-bit/2-hex-character groupings separated by spaces"""
    return ' '.join([string[i:i+2] for i in range(0, len(string), 2)])


def hexify(i, digits=4):
    """ convert an integer into a hex value of a given number of digits"""
    format_string = "0%dx" % digits
    return format(i, format_string).upper()


def process_command(command):
    print(f" | >>> {command}")
    os.system(command)


split_uuid = hexsplit(uuid)
# convert major/minor id into hex
major_hex = hexify(major, 4)
minor_hex = hexify(minor, 4)
# create split versions of these (for the hcitool command)
split_major_hex = hexsplit(major_hex)
split_minor_hex = hexsplit(minor_hex)
# convert power into hex
power_hex = hexify(power, 2)


def print_settings(**kwargs):
    print(f"Advertising on device {device}. Parameters:")
    print(f"       uuid: 0x{uuid}")
    print(f"major/minor: {major}/{minor} (0x{major_hex}/0x{minor_hex})")
    print(f"      power: {power} (0x{power_hex})")


def start_ibeacon_broadcast():
    print (f"Starting iBeacon broadcasting on {device}")
    process_command(f"hciconfig {device} up")
    process_command(f"hciconfig {device} leadv")
    process_command(f"hciconfig {device} noscan")
    process_command(f"hcitool -i {device} cmd 0x08 0x0008 1E 02 01 1A 1A FF 4C 00 02 15 {split_uuid} {split_major_hex} {split_minor_hex} {power_hex} 00 >/dev/null")


def stop_ibeacon_broadcast():
    print (f"Starting iBeacon broadcasting on {device}")
    process_command(f"hciconfig {device} noleadv")
    process_command(f"hciconfig {device} piscan")
    process_command(f"hciconfig {device} down")


if __name__ == "__main__":
    print_settings()
    start_ibeacon_broadcast()
    time.sleep(10)
    stop_ibeacon_broadcast
