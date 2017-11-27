from pwn import *
import string

never = remote("neverending.tuctf.com",12345)
char_set = "abcdefghijklmnopqrstuvwxyzABCDEFGHIJKLMNOPQRSTUVWXYZ0123456789 !\"#$%&\'()*+,-./:;<=>?@[\\]^_`{|}~\s"

def char_convert(message,n=95):
	pass

def round1(char="ABCDEFGHIJKLMNOPQRSTUVWXY"):
	never.sendlineafter("text:",char)
	#recv = never.recvuntil(Round 1. Give me some text:)
	enc_base = never.recvline().split("is ")[1]
	enc_msg = never.recvline().split("is ")[1]
	enc_msg = enc_msg.split(" decrypted?\n")[0]
	log.info("ENC BASE : -> {}".format(enc_base))
	log.info("ENC MSG : -> {}".format(enc_msg))
	cal = ord(char[0]) - ord(enc_base[0])
	dec = "".join([chr(ord(b) + cal) for b in enc_msg])
	
	non_printable = [ chr(ord(z)) for z in dec if z not in char_set]
	printable = "".join([ chr(ord(z)+95) for z in non_printable if z not in char_set])
	for i in range(len(printable)):
	    dec = dec.replace(non_printable[i],printable[i])

	non_printable2 = [ chr(ord(z)) for z in dec if z not in char_set]
	printable2 = "".join([ chr(ord(z)-190) for z in non_printable2 if z not in char_set])
	for i in range(len(printable2)):
	    dec = dec.replace(non_printable2[i],printable2[i])

	log.info("Decrypted -> {}".format(repr(dec)))
	never.sendlineafter(":",dec)

for i in range(100):
	try:
		log.info("Round {0}".format(i))
		round1()
		if never.recvline().split()[0] == "Correct!":
			log.info("-> BENAR")
			continue
		log.info("-> SALAH")
	except:
		print never.recv()
		never.close()
		break
# Round complete!
# TUCTF{wh0_w@s_her3_la5t_ye@r?!?}
# That's all folks. What did you think there would be more?


	
