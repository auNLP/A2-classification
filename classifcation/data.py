"""
This contains function for dealing with

# read more: https://huggingface.co/datasets/glue
# we will be using sst2 a sentiment dataset by stanford
# compare performance with others:
# https://paperswithcode.com/sota/sentiment-analysis-on-sst-2-binary

"""


from typing import Tuple
from datasets import load_dataset


def load_sst2(split: str="train") -> Tuple[list, list]:
    """load the sst2 dataset

    Args:
        split (str, optional): The dataset split, options include "train", "validation", "test". Defaults to "train".

    Returns:
        Tuple[List, List]: A tuple of two lists, one containing the texts, and the second one containing the labels. 
            0 is negative, 1 is positive.
    """

    dataset = load_dataset("glue", "sst2")

    split = dataset[split]
    return (split["sentence"], split["label"])