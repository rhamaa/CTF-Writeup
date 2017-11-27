import itertools
import string
import hashlib

leters = string.ascii_letters + string.punctuation + string.digits

def generator(n=1):
    a = itertools.product(leters,repeat=n)
    return a

def text3():
	for char in generator(3):
		char = "".join(char)
		possible = "Ooooh so{}salty".format(char)
		hashMD5 = hashlib.md5(possible).hexdigest()
		if hashMD5 == "d0061dcf056a06713d5a757e0288d1b3":
			print "Found Text3 {}".format(char)
			return char
		else:
			continue

def text4():
	for char in generator(1):
		char = "".join(char)
		hash384 = hashlib.sha384(char).hexdigest()
		possible = "Stop trying to crack me god damnit!!!{}".format(hash384)
		hashMD5 = hashlib.md5(possible).hexdigest()
		if hashMD5 == "5056e21f6af2a289c9c3116c16bba55f":
			print "Found Text4 {}".format(char)
			return char
		else:
			continue
def text7():
	hash384 = hashlib.sha384("Oh, i see you reading my source code! >:)").hexdigest()
	for char in generator(2):
		char = "".join(char)
		possible = "{0}{1}".format(hash384,char)
		hashMD5 = hashlib.md5(possible).hexdigest()
		if hashMD5 == "c866a4f386df3da51a54c1f8434603eb":
			print "Found Text7 {}".format(char)
			return char
		else:
			continue	
def text8():
	hash384 = hashlib.sha384(hashlib.sha512("FILL THE POWER OF SHA").hexdigest()).hexdigest()
	for char in generator(2):
		char = "".join(char)
		possible = "{0}{1}".format(hash384,char)
		hashMD5 = hashlib.sha256(possible).hexdigest()
		if hashMD5 == "7f6e2c5beefd0fd0000c3a72db28b54d0819a93f5cc87a48507f79cdac37cfe0":
			print "Found Text8 {}".format(char)
			return char
		else:
			continue	
def main():
	p1 = "541"
	p2 = "____"
	p3 = ""
	p4 = ""
	p5 = "19"
	p6 = "757"
	p7 = ""
	p8 = ""
	p3 += text3()
	p4 += text4()
	p7 += text7()
	p8 += text8()
	print "Flag : SchoolCTF{"+p8[1]+ p8[0]+ p6[1]+ p6[0]+ p2[3]+ p7[1]+ p1[1]+ p1[0]+ p7[0]+ p2[1]+  p1[2]+  p6[2]+  p2[2]+  p3[0]+  'y'+  p2[0]+  p3[1]+  p3[2]+  'r'+  p4[0]+  p5[0]+  'n'+  p5[1]+"}"
if __name__ == '__main__':
	main()
