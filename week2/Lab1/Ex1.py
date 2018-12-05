import tensorflow as tf 


a = tf.constant(2)
b = tf.constant(3)
x = tf.add(a,b)

with tf.Session() as session : 
    print(session.run(x))