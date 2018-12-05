import tensorflow as tf

# create variable a with scalar value
a = tf.Variable(2, name="scalar")
# create variable b as a vector
b = tf.Variable([2, 3], name="vector")

W = tf.Variable(tf.truncated_normal([700,100]))

with tf.Session() as session:
    session.run(W.initializer)
    writer = tf.summary.FileWriter('graphs_ex24', session.graph)
    print(W.eval()) 


writer.close()
