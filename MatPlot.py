import numpy as np
import matplotlib.pyplot as plt


height = np.sort(['170','179','159','160','180','164','168','174','160','183'])
weight = np.sort(['57','62','47','67','59','49','54','63','66','80'])

print(len(height))
print(len(weight))

plt.scatter(height, weight, s=40, c='r', marker='.')
plt.xlabel('height(cm)')
plt.ylabel('weight(kg)')
plt.title('Test')

plt.show()