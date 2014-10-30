import matplotlib.pyplot as plt
from numpy.random import normal
data = [10000]*5 + [15000]*20 + [20000]*40 + [25000]*50 + [30000]* 20 + [35000] * 50 + [40000] * 5 + [45000] * 10

mean = float(sum(data)) / len(data)
variance = reduce(lambda acc, x:  acc + pow(x-mean, 2), data, 0) / (len(data)-1)

print variance

#plt.hist(data)
#plt.title("Support in Database")
#plt.xlabel("Support / 1000")
#plt.ylabel("Frequency")
#plt.xticks(range(5, 50, 5))
#plt.show()
