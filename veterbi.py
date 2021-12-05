import hmmlearn.hmm as hmm
import numpy as np

transmat =  np.array([
  [0.7, 0.3],
  [0.4, 0.6]
])
emitmat = np.array([
  [0.1, 0.4, 0.5],
  [0.6, 0.3, 0.1]
])

startprob =np.array([0.6, 0.4])
h = hmm.MultinomialHMM(n_components=2)
h.startprob = startprob
h.transmat = transmat
h.emissionprob_ = emitmat
# works fine

felan= np.array([[0], [2], [1], [1], [2], [0]])
h.fit(felan)
# h.fit([[0, 0, 1, 0, 0], [0, 0], [1,1,1]]) # this is the reason for such
                                            # syntax, you can fit to multiple
                                            # sequences
a,b =  h.decode(felan)
print(a)
print(b)
print(h)
