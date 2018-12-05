import tensorflow as tf


t_0 = 19
# t_1 = [b"appple", b"peach", b"grape"]
t_2 = [[True, False, False], [False, True, False], [False, False, True]]

with tf.Session() as session:
    writer = tf.summary.FileWriter('graphs_ex15', session.graph)
    print(session.run(tf.zeros_like(t_0)))
    print(session.run(tf.ones_like(t_0)))
    # print(session.run(tf.zeros_like(t_1)))
    # print(session.run(tf.ones_like(t_1)))
    print(session.run(tf.zeros_like(t_2)))
    print(session.run(tf.ones_like(t_2)))

writer.close()
