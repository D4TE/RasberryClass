import sys
year= sys.stdin.readline()
year= int(year)

a = int(4)
b = int(100)
c = int(400)

if (year%a) ==0 and (year%b) != 0 or (year%c)==0:
    print('1')
else :
    print('0')
