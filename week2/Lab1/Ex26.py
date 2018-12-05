import tensorflow as tf


W = tf.Variable(10)

assign_op = W.assign(100)

with tf.Session() as session:
    session.run(assign_op)
    print(W.eval()) 

