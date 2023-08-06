import asyncio
import logging
import signal

import coloredlogs
from bleak import BleakClient, BleakScanner, exc

# Set up logging with colored output
coloredlogs.install(level="DEBUG")

# Set bleak logger to INFO
logging.getLogger("bleak").setLevel(logging.INFO)


class BLEDevice:
    HANDLERS = []
    FILTERS = []
    PAIRING_REQUIRED = True

    def __init__(self, device, loop):
        self.device = device
        self.loop = loop
        self.log = logging.getLogger(f"Device {device.name}")
        self.log.setLevel(logging.DEBUG)

    @classmethod
    def filter(cls, device):
        for f in cls.FILTERS:
            if "name" in f:
                if device.name.startswith(f["name"]):
                    return True
            if "address" in f:
                if device.address.startswith(f["address"]):
                    return True
        return False

    async def run(self):
        self.log.info("Starting...")
        # connect to device
        async with BleakClient(self.device.address, loop=self.loop) as client:
            # read device name
            # name = await client.read_gatt_char("00002a00-0000-1000-8000-00805f9b34fb")
            # self.log.debug(f"Device name: {name.decode('utf-8')}")

            if self.PAIRING_REQUIRED:
                res = await client.pair(protection_level=3)
                self.log.debug(f"Pairing result: {res!r}")

            readable_characteristics = []

            disconnected_event = asyncio.Event()

            def disconnect_callback(client):
                self.log.info(f"Disconnected!")
                self.loop.call_soon_threadsafe(disconnected_event.set)

            client.set_disconnected_callback(disconnect_callback)

            # read characteristics
            for service in client.services:
                self.log.debug(f"Service: {service.uuid}")
                for characteristic in service.characteristics:
                    self.log.debug(f"  Characteristic: {characteristic.uuid}")

                    # check if characteristic is readable
                    self.log.debug(characteristic.properties)
                    if "read" in characteristic.properties:
                        # value = await client.read_gatt_char(characteristic.uuid)
                        # self.log.debug(f"    Value: {value}")
                        readable_characteristics.append(characteristic.uuid)

                    if "notify" in characteristic.properties:
                        self.log.debug("    Subscribing to notifications...")
                        try:
                            await client.start_notify(
                                characteristic.uuid, notify_callback
                            )
                        except Exception as e:
                            self.log.exception("Error subscribing to notifications")

            # run this task forever
            while True:
                # read all readable characteristics
                for characteristic in readable_characteristics:
                    try:
                        value = await client.read_gatt_char(characteristic)
                    except Exception as e:
                        self.log.exception(
                            "Error reading characteristic {characteristic}"
                        )
                        return
                    # print the characteristic and its value as a hex array, grouped in bytes
                    self.log.debug(
                        f"  {characteristic}: {' '.join(f'{b:02x}' for b in value)}"
                    )
                    # call the respective handler, if it exists
                    if characteristic in self.HANDLERS:
                        self.HANDLERS[characteristic](self, value)
                await asyncio.sleep(1.0)


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


class BlueBattery(BLEDevice):
    FILTERS = [{"name": "BlueBattery_"}]
    PAIRING_REQUIRED = False

    def handle_live(self, data):
        self.log.error("Received LIVE")

    HANDLERS = {
        "4b616912-40bd-428b-bf06-698e5e422cd9": handle_live,
    }


async def notify_callback(sender, data):
    print(f"XXXXXXXXXXXX Notification from {sender}: {data}")


KNOWN_DEVICES = (
    #SmartSolar,
    BlueBattery,
)

# default logger
log = logging.getLogger(__name__)
log.setLevel(logging.DEBUG)


async def scan_and_connect(tasks, loop):
    device_list = []

    # scan for devices
    devices = await BleakScanner.discover(timeout=5.0, loop=loop)
    for device in devices:
        log.debug(device.metadata)
        for k in KNOWN_DEVICES:
            if k.filter(device):
                log.info(
                    f"Found device: {device.name} ({device.address})"
                )
                device_list.append((k, device))
                break
        else:
            log.info(f"Found other device: {device.name} ({device.address})")

    # ensure discovery has finished
    await asyncio.sleep(2.0)

    if not devices:
        return

    for cls, device in device_list:
        # check if any of the running tasks already covers this device
        if device.address in tasks:
            # if task is running, skip this device
            if not tasks[device.address].done():
                log.debug(f"Task for {device.address} is already running. Skipping.")
                continue
            # if task is done, remove it from the list
            else:
                del tasks[device.address]

        # else create a new task
        log.info(f"Connecting to {device.address}...")
        instance = cls(device, loop)
        try:
            device_task = asyncio.create_task(instance.run())
        except exc.BleakError as e:
            log.exception(f"Error connecting to {device.address}")
        tasks[device.address] = device_task


tasks = {}

async def scanTask():
    loop = asyncio.get_running_loop()
    while True:
        log.info("Scanning for devices...")
        try:
            await scan_and_connect(tasks, loop)
        except exc.BleakError as e:
            log.exception("Error scanning for devices")
        await asyncio.sleep(10.0)


async def main():
    loop = asyncio.get_running_loop()
    loop.create_task(scanTask())
    
    # run until shutdown
    while True:
        await asyncio.sleep(1.0)
    

def shutdown(_, __):
    log.info("Shutting down...")
    for task in tasks.values():
        task.cancel()
    loop = asyncio.get_running_loop()
    loop.stop()


signal.signal(signal.SIGINT, shutdown)
signal.signal(signal.SIGTERM, shutdown)

log.info("Started!")
asyncio.run(main())
