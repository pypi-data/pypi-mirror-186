# -*- coding: utf-8 -*-
from setuptools import setup

packages = \
['mqtt_io',
 'mqtt_io.config',
 'mqtt_io.config.validation',
 'mqtt_io.modules',
 'mqtt_io.modules.gpio',
 'mqtt_io.modules.sensor',
 'mqtt_io.modules.stream',
 'mqtt_io.mqtt',
 'mqtt_io.tests.features',
 'mqtt_io.tests.features.steps']

package_data = \
{'': ['*']}

install_requires = \
['Cerberus>=1.3.2,<2.0.0',
 'PyYAML>=5.4,<6.0',
 'asyncio-mqtt>=0.8.1,<0.9.0',
 'backoff>=1.10.0,<2.0.0',
 'confp>=0.4.0,<0.5.0',
 'typing-extensions>=3.7.4,<4.0.0']

extras_require = \
{':python_version >= "3.6" and python_version < "3.7"': ['dataclasses>=0.8,<0.9']}

setup_kwargs = {
    'name': 'mqtt-io',
    'version': '2.2.8',
    'description': 'Expose GPIO modules (Raspberry Pi, Beaglebone, PCF8754, PiFace2 etc.), digital sensors (LM75 etc.) and serial streams to an MQTT server for remote control and monitoring.',
    'long_description': "<!--\n***************************************************************************************\nDO NOT EDIT README.md DIRECTLY, IT'S GENERATED FROM README.md.j2 USING generate_docs.py\n***************************************************************************************\n-->\n\n# MQTT IO\n\n[![Discord](https://img.shields.io/discord/713749043662290974.svg?label=Chat%20on%20Discord&logo=discord&logoColor=ffffff&color=7389D8&labelColor=6A7EC2)](https://discord.gg/gWyV9W4)\n\nExposes general purpose inputs and outputs (GPIO), hardware sensors and serial devices to an MQTT server. Ideal for single-board computers such as the Raspberry Pi.\n\nVisit the [documentation](https://mqtt-io.app/) for more detailed information.\n\n## Supported Hardware\n\nHardware support is provided by specific GPIO, Sensor and Stream modules. It's easy to add support for new hardware and the list is growing fast.\n\n### GPIO Modules\n\n  - Beaglebone GPIO (`beaglebone`)\n  - Linux Kernel 4.8+ libgpiod (`gpiod`)\n  - GPIO Zero (`gpiozero`)\n  - MCP23017 IO expander (`mcp23017`)\n  - Orange Pi GPIO (`orangepi`)\n  - PCF8574 IO expander (`pcf8574`)\n  - PCF8575 IO expander (`pcf8575`)\n  - PiFace Digital IO 2 (`piface2`)\n  - Raspberry Pi GPIO (`raspberrypi`)\n\n### Sensors\n\n  - ADS1x15 analog to digital converters (`ads1x15`)\n  - AHT20 temperature and humidity sensor (`aht20`)\n  - BH1750 light level sensor (`bh1750`)\n  - BME280 temperature, humidity and pressure sensor (`bme280`)\n  - BME680 temperature, humidity and pressure sensor (`bme680`)\n  - DHT11/DHT22/AM2302 temperature and humidity sensors (`dht22`)\n  - DS18S20/DS1822/DS18B20/DS1825/DS28EA00/MAX31850K temperature sensors (`ds18b`)\n  - HCSR04 ultrasonic range sensor (connected to the Raspberry Pi on-board GPIO) (`hcsr04`)\n  - INA219 DC current sensor (`ina219`)\n  - LM75 temperature sensor (`lm75`)\n  - MCP3008 analog to digital converter (`mcp3008`)\n\n### Streams\n\n  - Serial port (`serial`)\n  - PN532 NFC/RFID reader (`pn532`)\n\n## Installation\n\n_Requires Python 3.6+_\n\n`pip3 install mqtt-io`\n\n## Execution\n\n`python3 -m mqtt_io config.yml`\n\n## Configuration Example\n\nConfiguration is written in a YAML file which is passed as an argument to the server on startup.\n\nSee the [full configuration documentation](https://github.com/flyte/pi-mqtt-gpio/wiki/Configuration) for details.\n\nThe following example will configure the software to do the following:\n\n- Publish MQTT messages on the `home/input/doorbell` topic when the doorbell is pushed and released.\n- Subscribe to the MQTT topic `home/output/port_light/set` and change the output when messages are received on it.\n- Periodically read the value of the LM75 sensor and publish it on the MQTT topic `home/sensor/porch_temperature`.\n- Publish any data received on the `/dev/ttyUSB0` serial port to the MQTT topic `home/serial/alarm_system`.\n- Subscribe to the MQTT topic `home/serial/alarm_system/send` and send any data received on that topic to the serial port.\n\n```yaml\nmqtt:\n  host: localhost\n  topic_prefix: home\n\n# GPIO\ngpio_modules:\n  # Use the Raspberry Pi built-in GPIO\n  - name: rpi\n    module: raspberrypi\n\ndigital_inputs:\n  # Pin 0 is an input connected to a doorbell button\n  - name: doorbell\n    module: rpi\n    pin: 0\n\ndigital_outputs:\n  # Pin 1 is an output connected to a light\n  - name: porch_light\n    module: rpi\n    pin: 1\n\n# Sensors\nsensor_modules:\n  # An LM75 sensor attached to the I2C bus\n  - name: lm75_sensor\n    module: lm75\n    i2c_bus_num: 1\n    chip_addr: 0x48\n\nsensor_inputs:\n  # The configuration of the specific sensor value to use (LM75 only has temperature)\n  - name: porch_temperature\n    module: lm75_sensor\n\n# Streams\nstream_modules:\n  # A serial port to communicate with the house alarm system\n  - name: alarm_system\n    module: serial\n    device: /dev/ttyUSB0\n    baud: 9600\n```",
    'author': 'Ellis Percival',
    'author_email': 'mqtt-io@failcode.co.uk',
    'maintainer': 'None',
    'maintainer_email': 'None',
    'url': 'None',
    'packages': packages,
    'package_data': package_data,
    'install_requires': install_requires,
    'extras_require': extras_require,
    'python_requires': '>=3.6,<4.0',
}


setup(**setup_kwargs)
