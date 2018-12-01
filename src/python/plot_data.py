import matplotlib
matplotlib.use('Pdf')
import matplotlib.pyplot as plt
from datetime import datetime
import matplotlib.dates as plt_dates
from matplotlib.pyplot import figure

def getMinutely(data, sensor='all'):

    x = []
    y = []
    if sensor == 'temperature': idx = 0
    elif sensor == 'light': idx = 1
    elif sensor == 'humidity': idx = 2
    elif sensor == 'moisture': idx = 3
    
    for date, sensor_reading in data.iteritems():
        date = datetime.strptime(date, '%Y,%m,%d,%H,%M,%S')
        #date = date.strftime('%m/%d/%Y')
        date = plt_dates.date2num(date)
        print date, ':', sensor_reading[idx]
        print
        x.append(date)
        y.append(sensor_reading[idx])

    #figure(figsize=(16,16))
    plt.figure(figsize=(16,16))
    plt.title(sensor)
    plt.plot_date(x,y)
    plt.savefig('plot_'+sensor+'.png')


def getHourly(f):
    return NotImplementedError

def getDaily(f):
    return NotImplementedError

def getMonthly(f):
    return NotImplementedError

def getYearly(f):
    return NotImplementedError

if __name__ == '__main__':

    data = {}
    with open('../../data/sensors.txt', 'r') as f:
        for line in f:
            temperature = float(line.rstrip().split(',')[0])
            humidity = float(line.rstrip().split(',')[1])
            light = float(line.rstrip().split(',')[2])
            moisture = float(line.rstrip().split(',')[3])
            data[','.join(line.rstrip().split(',')[4:])] = [temperature, humidity, light, moisture]

    getMinutely(data, sensor='temperature')
    getMinutely(data, sensor='light')
    getMinutely(data, sensor='moisture')
    getMinutely(data, sensor='humidity')
