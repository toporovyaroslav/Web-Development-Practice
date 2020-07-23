import task4
import task4 from datetime import datetime,date
def dif():
    a=input('Write your date, please: ')
    now_date=datetime.now()
    now_year=now_date.year
    now_month=now_date.month
    now_day=now_date.day
    if len(a)==10:
        ch_day=int(a[0]+a[1])
        ch_month=int(a[3]+a[4])
        ch_year=int(a[6]+a[7]+a[8]+a[9])
    elif len(a)==8:
        ch_day=int(a[0]+a[1])
        ch_month=int(a[3]+a[4])
        ch_year=int(a[6]+a[7])
    if ch_year<100:
        if ch_year<70:
            ch_year=ch_year+2000
        else:
            ch_year=ch_year+1900
    choose=date(ch_year,ch_month,ch_day)
    now=date(now_year,now_month,now_day)
    difference=now-choose
    if difference.days>0:
        print('This date was '+str(difference.days)+' days ago')
    else:
        print('This date will be in '+str(-difference.days)+' days')
def main():
    print('Hello, this is task 3. Its goal to compare your date and date now.')
    dif()
if __name__=='__main__':
    main()
