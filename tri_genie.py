import logging, json, sys
from genie.testbed import load
from genie.conf.base.device import Device
from genie.utils.diff import Diff

# init variable to control pre / post testing
pre_post = "post"

# prompt user to set variable to control pre / post testing
while pre_post not in ["pre", "post"]:
    pre_post = input("Please enter 'pre' or 'post' for testing phase: ").lower()

# load testbed file
tb = load('tri_testbed.yaml')

# loop over devices
for dev in tb.devices:
    # connect to each deivce
    device = tb.devices[dev]
    # disable logging
    device.connect(log_stdout=False)
    # grab routing table from each device
    routes = device.parse('show ip route')
    # save routing table output to file
    with open(f"{dev}_{pre_post}.info", "w+") as f:
        json.dump(routes, f)

    # additional processing for post testing
    if pre_post == 'post':
        # load pre-change routing table from file
        with open(f"{dev}_pre.info", "r") as f:
            pre = json.load(f)
            
        # load post-change routing table from file
        with open(f"{dev}_post.info", "r") as f:
            post = json.load(f)
        
        # set diff variables and exlude "updated" field
        diff = Diff(pre, post, exclude="updated")
        # diff pre/post files
        diff.findDiff()
        # write diff to file
        with open(f"{dev}.diff", "w+") as f:
            f.write(str(diff))
        # print message for end of device processing
        print(f"{dev} diff results written to file.")
