def ChangeDec(input:str):
    total = 0
    for i in input:
        if i.isalpha():
            total += ord(i)
        else:
            return 'Input Error'
    
    return total

print(f"Total Decimal of String is : {ChangeDec('Alex')}")
print(f"Total Decimal of String is : {ChangeDec('John')}")
print(f"Total Decimal of String is : {ChangeDec('Bob-2')}")