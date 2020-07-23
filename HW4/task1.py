def enc():
    code=input('Write what you want to encrypt: ')
    new_code_1=''
    for i in range(0,len(code)-1,1):
        new_code_1=new_code_1+code[i+1]
        new_code_1=new_code_1+code[i]
    print(new_code_1)
def dec():
    code=input('Write what you want to deccrypt: ')
    new_code=''
    if len(code)>1:
        new_code=new_code+code[1]
        new_code=new_code+code[0]
        for i in range(2,len(code)-1,2):
            new_code=new_code+code[i]
    else:
        print(code)
    print(new_code)
def main():
    print('Helo, this is task 1. Its goal to encrypt or decrypt your letter')
    choice=input('What do you want to do? ')
    if choice=='encrypt':
        enc()
    elif choice=='decrypt':
        dec()
    else:
        print('Error')
if  __name__=='__main__':
    main()
