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

    while True:
        city=input('please enter a city from chicago, new york city, washington\n').lower()
        if city not in CITY_DATA:
            print('please enter city from chicago, new york city, washington')
        else:
            break

    months=['january','jebruary','march','april','may','june','all']
    while True:
        month= input('please enter a month from from january to june or type all for all months\n').lower()
        if month not in months:
            print('please type correct month from january to june')
        else:
            break


    days=['saturday','sunday','monday','tuseday','wednesday','thursday','friday','all']
    while True:
        day=input('please enter a day from the week days or type all for all days\n').lower()
        if day not in days:
            print('please type correct day from week days')
        else:
            break


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
    df=pd.read_csv(CITY_DATA[city])





    return df


def time_stats(df):
    """Displays statistics on the most frequent times of travel."""

    print('\nCalculating The Most Frequent Times of Travel...\n')
    start_time = time.time()

    df['Start Time']=pd.to_datetime(df['Start Time'])
    df['month']=df['Start Time'].dt.month_name()
    print('the most comon month is:',df['month'].mode()[0])

    df['day_of_week']=df['Start Time'].dt.day_name()
    print('the most comon day is:',df['day_of_week'].mode()[0])

    df['hour']=df['Start Time'].dt.hour
    print('the most comon hour is:',df['hour'].mode()[0] )


    print("\nThis took %s seconds." % (time.time() - start_time))
    print('-'*40)


def station_stats(df):
    """Displays statistics on the most popular stations and trip."""

    print('\nCalculating The Most Popular Stations and Trip...\n')
    start_time = time.time()

    print('the most comon Start Station is:',df['Start Station'].mode()[0] )

    print('the most comon End Station is:',df['End Station'].mode()[0] )

    combinded_stations=df.groupby(['Start Station','End Station'])['Trip Duration'].count()
    combinded_stations.head(1)


    print("\nThis took %s seconds." % (time.time() - start_time))
    print('-'*40)


def trip_duration_stats(df):
    """Displays statistics on the total and average trip duration."""

    print('\nCalculating Trip Duration...\n')
    start_time = time.time()

    print('total travel time is:',df['Trip Duration'].sum())

    print('average travel time is:',df['Trip Duration'].mean())

    print("\nThis took %s seconds." % (time.time() - start_time))
    print('-'*40)


def user_stats(df):
    """Displays statistics on bikeshare users."""

    print('\nCalculating User Stats...\n')
    start_time = time.time()


    print('Counts of each User Type is:',df['User Type'].value_counts())

    if 'Gender' in df:
        print('Counts of each Gender is:',df['Gender'].value_counts())


    if 'Birth Year' in df:
        print('earliest Birth Year is:',int(df['Birth Year'].min()))
        print('most recent Birth Year is:',int(df['Birth Year'].max()))
        print('most common Birth Year is:',int(df['Birth Year'].mode()[0]))



    print("\nThis took %s seconds." % (time.time() - start_time))
    print('-'*40)

def raw_data(df):

    """Displays raw data on upon user request.
    """
    print(df.head())
    next = 0
    while True:
        raw_data = input("Would you like to see the raw data? Type 'yes' or 'no'.")
        if raw_data.lower() != 'yes':
            return
        next = next + 5
        print(df.iloc[next:next+5])


def main():
    while True:
        city, month, day = get_filters()
        df = load_data(city, month, day)

        time_stats(df)
        station_stats(df)
        trip_duration_stats(df)
        user_stats(df)
        raw_data(df)

        restart = input('\nWould you like to restart? Enter yes or no.\n')
        if restart.lower() != 'yes':
            break


if __name__ == "__main__":
    main()
