import tensorflow as tf

a = tf.zeros([2, 4], tf.int32)
with tf.Session() as session:
    writer = tf.summary.FileWriter('graphs_ex5', session.graph)
    print(session.run(a))
writer.close()
