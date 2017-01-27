####################################################
##
## Coded By  : 1337r00t
# # # # # # # # # # # # # # # # # # # # # # # # # #
## List File : 
# # # # # # # # # # # # # # # # # # # # # # # # # #
## Instagram : 1337r00t
##
## Twitter : 1337r00t
##
## Emaile : 
##
####################################################
import os
import time
import hashlib

class CrackHash(object):
	def __init__(self, Hash, List, Type):
		self.Hash = Hash
		self.List = List
		self.Type = Type.lower()

	def h4sh(self):
		Types = {32: "md5", 40: "sha1", 56: "sha224", 64: "sha256", 96: "sha384", 128: "sha512"}

		try:
			if(Types[len(self.Hash)] == self.Type):
				CrackHash.Lis7(self)

			else:
				print "Invalid Hash or Type"
				Stop = raw_input()
				main()

		except KeyError:
			print "Invalid Hash or Type"
			Stop = raw_input()
			main()

	def Lis7(self):
		try:
			L1st = open(self.List, "r")
			L1st.close()
			CrackHash.CrackHash(self)

		except IOError:
			print "file not found"
			Stop = raw_input()
			main()

	def CrackHash(self):
		Open = open(self.List, "r")
		data = (Open.read()).split()
		timeStart = time.clock()

		Typ3 = {"md5": hashlib.md5(), "sha1": hashlib.sha1(), "sha224": hashlib.sha224(), "sha256": hashlib.sha256(), "sha384": hashlib.sha384(), "sha512": hashlib.sha512()}

		for x in data:
			Password = x
			Try = Typ3[self.Type]
			Try.update(Password)
			print "[*] trying %s" % Password

			if Try.hexdigest() == self.Hash:
				print "[+] found: %s [+]" % Password
				break

			else:
				print "[-] not found: %s [-]" % Password
				print Try.hexdigest()

def main():
	os.system("cls")
	print "..........................................................................."
	print ".%%%%....%%%%%%..%%%%%%..%%%%%%.......%%%%%%\...../%%%\..../%%%\....%%%%%%."
	print "...%%........%%......%%.....(%/.......%%....%)...%:...:%..%:...:%.....%%..."
	print "...%%....%%%%%%..%%%%%%....(%/........%%%%)%.)...%:...:%..%:...:%.....%%..."
	print "...%%........%%......%%...(%/.........%%...\%)...%:...:%..%:...:%.....%%..."
	print ".%%%%%%..%%%%%%..%%%%%%..(%...........%%....\%)...\%%%/....\%%%/......%%..."
	print "..........................................................................."
	print "[Ctrl] + [C] = Exit"
	Hash = raw_input("Hash: ")
	List = raw_input("ListFile: ")
	os.system("cls")
	print "Types: [MD5] - [SHA1] (Only)"
	Type = raw_input("Type Hash: ")
	os.system("cls")
	crack = CrackHash(Hash, List, Type)
	crack.h4sh()

if __name__ == '__main__':
	main()
