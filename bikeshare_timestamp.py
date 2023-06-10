import time
import pandas as pd
import numpy as np

CITY_DATA = { 'chicago': 'chicago.csv',
              'new york city': 'new_york_city.csv',
              'washington': 'washington.csv' }

def get_filters():
    """
    Asks user to specify a city, month, and day to analyze.

    Returns:
        (str) city - name of the city to analyze
        (str) month - name of the month to filter by, or "all" to apply no month filter
        (str) day - name of the day of week to filter by, or "all" to apply no day filter
    """
    print('Hello! Let\'s explore some US bikeshare data!\n.\n..\n...\n')
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
        print('\nData to will be filtered by {}.\n'.format(Month.title()))

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


def load_data(city, month, day):
    """
    Loads data for the specified city and filters by month and day if applicable.

    Args:
        (str) city - name of the city to analyze
        (str) month - name of the month to filter by, or "all" to apply no month filter
        (str) day - name of the day of week to filter by, or "all" to apply no day filter
    Returns:
        df - Pandas DataFrame containing city data filtered by month and day
    """
    df = pd.read_csv(CITY_DATA[city])
    df['Start Time'] = pd.to_datetime(df['Start Time'])

    # extract month and day of week from Start Time to create new columns
    df['month'] = df['Start Time'].dt.month
    df['day_of_week'] = df['Start Time'].dt.weekday_name


    # filter by month if applicable
    if month != 'all':
        df = df[df['month']== month]

    # filter by day of week if applicable
    if day != 'all':
        df = df[df['day_of_week'] == day.title()]
    
    raw_data = input('\nDo you want to take a look on a sample of the raw data before calculating data statistics?\n(yes or no)\n')
    while str(raw_data).lower() not in ['yes' , 'no']:
        raw_data = input('please enter a value (yes) or (no)\n')
 
    if str(raw_data).lower() == 'yes':
        x = 0
        print(df.iloc[x:x+5 , 1:9])
        raw_data2 = input('\nContinue loading raw data before going to Statistical calculations? \n(yes) or (no)\n')
        while str(raw_data2).lower() not in ['yes' , 'no']:
            raw_data2 = input('please enter a value (yes) or (no)\n')
        while str(raw_data2).lower() == 'yes':
            x += 5
            print(df.iloc[x:x+5 , 1:9])
            raw_data2 = input('Continue loading raw data or skip to Statistical calculations? (yes) or (no)\n')
    else:
        print('\n OK, going to Statistical data\n')
    print("\n\n\nLet's go to The Statistical calculations\n.\n..\n...\n")
    return df


def time_stats(df):
    """Displays statistics on the most frequent times of travel."""

    print('\nCalculating The Most Frequent Times of Travel...\n')
    start_time = time.time()

    # TO DO: display the most common month
    if df['month'].nunique != '1':
        popular_month = df['month'].mode()[0]
        print('Most Popular Month       >>>   ({})'.format(popular_month))
    # TO DO: display the most common day of week
    if df['day_of_week'].nunique != '1':
        popular_day = df['day_of_week'].mode()[0]
        print('Most Popular Day         >>>   ({})'.format(popular_day))
        
    # TO DO: display the most common start hour
    df['hour'] = df['Start Time'].dt.hour
    popular_hour = df['hour'].mode()[0]
    print('Most Popular Start Hour  >>>   ({})'.format(popular_hour))


    print("\nThis took %s seconds." % (time.time() - start_time))
    print('-'*40)

def station_stats(df):
    """Displays statistics on the most popular stations and trip."""

    print('\nCalculating The Most Popular Stations and Trip...\n')
    start_time = time.time()

    # TO DO: display most commonly used start station
    popular_start = df['Start Station'].mode()[0]
    print('Most Popular Start Station  >>>   ({})'.format(popular_start))

    # TO DO: display most commonly used end station
    popular_end = df['End Station'].mode()[0]
    print('Most Popular End Station    >>>   ({})'.format(popular_end))

    # TO DO: display most frequent combination of start station and end station trip
    df['trip'] = 'from (' + df['Start Station']+ ') to (' + df['End Station']+')'
    popular_trip = df['trip'].mode()[0]
    print('Most Popular trip           >>>   ({})'.format(popular_trip))

    print("\nThis took %s seconds." % (time.time() - start_time))
    print('-'*40)


def trip_duration_stats(df):
    """Displays statistics on the total and average trip duration."""

    print('\nCalculating Trip Duration...\n')
    start_time = time.time()

    # TO DO: display total travel time
    total_time = df['Trip Duration'].sum()/3600
    print('Total trips travel time    >>>   ({} hours)'.format(total_time))
   
    # TO DO: display mean travel time
    average_time = df['Trip Duration'].mean()/60
    print('Average trip travel time   >>>   ({} minutes)'.format(average_time))

    print("\nThis took %s seconds." % (time.time() - start_time))
    print('-'*40)


def user_stats(df):
    """Displays statistics on bikeshare users."""

    print('\nCalculating User Stats...\n')
    start_time = time.time()

    # TO DO: Display counts of user types
    user_types = df['User Type'].value_counts()
    print('User types:\n{}\n'.format(user_types))


    # TO DO: Display counts of gender
    if 'Gender' in df:
        user_genders = df['Gender'].value_counts()
        print('\nTrip User genders: \n{}.'.format(user_genders))

    # TO DO: Display earliest, most recent, and most common year of birth
        earliest_birthyear = df['Birth Year'].min()
        print('\nEarliest year of birth: \n{}'.format(int(earliest_birthyear)))
        recent_birthyear = df['Birth Year'].max()
        print('\nMost recent year of birth: \n{}'.format(int(recent_birthyear)))
        common_birthyear = df['Birth Year'].mode()[0]
        print('\nMost common year of birth: \n{}'.format(int(common_birthyear)))

    print("\nThis took %s seconds." % (time.time() - start_time))
    print('-'*40)


def main():
    while True:
        city, month, day = get_filters()
        df = load_data(city, month, day)

        time_stats(df)
        station_stats(df)
        trip_duration_stats(df)
        user_stats(df)

        restart = input('\nWould you like to restart? Enter yes or no.\n')
        if restart.lower() != 'yes':
            break


if __name__ == "__main__":
	main()
