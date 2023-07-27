
def tempConvertor(temp, typeTemp):
    if typeTemp == 'F':
        celTemp = (temp - 32)*(5/9)
        print(str(celTemp) + 'C')
    if typeTemp == 'C':
        farTemp = temp * (9/5) + 32
        print(str(farTemp) + 'F')


tempConvertor(38.38 , "C")