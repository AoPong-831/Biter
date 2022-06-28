import numpy as np
import matplotlib.pyplot as plt

def graph(files,capacity):
    x = np.array(capacity)
    plt.pie(x,labels=files, counterclock=False, startangle=90, autopct="%1.1f%%")
    plt.show()
        