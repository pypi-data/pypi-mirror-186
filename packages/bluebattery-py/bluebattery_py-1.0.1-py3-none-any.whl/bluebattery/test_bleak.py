import asyncio
import logging
import signal

import coloredlogs
from bleak import BleakClient, BleakScanner, exc

# Set up logging with colored output
coloredlogs.install(level="DEBUG")

# Set bleak logger to INFO
logging.getLogger("bleak").setLevel(logging.INFO)



class SmartSolar(BLEDevice):
    FILTERS = [{"name": "SmartSolar "}]

    def handle_char_306b0002(self, data):
        # Get the first two bytes and interpret them as a 16-bit unsigned integer
        battery_voltage = int.from_bytes(data[:2], byteorder="little")

        # Get the next two bytes and interpret them as a 16-bit unsigned integer
        pv_voltage = int.from_bytes(data[2:4], byteorder="little")

        # Get the next two bytes and interpret them as a 16-bit signed integer
        pv_current = int.from_bytes(data[4:6], byteorder="little", signed=True)

        # Get the final byte and interpret it as an 8-bit unsigned integer
        charge_current = data[6]

        print(f"Battery voltage: {battery_voltage}")
        print(f"PV voltage: {pv_voltage}")
        print(f"PV current: {pv_current}")
        print(f"Charge current: {charge_current}")

    def handle_char_97580002(self, data):
        # Get the first two bytes and interpret them as a 16-bit signed integer
        temperature = int.from_bytes(data[:2], byteorder="little", signed=True)

        # Get the next two bytes and interpret them as a 16-bit unsigned integer
        charge_voltage = int.from_bytes(data[2:4], byteorder="little")

        # Get the next two bytes and interpret them as a 16-bit unsigned integer
        charge_current = int.from_bytes(data[4:6], byteorder="little")

        # Get the next two bytes and interpret them as a 16-bit unsigned integer
        battery_voltage = int.from_bytes(data[6:8], byteorder="little")

        # Get the next two bytes and interpret them as a 16-bit signed integer
        battery_current = int.from_bytes(data[8:10], byteorder="little", signed=True)

        # Get the next four bytes and interpret them as a 32-bit unsigned integer
        battery_capacity = int.from_bytes(data[10:14], byteorder="little")

        # Get the next four bytes and interpret them as a 32-bit signed integer
        battery_power = int.from_bytes(data[14:18], byteorder="little", signed=True)

        # Get the final two bytes and interpret them as a 16-bit unsigned integer
        yield_today = int.from_bytes(data[18:], byteorder="little")

        print(f"Temperature: {temperature}")
        print(f"Charge voltage: {charge_voltage}")
        print(f"Charge current: {charge_current}")
        print(f"Battery voltage: {battery_voltage}")
        print(f"Battery current: {battery_current}")
        print(f"Battery capacity: {battery_capacity}")
        print(f"Battery power: {battery_power}")
        print(f"Yield today: {yield_today}")

    def handle_char_97580006(self, data):
        self.log.error("Not implemented yet.")

    HANDLERS = {
        "306b0002-b081-4037-83dc-e59fcc3cdfd0": handle_char_306b0002,
        "97580002-ddf1-48be-b73e-182664615d8e": handle_char_97580002,
        "97580006-ddf1-48be-b73e-182664615d8e": handle_char_97580006,
    }



