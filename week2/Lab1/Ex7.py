import tensorflow as tf
 
a = tf.ones([2,3], dtype=tf.int32)
with tf.Session() as session:
    writer = tf.summary.FileWriter('graphs_ex7', session.graph)
    print(session.run(a))
writer.close()
