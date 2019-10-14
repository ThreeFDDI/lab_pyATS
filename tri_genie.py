import logging, json, sys
from genie.testbed import load
from genie.conf.base.device import Device
from genie.utils.diff import Diff

# init variable to control pre / post testing
pre_post = None

# prompt user to set variable to control pre / post testing
while pre_post not in ["pre", "post"]:
    pre_post = input("Please enter 'pre' or 'post' for testing phase: ").lower()

# load testbed file
tb = load('tri_testbed.yaml')

# init routes list
routes = []

# loop over devices
for dev in tb.devices:
    # connect to each deivce
    device = tb.devices[dev]
    # disable logging
    device.connect(log_stdout=False)
    
    routes = device.parse('show ip route')
    
    with open(f"{dev}-{pre_post}.info", "w+") as f:
        json.dump(routes, f)

    if pre_post == 'post':
        pass
        with open(f"{dev}-pre.info", "r") as f:
            pre = json.load(f)
        with open(f"{dev}-post.info", "r") as f:
            post = json.load(f)
        
        # Diff routing tables   
        print(f"{dev} diff:")
        print("~"*10)
        # set diff variable and exlude "updated" field
        diff = Diff(pre, post, exclude="updated")
        # diff pre/post files
        diff.findDiff()
        # print dif
        print(diff)
        print()

