import tensorflow as tf
import numpy as np

for x in np.linspace(0.0, 10.0, 4) :
    print(x)


with tf.Session() as session:
    writer = tf.summary.FileWriter('graphs_ex12', session.graph)
    for x in tf.linspace(0.0, 10.0,4):
        print(session.run(x))
writer.close()

for x in range(4):
    print(x)

with tf.Session() as session :
    writer = tf.summary.FileWriter('graphs_ex12', session.graph)
    for x in tf.range(4):
        print(session.run(x))
writer.close()