import csv
from datetime import datetime
import dateutil.parser
from matplotlib import dates as mdates
from matplotlib import pyplot as plt
import numpy as np


class Analyze():
    def __init__(self):
        pass

    def speed(self):
        """
        Plot average and maximum speed in km/h
        """

        filename = 'Daily Summaries.csv'
        with open(filename) as f:
            reader = csv.reader(f)
            fdates, avg_speeds, max_speeds, min_speeds = [], [], [], []
            for row in reader:
                try:
                    current_date = datetime.strptime(row[0],"%Y-%m-%d")
                    current_date = current_date.strftime("%Y%m%d")
                    datetime_date = datetime.strptime(current_date, '%Y%m%d')

                    avg_speed = int(float(row[7])) * 3.6
                    max_speed = int(float(row[8])) * 3.6
                    min_speed = int(float(row[9])) * 3.6
                except ValueError:
                    pass
                    print('Missing speed data')
                else:
                    if datetime_date > datetime(2018,7,1):
                        fdates.append(datetime_date)
                        avg_speeds.append(avg_speed)
                        max_speeds.append(max_speed)
                        min_speeds.append(min_speed)

        print(fdates)
        
        fig, ax = plt.subplots(dpi=170)
        fdates = mdates.date2num(fdates)
        ax.plot_date(fdates, max_speeds,'bo-', color='#CC4400')
        ax.plot_date(fdates, avg_speeds,'bo-', color='#0066CC')
        ax.plot_date(fdates, min_speeds,'bo-', color='#00CC22')
        date_formatter = mdates.DateFormatter('%d-%m')

        ax.xaxis.set_major_formatter(date_formatter)
        ax.set_title("Max Speed (km/h)")
        fig.autofmt_xdate()
        plt.show()


    def activity_time(self):
        """
        Activity type and duration in minutes
        """

        filename = 'Daily Summaries.csv'
        with open(filename) as f:
            reader = csv.reader(f)
           
            cycling_duration, walking_duration, running_duration = 0, 0, 0
            for row in reader:
                try:
                    cycle = int(float(row[14]))/60000
                    walk = int(float(row[17]))/60000
                    run = int(float(row[18]))/60000
                except ValueError:
                    pass
                else:
                    walking_duration = walking_duration + walk
                    cycling_duration = cycling_duration + cycle
                    running_duration = running_duration + run

        labels = 'Walking', 'Running', 'Cycling',
        sizes = [walking_duration, running_duration, cycling_duration]
        #explode = (0.1, 0.1, 0.1)  # only "explode" the 2nd slice (i.e. 'Hogs')

        def make_autopct(values):
            """
            Display both the percent value and the original value
            """

            def my_autopct(pct):
                total = sum(values)
                val = int(round(pct*total/100.0))
                return '{p:.2f}%  ({v:d})'.format(p=pct,v=val)
            return my_autopct

        fig1, ax1 = plt.subplots(dpi=170)
        ax1.pie(sizes, labels=labels,colors=['#11cbd7','#c6f1e7','#fa4659'] ,autopct=make_autopct(sizes),
                shadow=False, startangle=90)
        ax1.axis('equal')  # Equal aspect ratio ensures that pie is drawn as a circle.
        plt.title('Activity type by percentage and minutes.')
        plt.show()


    """
        # Plot data.
        fig = plt.figure(dpi=100, figsize=(7, 3))
        plt.plot(avg_speeds, c='blue')
        # Format plot.
        plt.title("Speed Data", fontsize=15)
        plt.xlabel('', fontsize=16)
        plt.ylabel('', fontsize=16)
        plt.tick_params(axis='both', which='major', labelsize=16)
        plt.show()
    """

def openFile():    
        filename = 'Daily Summaries.csv'
        with open(filename) as f:
            reader = csv.reader(f)
            return reader

def main():
    print('This program analyzes yout Google Fit data.\n')
    print('Make sure you have the file \'Daily Summaries.csv\' in the same directory.\n')
    user_input = input('Do you want to start? Y/N \n')
    if user_input == 'Y' or 'y':
        user_input = input('Type?\n')
        if user_input == 'speed':
            graph_speed = Analyze()
            graph_speed.speed()
        elif user_input == 'time':
            bar_time = Analyze()
            bar_time.activity_time()
    else:
        exit


if __name__ == '__main__':

    main()
