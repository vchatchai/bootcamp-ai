import os
import xlrd
import numpy as np
import tensorflow as tf
import matplotlib.pyplot as plt

os.environ['TF_CPP_MIN_LOG_LEVEL'] = '2'

DATA_FILE = 'fire_theft.xls'

book = xlrd.open_workbook(DATA_FILE, encoding_override='utf-8')
sheet = book.sheet_by_index(0)


number_of_rows = len(list(sheet.get_rows()))
data = np.asarray([sheet.row_values(i) for i in range(1, number_of_rows)])
number_of_samples = number_of_rows - 1


X = np.matrix(data.T[0].T)
# X = np.concatenate([np.ones([number_of_samples, 1]), X], 1)

y = np.matrix(data.T[1]).T

print("X = {0} \n Y = {1}", data, y )

estimcated_theta = np.linalg.inv(X.T * X) * X.T * y


print("theta0 is {0}".format(estimcated_theta.item(0)))
print("theta1 is {1}".format(estimcated_theta.item(1)))


plt.plot(data.T[0], data.T[1], 'ro', label='Original data')
plt.plot(data.T[0], estimcated_theta.item(0) + estimcated_theta.item(1) * data.T[0], 'b', label='Fitted line')
plt.xlabel('fire per 1000 housing units')
plt.ylabel('theft per 1000 population')
plt.legend()
plt.show()