print('PROJECT: Simple Text-Based Calculator\n')
def get_num(number):
    while True:
        num=input("Enter Number"+str(number)+ ":")
        try:
            return float(num)
            # num=float(num)
            # break
        except:
            print("\nInvalid Operand, Try Again!")
    # return num

num1=get_num(1)
num2=get_num(2)
signs={'Addtition':'+',
      'Subtraction':'-',
      'Multiplication':'*',
      'Division':'/',
      'Floor Division':'//',
      'Exponential':'**',
      'Modulus':'%',}
print("\nList of Operations ->")
for i in signs:
      print(i,signs[i],sep=": ")
sign=input('Sign :')
# Valid=False #Creating a flag
# while True:
#     try:
#         num1=float(num1)
#         num2=float(num1)
#         Valid=True
#         break
#     except:
#         print("\nInvalid Operand, Try Again!")
#         continue
result=0
if sign=='+':
    print("\nAddition :")
    result=(num1)+(num2)
elif sign=='-':
    print("\nSubtraction :")
    result=(num1)-(num2)
elif sign=='*':
    print("\nMultiplication :")
    result=(num1)*(num2)
elif sign=='/':
    if (num2)!=0:
        print("\nDivision :")
        result=(num1)/(num2)   
    else:
        print("Division By Zero...")
elif sign=='//':
    if (num2)!=0:
        print("\nFloor Division :")
        result=(num1)//(num2)
    else:
                print("Division By Zero...")
elif sign=='**':
            print('\nExponential :')
            result=(num1)**(num2)
elif sign=='%':
            print("\nModulus :")
            result=(num1)%(num2)
else:
    print('\nInvalid sign!')
print(result,'\n\nTHANK YOU, VISIT AGAIN!')