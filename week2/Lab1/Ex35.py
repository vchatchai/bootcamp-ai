import os
import tensorflow as tf
os.environ['TF_CPP_MIN_LOG_LEVEL']='2'

# create Operations, Tensors, etc (using the default graph)
a = tf.add(2, 5)
b = tf.multiply(a, 3)
# start up a `Session` using the default graph
sess = tf.Session()
# define a dictionary that says to replace the value of `a` with 15
replace_dict = {a: 15}
# Run the session, passing in `replace_dict` as the value to `feed_dict`
print(sess.run(b, feed_dict=replace_dict)) # returns 45

sess.close()