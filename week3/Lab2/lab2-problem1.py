import os
import numpy as np
import matplotlib.pyplot as plt
import tensorflow as tf
import xlrd

'''
Step 0: Suppress warning logs
'''
os.environ['TF_CPP_MIN_LOG_LEVEL'] = '2'

''' 
Step 1: Read in data from the .xls file
'''
DATA_FILE = 'fire_theft.xls'

book = xlrd.open_workbook(DATA_FILE, encoding_override='utf-8')
sheet = book.sheet_by_index(0)

number_of_rows = len(list(sheet.get_rows()))
data = np.asarray([sheet.row_values(i) for i in range(1, number_of_rows)])
number_of_samples = number_of_rows - 1
# x = [x[0] for x in data ]
# y = [x[1] for x in data ]
data_transpose =  data.transpose()

x = data_transpose[0]
y = data_transpose[1]


'''
Step 2: Create placeholders for feature X (number of fire) and target Y (number of theft)
'''
X = tf.placeholder(tf.float32, name='X')
Y = tf.placeholder(tf.float32, name='Y')

'''
Step 3: Create theta0 and theta1, initialized them to 0
'''
theta0 = tf.Variable(0.0, name='theta0')
theta1 = tf.Variable(0.0, name='theta1')

'''
Step 4: Define a hypothesis function to predict Y
'''
# hypothesis_function = theta0 + theta1*X
hypothesis_function = tf.add(theta0, tf.multiply(theta1, x))

'''
Step 5: Use the square error as the loss function
'''
# loss_function = (1/(2*number_of_samples)) * tf.reduce_sum(tf.pow(Y - hypothesis_function, 2))
loss_function = tf.multiply(tf.divide(1,2), tf.reduce_mean(tf.pow(Y-hypothesis_function,2)))
'''
Step 6: Using gradient descent with learning rate of 0.001 to minimize loss
'''
optimizer = tf.train.GradientDescentOptimizer(learning_rate=0.001).minimize(loss_function)

with tf.Session() as session:
    '''
    Step 7: Initialize the necessary variables, i.e. theta0 and theta1
    '''
    session.run(tf.global_variables_initializer())
    writer = tf.summary.FileWriter('./graphs/linear_regression', session.graph)

    '''
    Step 8: Train the model for 30,000 epochs
    '''
    for i in range(30000):
        session.run(optimizer, feed_dict={X: x, Y: y})
        cost = session.run(loss_function, feed_dict={X: x, Y: y})
        print("Epoch: {0}, cost = {1}, theta0 = {2}, theta1 = {3}".format(i + 1, cost, session.run(theta0), session.run(theta1)))

    '''
    Step 9: Prints the training cost, theta0, and theta1
    '''
    print("Optimization Finished!")
    training_cost  = session.run(loss_function, feed_dict={X: x, Y: y})
    print("Training cost = ", training_cost, "theta0 = ", session.run(theta0), " theta1= ",session.run(theta1), '\n')

    '''
    Step 10: Plot the results
    '''
    # Graphic display
    plt.plot(data.T[0], data.T[1], 'ro', label='Original data')
    plt.plot(data.T[0], session.run(theta0) + session.run(theta1) * data.T[0], 'b', label='Fitted line')
    plt.xlabel('fire per 1000 housing units')
    plt.ylabel('theft per 1000 population')
    plt.legend()
    plt.show()

# Close the writer when you finished using it
writer.close()
