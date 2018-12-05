import tensorflow as tf


W = tf.Variable(10)

W.assign(100)

with tf.Session() as session:
    session.run(W.initializer)
    print(W.eval()) 

