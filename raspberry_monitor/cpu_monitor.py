import os

cpu_usage = lambda: os.popen("top -n1 | awk '/Cpu\(s|):/ {print $2}'").readline()

if __name__ == '__main__':
	print(cpu_usage())
