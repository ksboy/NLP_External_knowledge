import pickle as pkl
import os

if __name__ == '__main__':
    base_dir = os.path.dirname(os.path.realpath(__file__))
    dst_dir = os.path.join(base_dir, 'data', 'sequence_and_features')
    worddict = pkl.load(open(os.path.join(dst_dir, 'vocab_cased_lemma.pkl'), 'rb'))
    print(worddict)


