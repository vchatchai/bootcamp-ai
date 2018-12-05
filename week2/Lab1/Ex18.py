import tensorflow as tf

a = tf.Variable(2, name="scalar")

b = tf.Variable([2, 3], name="vector")

c = tf.Variable([[0, 1], [2, 3]], name="matrix")

W = tf.Variable(tf.zeros([784, 10]))

with tf.Session() as session:
    writer = tf.summary.FileWriter('graphs_ex18', session.graph)
    print(session.run(a))
    print(session.run(b))
    print(session.run(c))
    print(session.run(W))


writer.close()
