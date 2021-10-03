

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
*Note*: The input features can be inferred when fitting feel free to adapt the function accordingly. Furthermore, you might wish the `fit` to take additional parameters such as learning rate and the number of epochs.


- [ ] A neural network class

Given the form of the tests it should be on the form:
```
# initialize the model
mdl = NeuralNet()

# fit the model to the data
mdl.fit(X, y)

# predict using the trained model:
y_hat = mdl.predict(X)
```

*Note*: it might be convenient to make the `Logistic` class a special case of the neural network class. Similar you might want to add arguments to the iniitalization of the neural network. Do note that you would then need to fix the test as well.

- [ ] Create function which for the SST2 dataset creates a TF-IDF representation of the documents.

Do not here that you will have to implement the tf-idf calculations yourself. For instance, you can't use the [tf-idf vectorizer](https://scikit-learn.org/stable/modules/generated/sklearn.feature_extraction.text.TfidfVectorizer.html) from sklearn, however I do recommend using the [dict vectorizer](https://scikit-learn.org/stable/modules/generated/sklearn.feature_extraction.DictVectorizer.html).

- [ ] Using this TF-IDF representation fit a both the logistic regression and the neural network model and test the performance on the test set

*Note* that the size of the neural network is unspecified. However it can't the equivalent to logistic regression.

- [ ] Make at least two experimeents which experiment either with:
- the size of the neural network
- the activation functions (e.g. relu or sigmoid)
- filtering of the word prior to creating to word counts or tf-idf (e.g. only include nouns or lowercase)
- document representation (e.g. using raw word frequencies vs. using term frequencies)
- or similar experimentation

Lastly, 
  - [ ] all functions should include documentation such that the code is readable, though it can be kept minimal
  - [ ] and you should fill out the readme containing a summary of your solution no longer than an abstract, a performance table and guide on how to reproduce the results.

*Note* that naturally the pre-implemented tests should pass and that you are welcome to add more tests.


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
