import tensorflow as tf

# create variable a with scalar value
a = tf.Variable(2, name="scalar")
# create variable b as a vector
b = tf.Variable([2, 3], name="vector")

init_ab = tf.variables_initializer([a,b], name="init_ab")


with tf.Session() as session:
    session.run(init_ab)
    writer = tf.summary.FileWriter('graphs_ex21', session.graph)
    print(session.run(a.value())) 
    print(session.run(b.value())) 


writer.close()
