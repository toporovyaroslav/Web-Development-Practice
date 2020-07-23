a=input('Write integer number from 0 to 30: ')
print(' '+'*'*int(a)+' ')
for i in range(0,int(a)-1,1):
    print('*'+' '*int(a)+'*')
print('*'*(int(a)+2))
for i in range(0,int(a),1):
    print('*'+' '*int(a)+'*')
