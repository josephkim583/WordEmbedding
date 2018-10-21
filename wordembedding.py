import gensim

model = gensim.models.Word2Vec.load_word2vec_format('GoogleNews-vectors-negative300.bin', binary=True, norm_only=True)
dog = model['dog']
print (model.most_similar(positive = ['woman', 'king'], negative = ['man']))
print (model.doesnt_match("breakfast cereal dinner lunch".split()))
print (model.similarity("woman", "man"))