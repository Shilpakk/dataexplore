import pandas as pd
import csv
import itertools
import matplotlib.pyplot as plt
#def dict_creater:
if __name__ =='__main__':
    with open('priceindex.csv', 'rb') as f:
        reader = csv.DictReader(f)
        data = reader.next()
        x = data.keys()
        y = data.values()
        print len(y)
        k = [int(i) for i in y if not len(i) > 3]   
        a =plt.plot(range(len(k)), k)
        plt.xlabel(x)      
        plt.show()
