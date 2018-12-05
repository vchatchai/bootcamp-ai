import tensorflow as tf
 
a = tf.fill([3,2],8)
with tf.Session() as session:
    writer = tf.summary.FileWriter('graphs_ex9', session.graph)
    print(session.run(a))
writer.close()
