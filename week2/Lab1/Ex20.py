import tensorflow as tf

init = tf.global_variables_initializer()

with tf.Session() as session:
    writer = tf.summary.FileWriter('graphs_ex18', session.graph)
    session.run(a.initializer)
    print(session.run(a.value())) 


writer.close()
