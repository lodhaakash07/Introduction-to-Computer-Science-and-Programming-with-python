s= '1.23,2.4,3.123'

total = 0
for number in s.split(','):
    total += float(number)
print total    