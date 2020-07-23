import random
def num(n):
    print(n)
    result=''
    a=int(input('Write your number, please: '))
    if n>a:
        print('My number is greater')
        result='no'
        num(n)
    elif a>n:
        print('My number is less')
        result='no'
        num(n)
    else:
        print('You guessed my number')
def main():
    print('Hello, this is task 2. Its goal to play with you in game, I choose one number from 1 to 10000. And you try to guess it')
    n=random.randint(1,10000)
    num(n)
if  __name__=='__main__':
    main()
