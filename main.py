import csv
from datetime import datetime
import dateutil.parser
from matplotlib import dates as mdates
from matplotlib import pyplot as plt


class Analyze():
    def __init__(self):
        pass

    def speed(self):
        """
        Plot average and maximum speed
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
    print('Make sure you have the file Daily Summaries.csv.\n')
    user_input = input('Do you want to start? Y/N \n')
    if user_input == 'Y' or 'y':
        speed = 'speed'
        if speed == 'speed':
            graph_speed = Analyze()
            graph_speed.speed()
    else:
        exit


if __name__ == '__main__':

    main()
