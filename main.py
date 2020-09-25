bandwidth = {}  # {"{server}-{interface_name}": bandwidth_value, ...}
output_headers = ('Timestamp', 'Server', 'Network Interface', 'Network Bandwidth Utilization')
OUTPUT = "{} | {} | {} | {}"

def parsecsv(csvpath):
	"""open (csvpath) and parse contents into 2D array of rows (minus the header row)"""
	with open(csvpath) as f:
		contents = f.read().strip()
		rows = [line.split(',') for line in contents.split('\n')]
		rows.pop(0)		# remove header row
	return rows			# [[r1c1, r1c2, ...], [r2c1, r2c2, ...], ... ]

def get_bandwidth_values():
	"""use built-in hash function to record bandwith value for unique "{server}{interface_name}" hash"""
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