import tensorflow as tf


a = tf.constant([2, 2], name="vector")
b = tf.constant([[0, 1], [2, 3]], name="b")
x= tf.add(a, b, name="Add")

with tf.Session() as session:
    writer = tf.summary.FileWriter('graphs_ex4', session.graph)
    print(session.run(x))

writer.close()
