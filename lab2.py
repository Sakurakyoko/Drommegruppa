limit_sum = 4999

def int_to_roman (integer):

    returnstring=''
    table=[['M',1000],['CM',900],['D',500],['CD',400],['C',100],['XC',90],['L',50],['XL',40],['X',10],['IX',9],['V',5],['IV',4],['I',1]]

    for pair in table:

        while integer-pair[1]>=0:

            integer-=pair[1]
            returnstring+=pair[0]

    return returnstring

def rom_to_int(string):

    table=[['M',1000],['CM',900],['D',500],['CD',400],['C',100],['XC',90],['L',50],['XL',40],['X',10],['IX',9],['V',5],['IV',4],['I',1]]
    returnint=0
    for pair in table:


        continueyes=True

        while continueyes:
            if len(string)>=len(pair[0]):

                if string[0:len(pair[0])]==pair[0]:
                    returnint+=pair[1]
                    string=string[len(pair[0]):]

                else: continueyes=False
            else: continueyes=False

    return returnint


def rom_or_int():
    answer = int(input("1 for decimal to roman, 2 for roman to decimal: "))
    
    if (answer == 1):
        print int_to_roman(input("Enter decimal number to convert to roman: "))
    elif (answer == 2):
        print rom_to_int(raw_input("Enter roman number to convert to decimal: " ))
    else:
        print "Error: Choose 1 or 2"

rom_or_int()

def add_roman(x, y):
    table=[['M',1000],['CM',900],['D',500],['CD',400],['C',100],['XC',90],['L',50],['XL',40],['X',10],['IX',9],['V',5],['IV',4],['I',1]]
    rom_sum = rom_to_int(x) + rom_to_int(y)
    
    if rom_sum <= limit_sum:
    
        int_to_roman(rom_sum)
        print ("Roman sum: %s + %s = %s" % (x, y, int_to_roman(rom_sum)))
        

print add_roman("VI","X")

def subtract_roman(x, y):
    table=[['M',1000],['CM',900],['D',500],['CD',400],['C',100],['XC',90],['L',50],['XL',40],['X',10],['IX',9],['V',5],['IV',4],['I',1]]
    rom_sum = rom_to_int(x) - rom_to_int(y)
    
    if rom_sum <= limit_sum:
    
        int_to_roman(rom_sum)
        print ("Roman sum: %s + %s = %s" % (x, y, int_to_roman(rom_sum)))
        

print subtract_roman("V","IV")

def multiply_roman(x, y):
    table=[['M',1000],['CM',900],['D',500],['CD',400],['C',100],['XC',90],['L',50],['XL',40],['X',10],['IX',9],['V',5],['IV',4],['I',1]]
    rom_sum = rom_to_int(x) * rom_to_int(y)
    
    if rom_sum <= limit_sum:
    
        int_to_roman(rom_sum)
        print ("Roman sum: %s + %s = %s" % (x, y, int_to_roman(rom_sum)))
        

print multiply_roman("X","X")
