import sys
if len(sys.argv) != 1
temp = float(sys.argv[1])
print(usage:python temp.py <temperature>)
else:
temp = 25
print("No input given - using default temp")
if temp < 15:
  status = "cold"
elif temp <= 30: 
  status = "normal"
else:
  status = "hot"
print("Temperature status:",status)
