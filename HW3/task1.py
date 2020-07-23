def country():
    top=['Russia','China','India','Kazakhstan','Saudi Arabia','Iran','Mongolia','United States','Canada','Brazil','Argentina','Greenland','Mexico','Peru','Australia','Indonesia','Antarctica','Algeria','Democratic Republic of Congo','Sudan','Libya','Chad','Niger','Angola','Mali']
    Asia=['Asia','Russia','China','India','Kazakhstan','Saudi Arabia','Iran','Mongolia']
    America=['America','United States','Canada','Brazil','Argentina','Greenland','Mexico','Peru']
    Oceania=['Oceania','Australia','Indonesia']
    Africa=['Africa','Algeria','Democratic Republic of Congo','Sudan','Libya','Chad','Niger','Angola','Mali']
    Antarctica=['Antarctica']
    region=[Asia,America,Oceania,Africa,Antarctica]
    a=input('Write a country in top-25(size): ')
    if a.capitalize() in top:
        for i in region:
            if a.capitalize() in i:
                print(i[0])
                print('https://ru.wikipedia.org/wiki/'+a.capitalize())
    else:
        print('You wrote a wrong country, please write again')
        country()
def main():
    country()
if  __name__=='__main__':
    main()
