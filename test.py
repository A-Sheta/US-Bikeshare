print('Hello! Let\'s explore some US bikeshare data!')
city_dict = {'a':'chicago', 'b':'new york city', 'c':'washington'}
city_choice = input('Please select a city to review its data? \n a - Chicaco\n b - New York\n c - Washington DC\n(Select a,b or c):\n')
city = city_dict[city_choice]
print('Great! you Chose {}.'.format(city.title()))