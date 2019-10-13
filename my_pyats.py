from genie.testbed import load
from genie.conf.base.device import Device

tb = load('my_testbed.yaml')

for dev in tb.devices:
    print(dev)
    device = tb.devices[dev]
    device.connect()
    sh_ip_int = device.parse('show ip interface brief')
    print(sh_ip_int)


