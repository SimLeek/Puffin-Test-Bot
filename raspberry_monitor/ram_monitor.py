import subprocess as sp

ram = sp.check_output(['free'])

if __name__ == '__main__':
	print(ram)
