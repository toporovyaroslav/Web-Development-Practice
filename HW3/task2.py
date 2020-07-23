def password():
    special=['~',':',"'",'+','[','\\','@','^','{','%','(','-','"','*','|',',','&','<','`','}','.','_','=',']','!','>',';','?','#','$',')','/',' ']
    digit=['1','2','3','4','5','6','7','8','9','0']
    lower_letter=['a','b','c','d','e','f','g','h','i','j','k','l','m','n','o','p','q','r','s','t','u','v','w','x','y','z']
    upper_letter=['A','B','C','D','E','F','G','H','I','J','K','L','M','N','O','P','Q','R','S','T','U','V','W','X','Y','Z']
    a=input('Write a password, please: ')
    num_special=0
    num_digit=0
    num_lowerl_etter=0
    num_upper_letter=0
    if 16>len(a)>9:
        for i in range (0,len(a),1):
            if a[i] in special:
                num_special=num_special+1
            elif a[i] in digit:
                num_digit=num_digit+1
            elif a[i] in lower_letter:
                num_lowerletter=num_lower_letter+1
            elif a[i] in upper_letter:
                num_upperletter=num_upper_letter+1
    else:
        print('Your password is not possible. Write new, please')
        password()
    if num_special>0 and num_digit>0 and num_lower_letter>0 and num_upper_letter>0:
        print('Success')
    else:
        print('Your password is not possible. Write new, please')
        password()
def main():
    password()
if  __name__=='__main__':
    main()
