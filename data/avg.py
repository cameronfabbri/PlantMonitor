import numpy as np
import sys

total_m = []
with open('sensors.csv', 'r') as f:
    for line in f:
        print(line.rstrip().split(',')[3])
        exit()
        moisture = float(line.rstrip().split(',')[3])
        total_m.append(moisture)

total_m = np.asarray(total_m)
tot = len(total_m)
#print np.mean(total_m[tot-int(sys.argv[1]):])
print(np.mean(total_m[:100]))
