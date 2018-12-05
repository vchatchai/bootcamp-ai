import tensorflow as tf

a = tf.linspace(10.0, 14.0, 11, name='linspace')
with tf.Session() as session:
    writer = tf.summary.FileWriter('graphs_ex10', session.graph)
    print(session.run(a))
writer.close()
