import tensorflow as tf
 
tensor_input = [[0,1],[2,3],[4,5]]
a = tf.ones_like(tensor_input)
with tf.Session() as session:
    writer = tf.summary.FileWriter('graphs_ex8', session.graph)
    print(session.run(a))
writer.close()
