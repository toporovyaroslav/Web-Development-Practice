def a():
    c=input('Your number( what task do you want to do): ')
    if c=='1':
        import task1
        task1.main()
        a()
    elif c=='2':
        import task2
        task2.main()
        a()
    elif c=='3':
        import task3
        task3.main()
        a()
    else:
        exit()
def main():
    print('Hello, what task do you want to choose?')
    print('Write number from 1 to 3, please')
    a()
if __name__=='__main__':
    main()
