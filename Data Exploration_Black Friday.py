
(base) C:\Users\nt65000>ipython
Python 3.7.1 (default, Dec 10 2018, 22:54:23) [MSC v.1915 64 bit (AMD64)]
Type 'copyright', 'credits' or 'license' for more information
IPython 7.2.0 -- An enhanced Interactive Python. Type '?' for help.

In [1]: %reset -f

In [2]: import numpy as np

In [3]: import pandas as pd

In [4]: import os

In [5]: import seaborn as sns

In [6]: import matplotlib.pyplot as plt

In [7]: os.chdir("C:\\Users\\nt65000\\Downloads")

In [8]: os.listdir()
Out[8]:
['APR-05TH TO 17TH SHEET.xlsx',
 'APR-05TH TO 22nd UPDATED SHEET .xlsx',
 'BlackFriday.csv',
 'black_friday_exploration_exercise.py',
 'block_friday_data_exploration.py',
 'BOT Restart Guide(1).docx',
 'BOT Restart Guide.docx',
 'Business Requirement DocumentV4.0.docx',
 'desktop.ini',
 'Java-SB-MS.docx',
 'ML Webinar.docx',
 'NAD_Assessment.zip',
 'PIVOT TABLE FOR CONSOLIDATED SHEET 09-MAR TO 05-APR-2019_Deepthi.xlsx',
 'PIVOT TABLE FOR CONSOLIDATED SHEET 09-MAR TO 31-MAR-2019_Deepthi_PROD RUN.xlsx',
 'PIVOT TABLE FOR CONSOLIDATED SHEET DAY-1 TO 08-MAR-2019_Deepthi.xlsx',
 'PIVOT TABLE FOR CONSOLIDATED SHEET DAY-1 TO 31-MAR-2019_Deepthi.xlsx',
 'POD_SAP.zip',
 'Python-Sample-Resume-1.docx',
 'Resume- Nagadeepthi Tangudu-JAVA-Python 11yrs.docx',
 'screenshots.docx',
 'Solenis AP Invoice Scanning & Archiving Process Automation.pptx',
 'Training Certification Reimbursement Policy.zip',
 'WLP Template.pptx',
 'Workshop on Pending IT ideas with Raj & Deepthi on 18th April 2019.xlsx',
 'Workshop_Ideas Updated As On 22-04-2019.xlsx',
 '~$Feb 27th Workshop_Ideas Updated As On 18th March.xlsx']

In [9]: # 1.8 Count the number of files in your current working folder

In [10]: len(os.listdir())
Out[10]: 26

In [11]: df = pd.read_csv( 'black-friday.csv')
---------------------------------------------------------------------------
FileNotFoundError                         Traceback (most recent call last)
<ipython-input-11-29f6054ff606> in <module>
----> 1 df = pd.read_csv( 'black-friday.csv')

~\AppData\Local\Continuum\anaconda3\lib\site-packages\pandas\io\parsers.py in parser_f(filepath_or_buffer, sep, delimiter, header, names, index_col, usecols, squeeze, prefix, mangle_dupe_cols, dtype, engine, converters, true_values, false_values, skipinitialspace, skiprows, nrows, na_values, keep_default_na, na_filter, verbose, skip_blank_lines, parse_dates, infer_datetime_format, keep_date_col, date_parser, dayfirst, iterator, chunksize, compression, thousands, decimal, lineterminator, quotechar, quoting, escapechar, comment, encoding, dialect, tupleize_cols, error_bad_lines, warn_bad_lines, skipfooter, doublequote, delim_whitespace, low_memory, memory_map, float_precision)
    676                     skip_blank_lines=skip_blank_lines)
    677
--> 678         return _read(filepath_or_buffer, kwds)
    679
    680     parser_f.__name__ = name

~\AppData\Local\Continuum\anaconda3\lib\site-packages\pandas\io\parsers.py in _read(filepath_or_buffer, kwds)
    438
    439     # Create the parser.
--> 440     parser = TextFileReader(filepath_or_buffer, **kwds)
    441
    442     if chunksize or iterator:

~\AppData\Local\Continuum\anaconda3\lib\site-packages\pandas\io\parsers.py in __init__(self, f, engine, **kwds)
    785             self.options['has_index_names'] = kwds['has_index_names']
    786
--> 787         self._make_engine(self.engine)
    788
    789     def close(self):

~\AppData\Local\Continuum\anaconda3\lib\site-packages\pandas\io\parsers.py in _make_engine(self, engine)
   1012     def _make_engine(self, engine='c'):
   1013         if engine == 'c':
-> 1014             self._engine = CParserWrapper(self.f, **self.options)
   1015         else:
   1016             if engine == 'python':

~\AppData\Local\Continuum\anaconda3\lib\site-packages\pandas\io\parsers.py in __init__(self, src, **kwds)
   1706         kwds['usecols'] = self.usecols
   1707
-> 1708         self._reader = parsers.TextReader(src, **kwds)
   1709
   1710         passed_names = self.names is None

pandas\_libs\parsers.pyx in pandas._libs.parsers.TextReader.__cinit__()

pandas\_libs\parsers.pyx in pandas._libs.parsers.TextReader._setup_parser_source()

FileNotFoundError: File b'black-friday.csv' does not exist

In [12]: df = pd.read_csv('BlackFriday.csv')

In [13]: type(df)
Out[13]: pandas.core.frame.DataFrame

In [14]: df.memory_usage()
Out[14]:
Index                              80
User_ID                       4300616
Product_ID                    4300616
Gender                        4300616
Age                           4300616
Occupation                    4300616
City_Category                 4300616
Stay_In_Current_City_Years    4300616
Marital_Status                4300616
Product_Category_1            4300616
Product_Category_2            4300616
Product_Category_3            4300616
Purchase                      4300616
dtype: int64

In [15]: df.shape
Out[15]: (537577, 12)

In [16]: df.columns
Out[16]:
Index(['User_ID', 'Product_ID', 'Gender', 'Age', 'Occupation', 'City_Category',
       'Stay_In_Current_City_Years', 'Marital_Status', 'Product_Category_1',
       'Product_Category_2', 'Product_Category_3', 'Purchase'],
      dtype='object')

In [17]: df.columns.values
Out[17]:
array(['User_ID', 'Product_ID', 'Gender', 'Age', 'Occupation',
       'City_Category', 'Stay_In_Current_City_Years', 'Marital_Status',
       'Product_Category_1', 'Product_Category_2', 'Product_Category_3',
       'Purchase'], dtype=object)

In [18]: df.head()
Out[18]:
   User_ID Product_ID Gender   Age  Occupation    ...    Marital_Status Product_Category_1  Product_Category_2  Product_Category_3  Purchase
0  1000001  P00069042      F  0-17          10    ...                 0                  3                 NaN                 NaN      8370
1  1000001  P00248942      F  0-17          10    ...                 0                  1                 6.0                14.0     15200
2  1000001  P00087842      F  0-17          10    ...                 0                 12                 NaN                 NaN      1422
3  1000001  P00085442      F  0-17          10    ...                 0                 12                14.0                 NaN      1057
4  1000002  P00285442      M   55+          16    ...                 0                  8                 NaN                 NaN      7969

[5 rows x 12 columns]

In [19]: df.head(5)
Out[19]:
   User_ID Product_ID Gender   Age  Occupation    ...    Marital_Status Product_Category_1  Product_Category_2  Product_Category_3  Purchase
0  1000001  P00069042      F  0-17          10    ...                 0                  3                 NaN                 NaN      8370
1  1000001  P00248942      F  0-17          10    ...                 0                  1                 6.0                14.0     15200
2  1000001  P00087842      F  0-17          10    ...                 0                 12                 NaN                 NaN      1422
3  1000001  P00085442      F  0-17          10    ...                 0                 12                14.0                 NaN      1057
4  1000002  P00285442      M   55+          16    ...                 0                  8                 NaN                 NaN      7969

[5 rows x 12 columns]

In [20]: df.dtypes
Out[20]:
User_ID                         int64
Product_ID                     object
Gender                         object
Age                            object
Occupation                      int64
City_Category                  object
Stay_In_Current_City_Years     object
Marital_Status                  int64
Product_Category_1              int64
Product_Category_2            float64
Product_Category_3            float64
Purchase                        int64
dtype: object

In [21]: df["User_ID"] = df.User_ID.astype(object)

In [22]: df.dtypes
Out[22]:
User_ID                        object
Product_ID                     object
Gender                         object
Age                            object
Occupation                      int64
City_Category                  object
Stay_In_Current_City_Years     object
Marital_Status                  int64
Product_Category_1              int64
Product_Category_2            float64
Product_Category_3            float64
Purchase                        int64
dtype: object

In [23]: df.dtypes.value_counts()
Out[23]:
object     6
int64      4
float64    2
dtype: int64

In [24]: print(df.describe(include=['int64','float64','object']))
          User_ID Product_ID  Gender     Age      ...        Product_Category_1 Product_Category_2 Product_Category_3       Purchase
count    537577.0     537577  537577  537577      ...             537577.000000      370591.000000      164278.000000  537577.000000
unique     5891.0       3623       2       7      ...                       NaN                NaN                NaN            NaN
top     1001680.0  P00265242       M   26-35      ...                       NaN                NaN                NaN            NaN
freq       1025.0       1858  405380  214690      ...                       NaN                NaN                NaN            NaN
mean          NaN        NaN     NaN     NaN      ...                  5.295546           9.842144          12.669840    9333.859853
std           NaN        NaN     NaN     NaN      ...                  3.750701           5.087259           4.124341    4981.022133
min           NaN        NaN     NaN     NaN      ...                  1.000000           2.000000           3.000000     185.000000
25%           NaN        NaN     NaN     NaN      ...                  1.000000           5.000000           9.000000    5866.000000
50%           NaN        NaN     NaN     NaN      ...                  5.000000           9.000000          14.000000    8062.000000
75%           NaN        NaN     NaN     NaN      ...                  8.000000          15.000000          16.000000   12073.000000
max           NaN        NaN     NaN     NaN      ...                 18.000000          18.000000          18.000000   23961.000000

[11 rows x 12 columns]

In [25]: df.loc[10:20, ['User_ID','Product_ID']]
Out[25]:
    User_ID Product_ID
10  1000005  P00251242
11  1000005  P00014542
12  1000005  P00031342
13  1000005  P00145042
14  1000006  P00231342
15  1000006  P00190242
16  1000006   P0096642
17  1000006  P00058442
18  1000007  P00036842
19  1000008  P00249542
20  1000008  P00220442

In [26]: df.isna().any()
Out[26]:
User_ID                       False
Product_ID                    False
Gender                        False
Age                           False
Occupation                    False
City_Category                 False
Stay_In_Current_City_Years    False
Marital_Status                False
Product_Category_1            False
Product_Category_2             True
Product_Category_3             True
Purchase                      False
dtype: bool

In [27]: df.Age.value_counts()
Out[27]:
26-35    214690
36-45    107499
18-25     97634
46-50     44526
51-55     37618
55+       20903
0-17      14707
Name: Age, dtype: int64

In [28]: df.Occupation.value_counts()
Out[28]:
4     70862
0     68120
7     57806
1     45971
17    39090
20    32910
12    30423
14    26712
2     25845
16    24790
6     19822
3     17366
10    12623
5     11985
15    11812
11    11338
19     8352
13     7548
18     6525
9      6153
8      1524
Name: Occupation, dtype: int64

In [29]: df.City_Category.value_counts()
Out[29]:
B    226493
C    166446
A    144638
Name: City_Category, dtype: int64

In [30]: len(df.Product_ID.unique())
Out[30]: 3623

In [31]: len(df.Product_Category_1.unique())
Out[31]: 18

In [32]: len(df.Product_Category_2.unique())
Out[32]: 18

In [33]: len(df.Product_Category_3.unique())
Out[33]: 16

In [34]: df.User_ID.value_counts().sort_values(ascending=False).head(10)
Out[34]:
1001680    1025
1004277     978
1001941     898
1001181     861
1000889     822
1003618     766
1001150     752
1001015     739
1002909     717
1001449     714
Name: User_ID, dtype: int64

In [35]: # 3.9 Make a barplot of frequency of top-10 User_IDs
    ...: #     that occur most frequently on Black Friday
    ...: #     Can you order the graph either in
    ...: #     decreasing/increasing order of frequency

In [36]: frames = df.User_ID.value_counts().sort_values(ascending=False).head(10).reset_index()

In [37]: frames.columns = ["User_ID","Frequency"]

In [38]: sns.barplot(x="User_ID", y="Frequency", data =frames, order=frames.loc[:,"User_ID"])
Out[38]: <matplotlib.axes._subplots.AxesSubplot at 0x22c6f4eb7b8>

In [39]: # Find average purchases ('Purchase') per User_ID
    ...: #    Hint: Use groupby(), sort_values() and head()

In [40]: df.groupby("User_ID").Purchase.mean().sort_values(ascending=False).head(10)
Out[40]:
User_ID
1005069    19278.375000
1003902    18777.247312
1005999    18345.944444
1001349    18162.739130
1000101    17511.369231
1003461    17508.700000
1002983    17349.100000
1005336    17084.961538
1006034    17006.363636
1004968    16889.000000
Name: Purchase, dtype: float64

In [41]: # Plot a barchart of User_IDs average purchases wise

In [42]: frames = df.groupby("User_ID").Purchase.mean().sort_values(ascending=False).head(10).reset_index()

In [43]: sns.barplot(x="User_ID", y="Purchase", data =frames, order=frames.loc[:,"User_ID"])
Out[43]: <matplotlib.axes._subplots.AxesSubplot at 0x22c6f4eb7b8>

In [44]: # Product_ID wise average 'Purchase'?

In [45]: df.groupby("Product_ID").Purchase.mean().sort_values(ascending=False).head(10)
Out[45]:
Product_ID
P00086242    21297.865672
P00085342    20993.804428
P00200642    20479.229885
P00116142    20478.264753
P00119342    20454.296053
P00117642    20453.368557
P00074542    20323.000000
P00341542    20291.000000
P00052842    20136.811983
P00087042    20079.646809
Name: Purchase, dtype: float64

In [46]: # Plot top-10 Product_IDs most purchased on an average

In [47]: frames = df.groupby("Product_ID").Purchase.mean().sort_values(ascending=False).head(10).reset_index()

In [48]: sns.barplot(x="Product_ID", y="Purchase", data =frames, order=frames.loc[:,"Product_ID"])
Out[48]: <matplotlib.axes._subplots.AxesSubplot at 0x22c6f4eb7b8>

In [49]: # Product_Category_1 wise mean 'Purchase'?

In [50]: df.groupby("Product_Category_1").Purchase.mean().sort_values(ascending=False).head(10)
Out[50]:
Product_Category_1
10    19679.974364
7     16373.830153
6     15837.893573
9     15538.297030
15    14776.422215
16    14764.157471
1     13607.701495
14    13145.452000
2     11255.680752
17    10156.440917
Name: Purchase, dtype: float64

In [51]: # Plot top-10 Product_Category_1 most purchased on an average

In [52]: frames = df.groupby("Product_Category_1").Purchase.mean().sort_values(ascending=False).head(10)

In [53]: sns.barplot(x="Product_Category_1", y="Purchase", data =frames, order=frames.loc[:,"Product_Category_1"])
---------------------------------------------------------------------------
IndexingError                             Traceback (most recent call last)
<ipython-input-53-a40f35fef3dc> in <module>
----> 1 sns.barplot(x="Product_Category_1", y="Purchase", data =frames, order=frames.loc[:,"Product_Category_1"])

~\AppData\Local\Continuum\anaconda3\lib\site-packages\pandas\core\indexing.py in __getitem__(self, key)
   1470             except (KeyError, IndexError):
   1471                 pass
-> 1472             return self._getitem_tuple(key)
   1473         else:
   1474             # we by definition only have the 0th axis

~\AppData\Local\Continuum\anaconda3\lib\site-packages\pandas\core\indexing.py in _getitem_tuple(self, tup)
    873
    874         # no multi-index, so validate all of the indexers
--> 875         self._has_valid_tuple(tup)
    876
    877         # ugly hack for GH #836

~\AppData\Local\Continuum\anaconda3\lib\site-packages\pandas\core\indexing.py in _has_valid_tuple(self, key)
    218         for i, k in enumerate(key):
    219             if i >= self.obj.ndim:
--> 220                 raise IndexingError('Too many indexers')
    221             try:
    222                 self._validate_key(k, i)

IndexingError: Too many indexers

In [54]: df1 = df.groupby('Product_Category_1').apply(lambda x: pd.Series(dict(AvgPurchase = x.Purchase.mean()))).reset_index().sort_values(ascending=False,
    ...:  by='AvgPurchase').head(10)

In [55]: df1.plot('Product_Category_1','AvgPurchase', kind='bar')
Out[55]: <matplotlib.axes._subplots.AxesSubplot at 0x22c736c64a8>

In [56]: # Product_Category_2 wise mean 'Purchase'?

In [57]: df.groupby('Product_Category_2').apply(lambda x: pd.Series(dict(AvgPurchase = x.Purchase.mean()))).reset_index()
Out[57]:
    Product_Category_2   AvgPurchase
0                  2.0  13621.740682
1                  3.0  11229.532628
2                  4.0  10218.319009
3                  5.0   9034.054649
4                  6.0  11500.585872
5                  7.0   6877.234146
6                  8.0  10278.036363
7                  9.0   7282.593633
8                 10.0  15656.014711
9                 11.0   8935.682467
10                12.0   6968.662299
11                13.0   9672.264346
12                14.0   7106.356752
13                15.0  10358.723290
14                16.0  10298.676025
15                17.0   9416.534196
16                18.0   9370.698168

In [58]: #Plot top-10 Product_Category_2 most purchased on an average

In [59]: df.groupby('Product_Category_2').apply(lambda x: pd.Series(dict(AvgPurchase = x.Purchase.mean()))).reset_index().sort_values(ascending=False, by='A
    ...: vgPurchase').head(10)
Out[59]:
    Product_Category_2   AvgPurchase
8                 10.0  15656.014711
0                  2.0  13621.740682
4                  6.0  11500.585872
1                  3.0  11229.532628
13                15.0  10358.723290
14                16.0  10298.676025
6                  8.0  10278.036363
2                  4.0  10218.319009
11                13.0   9672.264346
15                17.0   9416.534196

In [60]: df1.plot('Product_Category_2','AvgPurchase', kind='bar')
---------------------------------------------------------------------------
KeyError                                  Traceback (most recent call last)
~\AppData\Local\Continuum\anaconda3\lib\site-packages\pandas\core\indexes\base.py in get_loc(self, key, method, tolerance)
   3077             try:
-> 3078                 return self._engine.get_loc(key)
   3079             except KeyError:

pandas\_libs\index.pyx in pandas._libs.index.IndexEngine.get_loc()

pandas\_libs\index.pyx in pandas._libs.index.IndexEngine.get_loc()

pandas\_libs\hashtable_class_helper.pxi in pandas._libs.hashtable.PyObjectHashTable.get_item()

pandas\_libs\hashtable_class_helper.pxi in pandas._libs.hashtable.PyObjectHashTable.get_item()

KeyError: 'Product_Category_2'

During handling of the above exception, another exception occurred:

KeyError                                  Traceback (most recent call last)
<ipython-input-60-f8481f187515> in <module>
----> 1 df1.plot('Product_Category_2','AvgPurchase', kind='bar')

~\AppData\Local\Continuum\anaconda3\lib\site-packages\pandas\plotting\_core.py in __call__(self, x, y, kind, ax, subplots, sharex, sharey, layout, figsize, use_index, title, grid, legend, style, logx, logy, loglog, xticks, yticks, xlim, ylim, rot, fontsize, colormap, table, yerr, xerr, secondary_y, sort_columns, **kwds)
   2939                           fontsize=fontsize, colormap=colormap, table=table,
   2940                           yerr=yerr, xerr=xerr, secondary_y=secondary_y,
-> 2941                           sort_columns=sort_columns, **kwds)
   2942     __call__.__doc__ = plot_frame.__doc__
   2943

~\AppData\Local\Continuum\anaconda3\lib\site-packages\pandas\plotting\_core.py in plot_frame(data, x, y, kind, ax, subplots, sharex, sharey, layout, figsize, use_index, title, grid, legend, style, logx, logy, loglog, xticks, yticks, xlim, ylim, rot, fontsize, colormap, table, yerr, xerr, secondary_y, sort_columns, **kwds)
   1975                  yerr=yerr, xerr=xerr,
   1976                  secondary_y=secondary_y, sort_columns=sort_columns,
-> 1977                  **kwds)
   1978
   1979

~\AppData\Local\Continuum\anaconda3\lib\site-packages\pandas\plotting\_core.py in _plot(data, x, y, subplots, ax, kind, **kwds)
   1764                 if is_integer(x) and not data.columns.holds_integer():
   1765                     x = data_cols[x]
-> 1766                 elif not isinstance(data[x], ABCSeries):
   1767                     raise ValueError("x must be a label or position")
   1768                 data = data.set_index(x)

~\AppData\Local\Continuum\anaconda3\lib\site-packages\pandas\core\frame.py in __getitem__(self, key)
   2686             return self._getitem_multilevel(key)
   2687         else:
-> 2688             return self._getitem_column(key)
   2689
   2690     def _getitem_column(self, key):

~\AppData\Local\Continuum\anaconda3\lib\site-packages\pandas\core\frame.py in _getitem_column(self, key)
   2693         # get column
   2694         if self.columns.is_unique:
-> 2695             return self._get_item_cache(key)
   2696
   2697         # duplicate columns & possible reduce dimensionality

~\AppData\Local\Continuum\anaconda3\lib\site-packages\pandas\core\generic.py in _get_item_cache(self, item)
   2487         res = cache.get(item)
   2488         if res is None:
-> 2489             values = self._data.get(item)
   2490             res = self._box_item_values(item, values)
   2491             cache[item] = res

~\AppData\Local\Continuum\anaconda3\lib\site-packages\pandas\core\internals.py in get(self, item, fastpath)
   4113
   4114             if not isna(item):
-> 4115                 loc = self.items.get_loc(item)
   4116             else:
   4117                 indexer = np.arange(len(self.items))[isna(self.items)]

~\AppData\Local\Continuum\anaconda3\lib\site-packages\pandas\core\indexes\base.py in get_loc(self, key, method, tolerance)
   3078                 return self._engine.get_loc(key)
   3079             except KeyError:
-> 3080                 return self._engine.get_loc(self._maybe_cast_indexer(key))
   3081
   3082         indexer = self.get_indexer([key], method=method, tolerance=tolerance)

pandas\_libs\index.pyx in pandas._libs.index.IndexEngine.get_loc()

pandas\_libs\index.pyx in pandas._libs.index.IndexEngine.get_loc()

pandas\_libs\hashtable_class_helper.pxi in pandas._libs.hashtable.PyObjectHashTable.get_item()

pandas\_libs\hashtable_class_helper.pxi in pandas._libs.hashtable.PyObjectHashTable.get_item()

KeyError: 'Product_Category_2'

In [61]: frames = df.groupby("Product_Category_2").Purchase.mean().sort_values(ascending=False).head(10).reset_index()

In [62]: sns.barplot(x="Product_Category_2", y="Purchase", data =frames, order=frames.loc[:,"Product_Category_2"])
Out[62]: <matplotlib.axes._subplots.AxesSubplot at 0x22c736c64a8>

In [63]: df.groupby("Product_Category_3").Purchase.mean().sort_values(ascending=False).head(10)
Out[63]:
Product_Category_3
3.0     13957.166667
10.0    13522.985866
6.0     13189.812785
13.0    13183.002228
8.0     13029.554102
15.0    12338.232770
5.0     12128.351770
11.0    12112.626622
16.0    11982.500093
17.0    11779.470059
Name: Purchase, dtype: float64

In [64]: # Plot top-10 Product_Category_3s most purchased on an average

In [65]: frames = df.groupby("Product_Category_3").Purchase.mean().sort_values(ascending=False).head(10).reset_index()

In [66]: sns.barplot(x="Product_Category_3", y="Purchase", data =frames, order=frames.loc[:,"Product_Category_3"])
Out[66]: <matplotlib.axes._subplots.AxesSubplot at 0x22c736c64a8>

In [67]: # Which Product_Category_1 is more popular in which City_Category?

In [68]: df.groupby(["City_Category","Product_Category_1"]).apply(lambda x: pd.Series(dict(Popular=x.shape[0]))).sort_values("Popular",ascending=False).rese
    ...: t_index().drop
    ...: _duplicates("City_Category")
---------------------------------------------------------------------------
NameError                                 Traceback (most recent call last)
<ipython-input-68-78436067f471> in <module>
      1 df.groupby(["City_Category","Product_Category_1"]).apply(lambda x: pd.Series(dict(Popular=x.shape[0]))).sort_values("Popular",ascending=False).reset_index().drop
----> 2 _duplicates("City_Category")

NameError: name '_duplicates' is not defined

In [69]: df.groupby(["City_Category","Product_Category_1"]).apply(lambda x: pd.Series(dict(Popular=x.shape[0]))).sort_values("Popular",ascending=False).rese
    ...: t_index().drop_duplicates("City_Category")
Out[69]:
  City_Category  Product_Category_1  Popular
0             B                   5    63162
3             C                   1    46383
5             A                   5    41491

In [70]: #Get City_Category wise average 'Purchase'

In [71]: df.groupby("City_Category").Purchase.mean().sort_values(ascending=False).head(10)
Out[71]:
City_Category
C    9844.441855
B    9198.657848
A    8958.011014
Name: Purchase, dtype: float64

In [72]: # Get Age wise average 'Purchase'?

In [73]: df.groupby("Age").Purchase.mean().sort_values(ascending=Fals).head(10)
---------------------------------------------------------------------------
NameError                                 Traceback (most recent call last)
<ipython-input-73-cdc258572249> in <module>
----> 1 df.groupby("Age").Purchase.mean().sort_values(ascending=Fals).head(10)

NameError: name 'Fals' is not defined

In [74]: df.groupby("Age").Purchase.mean().sort_values().head(10)
Out[74]:
Age
0-17     9020.126878
18-25    9235.197575
46-50    9284.872277
26-35    9314.588970
36-45    9401.478758
55+      9453.898579
51-55    9620.616620
Name: Purchase, dtype: float64

In [75]: df.groupby("Age").Purchase.mean().sort_values(ascending=False).head(10)
Out[75]:
Age
51-55    9620.616620
55+      9453.898579
36-45    9401.478758
26-35    9314.588970
46-50    9284.872277
18-25    9235.197575
0-17     9020.126878
Name: Purchase, dtype: float64

In [76]: # Get City_Category wise and Age wise average 'Purchase'

In [77]: df.groupby(["City_Category","Age"]).Purchase.mean().sort_values(ascending=False).head(10)
Out[77]:
City_Category  Age
C              36-45    10008.983828
               26-35     9952.538704
               51-55     9917.586464
B              55+       9886.257757
C              18-25     9819.690145
               46-50     9661.676321
A              51-55     9575.454012
C              55+       9522.626968
B              51-55     9393.971724
               46-50     9297.089648
Name: Purchase, dtype: float64

In [78]: # Is there any relationship between City_Category and Age?

In [79]: #     Ref: https://machinelearningmastery.com/chi-squared-test-for-machine-learning/
    ...:
    ...: from scipy.stats import chi2_contingency

In [80]: #
    ...:  How confident would you want to be about the existence of any relationship?
    ...: #      95% or 90% or 99%......
  File "<ipython-input-80-ff42f1b111ce>", line 2
    get_ipython().run_line_magic('pinfo', 'relationship')
    ^
IndentationError: unexpected indent


In [81]: #  How confident would you want to be about the existence of any relationship?
    ...: #      95% or 90% or 99%......

In [82]: confidence_level = 0.95         # 95% confident

In [83]: level_of_significance = 1- confidence_level

In [84]: # Create a cross-table between two categorical variables

In [85]: table = pd.crosstab(df.City_Category,df.Age)

In [86]: table
Out[86]:
Age            0-17  18-25  26-35  36-45  46-50  51-55    55+
City_Category
A              2497  27025  72048  26142   7467   5969   3490
B              5288  42470  89767  46605  19900  17435   5028
C              6922  28139  52875  34752  17159  14214  12385

In [87]: # Apply chi-square test of independence and get p_value

In [88]: _, p_value, _, _ = chi2_contingency(table)

In [89]: # Now examine p_value

In [90]: if p_value <= level_of_significance:
    ...: ^Iprint("Categorical variables have relationships")
    ...: else:
    ...: ^Iprint("Categorical variables have no relationships")
    ...:
Categorical variables have relationships

In [91]: # Similarly examine if there is any relationship between Age and Occupation?

In [92]: df2 = pd.crosstab(df['Age'], df['Occupation'])

In [93]: chi2, p, dof, expec = chi2_contingency(df2)

In [94]: # And also examine if there is any Gender  and Marital_Status?

In [95]: df2 = pd.crosstab(df['Gender'], df['Marital_Status'])

In [96]: chi2, p, dof, expec = chi2_contingency(df2)

In [97]: table
Out[97]:
Age            0-17  18-25  26-35  36-45  46-50  51-55    55+
City_Category
A              2497  27025  72048  26142   7467   5969   3490
B              5288  42470  89767  46605  19900  17435   5028
C              6922  28139  52875  34752  17159  14214  12385

In [98]: