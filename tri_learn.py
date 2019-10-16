from genie.testbed import load

my_testbed = load('tri_testbed.yaml')

my_testbed.devices['Tri-CSR-1'].connect(log_stdout=False)

output = my_testbed.devices['Tri-CSR-1'].learn('interface')

print(output.info)

