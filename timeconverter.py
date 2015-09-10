# Unix Epoch Timestamp Converter version 1.1
# Author: Marshall University Network Forensics
# Converts Unix Epoch timestamps commonly found in
# Email headers and converts to HH:MM:SS value


# Allows raw input to input Epoch timestamp when run

s = raw_input("Enter your number for conversion: ")
try:
	s = int(s)
	i = s
except:

	i = int(s, 16)

# Imports Epoch value

import datetime

timestamp = i 

value = datetime.datetime.fromtimestamp(timestamp)

# Converts & prints Epoch timestamp in HH:MM:SS value

print(value.strftime('%Y-%m-%d %H:%M:%S'))

