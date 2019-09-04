#Eugene Charniak, Introduction to Deep Learning (2018).
#Chapter 4.2 Feed-Forward Language Model

import tensorflow as tf

inpt = tf.placeholder(tf.int32, shape=[batchSz])
answr = tf.placeholder(tf.int32, shape=[batchSz])

#E is the words embedding

E = tf.Variable(tf.random_normal([vocabSz, embedSz], stddev = 0.1))

embed = tf.nn.embedding_lookup(E, inpt)

#Compute cross entropy loss
xEnt = tf.nn.sparse_softmax_cross_entropy_with_logits(logits, labels=answr)
loss = tf.reduce_sum(xEnt)

#Add a node that finds the embedding of inpt2
embed2 = tf.nn.embedding_lookup(E, inpt2),
#Concatenating(link)
both = tf.concat([embed, embed2], 1)


#Dropout
KeepP = tf.placeholder(tf.float32)
w10ut = tf.nn.dropout(w10ut, KeepP)

#L2 Regularization
0.01 * tf.nn.l2.loss(W1)
