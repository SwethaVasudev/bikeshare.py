#References:Some codes are referenced from udacity practice problems
#https://stackoverflow.com/questions/25146121/extracting-just-month-and-year-separately-from-pandas-datetime-column
#https://stackoverflow.com/questions/319426/how-do-i-do-a-case-insensitive-string-comparison
#https://stackoverflow.com/questions/50866850/ask-user-to-continue-viewing-the-next-5-lines-of-data
#Used slack channel for my doubts about this project
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
    # TO DO: get user input for city (chicago, new york city, washington). HINT: Use a while loop to handle invalid inputs
    while True:
        city=input('Please select chicago or new york city or washington: ').lower()
        cities=['chicago','new york city','washington']
        if city not in cities:
            print("Please enter a valid city")
        else:
            break
              
    # TO DO: get user input for month (all, january, february, ... , june)
    while True:
        month=input('Please select any month between january to june or select all: ').lower()
        months=['january','february','march','april','may','june']
        if month not in months and month!='all':
            print("Please enter a valid month")
        else:
            break
    # TO DO: get user input for day of week (all, monday, tuesday, ... sunday)
    while True:
        day=input("Please select any day between sunday to saturday or select all: ").lower()
        days=['sunday','monday','tuesday','wednesday','thursday','friday','saturday']
        if day not in days and day!='all':
            print("Please enter a valid day")
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
    
    #load data file in DataFrame
    df=pd.read_csv(CITY_DATA[city])
    
    print(df.head())
    #convert start time column to datetime
    df['Start Time']=df['Start Time'].apply(pd.to_datetime)
    #extract month from start time column
    df['month']=df['Start Time'].dt.month
    #extract day_of_week from start time column
    df['day_of_week']=df['Start Time'].dt.day_name()
    #extract hour from start time column
    df['hour']=df['Start Time'].dt.hour
    
   
    #filtering by month with possible inputs
    if month!='all':
        months=['january','february','march','april','may','june']
        month=months.index(month)
        df=df[df['month']==month]
        
    #filtering by day with possible inputs
    if day !='all':
        df=df[df['day_of_week']==day.title()]
    

    return df


def time_stats(df):
    """Displays statistics on the most frequent times of travel."""

    print('\nCalculating The Most Frequent Times of Travel...\n')
    start_time = time.time()

    # TO DO: display the most common month
    common_month=df['month'].mode()[0]
    print(f"Most common month is {common_month}")


    # TO DO: display the most common day of week
    common_day=df['day_of_week'].mode()[0]
    print(f"Most common day of week is {common_day}")


    # TO DO: display the most common start hour
    common_hour=df['hour'].mode()[0]
    print(f"Most common start hour is {common_hour}")


    print("\nThis took %s seconds." % (time.time() - start_time))
    print('-'*40)


def station_stats(df):
    """Displays statistics on the most popular stations and trip."""

    print('\nCalculating The Most Popular Stations and Trip...\n')
    start_time = time.time()

    # TO DO: display most commonly used start station
    common_sstation=df['Start Station'].mode()[0]
    print(f"Most common start station is {common_sstation}")


    # TO DO: display most commonly used end station
    common_estation=df['End Station'].mode()[0]
    print(f"Most common end station is {common_estation}")


    # TO DO: display most frequent combination of start station and end station trip
    common_combination=(df['Start Station'] + df['End Station']).mode()[0]
    print(f"Most frequent combination of start station and end station {common_combination}")


    print("\nThis took %s seconds." % (time.time() - start_time))
    print('-'*40)


def trip_duration_stats(df):
    """Displays statistics on the total and average trip duration."""

    print('\nCalculating Trip Duration...\n')
    start_time = time.time()

    # TO DO: display total travel time
    ttravel_time=df['Trip Duration'].sum()
    print(f"Total travel time is {ttravel_time/3600}")


    # TO DO: display mean travel time
    mtravel_time=df['Trip Duration'].mean()
    print(f"Mean travel time is {mtravel_time/3600}")


    print("\nThis took %s seconds." % (time.time() - start_time))
    print('-'*40)


def user_stats(df):
    """Displays statistics on bikeshare users."""

    print('\nCalculating User Stats...\n')
    start_time = time.time()

    # TO DO: Display counts of user types
    user_types=df["User Type"].value_counts()
    print(f"Counts of user types is {user_types}")


    # TO DO: Display counts of gender
    if 'Gender' in df:
        gender=df['Gender'].value_counts()
        print(f"Counts of gender is {gender}")
    else:
        print("No Gender count available in your chosen city")


    # TO DO: Display earliest, most recent, and most common year of birth
    if 'Birth Year' in df:
        earliest=df['Birth Year'].min()
        recent=df['Birth Year'].max()
        mcommon=df['Birth Year'].mode()[0]
        print(f"Earliest birth year is {earliest}")
        print(f"Recent birth year is {recent}")
        print(f"Most common year of birth {mcommon}")
    else:
        print("No Birth Year available in your chosen city")
    


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
        display_raw_input(df)

        restart = input('\nWould you like to restart? Enter yes or no.\n')
        if restart.lower() != 'yes':
            break

def display_raw_input(df):
    #provide additional information to the users on request.
    #providing first five rows of actual input data
    print('\n Getting raw inputs...\n')
    start_time = time.time()
    i=5
    while True:
        raw_input=input('Would you like to see the additional five rows of information: ').lower()
        if raw_input !='yes':
            return
        i+=5
        print(df.head(i))
        
    print("\nThis took %s seconds." % (time.time() - start_time))
    print('-'*40)
if __name__ == "__main__":
	main()
