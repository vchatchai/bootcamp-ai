import tensorflow as tf 


a = tf.constant([3,6])
b = tf.constant([2,2])


with tf.Session() as session :
    writer = tf.summary.FileWriter('graphs_ex14', session.graph)
    print(session.run(tf.add(a,b)))
    print(session.run(tf.add_n([a,b,b])))
    print(session.run(tf.multiply(a,b)))
    # print(session.run(tf.matmul(a,b)))
    print(session.run(tf.matmul(tf.reshape(a, shape=[1,2]),tf.reshape(b,shape=[2,1]))))
    print(session.run(tf.div(a,b)))
    print(session.run(tf.mod(a,b)))

writer.close()
    
