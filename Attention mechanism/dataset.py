
import os
import math
import time
import spacy
import torch
import random
import numpy as np
import torch.nn as nn
import torch.optim as optim
from typing import List
from torchtext.datasets import Multi30k
from torchtext.data import Field, BucketIterator
import config
import itertools
from config import Tokenize


SEED = 2222
random.seed(SEED)
torch.manual_seed(SEED)


class Dataset():

    def get_data(self):
        source = config.source
        target = config.target
        train_data, valid_data, test_data = Multi30k.splits(exts=('.fr', '.en'), fields=(source, target), root="data/")
        l = len(train_data)
        train_data, test_data = train_data.split(split_ratio = 0.5, random_state=random.seed(SEED))
        train_data, valid_data = train_data.split(split_ratio=0.8, random_state=random.seed(SEED))


        print("train", len(train_data), round(100*len(train_data)/l), "%")
        print("val", len(valid_data), round(100*len(valid_data)/l), "%")
        print("test", len(test_data), round(100*len(test_data)/l), "%")
        
        

        source.build_vocab(train_data, min_freq=2, vectors='fasttext.simple.300d')
        target.build_vocab(train_data, min_freq=2, vectors='fasttext.simple.300d')
        print(f"Unique tokens in source (fr) vocabulary: {len(source.vocab)}")
        print(f"Unique tokens in target (en) vocabulary: {len(target.vocab)}")

        return train_data, valid_data, test_data, len(source.vocab), len(target.vocab)

if __name__ == "__main__":
    print('Helo')
    dataset  = Dataset()
    dataset.get_data()
