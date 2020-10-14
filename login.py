import hash
import getpass

H = hash.hash()

def init():
	ifile = open('permission.pass','r')

	global users
	global hashes

	users = list()
	hashes = list()

	for i in ifile.readlines():
		users.append(i.strip().split()[0])
		hashes.append(i.strip().split()[1])

	ifile.close()

init()

while True:
	print("Press 's' and then hit Enter to sign-up!")

	user = input('UserName: ')

	if user == 's':
		user = input('\nEnter New UserName: ')
		if user in users:
			print('UserName already taken.\n')
			continue
		p = getpass.getpass('Enter New Password: ')
		if p == getpass.getpass('Confirm Password: '):
			f = H.hash(p)
			ofile = open('permission.pass','a')
			ofile.write(user + ' ' + f + '\n')
			ofile.close()
			init()
			print()		
			continue
		else:
			print("Passwords don't Match!\n")
			continue
	if user not in users:
		print('\nUser does not exist!')
		print('Try again\n')
		continue	

	f = hashes[users.index(user)]	
	#print(f)
	p = getpass.getpass(prompt = 'Password: ')

	if H.hash(p) == f:
		print('\nYou have logged in sucessfully!\n')
		F = input('Enter F to change password.\n')			
		if F == 'f' or F == 'F':
			p = getpass.getpass('Enter New Password: ')
			if p == getpass.getpass('Confirm Password: '):
				hashes[users.index(user)] = H.hash(p)
			ofile = open('permission.pass','w')
			for i in range(len(users)):			
				ofile.write(users[i] + ' ' + hashes[i] + '\n')
			ofile.close()
			init()
			print('Password changed sucessfully!')
			print()				
		break
	else:
		print('\nWrong Password!')
		print('Try Again!\n')

