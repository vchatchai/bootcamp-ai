import tensorflow as tf
import numpy as np

 
with tf.Session() as session:
    writer = tf.summary.FileWriter('graphs_ex16', session.graph)
    print(session.run(tf.ones([2,2], np.float32)))
 

writer.close()
