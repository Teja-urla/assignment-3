mport numpy as np
import pandas as pd

#reading from excel
read = pd.read_excel('table-1.xlsx')
raw_data = np.array(read)

#generates bins and class intervals
bin = [0+5*i for i in range(5)]
class_intervals = ["{}-{}".format(bin[i],bin[i+1]) for i in range(4)]

#this generates frequencies and class indices
hist = np.histogram(raw_data,bins=bin)
print(hist[0])

#writing to excel file
write = pd.DataFrame({"Duration(hrs)":class_intervals,"frequency":hist[0]})
write.to_excel('frequency_distribution.xlsx',index=False)
