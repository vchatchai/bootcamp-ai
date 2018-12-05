import tensorflow as tf

a = tf.Variable(2, name="scalar")
a_time_two = a.assign(a * 2)
init = tf.global_variables_initializer()

with tf.Session() as session:
    writer = tf.summary.FileWriter('graphs_ex27', session.graph)
    session.run(init)
    print(session.run(a_time_two))
    print(session.run(a_time_two))
    print(session.run(a_time_two))


writer.close()
