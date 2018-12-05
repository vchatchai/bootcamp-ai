import tensorflow as tf

session = tf.InteractiveSession()
a = tf.constant(5.0)
b = tf.constant(6.0)
c = a * b
# We can just use 'c.eval()' without passing 'session'
print(c.eval()) # >> 30.0
session.close()