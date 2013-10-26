s = 'usuustzehxwhrmmp'

def get_alphabetical_substring(s):
    point = ''
    ans = ''
    temp = ''
    for letter in s: 
        if letter >= point:            
            temp += letter
        else:                        
            temp = letter   
        point = letter
        if len(temp) > len(ans):               
                ans = temp                                     
    return ans
print  get_alphabetical_substring(s)                      
            
    