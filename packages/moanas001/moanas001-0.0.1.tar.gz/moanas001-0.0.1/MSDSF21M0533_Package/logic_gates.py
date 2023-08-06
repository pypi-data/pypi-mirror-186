######## This is a module contains functions to perform Logical gate operations on strings ########

################################### Function for AND Gate ##########################################

def And(a,b):
    result = ''
    if len(a) != len(b):
        return 'Use Strings of same length'
    for i,j in zip(a,b):
        if int(i) > 1 or int(i) <0 or int(j) > 1 or int(j) <0:
            return 'Use binary number as string, String contains digit greater than 1 or less than 0'
        result = result + str(int(i)&int(j))
    return result

################################### Function for OR Gate ##########################################

def Or(a,b):
    result = ''
    if len(a) != len(b):
        return 'Use Strings of same length'
    for i,j in zip(a,b):
        if int(i) > 1 or int(i) <0 or int(j) > 1 or int(j) <0:
            return 'Use binary number as string, String contains digit greater than 1 or less than 0'
        result = result + str(int(i)|int(j))
    return result

################################### Function for NOT Gate ##########################################

def Not(a):
    result = ''
    for i in a:
        if int(i) > 1 or int(i) <0:
            return 'Use binary number as string, String contains digit greater than 1 or less than 0'
        result = result + str(int(not int(i)))
    return result


################################### Function for NOR Gate ##########################################

def Nor(a,b):
    orResult = Or(a,b)
    result = Not(orResult)
    return result


################################### Function for NAND Gate ##########################################

def Nand(a,b):
    andResult = And(a,b)
    result = Not(andResult)
    return result

################################### Function for XOR Gate ##########################################

def Xor(a,b):
    result = ''
    if len(a) != len(b):
        return 'Use Strings of same length'
    for i,j in zip(a,b):
        if int(i) > 1 or int(i) <0 or int(j) > 1 or int(j) <0:
            return 'Use binary number as string, String contains digit greater than 1 or less than 0'
        result = result + str(int(i)^int(j))
    return result

################################### Function for XNOR Gate ##########################################

def Xnor(a,b):
    xnorResult = Xor(a,b)
    result = Not(xnorResult)
    return result

######################################################################################################





