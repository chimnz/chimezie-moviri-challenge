bandwidth = {}  # {"{server}-{interface_name}": bandwidth_value, ...}
output_headers = ('Timestamp', 'Server', 'Network Interface', 'Network Bandwidth Utilization')
OUTPUT = "{} | {} | {} | {}"

def parsecsv(csvpath):
	with open(csvpath) as f:
		contents = f.read().strip()
		data = [line.split(',') for line in contents.split('\n')]
		data.pop(0)	# remove header line
	return data

def get_bandwidth_values():
	# use built-in hash function to record unique bandwith value for each distinct server and interface combo
	for server, interface_name, bandwidth_value  in parsecsv('bandwidth.csv'):
		bandwidth_hash = hash(server+interface_name)
		bandwidth[ bandwidth_hash ] = bandwidth_value

def print_network_bandwidth_utilization():
	header = OUTPUT.format(*output_headers)
	print(header + '\n' + '-'*len(header))
	for timestamp, server, interface_name, netbitrate in parsecsv('netbitrate.csv'):
		bandwidth_value = bandwidth[ hash(server+interface_name) ]
		network_bandwidth_utilization = float(netbitrate) / float(bandwidth_value)
		print(OUTPUT.format(timestamp, server, interface_name, network_bandwidth_utilization))

get_bandwidth_values()
print_network_bandwidth_utilization()