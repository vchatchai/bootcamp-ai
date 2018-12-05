import tensorflow as tf

a = tf.range(3,18,3)
b = tf.range(3,1,-0.5)
c = tf.range(5)

print('a = {}'.format(a))
print('b = {}'.format(b))
print('c = {}'.format(c))

with tf.Session() as session:
    writer = tf.summary.FileWriter('graphs_ex11', session.graph)
    print(session.run(a),session.run(b),session.run(c))
writer.close()
