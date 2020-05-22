# Noob

def toAccounting(number):
    if(number < 0):
        return '(' + str(abs(number)) + ')'
    else:
        return str(number)


# Advanced

def numberToAccounting(number):
    if number != None:
        if(number < 0):
            return f'({str(abs(number))})'
        else:
            return str(number)



#  Pro

def numberToAccountingString(number):
    if number == None: return
    if number < 0: return f'({ str(abs(number)) })'
    return str(number)


if __name__ == "__main__":
    for i in [None, 5, -5, 16]:
        print(numberToAccountingString(i))
