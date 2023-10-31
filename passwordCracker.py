import crypt
import hashlib

def crack_salted_passwords():
	shadow = open(input("Enter your file: "), "r")
	password = input("Enter your password file: ")
	results = open("saltedPasswordResults.txt", "w")
	tempPass = password
	count = 0
	tf=False
	line = shadow.readline()
	with open(password) as f:
    		pw = f.read().splitlines()
	while line:
		for passw in pw:
			passwSplit=passw.split("\n")
			temp = line.split(":")
			splitTemp = temp[1].rsplit("$", 1)
			print("\n"+temp[0])
			print(splitTemp[0])
			print(passwSplit[0])
			if(splitTemp[0] != "!" and temp[0] != "cs4351"):
				cryptTemp = crypt.crypt(passwSplit[0], splitTemp[0])
				cryptTemp = cryptTemp.split("$")
				print(cryptTemp[3])
				print(splitTemp[1])
				if(cryptTemp[3] == splitTemp[1]):
					results.write(temp[0]+":"+passwSplit[0]+"\n")
					count+=1
					tf=True
					break
			else:
				break
		if(password != tempPass):
			password == tempPass
		if(tf==False):
			diff = input("Would you like to try a diffrent dictionary? Y/N\n")
			if(diff == "Y"):
				password = input("Enter your new password file: ")
			if(diff == "N"):
				line = shadow.readline()
		elif(tf==True):
			line = shadow.readline()
			tf=False
	shadow.close()
	results.close()
	print(count)

def unsaltedPassword():
	shadow = open(input("Enter your file: "), "r")
	password = input("Enter your password file: ")
	results = open("unsaltedPasswordResults.txt", "w")
	count = 0
	tf=False
	line = shadow.readline()
	with open(password) as f:
    		pw = f.read().splitlines()
	while line:
		for passw in pw:
			passwSplit=passw.split("\n")
			if(len(passwSplit[0])<6):
				pw.remove(passw)
				continue
			temp = line.split(":")
			tempPW = temp[1].split("\n")
			print("\n"+temp[0])
			print(passwSplit[0])
			result = hashlib.md5(passwSplit[0].encode()).hexdigest()
			print(result)
			print(tempPW[0])
			if(result == tempPW[0]):
				results.write(temp[0]+":"+passwSplit[0]+"\n")
				count+=1
				tf=True
				break
			elif(10-len(passwSplit[0]) < 10):
				tempInt = 10-len(passwSplit[0])-1
				tempInt1 = '9'+'9'*tempInt
				for i in range(int(tempInt1)+1):
					tempResult = passwSplit[0]+str(i)
					print("\n"+temp[0])
					print(tempResult)
					result = hashlib.md5(tempResult.encode()).hexdigest()
					print(result)
					print(tempPW[0])
					if(result == tempPW[0]):
						results.write(temp[0]+":"+passwSplit[0]+str(i)+"\n")
						count+=1
						tf=True
						break
			if(tf == True):
				break
			for passw2 in pw:
				passwSplit2=passw2.split("\n")
				if(len(passwSplit2[0])<6):
					pw.remove(passw2)
					continue
				print("\n"+temp[0])
				tempPass = passwSplit[0]+passwSplit2[0]
				print(tempPass)
				result = hashlib.md5(tempPass.encode()).hexdigest()
				print(result)
				print(tempPW[0])
				if(result == tempPW[0]):
					results.write(temp[0]+":"+passwSplit[0]+passwSplit2[0]+"\n")
					count+=1
					tf=True
					break
			if(tf == True):
				break
		if(tf == False):
			for i in range(00000000,99999999):
				temp = line.split(":")
				print("\n"+temp[0])
				tempStr = str(i).zfill(8)
				print(tempStr)
				result = hashlib.md5(str(i).encode()).hexdigest()
				print(result)
				print(temp[1])
				if(result == temp[1]):
					results.write(temp[0]+":"+str(i)+"\n")
					count+=1
					tf=True
					break
			if(tf==False):
				line = shadow.readline()
		if(tf == True):
			line = shadow.readline()
			tf=False	
	shadow.close()
	results.close()
	print(count)		
	
def knowsaltedPassword():
	shadow = open(input("Enter your file: "), "r")
	password = input("Enter your password file: ")
	results = open("saltedPasswordResults.txt", "w")
	count = 0
	tf=False
	line = shadow.readline()
	with open(password) as f:
    		pw = f.read().splitlines()
	while line:
		for passw in pw:
			passwSplit=passw.split("\n")
			if(len(passwSplit[0])<6):
				pw.remove(passw)
				continue
			temp = line.split(":")
			tempPW = temp[2].split("\n")
			print("\n"+temp[0])
			print(passwSplit[0])
			tempPass = temp[1]+passwSplit[0]
			print(passwSplit[0])
			result = hashlib.md5(tempPass.encode()).hexdigest()
			print(result)
			print(tempPW[0])
			if(result == tempPW[0]):
				results.write(temp[0]+":"+passwSplit[0]+"\n")
				count+=1
				tf=True
				break
			elif(10-len(passwSplit[0]) < 10):
				tempInt = 10-len(passwSplit[0])-1
				tempInt1 = '9'+'9'*tempInt
				for i in range(int(tempInt1)+1):
					tempResult = temp[1]+passwSplit[0]+str(i)
					print("\n"+temp[0])
					print(passwSplit[0]+str(i))
					result = hashlib.md5(tempResult.encode()).hexdigest()
					print(result)
					print(tempPW[0])
					if(result == tempPW[0]):
						results.write(temp[0]+":"+passwSplit[0]+str(i)+"\n")
						count+=1
						tf=True
						break
			if(tf == True):
				break
			for passw2 in pw:
				passwSplit2=passw2.split("\n")
				if(len(passwSplit2[0])<6):
					pw.remove(passw2)
					continue
				print("\n"+temp[0])
				tempPass = temp[1]+passwSplit[0]+passwSplit2[0]
				print(tempPass)
				result = hashlib.md5(tempPass.encode()).hexdigest()
				print(result)
				print(tempPW[0])
				if(result == tempPW[0]):
					results.write(temp[0]+":"+passwSplit[0]+passwSplit2[0]+"\n")
					count+=1
					tf=True
					break
			if(tf == True):
				break
		if(tf == False):
			for i in range(00000000,99999999):
				temp = line.split(":")
				print("\n"+temp[0])
				tempStr = temp[1]+str(i).zfill(8)
				print(tempStr)
				result = hashlib.md5(str(i).encode()).hexdigest()
				print(result)
				print(temp[1])
				if(result == temp[1]):
					results.write(temp[0]+":"+tempStr+"\n")
					count+=1
					tf=True
					break
			if(tf==False):
				line = shadow.readline()
		if(tf == True):
			line = shadow.readline()
			tf=False	
	shadow.close()
	results.close()
	print(count)	
	
knowSalt = input("Do we have the full shadow file? Y/N\n")
if(knowSalt == "Y"):
	crack_salted_passwords()
else:
	knowSalt = input("Do we know that salt and encryption? Y/N\n")
	if(knowSalt == "Y"):
		knowsaltedPassword()
	else:
		unsaltedPassword()
