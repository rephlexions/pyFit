from analyze import Analyze
from util import validate_date


def main():
    print('This program analyzes yout Google Fit data.')
    print('Make sure you have the file \'Daily Summaries.csv\' in the same directory.')
    user_input = input('Do you want to start? Y/N \n')
    if user_input == 'Y' or 'y':

        print('Type (enter number):\n')
        print('1 - Speed')
        print('2 - Activities time')
        print('3 - Steps')
        
        user_input = input()
        user_date = input('Please enter date in format YYY-MM-DD\n')
        
        validate_date(user_date)
        
        if user_input == '1':
            graph_speed = Analyze(user_date)
            graph_speed.speed()
        elif user_input == '2':
            bar_time = Analyze(user_date)
            bar_time.activity_time()
        elif user_input == '3':
            step_bar = Analyze(user_date)
            step_bar.steps()
    else:
        exit


if __name__ == '__main__':
    main()
