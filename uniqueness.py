import numpy as np
import pandas as pd
from scipy.special import comb
import ArrayRecord as Record
import SparseADTree as ADTree
import IteratedTreeContingencyTable as ContingencyTable


def powerset(s):
    """
    simple powerset generator
    
    Parameters
    ----------
    s: arbitrary list 
            
    Returns
    -------
    generator for powerset of s
    """
    x = len(s)
    masks = [1 << i for i in range(x)]
    for i in range(1 << x):
        yield [ss for mask, ss in zip(masks, s) if i & mask]

def extract(j,p,n,ps,mat):
    """
    Calcuates uniqueness shapleys for one features
    
    Parameters
    ----------
    j: integer, the target feature to calculate the shapley value for
    p: integer, the number of features
    n: integer, the number of instances
    ps: list, powerset of the features
    mat:  numpy array, each row corresponding to an instance in the data, each column corresponding to an element of the powerset of the features
        The values should be the value function output for that subset and that instance.  That is the negative log cohort size.
            
    Returns
    -------
    a numpy array of the Uniqueness Shapley values for corresponding to the data from valmat for feature j
    """
    m = len(ps)
    list1 = list(powerset(list(range(1,1+p))[:j-1]+list(range(1,1+p))[j:]))
    jlist = [np.sort(l+[j]) for l in list1]
    res = np.empty([n,len(list1)])
    for i in range(1,len(list1)):
        temp1 = np.empty(m)
        temp2 = np.empty(m)
        temp3 = np.empty(m)
        for k in range(m):
            temp1[k]=(set(ps[k])==set(list1[i]))
            temp2[k]=(set(ps[k])==set(jlist[i]))
        colind1 = int(np.where(temp1==True)[0])
        colind2 = int(np.where(temp2==True)[0])
        fac = 1/(comb(p-1,len(list1[i])))
        res[:,i] = fac*(mat[:,colind2]-mat[:,colind1])
    for k in range(m):
        temp3[k]=(set(ps[k])==set([j]))
    colind3 = int(np.where(temp3==True)[0])
    fac = 1/(comb(p-1,0))
    res[:,0] = fac*(mat[:,colind3]-mat[:,0])
    return(np.sum(res,axis=1)*(1/p))

def calcShap(valmat,p,ps):
    """
    Calcuates uniqueness shapleys for all features
    
    Parameters
    ----------
    valmat: numpy array, each row corresponding to an instance in the data, each column corresponding to an element of the powerset of the features
        The values should be the value function output for that subset and that instance.  That is the negative log cohort size.
    p: integer, the number of features
    ps: list, containing the powerset of the features
    
    Returns
    -------
    a numpy array of the Uniqueness Shapley values for corresponding to the data from valmat
    """
    n = np.shape(valmat)[0]
    res = np.empty([n,p])
    for j in range(p):
        res[:,j] = extract((j+1),p,n,ps,valmat)
    return(res)

def uniqueShap(df):
    """
    main wrapper function
    
    Parameters
    ----------
    df: a Pandas dataframe with categorical data.  Currently requires that the features be recoded with levels taking consecutive integer values starting with one. 
            
    Returns
    -------
    a numpy array of the Uniqueness Shapley values for df
    
    """

    arityList = list(df.nunique())
    recordsTable = df.values.tolist()
    
    #if __name__ == '__main__':
    # import the original dataset to the record module
    Record.initRecord([arityList, recordsTable])

    # declare that the ADTree module uses ArrayRecord module as dataset
    ADTree.importModules('ArrayRecord')
    
    # declare that the ContingencyTable uses ArrayRecord and SparsADTree modules
    ContingencyTable.importModules('ArrayRecord', 'SparseADTree')

    # initialise recordNums containing all numbers in the dataset
    recordNums = [num for num in range(1, Record.recordsLength+1)]

    # build an AD-Tree with attribute list starts from the first attribute,
    # and for all the records
    adtree = ADTree.ADNode(1, recordNums)

    n = np.shape(df)[0]
    p = np.shape(df)[1]
    ps = list(powerset(list(range(1,1+p))))
    m = len(ps)

    counts = np.empty([n,m])
    counts[:,0] = n
    for j in range(1,m):
        ind = df.iloc[:,np.subtract(ps[j],1)].values.tolist()
        contab = ContingencyTable.ContingencyTable(ps[j], adtree)
        counts[:,j] = list(map(contab.getCount,ind))
    vals = -np.log2(counts)
    res = calcShap(vals,p,ps)
    return(res)