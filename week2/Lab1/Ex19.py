import tensorflow as tf

a = tf.Variable(2, name="scalar")
 

with tf.Session() as session:
    writer = tf.summary.FileWriter('graphs_ex19', session.graph)
    session.run(a.initializer)
    print(session.run(a.value())) 


writer.close()
