from enum import Enum

import hid
from aenum import MultiValueEnum

from .protocol import Report, Config


class SupportedDevices(MultiValueEnum):
    """Enumeration with supported product ID's"""

    # product ID determines if mouse is plugged in (8209 plugged in, 8226 not)
    MODEL_O_WIRELESS = 8209, 8226


class GloriousDevice:
    def __new__(cls, device_dict):
        """Returns a device class depending on the device_dict passed in"""

        # alias SupportedDevices so it's easier to access
        SD = SupportedDevices

        if device_dict["vendor_id"] != 9610:
            raise ValueError("Invalid device_dict!")

        product_id = device_dict["product_id"]
        product = SD(product_id) # raises ValueError if no device was found

        if product == SD.MODEL_O_WIRELESS:
            device = ModelOWireless(device_dict)
            device.open(device_dict["vendor_id"], device_dict["product_id"])
        
        return device

    @staticmethod
    def find_all(device_dicts: list[dict, ...] = None) -> list[dict, ...]:
        if device_dicts is None:
            device_dicts = hid.enumerate()

        found_devices = []
        supported_devices = []

        # check for glorious vendor id
        for device_dict in device_dicts:
            if device_dict["vendor_id"] == 9610:
                found_devices.append(device_dict)
        
        # get device product strings
        for device in found_devices:
            device_product_strings = [
                supported_device["product_string"]
                for supported_device in supported_devices
            ]
        
        # get all supported product id's
        supported_product_ids = [
            item for subtuple in [x.values for x in SupportedDevices]
            for item in subtuple
        ]

        # remove duplicates and create list
        if (device["product_id"] in supported_product_ids
            and device["product_string"] not in device_product_strings):
            supported_devices.append(device)

        return supported_devices


class ModelOWireless(hid.device):
    def __init__(self, device_dict: dict):
        super().__init__()

        self.device_dict = device_dict
    
    @property
    def battery(self) -> int:
        # get battery percentage
        data = Report.get(Report.BATTERY, device=self)
        self.battery_percent = data[8]

        return self.battery_percent
    
    @property
    def wired(self) -> bool:
        all_device_dicts = hid.enumerate()

        # product ID determines if it's wired; remove it
        def new_dict(old_dict):
            new = old_dict.copy()
            new.pop('product_id')
            return new

        all_without_product_id = [
            new_dict(device_dict)
            for device_dict in all_device_dicts
        ]
        own_without_product_id = new_dict(self.device_dict)

        index = all_without_product_id.index(own_without_product_id)
        product_id = all_device_dicts[index]['product_id']
        if product_id == 8209:
            return True # mouse is wired 
        elif product_id == 8226:
            return False
    
    @property
    def firmware(self) -> str:
        if self.wired:
            data = Report.get(Report.FIRMWARE_WIRED, device=self)
        else:
            data = Report.get(Report.FIRMWARE_WIRELESS, device=self)
        
        self.firmware_version = f"{data[7]}.{data[8]}.{data[9]}.{data[10]}"

        return self.firmware_version


    @property
    def profile(self) -> int:
        raise NotImplementedError # TODO
    
    @profile.setter
    def profile(self, val: int):
        Config.send(Config.PROFILE, self, val)