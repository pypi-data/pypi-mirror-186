# -*- coding: utf-8 -*-
from setuptools import setup

packages = \
['bluebattery', 'bluebattery.output']

package_data = \
{'': ['*']}

install_requires = \
['bleak>=0.19.5,<0.20.0',
 'coloredlogs>=15.0.1,<16.0.0',
 'hummable>=0.1.0,<0.2.0',
 'paho-mqtt>=1.6.1,<2.0.0',
 'py-flags>=1.1.4,<2.0.0']

setup_kwargs = {
    'name': 'bluebattery-py',
    'version': '1.0.0',
    'description': '',
    'long_description': '# bluebattery.py\n\nSoftware for interacting with the [BlueBattery](https://www.blue-battery.com/) line of battery computers for RVs.\n\nFeatures:\n\n- [x] Reading of periodically sent measurements\n- [x] Publishes value to an MQTT broker\n- [x] Auto-discovery of BB devices\n- [x] Access to stored logs\n- [ ] Modification of device settings\n- [ ] Firmware update\n\n## Changelog\n\n2023-01-14: Moved to bleak library. This should make the software much more reliable. Multiple devices are now supported and the MQTT topic has changed to include the device address.\n\n## Installation\n\n```\nsudo apt-get install python3-pip\n# log out and in again to apply new environment variables \npip3 install git+https://github.com/danielfett/bluebattery.py.git\n```\n\n## Setting up a Systemd Service\n\nSee the [systemd service](assets/bb.service) file for details.\n\n\n## Reading values from the command line\n\n```\n$ bb_cli log\n```\n\nIf you want to see more details of what is going on, use the debug flag:\n\n```\n$ bb_cli --log-level DEBUG log\n```\n\n## Publishing values to an MQTT server\n\nIf you want to use the MQTT features, start the MQTT publisher using\n\n```\n$ bb_cli mqtt\n```\n\nAppend `--help` to see the configuration options.\n\nThis is an example of the values published to the MQTT broker:\n\n```\nservice/bluebattery/FC:45:C3:CA:FF:EE/live/solar_charger_ext/max_solar_current_day_A 0.0\nservice/bluebattery/FC:45:C3:CA:FF:EE/live/solar_charger_ext/max_solar_watt_day_W 0.0\nservice/bluebattery/FC:45:C3:CA:FF:EE/live/solar_charger_ext/solar_charge_day_Ah 0.0\nservice/bluebattery/FC:45:C3:CA:FF:EE/live/solar_charger_ext/solar_energy_day_Wh 0\nservice/bluebattery/FC:45:C3:CA:FF:EE/live/solar_charger_ext/solar_charger_status 1\nservice/bluebattery/FC:45:C3:CA:FF:EE/live/solar_charger_ext/solar_module_voltage_V 0.0\nservice/bluebattery/FC:45:C3:CA:FF:EE/live/solar_charger_ext/relay_status RelayStatus()\nservice/bluebattery/FC:45:C3:CA:FF:EE/live/battery_comp_1/battery_charge_Ah 158.48\nservice/bluebattery/FC:45:C3:CA:FF:EE/live/battery_comp_1/state_of_charge_percent 83.4\nservice/bluebattery/FC:45:C3:CA:FF:EE/live/battery_comp_1/max_battery_current_day_A 0.0\nservice/bluebattery/FC:45:C3:CA:FF:EE/live/battery_comp_1/min_battery_current_day_A -1.1\nservice/bluebattery/FC:45:C3:CA:FF:EE/live/battery_comp_1/max_battery_charge_day_Ah 16.16\nservice/bluebattery/FC:45:C3:CA:FF:EE/live/battery_comp_1/min_battery_charge_day_Ah 15.84\nservice/bluebattery/FC:45:C3:CA:FF:EE/live/battery_comp_1/max_battery_voltage_day_V 12.54\nservice/bluebattery/FC:45:C3:CA:FF:EE/live/battery_comp_1/min_battery_voltage_day_V 12.5\nservice/bluebattery/FC:45:C3:CA:FF:EE/live/info/battery_voltage_V 12.61\nservice/bluebattery/FC:45:C3:CA:FF:EE/live/info/starter_battery_voltage_V 12.43\n```\n\n\n## Troubleshooting\n\nDepending on your environment, you may need to enable BLE first or to set up your linux user to allow using BLE:\n\n### Enabling Bluetooth LE\n\nIf the above command does not work out-of-the-box, you might have to enable Bluetooth Low-Energy. \n\nOn Ubuntu, add the following two lines at the bottom of `/etc/bluetooth/main.conf`:\n\n```\nEnableLE=true\nAttributeServer=true\n```\n\nThen restart bluetooth: `sudo service bluetooth restart`\n\n### On the Raspberry Pi\n\nThis software works on a Raspberry Pi and was tested with the built-in bluetooth device. To use the software as the user `pi` (recommended!), you need to make the dbus policy changes [described here](https://www.raspberrypi.org/forums/viewtopic.php?t=108581#p746917).\n',
    'author': 'Daniel Fett',
    'author_email': 'fett@danielfett.de',
    'maintainer': 'None',
    'maintainer_email': 'None',
    'url': 'None',
    'packages': packages,
    'package_data': package_data,
    'install_requires': install_requires,
    'python_requires': '>=3.7,<4.0',
}


setup(**setup_kwargs)
