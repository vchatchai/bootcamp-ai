import tensorflow as tf

W = tf.Variable(10)
with tf.Session() as session:
    session.run(W.initializer)
    print(session.run(W.assign_add(10)))
    print(session.run(W.assign_sub(2)))