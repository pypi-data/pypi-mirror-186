# Description

Build random forests for classification and regression problems. 
The same program is available on [CRAN](URL 'https://cran.r-project.org/web/packages/brif/index.html') for R users. 

# Installation

For Python:
```bash
pip install brif
```

For R:
```R
install.packages('brif')
```

To use on Google Colab:
```python
!pip install brif
from brif import brif
```

# Examples

```python
from brif import brif
import pandas as pd

# Create a brif object with default parameters.
bf = brif.brif()  

# Display the current parameter values. 
bf.get_param()  

# To change certain parameter values, e.g.:
bf.set_param({'ntrees':100, 'nthreads':2})

# Or simply:
bf.ntrees = 200

# Load input data frame. Data must be a pandas data frame with appropriate headers.
df = pd.read_csv("auto.csv")

# Train the model
bf.fit(df, 'origin')  # specify the target column name

# Or equivalently
bf.fit(df, 7)  # specify the target column index

# Make predictions 
# The target variable column must be excluded, and all other columns should appear in the same order as in training
# Here, predict the first 10 rows of df
pred_labels = bf.predict(df.iloc[0:10, 0:7], type='class')  # return a list containing the predicted class labels
pred_scores = bf.predict(df.iloc[0:10, 0:7], type='score')  # return a data frame containing predicted probabilities by class

# Note: for a regression problem (i.e., when the response variable is numeric type), the predict function will always return a list containing the predicted values

```

# Parameters
**tmp_preddata**
a character string specifying a filename to save the temporary scoring data. Default is "tmp_brif_preddata.txt".

**n_numeric_cuts**	
an integer value indicating the maximum number of split points to generate for each numeric variable.

**n_integer_cuts**	
an integer value indicating the maximum number of split points to generate for each integer variable.

**max_integer_classes**
an integer value. If the target variable is integer and has more than max_integer_classes unique values in the training data, then the target variable will be grouped into max_integer_classes bins. If the target variable is numeric, then the smaller of max_integer_classes and the number of unique values number of bins will be created on the target variables and the regression problem will be solved as a classification problem.

**max_depth**
an integer specifying the maximum depth of each tree. Maximum is 40.

**min_node_size**	
an integer specifying the minimum number of training cases a leaf node must contain.

**ntrees**
an integer specifying the number of trees in the forest.

**ps**
an integer indicating the number of predictors to sample at each node split. Default is 0, meaning to use sqrt(p), where p is the number of predictors in the input.

**max_factor_levels**
an integer. If any factor variables has more than max_factor_levels, the program stops and prompts the user to increase the value of this parameter if the too-many-level factor is indeed intended.

**bagging_method**
an integer indicating the bagging sampling method: 0 for sampling without replacement; 1 for sampling with replacement (bootstrapping).

**bagging_proportion**	
a numeric scalar between 0 and 1, indicating the proportion of training observations to be used in each tree.

**split_search**
an integer indicating the choice of the split search method. 0: randomly pick a split point; 1: do a local search; 2: random pick subject to regulation; 3: local search subject to regulation; 4 or above: a mix of options 0 to 3.

**search_radius**
a positive integer indicating the split point search radius. This parameter takes effect only in the self-regulating local search (split_search = 2 or above).

**seed**
a positive integer, random number generator seed.

**nthreads**
an integer specifying the number of threads used by the program. This parameter takes effect only on systems supporting OpenMP.

**vote_method**
an integer (0 or 1) specifying the voting method in prediction. 0: each leaf contributes the raw count and an average is taken on the sum over all leaves; 1: each leaf contributes an intra-node fraction which is then averaged over all leaves with equal weight.

**na_numeric**
a numeric value, substitute for 'nan' in numeric variables.

**na_integer**
an integer value, substitute for 'nan' in integer variables.

**na_factor**
a character string, substitute for missing values in factor variables. 

**type**
a character string indicating the return content of the predict function. For a classification problem, "score" means the by-class probabilities and "class" means the class labels (i.e., the target variable levels). For regression, the predicted values are returned. This is a parameter for the predict function, not an attribute of the brif object. 

