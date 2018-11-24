import serial
import datetime

if __name__ == '__main__':

    f = open('sensors.txt','a')

    while True:
        s = serial.Serial('/dev/ttyACM0',9600)
        vals = s.readline().rstrip().split(',')

        try:
            temp = vals[0]
            humidity = vals[1]
            light = vals[2]
            moisture = vals[3]
        except:
            continue

        now = datetime.datetime.now()
        year = str(now.year)
        month = str(now.month)
        day = str(now.day)
        hour = str(now.hour)
        minute = str(now.minute)
        second = str(now.second)
        print temp+','+humidity+','+light+','+moisture+','+year+','+month+','+day+','+hour+','+minute+','+second+'\n'
