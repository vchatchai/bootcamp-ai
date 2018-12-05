import tensorflow as tf

# create variable a with scalar value
a = tf.Variable(2, name="scalar")
# create variable b as a vector
b = tf.Variable([2, 3], name="vector")

W = tf.Variable(tf.zeros([784,10]))

with tf.Session() as session:
    session.run(W.initializer)
    writer = tf.summary.FileWriter('graphs_ex22', session.graph)
    print(session.run(W)) 


writer.close()
