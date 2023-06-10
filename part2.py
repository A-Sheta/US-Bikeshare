def filter ():
    print('Hello! Let\'s explore some US bikeshare data!')

    city_dict = {'1':'chicago', '2':'new york city', '3':'washington'}
    city_choice = input('Please select a city to review its data? \n 1: Chicaco\n 2: New York\n 3: Washington DC\n(Select 1,2 or 3):\n')
    while city_choice not in city_dict:
        city_choice = input('\n 1: Chicaco\n 2: New York\n 3: Washington DC\n(Select 1,2 or 3):\n')
    city = city_dict[city_choice]
    print('Great! you Chose {}.\n'.format(city.title()))

    months = ['january', 'february', 'march', 'april', 'may', 'june']
    month_filter = input('Do you want to filter by month?\n(yes or no)\n')
    while str(month_filter).lower() not in ['yes' , 'no']:
        print('please enter a value (yes) or (no)\n')
        month_filter = input('\n')
    if str(month_filter).lower() == 'no':
        month = 'all'
        print('OK')
        
    else:
        month_selection = input('OK select a month:\n1: January\n2: February\n3: March\n4: April\n5: May\n6: June\n')
        while month_selection not in ['1', '2', '3', '4', '5', '6']:
            month_selection = input('Please select a value from 1 to 6\n')
         
      
        month = months[int(month_selection)-1]
        print('Data to will be filtered by {}.\n'.format(month.title()))
        
        
        
    print('-'*40)
    return city, month
filter()