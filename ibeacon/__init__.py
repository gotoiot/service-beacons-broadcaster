#!/usr/bin/python3
import os
import subprocess
import sys
import re
import getopt
import uuid
import time


def _get_random_uuid():
    return uuid.uuid4().hex


def _hexsplit(string):
    """ Split a hex string into 8-bit/2-hex-character groupings separated by spaces"""
    return ' '.join([string[i:i+2] for i in range(0, len(string), 2)])


def _hexify(i, digits=4):
    """ convert an integer into a hex value of a given number of digits"""
    format_string = "0%dx" % digits
    return format(i, format_string).upper()


def _process_command(command):
    print(f" | >>> {command}")
    os.system(command)


def _is_valid_device(device):
    """ check to see if the hci device is valid
    # kind of a cheaty way of doing this, we just grep the output of
    # `hcitool list' to make sure the passed-in device string is present"""
    return not os.system("hciconfig list 2>/dev/null | grep -q ^%s:" % device)


def _get_cli_args(**default_settings):
    parser = argparse.ArgumentParser(
        description='Help of usage iBeacon broadcaster'
        )
    parser.add_argument(
        "-u", "--uuid", 
        metavar='major',
        type=str,
        help="iBeacon UUID",
        default=default_settings['uuid']
        )
    parser.add_argument(
        "-m", "--major",
        metavar='major',
        type=int,
        help='The iBeacon major',
        default=default_settings['major']
        )
    parser.add_argument(
        "-n", "--minor",
        metavar='minor',
        type=int,
        help='The iBeacon minor',
        default=default_settings['minor']
        )
    parser.add_argument(
        "-p", "--power",
        metavar='power',
        type=int,
        help='The iBeacon power',
        default=default_settings['power']
        )
    args = parser.parse_args()
    return vars(args)


def _get_hci_keys(**kwargs):
    return {
        'hci_uuid': _hexsplit(kwargs['uuid']),
        'hci_major': _hexsplit(_hexify(kwargs['major'], 4)),
        'hci_minor': _hexsplit(_hexify(kwargs['minor'], 4)),
        'hci_power': _hexify(kwargs['power'], 2),
    }


def ibeacon_get_settings():
    settings = {
        'device': os.getenv("DEVICE", "hci0"),
        'uuid': os.getenv("IBEACON_UUID", "E20A39F473F54BC4A12F17D1AD07A961"),
        'major': int(os.getenv("IBEACON_MAJOR", "0")),
        'minor': int(os.getenv("IBEACON_MINOR", "0")),
        'power': int(os.getenv("IBEACON_POWER", "200")),
    } 
    cli_args = _get_cli_args(**settings)
    settings.update(cli_args)
    settings['uuid'] = settings['uuid'].replace("-", "")
    hci_settings = _get_hci_keys(**settings)
    settings.update(hci_settings)
    return settings


def ibeacon_print_settings(**kwargs):
    print(f"Advertising on device {kwargs['device']}. Parameters:")
    print(f"       uuid: 0x{kwargs['uuid']}")
    print(f"major/minor: {kwargs['major']}/{kwargs['minor']} (0x{kwargs['hci_major']}/0x{kwargs['hci_minor']})")
    print(f"      power: {kwargs['power']} (0x{kwargs['hci_power']})")


def ibeacon_start_broadcaster(**kwargs):
    print (f"Starting iBeacon broadcasting on {kwargs['device']}")
    _process_command(f"hciconfig {kwargs['device']} up")
    _process_command(f"hciconfig {kwargs['device']} leadv")
    _process_command(f"hciconfig {kwargs['device']} noscan")
    _process_command(f"hcitool -i {kwargs['device']} cmd 0x08 0x0008 1E 02 01 1A 1A FF 4C 00 02 15 {kwargs['hci_uuid']} {kwargs['hci_major']} {kwargs['hci_minor']} {kwargs['hci_power']} 00 >/dev/null")


def ibeacon_stop_broadcaster(**kwargs):
    print (f"Starting iBeacon broadcasting on {kwargs['device']}")
    _process_command(f"hciconfig {kwargs['device']} noleadv")
    _process_command(f"hciconfig {kwargs['device']} piscan")
    _process_command(f"hciconfig {kwargs['device']} down")

