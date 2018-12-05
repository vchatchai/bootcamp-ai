import tensorflow as tf 


a = tf.constant([2,2],name="a")
b = tf.constant([3,6],name="b")
x = tf.add(a,b, name="add") 

with tf.Session() as session : 
    writer = tf.summary.FileWriter('./graphs_ex3', session.graph)
    print(session.run(x))

writer.close()