def get_filters():
    """
    Asks user to specify a city, month, and day to analyze.

    Returns:
        (str) city - name of the city to analyze
        (str) month - name of the month to filter by, or "all" to apply no month filter
        (str) day - name of the day of week to filter by, or "all" to apply no day filter
    """
    print('Hello! Let\'s explore some US bikeshare data!\n.\n..\n..\n')
    
# City    
    cities = {'1':'chicago', '2':'new york city', '3':'washington'}
    city_choice = input('Please select a city to review its data? \n 1: Chicaco\n 2: New York\n 3: Washington DC\n(Select 1,2 or 3):\n')
    while city_choice not in cities:
        city_choice = input('\n 1: Chicaco\n 2: New York\n 3: Washington DC\n(Select 1,2 or 3):\n')
    city = cities[city_choice]
    print('\nGreat! you Chose {}.\n'.format(city.title()))

# Months    
    months = ['january', 'february', 'march', 'april', 'may', 'june']
    month_filter = input('Do you want to filter by month?\n(yes or no)\n')
    while str(month_filter).lower() not in ['yes' , 'no']:
        month_filter = input('please enter a value (yes) or (no)\n')
 
    if str(month_filter).lower() == 'no':
        month = 'all'
        print('\nOK, All months selected')
    else:
        month_choice = input('OK select a month:\n1: January\n2: February\n3: March\n4: April\n5: May\n6: June\n')
        while month_choice not in ['1', '2', '3', '4', '5', '6']:
            month_choice = input('Please select a value from 1 to 6\n')
        Month = months[int(month_choice)-1]
        month = int(month_choice)
        print('\nData to will be filtered by {}.\n'.format(month.title()))

    # TO DO: get user input for day of week (all, monday, tuesday, ... sunday)
# Days    
    days = {'1':'Sunday', '2':'Monday', '3':'Tuesday', '4':'Wednesday', '5':'Thursday', '6':'Friday', '7':'Saturday', '8': 'all'}
    day_choice = input('Please Select days for filter\n1: Sunday       2: Monday       3: Tuesday      4: Wednesday\n5: Thursday     6: Friday       7: Saturday     8: Select all days\nselect a value from 1 to 8\n')
    
    while day_choice not in days:
        city_choice = input('\n1: Sunday       2: Monday       3: Tuesday      4: Wednesday\n5: Thursday     6: Friday       7: Saturday     8: Select all days\nselect a value from 1 to 8\n')

 
    if int(day_choice) == 8:
        day = 'all'
        print('\nOK, All Weekdays selected')
    else:
        day = days[city_choice]
        print('\nYou selected {} to filter by.\n'.format(day.title()))


    print('-'*40)
    return city, month, day


get_filters()

