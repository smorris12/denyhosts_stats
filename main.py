# imports
import re

# open our hosts.deny file
hosts_file = tuple(open('hosts.deny', 'r'))

# for next the lines into an array for processing
ip_list = []

for line in hosts_file:

    if line.find("sshd:") != -1:
        ip_address = re.findall('(?:[\d]{1,3})\.(?:[\d]{1,3})\.(?:[\d]{1,3})\.(?:[\d]{1,3})', line)

        ip_list.append(ip_address[0])

ip_list.sort()

for items in ip_list:
	print items
