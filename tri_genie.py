import logging
from genie.testbed import load
from genie.conf.base.device import Device
from genie.utils.diff import Diff

pre_post = input("Please enter 'pre' or 'post' for testing phase: ")

# load testbed file
tb = load('tri_testbed.yaml')

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
    
    routes = device.parse('show ip route')
    
    with open(f"{dev}-{pre_post}.info", "w+") as f:
        f.write(str(routes))

    if pre_post == 'post':
        pass
        # Diff routing tables   
        #print("Diff:")
        #diff = Diff(routes[0], routes[1])
        #diff.findDiff()
        #print(diff)

    
    # send command and parse output
    #routes.append()

    # print device routing table
    print()

