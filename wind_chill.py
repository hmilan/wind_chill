#! /usr/bin/python

import sys

def wc(temp,v):
    return 13.12+0.6215*temp-11.37*(v**0.16)+0.3965*temp*(v**0.16)

# debug: print(wc(float(sys.argv[1]),3.6*float(sys.argv[2])))
# end debug: exit(0)

t=float(sys.argv[1])
winds=sys.argv[2]
convert=3.6 # default input = m/s
wind=winds
if winds.find('km') > 0 :
    convert = 1.0
    wind = winds[:winds.find('km')-2]
if 'm/s' in winds :
    convert = 3.6
    wind = winds[:winds.find('m')-2]
if 'kn' in winds :
    convert = 3.6/1.852 # nautical miles
    wind = winds[:winds.find('kn')-2]

v=float(wind)*convert # for wc() convert to km/h; temp is in C
WC = wc(t,v)

print('wind = {0:.2f} km/h Temp = {1:.1f} C WindChill = {2:.2f} C'.format(v,t,WC))

