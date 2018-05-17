import subprocess as sp

disk_usage_str = lambda: sp.check_output([r'df',r'-h',r'/'])

if __name__ == '__main__':
	print(disk_usage_str())


