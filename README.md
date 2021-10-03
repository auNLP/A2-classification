

# Assignment 1: Getting started
The first assignment,where we want to get you started with pytesting, Github actions and continuous integration.

The requirement for the assignment is submitting a working neural network with test included. The tests should
- [ ] Classify more than 90% of digits correctly in the MNIST database. This should look something like this:
```
def test_mnist():
    network = NeuralNetwork([784, 30, 10])
    # train and evaluate

    # check that accuracy is above 90%
    assert test_acc >= 0.90
```

*Note*: This is dummy code. It displays the intention. Not the exact form.

- [ ] It can memorize 10 random examples. *Note* that while this is not something we want our network to do in general, it simply shows that the network is able to overfit. Assuming that it couldn't with 20k+ parameters there is probably an error in the code.
```
def test_memorize():
    sample = random.sample(train_data, k=10)
    network = NeuralNetwork([784, 30, 10])

    # train on sample

    # check that classifies all correctly on the same sample
    assert acc == 1
```

- [ ] generalize it to take an input of binary and outputs the corresponding digit. Where the possibles inputs is the number between 0 and 9.
```
def test_binary():
    train, test = generate_binary()
    network = NeuralNetwork([784, 30, 10])

    # train on sample
    # ...
```

<br /> 

<details>
  <summary> Binary, how does that look? </summary>

The representation of the digits 0-9 looks represented using 4 binary digits look like so:

|Number|Binary|
|---|---|
| 0| 0000 |
| 1| 0001 |
| 2| 0010 |
| 3| 0011 |
| 4| 0100 |
| 5| 0101 |
| 6| 0110 |
| 7| 0111 |
| 8| 1000 |
| 9| 1001 |

Is this important? Not really. What matters is that to see that this network also works on things that aren't images.

</details>

<br /> 

- [ ] Test that the networks performance improve over 10 epochs.

Potentially:
- [ ] Test that the network trains faster using SGD as opposed to simply using backpropagation.

## I weren't there for the workshop
No problem. A solution for the code exist [here](https://github.com/CHCAA-EDUX/Scientific-Computing-Workshop-E21/tree/main/dev/solutions). However, you might need some context, I suggest watching the first [videos](https://www.youtube.com/playlist?list=PLZHQObOWTQDNU6R1_67000Dx_ZCJB-3pi) by 3Blue1Brown and/or reading the first chapter in the book [Neural Network and Deep learning](http://neuralnetworksanddeeplearning.com/index.html) by Michael Nielsen.

You can then import the NeuralNetwork model from the `*_solution.py`.

```
from task_neural_network_solution import NeuralNetwork
import mnist_loader

# import training data
train_data, val_data, test_data = mnist_loader.load_data_wrapper()

# initialize the neural network
network = NeuralNetwork([784, 30, 10])

# train the neural network for 10 epochs using backpropagation
epochs = 10
for i in range(epochs):
    network.backprop(train_data, learning_rate=3)
    print(network.evaluate(val_data))
```

However, there is still a lot of context regarding vector shapes you might find too challenging. This is not an exercise in neural networks. We will come back to it later on again using a much simpler approach. So if you weren't there for the workshop I suggest you instead do the following.


<br /> 

<details>
  <summary> The following </summary>

- [ ] Create a function which reverse the order of any string. For example:
```
def reverse(text: str) -> str:
    ...

reverse("I am happy")
# "yppah ma I"
```

- [ ] Create a function that extracts the middle row in a 1D array. If there is an even amount of entries extracts the two middle rows.

```
import numpy

def get_middle(x):
    # your code

d = np.array([1, 2, 3])
print(get_middle(d))
# 2
print(get_middle(np.arange(4)))
# [1 2]
```

- [ ] Create three functions one which takes a string and counts all digits in it, one that removes all punctuations, and one which gives you the index of the first and the last digit. 

```
input_str = "My number is 12 43 78 32.?"


def count_d(x):
    # your code
  
def remove_punct(x):
    # your code

def first_and_last_idx(x):
    # your code


print(count_d(input_str))
# 8

print(remove_punct(input_str))
# "My number is 12 43 78 32"
```

*Hint*: `string.punctuation` contains a list of punctuations.

- [ ] Lastly, write tests for all of the functions.

</details>

<br /> 



## Project Organization
```
├── LICENSE                <- the license of this code
├── README.md              <- The top-level README for this project.
├── .github            
│   └── workflows          <- workflows to automatically run when code is pushed
│   │    └── pytest.yml    <- A workflow which runs pytests upon push
├── tests                  <- The pytest test suite
│   ├── test_numpy.py         
│   └── test_neural_network.py
├── .gitignore             <- A list of files not uploaded to git
├── requirement.txt        <- A requirements file of the required packages.
├── neural_network.py      <- A script containing code for a numpy neural network (currently missing)
└── ...
```


## Prerequisites
- Have done the data camp on unit testing with pytest
- Have participated in day 3 on the workshop, otherwise see section `I weren't there for the workshop`


## Intended learning goals
- Being able to use tests and check when and why tests pass
- Being able to hand-in an assignment using Github classrooms

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

<details>
  <summary> I weren't there for the class presenting the assignment what did I miss. </summary>

Well assuming you have done the [preparations](https://github.com/CHCAA-EDUX/NLP-E21/blob/main/syllabus/classes/class1.md) for the class you are in good shape. You should know about pytests from the data camp course and for running the pytest see corresponding FAQ.

The primary introduction of this assignment is to get your started with GitHub classrooms. A GitHub tool for doing assignments in classes. In the `classes` channel on Slack you should see a link to joining the assignment, remember to join the team you want to work with.

The benefit of using GitHub classrooms is that you get presented to continous integration. Namely that the code is automatically tested when pushed to git. For this assignment, you will create your own test and they will run when you push it to the git. You can see the "Actions" tab you should see two different workflows. You want to see that the `Pytest (Ubuntu)` has passed. This should correspond to running the tests on your own computer. If not you can always debug by examing the code output of the workflow.


</details>
