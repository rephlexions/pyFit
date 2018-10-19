import csv
import pygal
import dateutil.parser
from datetime import datetime
from pygal.style import DarkStyle

class Analyze():
    def __init__(self,option):
        self.option = option
    
    def openFile():    
        filename = 'Daily Summaries.csv'
        with open(filename) as f:
            reader = csv.reader(f)
            return reader



def analyze_data():
    filename = os.path.abspath(r'Fit\Daily Aggregations\Daily Summaries.csv')
    with open(filename) as f:
        reader = csv.reader(f)
   
        dates, distances, steps, avg_speeds, cycl_duration, walk_duration = [], [], [], [], [], []
        for row in reader:
            try:
                current_date = datetime.strptime(row[0],"%Y-%m-%d")
                distance = int(float(row[2]))
                step = int(row[10])
                avg_speed = int(float(row[7])) * 3.6
                cycl_time = int(row[14])/3600000
                walk_time = int(row[17])/3600000
            except ValueError:
                print('Missing data')
            else:
                if distance > 2000 and current_date > datetime(2018,6,1) and current_date < datetime(2018,9,1):
                    dates.append(current_date.month)
                    distances.append(distance)
                    avg_speeds.append(avg_speed)
                    steps.append(step)
                    cycl_duration.append(cycl_time)
                    walk_duration.append(walk_time)

    line_chart = pygal.Line(height=800,width=1500, spacing=10,margin=50,)
    line_chart.title = 'Distance (m) and Average Speed (km/h)'
    line_chart.x_labels = map(str, dates)
    line_chart.add('Distance', distances)
    line_chart.add('Avg Speed',avg_speeds, secondary=True)

    line_chart.render_to_file('distance_speed.svg')

    line_chart = pygal.Pie(height=800,width=1500, spacing=10,margin=50,)
    line_chart.title = 'Walking and Cycling Duration'
    line_chart.add('Walking', walk_duration)
    line_chart.add('Cylcing',cycl_duration)

    line_chart.render_to_file('duration.svg')


def main():

    print('This program analyzes yout Google Fit data.\n')
    print('Make sure you have the file Daily Summaries.csv.\n')
    user_input = input('Do you want to start? Y/N \n')
    if user_input == 'Y' or 'y':
        analyze_data()
    else:
        exit


if __name__ == '__main__':

    main()
