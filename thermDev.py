# -*- coding: UTF-8 -*-
import subprocess as sb

__temp_str = lambda: sb.check_output([r'cat',r'/sys/class/thermal/thermal_zone0/temp'])
__temp_int = lambda: int(__temp_str(), 10)

cpu_temp = lambda: float(__temp_int())/1000.0

if __name__ == '__main__':
    print(u"CPU Temperature: {} °C".format(cpu_temp()) )

