import tensorflow as tf
import numpy as np

 

a = tf.random_normal([2, 2], mean=0.0, stddev=1.0, dtype=tf.float32)
b = tf.truncated_normal([2, 2], mean=0.0, stddev=1.0, dtype=tf.float32)
c = tf.random_uniform([2, 3], minval=0, maxval=None, dtype=tf.float32)
d = tf.random_shuffle([12, 35, 64, 5, 16])

with tf.Session() as session:
    writer = tf.summary.FileWriter('graphs_ex13', session.graph)
    print(session.run(a), session.run(b),session.run(c),session.run(d))
writer.close()
