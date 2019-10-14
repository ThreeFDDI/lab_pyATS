import logging
from genie.testbed import load
from genie.conf.base.device import Device
from genie.utils.diff import Diff

# load testbed file
tb = load('my_testbed.yaml')

# init routes list
routes = []

# loop over devices
for dev in tb.devices:
    # print each device name
    print(dev)
    # connect to each deivce
    device = tb.devices[dev]
    # disable logging
    device.connect(log_stdout=False)

    # send command and parse output
    routes.append(device.parse('show ip route vrf Mgmt-intf'))

    # print device routing table
    print(routes)

# Diff routing tables   
print("\nDiff:")
diff = Diff(routes[0], routes[1])
diff.findDiff()
print(diff)
