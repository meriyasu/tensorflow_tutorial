import numpy as np
import tensorflow as tf
import matplotlib.pyplot as plt


def weight(shape = []):
    initial = tf.truncated_normal(shape, stddev = 0.01)
    return tf.Variable(initial)

def bias(dtype = tf.float32, shape = []):
    initial = tf.zeros(shape, dtype = dtype)
    return tf.Variable(initial) 

def loss(t, f):
    cross_entropy = tf.reduce_mean(-tf.reduce_sum(t * tf.log(f)))
    return cross_entropy

Q = 4
P = 4
R = 3

sess = tf.InteractiveSession()

X = tf.placeholder(dtype = tf.float32, shape = [None, Q], name='X')
t = tf.placeholder(dtype = tf.float32, shape = [None, R], name='t')


with tf.name_scope('layer1'):
    W1 = weight(shape = [Q, P])
    b1 = bias(shape = [P])
    f1 = tf.matmul(X, W1) + b1
    sigm = tf.nn.sigmoid(f1)
    tf.summary.histogram('W1', W1)
    tf.summary.histogram('b1', b1)
    tf.summary.histogram('sigm', sigm)

with tf.name_scope('layer2'):
    W2 = weight(shape = [P, R])
    b2 = bias(shape = [R])
    f2 = tf.matmul(sigm, W2) + b2
    f = tf.nn.softmax(f2)
    tf.summary.histogram('W2', W2)
    tf.summary.histogram('b2', b2)
    tf.summary.histogram('f', f)

with tf.name_scope('loss'):
    loss = loss(t, f)
    tf.summary.scalar('loss', loss)

# Merge summary
merged = tf.summary.merge_all()

optimizer = tf.train.GradientDescentOptimizer(learning_rate = 0.001)
train_step = optimizer.minimize(loss)

# Tensorboard logfile
if tf.gfile.Exists('./logdir'):
    tf.gfile.DeleteRecursively('./logdir')
writer = tf.summary.FileWriter('./logdir', sess.graph)


init = tf.global_variables_initializer()
sess.run(init) ## TensorFlowの世界を初期化(必ず必要)


from sklearn import datasets
iris = datasets.load_iris()
train_x = iris.data
train_t = iris.target
train_t = np.eye(3)[train_t]

num_epoch = 1000
for epoch in range(num_epoch):
    sess.run(train_step, feed_dict = {X: train_x, t: train_t})
    if epoch % 100 == 0:
        summary, train_loss = sess.run([merged, loss], feed_dict = {X: train_x, t: train_t})
        writer.add_summary(summary, epoch)
        print('epoch : {}, loss:{}'.format(epoch, train_loss))
        # plt.scatter(epoch, train_loss, c='black', s=10)

# plt.show()




