"""
This contains function for dealing with

# read more: https://huggingface.co/datasets/glue
# we will be using sst2 a sentiment dataset by stanford
# compare performance with others:
# https://paperswithcode.com/sota/sentiment-analysis-on-sst-2-binary

"""


from typing import Tuple
from datasets import load_dataset
import random

def load_sst2(split: str="train") -> Tuple[list, list]:
    """load the sst2 dataset. Do note that the test, train set here does correspond to the original test and train set. 
    As the official test set is hidden (to ensure that researcher does not accidentally or intentionally train on it) 
    we have created a new test set by using excluding 1000 random samples from the train set.

    Args:
        split (str, optional): The dataset split, options include "train", "validation", "test". Defaults to "train".
    Returns:
        Tuple[List, List]: A tuple of two lists, one containing the texts, and the second one containing the labels. 
            0 is negative, 1 is positive.
    """

    dataset = load_dataset("glue", "sst2")


    if split in {"test", "train"}:
        # don't change the seed or n_test
        random.seed(10) # seed to ensure the test set is the same for everyone
        n_test = 1000 # number of test samples
        test_idx = [0 if i >= n_test else 1 for i in range(dataset["train"].num_rows)]
        random.shuffle(test_idx)
        

    if split == "test":
        split = dataset["train"]
        test = [(s, l) for s, l, is_test in zip(split["sentence"],  split["label"], test_idx) if is_test]
        sent, labels =  zip(*test)
        return (list(sent), list(labels))
    elif split == "train":
        split = dataset["train"]
        train = [(s, l) for s, l, is_test in zip(split["sentence"],  split["label"], test_idx) if not is_test]
        sent, labels =  zip(*train)
        return (list(sent), list(labels))

    else:
        split = dataset[split]
        return (split["sentence"], split["label"])
