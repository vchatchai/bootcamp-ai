import tensorflow as tf

a = tf.Variable(2, name="scalar")
init = tf.global_variables_initializer()

with tf.Session() as session:
    session.run(init)
    writer = tf.summary.FileWriter('graphs_ex20', session.graph)
    print(session.run(a.value())) 


writer.close()
