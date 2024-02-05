def SplitType(strList):
    digits = []
    alphas = []
    special_chars = []

    for element in strList:
        special = ''
        digit = ''
        alpha = ''
        for i in element:
            if i.isdigit():
                digit += i
            elif i.isalpha():
                alpha += i
            else:
                special += i
        alphas.append(alpha)   
        digits.append(digit)
        special_chars.append(special)
    return alphas,digits,special_chars



OriginalList = ['A@10', 'BMW!320i', 'Nissan-NSX200', 'Benz-220c']

chars,digits,specials = SplitType(OriginalList)

print(f"List of digits = {digits}")
print(f"List of chars = {chars}")
print(f"List of special chars = {specials}")




    

