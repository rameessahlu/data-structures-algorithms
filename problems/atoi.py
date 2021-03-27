def atoi(str):
    result = 0
    for s in str:
        result = (result*10) +(ord(s)-ord('0'))
    return result
    
print(atoi('160345'))