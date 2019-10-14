from genie.testbed import load
from genie.conf.base.device import Device
import logging

# load testbed file
tb = load('my_testbed.yaml')

# loop over devices
for dev in tb.devices:
    # print each device name
    print(dev)
    # connect to each deivce
    device = tb.devices[dev]
    # disable logging
    device.connect(log_stdout=False)

    # send command and parse output
    sh_ip_int = device.parse('show ip interface brief')
    
    # loop over interfaces
    for int in sh_ip_int['interface']:
        # check if interface is up
        if sh_ip_int['interface'][int]['status'] == 'up':
            # print interface name and ip address
            print(f"{int}: {sh_ip_int['interface'][int]['ip_address']}")
