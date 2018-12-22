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

X = tf.placeholder(tf.float32, name='X')
Y = tf.placeholder(tf.float32, name="Y")


theta0 = tf.Variable(0.0, name='theta0')
theta1 = tf.Variable(0.0, name='theta1')

hypothesis_function = theta0 + theta1*X


"""
cost_function = 1/2 sqrt(Y**2 + hypothesis**2)

"""
# cost_function = tf.multiply(tf.divide(1, 2), tf.reduce_mean(tf.pow(Y - hypothesis_function, 2)))


cost_function =  tf.reduce_mean(tf.pow(Y - hypothesis_function, 2))


optimizer = tf.train.GradientDescentOptimizer(
    learning_rate=0.001).minimize(cost_function)

with tf.Session() as session:
    session.run(tf.global_variables_initializer())
    writer = tf.summary.FileWriter('./graphs/linear_regression', session.graph)

    for i in range(30000):
        session.run(optimizer, feed_dict={X: data.T[0], Y: data.T[1]})
        cost = session.run(cost_function, feed_dict={
                           X: data.T[0], Y: data.T[1]})
        print("Epoch: {0}, cost={1}, theta0={2}, theta1= {3}".format(i+1, cost, session.run(theta0), session.run(theta1)))

    print("Optimization Finished!")
    training_cost = session.run(cost_function, feed_dict={X: data.T[0], Y: data.T[1]})
    print("Epoch: {0}, cost= {1}, theta0 = {2}, theta1={3}".format(i + 1, cost, session.run(theta0), session.run(theta1))) 
 
    print("Optimization Finished!")
    training_cost = session.run(cost_function,feed_dict={X: data.T[0], Y: data.T[1]})
    print("Cost =", training_cost, "theta0 =", session.run(theta0), "theta1 =", session.run(theta1), '\n')

    plt.plot(data.T[0], data.T[1], 'ro', label='Original data')
    plt.plot(data.T[0], session.run(theta0) + session.run(theta1)* data.T[0], 'b', label="Fitted line")
    plt.xlabel('fire per 1000 housing units')
    plt.ylabel('theft per 1000 poplation')
    plt.legend()
    plt.show()

writer.close()