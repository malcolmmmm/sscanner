import requests
def main(social, infile, outfile):
	with open(infile,'r') as f:
		name=f.read().split('\n')
	possible_user = list()
	for i in range(1,len(name)):
		try:
			url = (social+name[i])
			r = requests.post(url)
			if r.status_code == 404:
				possible_user.append(str(name[i]))
				print('test['+str(i)+'] '+name[i]+' is not in use')
			else:
				print('test['+str(i)+'] '+name[i]+' is in use')
		except:
			print('An error has occured trying next instance....')
	possible_user="\n".join(possible_user)
	with open(outfile,'w') as f:
		f.write(possible_user)
print('''
===============================================================
# __            _       _   __                                 #
#/ _\ ___   ___(_) __ _| | / _\ ___ __ _ _ __  _ __   ___ _ __ #
#\ \ / _ \ / __| |/ _` | | \ \ / __/ _` | '_ \| '_ \ / _ \ '__|#
#_\ \ (_) | (__| | (_| | | _\ \ (_| (_| | | | | | | |  __/ |   #
#\__/\___/ \___|_|\__,_|_| \__/\___\__,_|_| |_|_| |_|\___|_|   #
#                     By:Malcolm McDonough                     #
================================================================
Want to see if somebody owns an account on social media?
Select your option:
	[1]FaceBook
	[2]Twitter
	[3]Instagram
''')
while True:
	social=input("Enter your choice:")
	if social == str(1) or social == str(2) or social == str(3):
		if social == str(1):
			social = 'https://facebook.com/'
		elif social == str(2):
			social = 'https://twitter.com/'
		elif social == str(3):
			social = 'https://instagram.com/'
		break
	else:
		print("you entered a incorrect option...")
while True:
	infile=input("Enter the worldlist file path(must be a .txt file:")
	if '.txt' not in infile:
		print('must be a .txt file')
	else:
		break
while True:
	outfile=input("Enter the file where the info will be stored(must be a .txt file):")
	if '.txt' not in outfile:
		print('must be a .txt file')
	else:
		break
main(social,infile,outfile)
print('process complete check results in:'+outfile)
