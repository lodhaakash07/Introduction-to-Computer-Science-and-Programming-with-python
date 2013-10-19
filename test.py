counter = 10 
message = 'please,introduce a number: '
odds = False

while(counter != 0):
    number = int(raw_input(message))
    if(counter == 10):
        ans = number
    if (number%2 != 0):
        odds = True
        if (number > ans):
            ans = number
    counter = counter -1
    
if (odds):
    print 'the largest one: ' + str(ans)
else:
    print 'No odds numbers'   
        
    
    