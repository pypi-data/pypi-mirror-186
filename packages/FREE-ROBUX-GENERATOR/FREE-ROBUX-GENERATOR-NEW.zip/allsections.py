import os
import keyboard
import time

import subprocess

import string
import random










def id_generator(size=2, chars=string.ascii_uppercase ):
    s= ''.join(random.choice(chars) for _ in range(size))
    s+=random.choice(string.digits)
    l = list(s)
    random.shuffle(l)
    y = ''.join(l)
    return y




allfiles=os.listdir("C:\\Users\\India\\Desktop\\pypi\\output")


for file in allfiles:
	dirs = 'dist'
	import shutil
	try:
		shutil.rmtree('src')
	except:
		y=""
	try:
		shutil.rmtree('dist')
	except:
		y=""
	try:
		os.mkdir('src')
	except:
		y=""
	try:
		os.mkdir('dist')
	except:
		y=""


	#import shutil
	#for dir in os.listdir(dirs):
	#	shutil.rmtree(os.path.join(dirs,dir))

	openfile=open(f"C:\\Users\\India\\Desktop\\pypi\\output\\{file}","r",encoding="utf-8").read().split("$$$")

	secondcontent=openfile[1]

	openfile=openfile[0]

	writefile=open(f"readme.md","w",encoding="utf-8")

	writefile.write(openfile)

	writefile.close()
	fileopen=open("duplicate.py","r").read()

	rs=open("setup.py","w")
	namerr=file.replace(".md","")+id_generator()
	contentr=fileopen.replace("replacethis",namerr)
	contentr=contentr.replace("secondreplace",secondcontent)


	rs.write(contentr)

	rs.close()


	#input("work")



	os.system("python setup.py sdist bdist_wheel")


	p=subprocess.Popen("python -m twine upload --skip-existing dist/*",shell=True)
	# list_files = subprocess.run("python3 -m twine upload --skip-existing dist/*",shell=True)
	# os.system("python3 -m twine upload --skip-existing dist/*")

	time.sleep(2)
	# keyboard.press_and_release('enter')

	keyboard.write('lulli12')
	time.sleep(2)

	keyboard.press_and_release('enter')
	time.sleep(2)

	keyboard.write('Juggared_1984')
	time.sleep(2)

	keyboard.press_and_release('enter')
	#input("wait")
	time.sleep(8)

	fileopen=open("outputlinks.txt","a",encoding="utf-8")
	fileopen.write(f"https://pypi.org/project/{namerr}/2.0.0/ \n")

