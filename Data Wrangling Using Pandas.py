
(base) C:\Users\nt65000>python
Python 3.7.1 (default, Dec 10 2018, 22:54:23) [MSC v.1915 64 bit (AMD64)] :: Anaconda, Inc. on win32
Type "help", "copyright", "credits" or "license" for more information.
>>> import numpy as np
>>> import pandas as pd
>>> transactions = pd.DataFrame(
...                              {
...                               'TransactionID': np.arange(10)+1,
...                               'TransactionDate': pd.to_datetime(['2010-08-21', '2011-05-26', '2011-06-16', '2012-08-26', '2013-06-06',
...                                                                 '2013-12-23', '2013-12-30', '2014-04-24', '2015-04-24', '2016-05-08']).date,
...                                'UserID':    [7, 3, 3, 1, 2, 2, 3, np.nan, 7, 3],
...                                'ProductID': [2, 4, 3, 2, 4, 5, 4, 2, 4, 4],
...                                'Quantity':  [1, 1, 1, 3, 1, 6, 1, 3, 3, 4]
...                             }
... )
>>> # Show dataframe summary
... transactions.info()
<class 'pandas.core.frame.DataFrame'>
RangeIndex: 10 entries, 0 to 9
Data columns (total 5 columns):
TransactionID      10 non-null int32
TransactionDate    10 non-null object
UserID             9 non-null float64
ProductID          10 non-null int64
Quantity           10 non-null int64
dtypes: float64(1), int32(1), int64(2), object(1)
memory usage: 440.0+ bytes
>>> No.of observations (rows) present in the dataframe
  File "<stdin>", line 1
    No.of observations (rows) present in the dataframe
                     ^
SyntaxError: invalid syntax
>>> #No.of observations (rows) present in the dataframe
... transactions.shape[0]
10
>>> #No.of features (columns) present in the dataframe
... transactions.shape[1]
5
>>> #Get feature names
... #Get row names
... transactions.index.values
array([0, 1, 2, 3, 4, 5, 6, 7, 8, 9], dtype=int64)
>>> #Get column names
... transactions.columns.values
array(['TransactionID', 'TransactionDate', 'UserID', 'ProductID',
       'Quantity'], dtype=object)
>>> #Change the name of column "Quantity" to "Quant"
... transactions.rename(columns={'Quantity': 'Quant'})
   TransactionID TransactionDate  UserID  ProductID  Quant
0              1      2010-08-21     7.0          2      1
1              2      2011-05-26     3.0          4      1
2              3      2011-06-16     3.0          3      1
3              4      2012-08-26     1.0          2      3
4              5      2013-06-06     2.0          4      1
5              6      2013-12-23     2.0          5      6
6              7      2013-12-30     3.0          4      1
7              8      2014-04-24     NaN          2      3
8              9      2015-04-24     7.0          4      3
9             10      2016-05-08     3.0          4      4
>>> #Change the name of columns ProductID and UserID to PID and UID respectively
... transactions.rename(columns={'Quantity': 'Quant', 'UserID':'UID'})
   TransactionID TransactionDate  UID  ProductID  Quant
0              1      2010-08-21  7.0          2      1
1              2      2011-05-26  3.0          4      1
2              3      2011-06-16  3.0          3      1
3              4      2012-08-26  1.0          2      3
4              5      2013-06-06  2.0          4      1
5              6      2013-12-23  2.0          5      6
6              7      2013-12-30  3.0          4      1
7              8      2014-04-24  NaN          2      3
8              9      2015-04-24  7.0          4      3
9             10      2016-05-08  3.0          4      4
>>> transactions.rename(columns={'ProductID': 'PID', 'UserID':'UID'})
   TransactionID TransactionDate  UID  PID  Quantity
0              1      2010-08-21  7.0    2         1
1              2      2011-05-26  3.0    4         1
2              3      2011-06-16  3.0    3         1
3              4      2012-08-26  1.0    2         3
4              5      2013-06-06  2.0    4         1
5              6      2013-12-23  2.0    5         6
6              7      2013-12-30  3.0    4         1
7              8      2014-04-24  NaN    2         3
8              9      2015-04-24  7.0    4         3
9             10      2016-05-08  3.0    4         4
>>> #Set the column order of transactions as ProductID, Quantity, TransactionDate, TransactionID, UserID
... transactions[['ProductID', 'Quantity', 'TransactionDate', 'TransactionID', 'UserID']]
   ProductID  Quantity TransactionDate  TransactionID  UserID
0          2         1      2010-08-21              1     7.0
1          4         1      2011-05-26              2     3.0
2          3         1      2011-06-16              3     3.0
3          2         3      2012-08-26              4     1.0
4          4         1      2013-06-06              5     2.0
5          5         6      2013-12-23              6     2.0
6          4         1      2013-12-30              7     3.0
7          2         3      2014-04-24              8     NaN
8          4         3      2015-04-24              9     7.0
9          4         4      2016-05-08             10     3.0
>>> #Make UserID the first column of transactions
... transactions[pd.unique(['UserID'] + transactions.columns.values.tolist()).tolist()]
   UserID  TransactionID TransactionDate  ProductID  Quantity
0     7.0              1      2010-08-21          2         1
1     3.0              2      2011-05-26          4         1
2     3.0              3      2011-06-16          3         1
3     1.0              4      2012-08-26          2         3
4     2.0              5      2013-06-06          4         1
5     2.0              6      2013-12-23          5         6
6     3.0              7      2013-12-30          4         1
7     NaN              8      2014-04-24          2         3
8     7.0              9      2015-04-24          4         3
9     3.0             10      2016-05-08          4         4
>>> #Get the 2nd column
... transactions[[1]].values[:, 0]
Traceback (most recent call last):
  File "<stdin>", line 2, in <module>
  File "C:\Users\nt65000\AppData\Local\Continuum\anaconda3\lib\site-packages\pandas\core\frame.py", line 2682, in __getitem__
    return self._getitem_array(key)
  File "C:\Users\nt65000\AppData\Local\Continuum\anaconda3\lib\site-packages\pandas\core\frame.py", line 2726, in _getitem_array
    indexer = self.loc._convert_to_indexer(key, axis=1)
  File "C:\Users\nt65000\AppData\Local\Continuum\anaconda3\lib\site-packages\pandas\core\indexing.py", line 1327, in _convert_to_indexer
    .format(mask=objarr[mask]))
KeyError: '[1] not in index'
>>> transactions[['Quantity']].values[:, 0]
array([1, 1, 1, 3, 1, 6, 1, 3, 3, 4], dtype=int64)
>>> #Get the ProductID array
... transactions.ProductID.values
array([2, 4, 3, 2, 4, 5, 4, 2, 4, 4], dtype=int64)
>>> #Get the ProductID array using a variable
... col = "ProductID"
>>> transactions[[col]].values[:, 0]
array([2, 4, 3, 2, 4, 5, 4, 2, 4, 4], dtype=int64)
>>> #Subset rows 1, 3, and 6
... transactions.iloc[[0,2,5]]
   TransactionID TransactionDate  UserID  ProductID  Quantity
0              1      2010-08-21     7.0          2         1
2              3      2011-06-16     3.0          3         1
5              6      2013-12-23     2.0          5         6
>>> #Subset rows exlcuding 1, 3, and 6
... transactions.drop([0,2,5], axis=0)
   TransactionID TransactionDate  UserID  ProductID  Quantity
1              2      2011-05-26     3.0          4         1
3              4      2012-08-26     1.0          2         3
4              5      2013-06-06     2.0          4         1
6              7      2013-12-30     3.0          4         1
7              8      2014-04-24     NaN          2         3
8              9      2015-04-24     7.0          4         3
9             10      2016-05-08     3.0          4         4
>>> Subset the first 3 rows
  File "<stdin>", line 1
    Subset the first 3 rows
             ^
SyntaxError: invalid syntax
>>> #Subset the first 3 rows
... transactions[:3]
   TransactionID TransactionDate  UserID  ProductID  Quantity
0              1      2010-08-21     7.0          2         1
1              2      2011-05-26     3.0          4         1
2              3      2011-06-16     3.0          3         1
>>> transactions.head(3)
   TransactionID TransactionDate  UserID  ProductID  Quantity
0              1      2010-08-21     7.0          2         1
1              2      2011-05-26     3.0          4         1
2              3      2011-06-16     3.0          3         1
>>> #Subset rows excluding the first 3 rows
... transactions[3:]
   TransactionID TransactionDate  UserID  ProductID  Quantity
3              4      2012-08-26     1.0          2         3
4              5      2013-06-06     2.0          4         1
5              6      2013-12-23     2.0          5         6
6              7      2013-12-30     3.0          4         1
7              8      2014-04-24     NaN          2         3
8              9      2015-04-24     7.0          4         3
9             10      2016-05-08     3.0          4         4
>>> transactions.tail(-3)
   TransactionID TransactionDate  UserID  ProductID  Quantity
3              4      2012-08-26     1.0          2         3
4              5      2013-06-06     2.0          4         1
5              6      2013-12-23     2.0          5         6
6              7      2013-12-30     3.0          4         1
7              8      2014-04-24     NaN          2         3
8              9      2015-04-24     7.0          4         3
9             10      2016-05-08     3.0          4         4
>>> #Subset the last 2 rows
... transactions[:2]
   TransactionID TransactionDate  UserID  ProductID  Quantity
0              1      2010-08-21     7.0          2         1
1              2      2011-05-26     3.0          4         1
>>> transactions[2:]
   TransactionID TransactionDate  UserID  ProductID  Quantity
2              3      2011-06-16     3.0          3         1
3              4      2012-08-26     1.0          2         3
4              5      2013-06-06     2.0          4         1
5              6      2013-12-23     2.0          5         6
6              7      2013-12-30     3.0          4         1
7              8      2014-04-24     NaN          2         3
8              9      2015-04-24     7.0          4         3
9             10      2016-05-08     3.0          4         4
>>> transactions.tail(2)
   TransactionID TransactionDate  UserID  ProductID  Quantity
8              9      2015-04-24     7.0          4         3
9             10      2016-05-08     3.0          4         4
>>> transactions[9:]
   TransactionID TransactionDate  UserID  ProductID  Quantity
9             10      2016-05-08     3.0          4         4
>>> transactions[8:]
   TransactionID TransactionDate  UserID  ProductID  Quantity
8              9      2015-04-24     7.0          4         3
9             10      2016-05-08     3.0          4         4
>>> #Subset rows excluding the last 2 rows
... transactions.tail(-2)
   TransactionID TransactionDate  UserID  ProductID  Quantity
2              3      2011-06-16     3.0          3         1
3              4      2012-08-26     1.0          2         3
4              5      2013-06-06     2.0          4         1
5              6      2013-12-23     2.0          5         6
6              7      2013-12-30     3.0          4         1
7              8      2014-04-24     NaN          2         3
8              9      2015-04-24     7.0          4         3
9             10      2016-05-08     3.0          4         4
>>> transactions.tail(2)
   TransactionID TransactionDate  UserID  ProductID  Quantity
8              9      2015-04-24     7.0          4         3
9             10      2016-05-08     3.0          4         4
>>> transactions.tail(-8)
   TransactionID TransactionDate  UserID  ProductID  Quantity
8              9      2015-04-24     7.0          4         3
9             10      2016-05-08     3.0          4         4
>>> #Subset rows where Quantity > 1
... transactions[transactions.Quantity > 1]
   TransactionID TransactionDate  UserID  ProductID  Quantity
3              4      2012-08-26     1.0          2         3
5              6      2013-12-23     2.0          5         6
7              8      2014-04-24     NaN          2         3
8              9      2015-04-24     7.0          4         3
9             10      2016-05-08     3.0          4         4
>>> transactions[:8]
   TransactionID TransactionDate  UserID  ProductID  Quantity
0              1      2010-08-21     7.0          2         1
1              2      2011-05-26     3.0          4         1
2              3      2011-06-16     3.0          3         1
3              4      2012-08-26     1.0          2         3
4              5      2013-06-06     2.0          4         1
5              6      2013-12-23     2.0          5         6
6              7      2013-12-30     3.0          4         1
7              8      2014-04-24     NaN          2         3
>>> #Subset rows where UserID = 2
... transactions[transactions.UserID == 2]
   TransactionID TransactionDate  UserID  ProductID  Quantity
4              5      2013-06-06     2.0          4         1
5              6      2013-12-23     2.0          5         6
>>> #Subset rows where Quantity > 1 and UserID = 2
... transactions[(transactions.Quantity > 1) & (transactions.UserID == 2)]
   TransactionID TransactionDate  UserID  ProductID  Quantity
5              6      2013-12-23     2.0          5         6
>>> #Subset rows where Quantity + UserID is > 3
... transactions[transactions.Quantity + transactions.UserID > 3]
   TransactionID TransactionDate  UserID  ProductID  Quantity
0              1      2010-08-21     7.0          2         1
1              2      2011-05-26     3.0          4         1
2              3      2011-06-16     3.0          3         1
3              4      2012-08-26     1.0          2         3
5              6      2013-12-23     2.0          5         6
6              7      2013-12-30     3.0          4         1
8              9      2015-04-24     7.0          4         3
9             10      2016-05-08     3.0          4         4
>>> #Subset rows where an external array, foo, is True
... foo=np.array([True, False, True, False, True, False, True, False, True, False])
>>> transactions[foo]
   TransactionID TransactionDate  UserID  ProductID  Quantity
0              1      2010-08-21     7.0          2         1
2              3      2011-06-16     3.0          3         1
4              5      2013-06-06     2.0          4         1
6              7      2013-12-30     3.0          4         1
8              9      2015-04-24     7.0          4         3
>>> #Subset rows where an external array, bar, is positive
... bar=np.array([-1, -2, -3, -4, 0, 1, 2, 3, 4, 5])
>>> transactions[bar > 0]
   TransactionID TransactionDate  UserID  ProductID  Quantity
5              6      2013-12-23     2.0          5         6
6              7      2013-12-30     3.0          4         1
7              8      2014-04-24     NaN          2         3
8              9      2015-04-24     7.0          4         3
9             10      2016-05-08     3.0          4         4
>>> #Subset rows where foo is TRUE or bar is negative
... foo=np.array([True, -2, -3, True, 0, -1, True, 3, 4, -5])
>>> transactions[foo | foo < 0]
   TransactionID TransactionDate  UserID  ProductID  Quantity
1              2      2011-05-26     3.0          4         1
2              3      2011-06-16     3.0          3         1
5              6      2013-12-23     2.0          5         6
9             10      2016-05-08     3.0          4         4
>>> transactions[foo & foo < 0]
   TransactionID TransactionDate  UserID  ProductID  Quantity
1              2      2011-05-26     3.0          4         1
2              3      2011-06-16     3.0          3         1
5              6      2013-12-23     2.0          5         6
9             10      2016-05-08     3.0          4         4
>>> transactions[foo < 0]
   TransactionID TransactionDate  UserID  ProductID  Quantity
1              2      2011-05-26     3.0          4         1
2              3      2011-06-16     3.0          3         1
5              6      2013-12-23     2.0          5         6
9             10      2016-05-08     3.0          4         4
>>> transactions[foo]
Traceback (most recent call last):
  File "<stdin>", line 1, in <module>
  File "C:\Users\nt65000\AppData\Local\Continuum\anaconda3\lib\site-packages\pandas\core\frame.py", line 2682, in __getitem__
    return self._getitem_array(key)
  File "C:\Users\nt65000\AppData\Local\Continuum\anaconda3\lib\site-packages\pandas\core\frame.py", line 2726, in _getitem_array
    indexer = self.loc._convert_to_indexer(key, axis=1)
  File "C:\Users\nt65000\AppData\Local\Continuum\anaconda3\lib\site-packages\pandas\core\indexing.py", line 1327, in _convert_to_indexer
    .format(mask=objarr[mask]))
KeyError: '[ 1 -2 -3  1  0 -1  1  3  4 -5] not in index'
>>> #Subset the rows where foo is not TRUE and bar is not negative
... transactions[~foo & (bar >= 0)]
Traceback (most recent call last):
  File "<stdin>", line 2, in <module>
  File "C:\Users\nt65000\AppData\Local\Continuum\anaconda3\lib\site-packages\pandas\core\frame.py", line 2682, in __getitem__
    return self._getitem_array(key)
  File "C:\Users\nt65000\AppData\Local\Continuum\anaconda3\lib\site-packages\pandas\core\frame.py", line 2726, in _getitem_array
    indexer = self.loc._convert_to_indexer(key, axis=1)
  File "C:\Users\nt65000\AppData\Local\Continuum\anaconda3\lib\site-packages\pandas\core\indexing.py", line 1327, in _convert_to_indexer
    .format(mask=objarr[mask]))
KeyError: '[0 0 0 0 1 0 0 0 1 0] not in index'
>>> transactions[~foo & (bar >= 0)]
Traceback (most recent call last):
  File "<stdin>", line 1, in <module>
  File "C:\Users\nt65000\AppData\Local\Continuum\anaconda3\lib\site-packages\pandas\core\frame.py", line 2682, in __getitem__
    return self._getitem_array(key)
  File "C:\Users\nt65000\AppData\Local\Continuum\anaconda3\lib\site-packages\pandas\core\frame.py", line 2726, in _getitem_array
    indexer = self.loc._convert_to_indexer(key, axis=1)
  File "C:\Users\nt65000\AppData\Local\Continuum\anaconda3\lib\site-packages\pandas\core\indexing.py", line 1327, in _convert_to_indexer
    .format(mask=objarr[mask]))
KeyError: '[0 0 0 0 1 0 0 0 1 0] not in index'
>>> #Subset by columns 1 and 3
... transactions.iloc[:, [0, 2]]
   TransactionID  UserID
0              1     7.0
1              2     3.0
2              3     3.0
3              4     1.0
4              5     2.0
5              6     2.0
6              7     3.0
7              8     NaN
8              9     7.0
9             10     3.0
>>> transactions.iloc[0, 2]
7.0
>>> #Subset by columns TransactionID and TransactionDate
... transactions[['TransactionID', 'TransactionDate']]
   TransactionID TransactionDate
0              1      2010-08-21
1              2      2011-05-26
2              3      2011-06-16
3              4      2012-08-26
4              5      2013-06-06
5              6      2013-12-23
6              7      2013-12-30
7              8      2014-04-24
8              9      2015-04-24
9             10      2016-05-08
>>> #Subset rows where TransactionID > 5 and subset columns by TransactionID and TransactionDate
... transactions.loc[transactions.TransactionID > 5, ['TransactionID', 'TransactionDate']]
   TransactionID TransactionDate
5              6      2013-12-23
6              7      2013-12-30
7              8      2014-04-24
8              9      2015-04-24
9             10      2016-05-08
>>> #Subset columns by a variable list of columm names
... cols = ["TransactionID", "UserID", "Quantity"]
>>> transactions[cols]
   TransactionID  UserID  Quantity
0              1     7.0         1
1              2     3.0         1
2              3     3.0         1
3              4     1.0         3
4              5     2.0         1
5              6     2.0         6
6              7     3.0         1
7              8     NaN         3
8              9     7.0         3
9             10     3.0         4
>>> #Subset columns excluding a variable list of column names
... cols = ["TransactionID", "UserID", "Quantity"]
>>> transactions.drop(cols, axis=1)
  TransactionDate  ProductID
0      2010-08-21          2
1      2011-05-26          4
2      2011-06-16          3
3      2012-08-26          2
4      2013-06-06          4
5      2013-12-23          5
6      2013-12-30          4
7      2014-04-24          2
8      2015-04-24          4
9      2016-05-08          4
>>> #Convert the TransactionDate column to type Date
... transactions['TransactionDate'] = pd.to_datetime(transactions.TransactionDate)
>>> Insert a new column, Foo = UserID + ProductID
  File "<stdin>", line 1
    Insert a new column, Foo = UserID + ProductID
           ^
SyntaxError: invalid syntax
>>> #Insert a new column, Foo = UserID + ProductID
... transactions['Foo'] = transactions.UserID + transactions.ProductID
>>> #Subset rows where TransactionID is even and set Foo = NA
... transactions.loc[transactions.TransactionID % 2 == 0, 'Foo'] = np.nan
>>> #Add 100 to each TransactionID
... transactions.TransactionID = transactions.TransactionID + 100
>>> #Insert a column indicating each row number
... transactions['RowIdx'] = np.arange(transactions.shape[0])
>>> #Insert columns indicating the rank of each Quantity, minimum Quantity and maximum Quantity
... transactions['QuantityRk'] = transactions.Quantity.rank(method='average')
>>> transactions['QuantityMin'] = transactions.Quantity.min()
>>> transactions['QuantityMax'] = transactions.Quantity.max()
>>> #Remove column Foo
... transactions.drop('Foo', axis=1, inplace=True)
>>> #Remove multiple columns RowIdx, QuantityRk, and RowIdx
... transactions.drop(['QuantityRk', 'QuantityMin', 'QuantityMax'], axis=1, inplace=True)
>>> #Group the transations per user, measuring the number of transactions per user
... transactions.groupby('UserID').apply(lambda x: pd.Series(dict(
...                                                              Transactions=x.shape[0]
... ))).reset_index()
   UserID  Transactions
0     1.0             1
1     2.0             2
2     3.0             4
3     7.0             2
>>> #Group the transactions per user, measuring the transactions and average quantity per user
... ransactions.groupby('UserID').apply(lambda x: pd.Series(dict(
...                                                              Transactions=x.shape[0],
...                                                              QuantityAvg=x.Quantity.mean()
... ))).reset_index()
Traceback (most recent call last):
  File "<stdin>", line 2, in <module>
NameError: name 'ransactions' is not defined
>>> transactions.groupby('UserID').apply(lambda x: pd.Series(dict(
...                                                              Transactions=x.shape[0],
...                                                              QuantityAvg=x.Quantity.mean()
... ))).reset_index()
   UserID  Transactions  QuantityAvg
0     1.0           1.0         3.00
1     2.0           2.0         3.50
2     3.0           4.0         1.75
3     7.0           2.0         2.00
>>>