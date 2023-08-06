from __future__ import annotations

import time
from enum import Enum

import hid


class Report(list, Enum):
    BATTERY = [
        0, 0, 0, 2, 2, 0, 131, 0, 0, 0, 0, 0, 0,
        0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0,
        0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0,
        0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0,
        0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0,
    ]

    # if device is wired 4th element should be 2 instead of 0
    FIRMWARE_WIRELESS = [
        0, 0, 0, 0, 3, 0, 129, 0, 0, 0, 0, 0, 0,
        0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0,
        0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0,
        0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0,
        0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0,
    ]
    FIRMWARE_WIRED = [
        0, 0, 0, 2, 3, 0, 129, 0, 0, 0, 0, 0, 0,
        0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0,
        0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0,
        0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0,
        0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0,
    ]


    @staticmethod
    def get(report: Report, device: hid.device) -> list[int, ...]:
        device.send_feature_report(report)
        time.sleep(0.1) # wait for device to send back data
        data = device.get_feature_report(report_num=0, max_length=65)

        return data


class Config(list, Enum):
    PROFILE = [
        0, 0, 0, 2, 1, 0, 5, None, 0, 0, 0, 0, 0,
        0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0,
        0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0,
        0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0,
        0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0,
    ]


    @classmethod
    def send(cls, config: Config, device: hid.device, *args):
        if not args:
            raise ValueError("At least one argument is required for *args!")
        elif len(args) != len([x for x in config if x is None]):
            # None in a list represents an argument that needs to be supplied
            # so if the user didn't supply enough arguments to fill the list:
            raise ValueError("Not enough arguments were supplied!")

        # replace all items that are None with user arguments
        args_list = list(args)
        device.send_feature_report([
                val if val is not None else args_list.pop(0)
                for val in config
        ])
