import numpy as np
import matplotlib.pyplot as plt


height = ['170','179','159','160','180','164','168','174','160','183']
weight = ['57','62','47','67','59','49','54','63','66','80']

plt.scatter(height, weight, s=40, c='b', marker='.')
plt.xlabel('height(cm)')
plt.ylabel('weight(kg)')
plt.title('Test')

plt.show()