#!/usr/local/bin/python3

from genie.utils.config import Config
from genie.utils.diff import Diff
from genie.testbed import load

tb = load('my_testbed.yaml')

for device_name, device in tb.devices.items():
    device.connect()
    startup = device.execute("show startup")
    startup_config = Config(startup)
    startup_config.tree()

    running = device.execute("show running")
    running_config = Config(running)
    running_config.tree()

    diff = Diff(running_config, startup_config)
    diff.findDiff()
    print(diff)