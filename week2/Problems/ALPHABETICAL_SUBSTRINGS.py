s = 'usuustzabcfgehxwhrmmp'

def get_alphabetical_substring(s):
    offset = ''
    ans = ''
    temp = ''
    for letter in s: 
        if letter >= offset:            
            temp += letter
        else:                        
            temp = letter   
        offset = letter
        if len(temp) > len(ans):               
                ans = temp                                     
    return ans
print  get_alphabetical_substring(s)                      
            
    