from genie.testbed import load
from genie.conf.base.device import Device
import logging

#
tb = load('my_testbed.yaml')

for dev in tb.devices:
    print(dev)
    device = tb.devices[dev]
    device.connect(log_stdout=False)

    sh_ip_int = device.parse('show ip interface brief')
    
    for int in sh_ip_int['interface']:
        if sh_ip_int['interface'][int]['status'] == 'up':
            print(f"{int}: {sh_ip_int['interface'][int]['ip_address']}")
