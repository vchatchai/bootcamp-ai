import tensorflow as tf

# create a placeholder of type float 32-bit, shape is a vector of 3 elements
a = tf.placeholder(tf.float32, shape=[3])
# create a constant of type float 32-bit, shape is a vector of 3 elements
b = tf.constant([5, 5, 5], tf.float32)
# use the placeholder as you would a constant or a variable
c = a + b  # Short for tf.add(a, b)
# If we try to fetch c, we will run into error.
with tf.Session() as session:
    writer = tf.summary.FileWriter('./graphs_ex33', session.graph)
    for a_value in [[1,2,3],[4,5,6]]:
        print(session.run(c, {a: a_value}))

writer.close()
