# Uniqueness Shapley
Uniqueness Shapley is an EDA tool based on the feature importance method Cohort Shapley, and it quantifies the extent to which different features in a dataset make subjects in that dataset more identifiable.  Using the code in the repository, one can calculate the Uniqueness Shapley value for feature corresponding to each subject or instance in the dataset, which can also be aggregated to answer questions about subpopulations of interest.  For more details on the method and how to interpret the results, please see the [paper](https://arxiv.org/pdf/2105.08013.pdf):
> Seiler, B., Mase, M., & Owen, A. B. (2021). What Makes You Unique? arXiv preprint arXiv:2105.08013.

## Prerequisites
This code is tested on:
- Python 3.8.8
- NumPy 1.20.1
- Pandas 1.2.4
- scipy 1.6.2

For example notebooks, we need:
- jupyter 1.0.0


# Getting Started
See Jupyter notebook example [here](UniquenessShapley.ipynb)

# Usages
Please note that as of the current version, this repository will only take as input, pandas data frames with categorical features coded with levels taking consecutive integer values starting with one.  The current implementation has a runtime linear in the number of rows, but exponential in the number of features.

# Future Additions
We will be adding more flexible code to handle more types of input.  We will be adding more examples to the Jupyter Notebook.  We will be adding an approximate method for dealing with larger numbers of features.

# Sources
The files ArrayRecord.py, IteratedTreeContingencyTable.py, and SparseADTree.py are from [uraplutonium](https://github.com/uraplutonium/adtree-py) and used under their [license](https://github.com/uraplutonium/adtree-py/blob/master/LICENSE).  No changes have been made to these files except to include references to their source at the top.
