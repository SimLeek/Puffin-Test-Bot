import subprocess as sp

wifi_str = lambda: sp.check_output(['nmcli','-f','SIGNAL,SSID,CHAN,RATE,SECURITY,MODE','d','wifi','list'])

if __name__ == '__main__':
	print(wifi_str())
