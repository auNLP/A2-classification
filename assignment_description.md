

# Assignment 2: Sentiment Classification
This is the second assignment, where the goal is to perform classification using logistic regression and neural networks based upon bag-of-words representations.

You will need to submit

- [ ] A logistic regression class


Given the form of the tests it should be on the form:
```
# initialize the model
mdl = Logistic(input_features=10)

# fit the model to the data
mdl.fit(X, y)

# predict using the trained model:
y_hat = mdl.predict(X)
```

The logistic regression should be implemented in pytorch thus you naturally can not use the [logistic regression](https://scikit-learn.org/stable/modules/generated/sklearn.linear_model.LogisticRegression.html) implementation from scikit-learn.

*Note*: The input features can be inferred when fitting feel free to adapt the function accordingly. Furthermore, you might wish the `fit` to take additional parameters such as learning rate and the number of epochs. 


- [ ] A neural network class

Given the form of the tests it should be on the form:

```py
# initialize the model
mdl = NeuralNet()

# fit the model to the data
mdl.fit(X, y)

# predict using the trained model:
y_hat = mdl.predict(X)
```

*Note*: it might be convenient to make the `Logistic` class a special case of the neural network class. Similar you might want to add arguments to the iniitalization of the neural network. Do note that you would then need to fix the test as well.

- [ ] Create function which for a list of tokenized texts (`List[List[str]]`) creates a TF-IDF representation of the documents.

The function could look something like this:
```py
def tfidf(texts: list, df: Optional[dict]=None) -> List[dict]:
    """
    takes in a list of tokenized texts and returns a list of dictionaries

    args:
        df (dict): Document frequencies, defaults to None, in which case it is estimated from the texts.
    """
```

You will have to implement the TF-IDF calculations yourself. For instance, you **can't use** the [tf-idf vectorizer](https://scikit-learn.org/stable/modules/generated/sklearn.feature_extraction.text.TfidfVectorizer.html) from scikit-learn. 

- [ ] Apply the function to the SST2 dataset to create a TF-IDF representation of the document.
Do note that document frequencies should be estimated on the train set as otherwise, your test data will influence your training samples leading to inflated performance scores.


- [ ] Using this TF-IDF representation fit a both the logistic regression and the neural network model and test the performance on the test set
When turning the TF-IDF dictionaries into vectors for your model I recommend using the [dict vectorizer](https://scikit-learn.org/stable/modules/generated/sklearn.feature_extraction.DictVectorizer.html) for scikit-learn.

*Note* that the size of the neural network is unspecified. However, it can't be the equivalent to logistic regression, i.e. it will have to contain at least 2 linear layers.

- [ ] Make at least two experiments which experiment either with:
- the size of the neural network
- the activation functions (e.g. relu or sigmoid)
- filtering of the word prior to creating to word counts or TF-IDF (e.g. only include nouns or lowercase)
- document representation (e.g. using raw word frequencies vs. using term frequencies)
- or similar experimentation

Lastly, 
  - [ ] all functions should include documentation such that the code is readable, though it can be kept minimal
  - [ ] and you should fill out the readme containing a summary of your solution no longer than an abstract, a performance table and guide on how to reproduce the results.

*Note* that, naturally, the pre-implemented tests should pass and that you are welcome to add more tests. Please also tick off the boxes if you feel you have completed the task.


## Project Organization
The organization of the project is as follows

```
├── LICENSE                <- the license of this code
├── README.md              <- The top-level README for this project.
├── .github            
│   └── workflows          <- workflows to automatically run when code is pushed
│   │    └── pytest.yml    <- A workflow which runs pytests upon push
├── classification         <- The main folder for scripts
│   ├── tests              <- The pytest test suite
│   │   └── ...
|   └── ...
├── .gitignore             <- A list of files not uploaded to git
└── requirement.txt        <- A requirements file of the required packages.
```


## Intended learning goals
- Being able to work with vector representation of a document such as tf-idf
  - and being able to transform a text to such representation
- Being able to implement a neural networks and a simple logistic regression using pytorch
- Being able to make meaningful experiments which influence the performance of the model


## Packages which might be useful
This includes a few additional packages which you might find useful: 

- [wasabi](https://pypi.org/project/wasabi/) is a package which allows you to create and write markdown tables which might be especially nice when creating the performance table
- Recall from the workshop that argument can be parsed using [argparse](https://docs.python.org/3/library/argparse.html)


## FAQ

<br /> 

<details>
  <summary> Pytest: How do I test the code and run the test suite?</summary>

To run the test suite (pytests) you will need to install the required dependencies. This can be done using 


```
pip install -r requirements.txt
pip install pytest

python -m pytest
```

which will run all the test in the `tests` folder.

Specific tests can be run using:

```
python -m pytest path/to/test_script.py
```

**VS Code**
You can also run your test directly in VS Code. See the guide on the [pytest integration](https://code.visualstudio.com/docs/python/testing) here.

**Code Coverage**
If you want to check code coverage you can run the following:
```
pip install pytest-cov

python -m pytest --cov=.
```



</details>


<br /> 
