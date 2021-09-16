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
    print('Hello! Let\'s explore some US bikeshare data!')
    # get user input for city (chicago, new york city, washington). HINT: Use a while loop to handle invalid inputs
    city = ''
    while city not in CITY_DATA.keys():
        print("Hello, please choose a city!")
        city = input().lower()
        if city not in CITY_DATA.keys():
            print("please choose a city from('chicago', 'new york city', 'washington')!")


    # get user input for month (all, january, february, ... , june)
    months_list = ['january', 'february', 'march', 'april', 'may', 'june']
    month = ''
    while month not in months_list and month != 'all':
        print("choose a month")
        month = input().lower()
        if month not in months_list and month != 'all':
            print("please choose from('january', 'february', 'march', 'april', 'may', 'june') or all")


    # get user input for day of week (all, monday, tuesday, ... sunday)
    days_list = [ 'monday', 'tuesday', 'wednesday', 'thursday', 'friday', 'saturday', 'sunday']
    day = ''
    while day not in days_list and day != 'all':
        print("please choose a day!")
        day = input().lower()
        if day not in days_list and day != 'all' :
            print("please choose from('monday', 'tuesday', 'wednesday', 'thursday', 'friday', 'saturday', 'sunday') or all")

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
    df['months'] = df['Start Time'].dt.month
    df['days'] = df['Start Time'].dt.weekday_name
    #Filter by month if applicable
    if month != 'all':
        months_list = ['january', 'february', 'march', 'april', 'may', 'june']
        month = months_list.index(month) + 1
        df = df[df['months'] == month]
    
    #Filter by day of week if applicable
    if day != 'all':
        df = df[df['days'] == day.title()]


    return df


def time_stats(df):
    """Displays statistics on the most frequent times of travel."""

    print('\nCalculating The Most Frequent Times of Travel...\n')
    start_time = time.time()

    # display the most common month
    print(df['months'].mode()[0])


    # display the most common day of week
    print(df['days'].mode()[0])


    # display the most common start hour
    df['hours'] = df['Start Time'].dt.hour
    print(df['hours'].mode()[0])

    print("\nThis took %s seconds." % (time.time() - start_time))
    print('-'*40)


def station_stats(df):
    """Displays statistics on the most popular stations and trip."""

    print('\nCalculating The Most Popular Stations and Trip...\n')
    start_time = time.time()

    # display most commonly used start station
    print(df['Start Station'].mode()[0])


    # display most commonly used end station
    print(df['End Station'].mode()[0])


    # display most frequent combination of start station and end station trip
    df['full_trip'] = df['Start Station'] +' to '+ df['End Station']
    print(df['full_trip'].mode()[0])


    print("\nThis took %s seconds." % (time.time() - start_time))
    print('-'*40)


def trip_duration_stats(df):
    """Displays statistics on the total and average trip duration."""

    print('\nCalculating Trip Duration...\n')
    start_time = time.time()

    # display total travel time
    total_duration = df['Trip Duration'].sum()
    print(total_duration)


    # display mean travel time
    average_duration = df['Trip Duration'].mean()
    print(average_duration)


    print("\nThis took %s seconds." % (time.time() - start_time))
    print('-'*40)


def user_stats(df):
    """Displays statistics on bikeshare users."""

    print('\nCalculating User Stats...\n')
    start_time = time.time()

    # Display counts of user types
    count_user = df['User Type'].value_counts()
    print(count_user)


    # Display counts of gender
    count_gender = df['Gender'].value_counts()
    print(count_gender)


    # Display earliest, most recent, and most common year of birth
    earliest = int(df['Birth Year'].min())
    recent = int(df['Birth Year'].max())
    common_year = int(df['Birth Year'].mode()[0])

    print(earliest, recent, common_year)


    print("\nThis took %s seconds." % (time.time() - start_time))
    print('-'*40)



def show_data(df):
    bin_data = ['yes', 'no']
    user_choice = ''
    start_loc = 0
    while user_choice not in bin_data:
        print("Do you want to show data?")
        user_choice = input().lower()
        if user_choice == 'yes':
            print(df.head())
        elif user_choice not in bin_data:
            print("please choose from('Yes' or 'No'!")
        
    while user_choice == 'yes':
        print("Do you need to show more data?")
        view_display = input("Do you wish to continue?: ").lower()
        start_loc += 5
        if view_display == 'yes':
            end_loc = start_loc + 5
            print(df.iloc[start_loc:end_loc])
        else:
            break
    print('-'*80)
        
def main():
    while True:
        city, month, day = get_filters()
        df = load_data(city, month, day)

        
        time_stats(df)
        station_stats(df)
        trip_duration_stats(df)
        user_stats(df)
        show_data(df)

        restart = input('\nWould you like to restart? Enter yes or no.\n')
        if restart.lower() != 'yes':
            break        


            
if __name__ == "__main__":
	main()