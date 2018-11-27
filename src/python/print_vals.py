import serial
import datetime
import numpy as np

if __name__ == '__main__':

    m = []
    with open('../../data/sensors.txt','a') as f:
        while True:
            s = serial.Serial('/dev/ttyACM0',9600)
            vals = s.readline().rstrip().split(',')

            try:
                #temp = vals[0]
                #humidity = vals[1]
                #light = vals[2]
                moisture = float(vals[3])
                m.append(moisture)
                #print 'temp:',temp,'humidity:',humidity,'light:',light,'mositure:',mositure
                #print 'moisture:',moisture
                print 'average:',np.mean(np.asarray(m))
            except:
                continue
