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
print("number_of_rows", number_of_rows)

data = np.asarray([sheet.row_values(i) for i in range(1, number_of_rows)])
number_of_samples = number_of_rows - 1

print('number_of_samples', number_of_samples)

X = tf.placeholder(tf.float32, name='X')
Y = tf.placeholder(tf.float32, name='Y')


theta0 = tf.Variable(0.0, name='theta0')
theta1 = tf.Variable(0.0, name='theta1')

hypothesis_function = theta0 + theta1*X

loss_function = (1/(2*number_of_samples)) * tf.reduce_sum(tf.pow(Y - hypothesis_function, 2))
tf.summary.scalar('total_cost', loss_function)

optimizer = tf.train.GradientDescentOptimizer(
    learning_rate=0.001).minimize(loss_function)
x = [x[0] for x in data ]
y = [x[1] for x in data ]
print(data)
print('x',x)
print('y',y)
with tf.Session() as session:
    session.run(tf.global_variables_initializer())
    merged = tf.summary.merge_all()

    writer = tf.summary.FileWriter("problem1", session.graph)

    for i in range(30000):
        session.run(optimizer, feed_dict={X: x, Y: y})
        summary, cost = session.run([merged,loss_function], feed_dict={X: x, Y: y})
        writer.add_summary(summary,i)
        # print("Epoch: {0}, cost = {1}, theta0 = {2}, theta1 = {3}".format(i + 1, cost,     session.run(theta0), session.run(theta1)))
    print("Optimization Finished!")
    training_cost  = session.run( loss_function, feed_dict={X: x, Y: y})
    print("Training cost = ", training_cost, "theta0 = ", session.run(theta0), " theta1= ",session.run(theta1), '\n')

    plt.plot(data.T[0], data.T[1], 'ro', label='Original data')
    plt.plot(data.T[0], session.run(theta0) + session.run(theta1) * data.T[0], 'b', label='Fitted line')
    plt.xlabel('fire per 1000 housing units')
    plt.ylabel('theft per 1000 population')
    plt.legend()
    plt.show()


writer.close()