
*see assignment_description.md for a description of the assignment*

# Summary

<!-- 
This should include a short description of which models you have tried and conclusions from comparing these models. It should also include an argument This should be no longer than an abstract. This section can also include questions regarding the assignment.
-->

# Performance
<!-- 
This should include a table of performance metrics of different models. The table should at least include the performance metrics of logistic regression and a neural network applied to a TF-IDF representation of the documents. It should also include a least two experiments which experiment either with:
- the size of the neural network
- the activation functions (e.g. relu or sigmoid)
- filtering of the word prior to creating to word counts or tf-idf (e.g. only include nouns or lowercase)
- document representation (e.g. using raw word frequencies vs. using term frequencies)
- or similar experimentation

You should at least report the accuracy but are free to report other measures such as AUC, sensitivity and specificity. 
 -->

## Project Organization
The organization of the project is as follows:

<!-- 
Correct this to reflect changes which you might have made
-->

```
├── LICENSE                    <- the license of this code
├── README.md                  <- The top-level README for this project.
├── .github            
│   └── workflows              <- workflows to automatically run when code is pushed
│   │    └── pytest.yml        <- A workflow which runs pytests upon push
├── classification             <- The main folder for scripts
│   ├── tests                  <- The pytest test suite
│   │   └── ...
|   └── ...
├── .gitignore                 <- A list of files not uploaded to git
├── requirement.txt            <- A requirements file of the required packages.
└── assignment_description.md  <- the assignment description
```



## Running the code
You can run the reproduce all the experiment by cloning the GitHub repository and running the following:

<!-- Fill out to match, this code should run all the experiemnts in the performance section and print the performances. It might be preferable to set a seed to ensure reproducibility. -->
```
pip install -r requirement.txt
python classification/main.py
```