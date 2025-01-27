import numpy as np
import matplotlib.pyplot as plt

plt.rcParams["figure.figsize"] = (10.0, 8.0)
plt.rcParams['image.interpolation'] = 'nearest'
plt.rcParams['image.cmap'] = 'gray'

np.random.seed(0)
N = 100
D = 2
K = 3
X = np.zeros((N*K, D))
Y = np.zeros(N*K, dtype='uint8')
for j in range(K):
    ix = range(N*j, N*(j+1))
    r = np.linspace(0.0, 1, N)
    t = np.linspace(j*4, (j+1)*4, N)+np.random.randn(N)*0.2
    X[ix] = np.c_[r*np.sin(t), r*np.cos(t)]
    Y[ix] = j
plt.scatter(X[:, 0], X[:, 1], c=Y, s=50, cmap=plt.cm.Spectral)
plt.show()

# W = 0.01*np.random.randn(D, K)
# b = np.zeros((1, K))

# step_size = le-0
# reg = le-3
# num_examples = X.shape[0]
# for i in range(1000):
#     scores = np.dot(X, W) + b
#     exp_scores = np.exp(scores)
#     probs = exp_scores/np.sum(exp_scores, axis=1, keepdims=True)
#     corect_logprobs = -np.log(probs[range(num_examples), y])

#     data_loss = np.sum(corect_logprobs)/num_examples
#     reg_loss = 0.5*reg*np.sum(W*W)
#     loss = data_loss+reg_loss

#     if i % 100 == 0:
#         print("iteration %d:loss %f" % (i, loss))
#     dscores = probs
#     dscores[range(num_examples), y] = -1
#     db = np.sum(dscores, axis=0, keepdims=True)

#     dW += reg*W

#     W += -step_size*dW
#     b += -step_size*db

#     scores = np.dot(X, W) + b
# predicted_class = np.argmax(scores, axis=1)
# print('training accuracy:%.2f' % (np.mean(predicted_class == y)))

# h = 0.02
# x_min, x_max = X[:, 0].min() - 1, X[:, 0].max()+1
# y_min, y_max = X[:, 1].min() - 1, X[:, 1].max()+1
# xx, yy = np.meshgrid(np.arange(x_min, x_max, h), np.arange(y_min, y_max, h))

# Z = np.dot(np.c_[xx.ravel(), yy.ravel()], W)+b
# Z = np.argmax(Z, axis=1)
# Z = Z.reshape(xx.shape)
# fig = plt.figure()
# plt.scatter(X[:, 0], X[:, 1], c=y, s=40, cmap=plt.Spectral)
# plt.xlim(xx.min(), xx.max())
# plt.ylim(yy.min(), yy.max())
# plt.show()
