# awk_dataframe

This library is intended to use for fast and low RAM memory consumption of very large .csv files. It works by accumulating a sequence of awk commands that will be executed through pipes in bash when the actual values of the dataframe are to be consumed.

## First things first

This is an wrapper around AWK for its use as a dataframe implementation, therefore, it won't work unless you are using a Linux distribution that can run BASH and GAWK. It could work on a macOS but I haven't tested it. I am personally running Ubuntu 22.04. It also compiles two C++ files (to read and save) and needs g++ in the system in order to compile them.

It will also not work if your regional settings use the comma as the decimal separator. One way to change this is to set the regional settings to the UK as follows:

```
sudo update-locale LC_NUMERIC="en_GB.UTF-8"
```

and then logout of your system.

## Disk usage

Not only this library runs directly from the hard drive trying to avoid RAM limitations which will degrade your hard drive.
It also stores temporary files into the ```~/.tmp``` folder. Altough they should be deleted automatically, please check from time to time, since there might be some bug that leaves files behind. Also, although it will be automatically created, make sure that it already exists in your disk, in order to avoid failures at creation time due to permissions.

Most commands do not take time, but be advised that ```df.shape()```, ```print(df)```, ```df.head()```, ```df.values()```, ```df.to_pandas()```, ```df.to_npd()``` and ```df.to_csv(path)``` will run the full set of commands and might take time, avoid using them as much as possible. The best implementation would be to generate all conditions for subsetting and then either going to a pandas/numpy_dataframe object if you want to further manipulate in RAM or using ```df.to_csv(path)``` to save the results to the hard drive.

## Authors and acknowledgment
Idea and implementation by Carlos Molinero.

## License
MIT license.


## Project status
Currently this is an early implementation, meaning that it is in a very unstable state, and the syntax might change and bugs may arise. I do not recommend installing it, I am publishing it for my personal use.

---
# Usage:
In the following lines I paste examples of the main commands, as some sort of documentation until a more complete documentation is available.

# INIT


```python
import os
import sys
import numpy as np
import numpy_dataframe as npd
import pandas as pd
import awk_dataframe as ad
import importlib
import time
import random
import string
```

# Functions


```python
def get_random_string(length):
    # thanks to https://pynative.com/python-generate-random-string/
    # choose from all lowercase letter
    letters = string.ascii_lowercase
    result_str = ''.join(random.choice(letters) for i in range(length))
    return result_str
```

## create test csv


```python
n = 20
names = np.array([get_random_string(5) for x in range(5)])

t = npd.DataFrame()
t.values = np.random.rand(n)
t.some_ints = np.floor(np.random.rand(n)*50).astype(int)
t.name = names[np.random.choice(range(5),n)]

path = os.path.expanduser("~") + "/.tmp/example.csv"
t.to_csv(path)
```

# Gawk dataframe

## contruct object / read csv


```python
path = os.path.expanduser("~") + "/.tmp/example.csv"
df = ad.read_csv(path)
```

or


```python
path = os.path.expanduser("~") + "/.tmp/example.csv"
df = ad.DataFrame()
df.read_csv(path)
```

## select rows/columns


```python
df[0:10,:]
```




    values,some_ints,name
    0.8633713864104114,21,mlyas
    0.7797461486214806,32,efcsm
    0.9415640935512127,24,tcbtr
    0.7678670658611503,44,efcsm
    0.8223095493965592,2,bgmqd
    0.06832888693954564,31,bgmqd
    0.717887788740719,44,mlyas
    0.6559538612897098,49,efcsm
    0.08927654448880817,44,tcbtr
    0.7338088959472877,36,tcbtr




```python
df.some_ints
```




    some_ints
    21
    32
    24
    44
    2
    31
    44
    49
    44
    36
    9
    11
    12
    31
    7
    40
    26
    38
    35
    26




```python
df["some_ints"]
```




    some_ints
    21
    32
    24
    44
    2
    31
    44
    49
    44
    36
    9
    11
    12
    31
    7
    40
    26
    38
    35
    26




```python
df[:,"some_ints"]
```




    some_ints
    21
    32
    24
    44
    2
    31
    44
    49
    44
    36
    9
    11
    12
    31
    7
    40
    26
    38
    35
    26




```python
df[:,["some_ints","name"]]
```




    some_ints,name
    21,mlyas
    32,efcsm
    24,tcbtr
    44,efcsm
    2,bgmqd
    31,bgmqd
    44,mlyas
    49,efcsm
    44,tcbtr
    36,tcbtr
    9,mlyas
    11,lmqgd
    12,bgmqd
    31,mlyas
    7,efcsm
    40,tcbtr
    26,mlyas
    38,efcsm
    35,mlyas
    26,mlyas




```python
df[:,1:2]
```




    some_ints
    21
    32
    24
    44
    2
    31
    44
    49
    44
    36
    9
    11
    12
    31
    7
    40
    26
    38
    35
    26




```python
df[:,1:]
```




    some_ints,name
    21,mlyas
    32,efcsm
    24,tcbtr
    44,efcsm
    2,bgmqd
    31,bgmqd
    44,mlyas
    49,efcsm
    44,tcbtr
    36,tcbtr
    9,mlyas
    11,lmqgd
    12,bgmqd
    31,mlyas
    7,efcsm
    40,tcbtr
    26,mlyas
    38,efcsm
    35,mlyas
    26,mlyas




```python
df[:10,:]
```




    values,some_ints,name
    0.8633713864104114,21,mlyas
    0.7797461486214806,32,efcsm
    0.9415640935512127,24,tcbtr
    0.7678670658611503,44,efcsm
    0.8223095493965592,2,bgmqd
    0.06832888693954564,31,bgmqd
    0.717887788740719,44,mlyas
    0.6559538612897098,49,efcsm
    0.08927654448880817,44,tcbtr
    0.7338088959472877,36,tcbtr




```python
df[3,2]
```




    name
    efcsm




```python
df[3,:]
```




    values,some_ints,name
    0.7678670658611503,44,efcsm




```python
df[:,1]
```




    some_ints
    21
    32
    24
    44
    2
    31
    44
    49
    44
    36
    9
    11
    12
    31
    7
    40
    26
    38
    35
    26




```python
df[[0,3],1]
```




    some_ints
    21
    44




```python
df[:,[0,1]]
```




    values,some_ints
    0.8633713864104114,21
    0.7797461486214806,32
    0.9415640935512127,24
    0.7678670658611503,44
    0.8223095493965592,2
    0.06832888693954564,31
    0.717887788740719,44
    0.6559538612897098,49
    0.08927654448880817,44
    0.7338088959472877,36
    0.701592457357365,9
    0.04338298448626843,11
    0.3297427254572507,12
    0.1011755876260031,31
    0.8235585667750851,7
    0.5829664850991141,40
    0.14016453615592928,26
    0.43436632265162967,38
    0.4097725083991255,35
    0.6379834519420476,26




```python
df[range(5),:]
```




    values,some_ints,name
    0.8633713864104114,21,mlyas
    0.7797461486214806,32,efcsm
    0.9415640935512127,24,tcbtr
    0.7678670658611503,44,efcsm
    0.8223095493965592,2,bgmqd




```python
df.get_rows(range(10))
```




    values,some_ints,name
    0.8633713864104114,21,mlyas
    0.7797461486214806,32,efcsm
    0.9415640935512127,24,tcbtr
    0.7678670658611503,44,efcsm
    0.8223095493965592,2,bgmqd
    0.06832888693954564,31,bgmqd
    0.717887788740719,44,mlyas
    0.6559538612897098,49,efcsm
    0.08927654448880817,44,tcbtr
    0.7338088959472877,36,tcbtr




```python
df.get_cols(range(2))
```




    values,some_ints
    0.8633713864104114,21
    0.7797461486214806,32
    0.9415640935512127,24
    0.7678670658611503,44
    0.8223095493965592,2
    0.06832888693954564,31
    0.717887788740719,44
    0.6559538612897098,49
    0.08927654448880817,44
    0.7338088959472877,36
    0.701592457357365,9
    0.04338298448626843,11
    0.3297427254572507,12
    0.1011755876260031,31
    0.8235585667750851,7
    0.5829664850991141,40
    0.14016453615592928,26
    0.43436632265162967,38
    0.4097725083991255,35
    0.6379834519420476,26



## names, shape, head


```python
df.names()
```




    array(['values', 'some_ints', 'name'], dtype='<U9')




```python
df.shape()
```




    array([20,  3])




```python
df.head()
```




    values,some_ints,name
    0.8633713864104114,21,mlyas
    0.7797461486214806,32,efcsm
    0.9415640935512127,24,tcbtr
    0.7678670658611503,44,efcsm
    0.8223095493965592,2,bgmqd
    0.06832888693954564,31,bgmqd
    0.717887788740719,44,mlyas
    0.6559538612897098,49,efcsm
    0.08927654448880817,44,tcbtr
    0.7338088959472877,36,tcbtr
    0.701592457357365,9,mlyas
    0.04338298448626843,11,lmqgd




```python
df.head(5)
```




    values,some_ints,name
    0.8633713864104114,21,mlyas
    0.7797461486214806,32,efcsm
    0.9415640935512127,24,tcbtr
    0.7678670658611503,44,efcsm
    0.8223095493965592,2,bgmqd
    0.06832888693954564,31,bgmqd
    0.717887788740719,44,mlyas



## where


```python
df.where("values < 0.8 && values > .6")
```

    gawk: warning: escape sequence `\/' treated as plain `/'





    values,some_ints,name
    0.7797461486,32,efcsm
    0.7678670659,44,efcsm
    0.7178877887,44,mlyas
    0.6559538613,49,efcsm
    0.7338088959,36,tcbtr
    0.7015924574,9,mlyas
    0.6379834519,26,mlyas




```python
df.where("""  name == "mlyas"  """)
```

    gawk: warning: escape sequence `\/' treated as plain `/'





    values,some_ints,name
    0.8633713864104114,21,mlyas
    0.717887788740719,44,mlyas
    0.701592457357365,9,mlyas
    0.1011755876260031,31,mlyas
    0.14016453615592928,26,mlyas
    0.4097725083991255,35,mlyas
    0.6379834519420476,26,mlyas




```python
df.where("""  name in ["efcsm","tcbtr"]  """)
```

    gawk: warning: escape sequence `\/' treated as plain `/'





    values,some_ints,name
    0.7797461486214806,32,efcsm
    0.9415640935512127,24,tcbtr
    0.7678670658611503,44,efcsm
    0.6559538612897098,49,efcsm
    0.08927654448880817,44,tcbtr
    0.7338088959472877,36,tcbtr
    0.8235585667750851,7,efcsm
    0.5829664850991141,40,tcbtr
    0.43436632265162967,38,efcsm



## unique


```python
df.unique("name")
```




    name
    lmqgd
    efcsm
    mlyas
    bgmqd
    tcbtr



## add column


```python
df_with_new_column = df.add_column("new_column")
df_with_new_column
```




    values,some_ints,name,new_column
    0.8633713864104114,21,mlyas,
    0.7797461486214806,32,efcsm,
    0.9415640935512127,24,tcbtr,
    0.7678670658611503,44,efcsm,
    0.8223095493965592,2,bgmqd,
    0.06832888693954564,31,bgmqd,
    0.717887788740719,44,mlyas,
    0.6559538612897098,49,efcsm,
    0.08927654448880817,44,tcbtr,
    0.7338088959472877,36,tcbtr,
    0.701592457357365,9,mlyas,
    0.04338298448626843,11,lmqgd,
    0.3297427254572507,12,bgmqd,
    0.1011755876260031,31,mlyas,
    0.8235585667750851,7,efcsm,
    0.5829664850991141,40,tcbtr,
    0.14016453615592928,26,mlyas,
    0.43436632265162967,38,efcsm,
    0.4097725083991255,35,mlyas,
    0.6379834519420476,26,mlyas,



# modify


```python
df.modify("values = values + some_ints * 3")
```

    gawk: warning: escape sequence `\/' treated as plain `/'
    gawk: warning: escape sequence `\/' treated as plain `/'





    values,some_ints,name
    63.86337139,21,mlyas
    96.77974615,32,efcsm
    72.94156409,24,tcbtr
    132.7678671,44,efcsm
    6.822309549,2,bgmqd
    93.06832889,31,bgmqd
    132.7178878,44,mlyas
    147.6559539,49,efcsm
    132.0892765,44,tcbtr
    108.7338089,36,tcbtr
    27.70159246,9,mlyas
    33.04338298,11,lmqgd
    36.32974273,12,bgmqd
    93.10117559,31,mlyas
    21.82355857,7,efcsm
    120.5829665,40,tcbtr
    78.14016454,26,mlyas
    114.4343663,38,efcsm
    105.4097725,35,mlyas
    78.63798345,26,mlyas



The previous operation does not modify the values in df


```python
df
```




    values,some_ints,name
    0.8633713864104114,21,mlyas
    0.7797461486214806,32,efcsm
    0.9415640935512127,24,tcbtr
    0.7678670658611503,44,efcsm
    0.8223095493965592,2,bgmqd
    0.06832888693954564,31,bgmqd
    0.717887788740719,44,mlyas
    0.6559538612897098,49,efcsm
    0.08927654448880817,44,tcbtr
    0.7338088959472877,36,tcbtr
    0.701592457357365,9,mlyas
    0.04338298448626843,11,lmqgd
    0.3297427254572507,12,bgmqd
    0.1011755876260031,31,mlyas
    0.8235585667750851,7,efcsm
    0.5829664850991141,40,tcbtr
    0.14016453615592928,26,mlyas
    0.43436632265162967,38,efcsm
    0.4097725083991255,35,mlyas
    0.6379834519420476,26,mlyas



You need to assign it in order for the modifications to be "saved"


```python
df_mod = df.modify("values = values + some_ints * 3")
df_mod
```

    gawk: warning: escape sequence `\/' treated as plain `/'
    gawk: warning: escape sequence `\/' treated as plain `/'





    values,some_ints,name
    63.86337139,21,mlyas
    96.77974615,32,efcsm
    72.94156409,24,tcbtr
    132.7678671,44,efcsm
    6.822309549,2,bgmqd
    93.06832889,31,bgmqd
    132.7178878,44,mlyas
    147.6559539,49,efcsm
    132.0892765,44,tcbtr
    108.7338089,36,tcbtr
    27.70159246,9,mlyas
    33.04338298,11,lmqgd
    36.32974273,12,bgmqd
    93.10117559,31,mlyas
    21.82355857,7,efcsm
    120.5829665,40,tcbtr
    78.14016454,26,mlyas
    114.4343663,38,efcsm
    105.4097725,35,mlyas
    78.63798345,26,mlyas



Modify accepts conditional equations, and its results are 1 for true and 0 for false, which allows to construct functions such as sign() or abs(), etc as an example:


```python
df_mod = df_with_new_column.modify("new_column = values - .5")
df_mod
```

    gawk: warning: escape sequence `\/' treated as plain `/'
    gawk: warning: escape sequence `\/' treated as plain `/'





    values,some_ints,name,new_column
    0.8633713864104114,21,mlyas,0.3633713864
    0.7797461486214806,32,efcsm,0.2797461486
    0.9415640935512127,24,tcbtr,0.4415640936
    0.7678670658611503,44,efcsm,0.2678670659
    0.8223095493965592,2,bgmqd,0.3223095494
    0.06832888693954564,31,bgmqd,-0.4316711131
    0.717887788740719,44,mlyas,0.2178877887
    0.6559538612897098,49,efcsm,0.1559538613
    0.08927654448880817,44,tcbtr,-0.4107234555
    0.7338088959472877,36,tcbtr,0.2338088959
    0.701592457357365,9,mlyas,0.2015924574
    0.04338298448626843,11,lmqgd,-0.4566170155
    0.3297427254572507,12,bgmqd,-0.1702572745
    0.1011755876260031,31,mlyas,-0.3988244124
    0.8235585667750851,7,efcsm,0.3235585668
    0.5829664850991141,40,tcbtr,0.0829664851
    0.14016453615592928,26,mlyas,-0.3598354638
    0.43436632265162967,38,efcsm,-0.06563367735
    0.4097725083991255,35,mlyas,-0.0902274916
    0.6379834519420476,26,mlyas,0.1379834519



now, let's get the absolute value of new column and put it in a new column


```python
df_mod_2 = df_mod.add_column("abs_new_column").modify("abs_new_column = new_column * ((new_column >= 0) * 2 - 1)")
df_mod_2
```

    gawk: warning: escape sequence `\/' treated as plain `/'
    gawk: warning: escape sequence `\/' treated as plain `/'





    values,some_ints,name,new_column,abs_new_column
    0.8633713864104114,21,mlyas,0.3633713864,0.3633713864
    0.7797461486214806,32,efcsm,0.2797461486,0.2797461486
    0.9415640935512127,24,tcbtr,0.4415640936,0.4415640936
    0.7678670658611503,44,efcsm,0.2678670659,0.2678670659
    0.8223095493965592,2,bgmqd,0.3223095494,0.3223095494
    0.06832888693954564,31,bgmqd,-0.4316711131,0.4316711131
    0.717887788740719,44,mlyas,0.2178877887,0.2178877887
    0.6559538612897098,49,efcsm,0.1559538613,0.1559538613
    0.08927654448880817,44,tcbtr,-0.4107234555,0.4107234555
    0.7338088959472877,36,tcbtr,0.2338088959,0.2338088959
    0.701592457357365,9,mlyas,0.2015924574,0.2015924574
    0.04338298448626843,11,lmqgd,-0.4566170155,0.4566170155
    0.3297427254572507,12,bgmqd,-0.1702572745,0.1702572745
    0.1011755876260031,31,mlyas,-0.3988244124,0.3988244124
    0.8235585667750851,7,efcsm,0.3235585668,0.3235585668
    0.5829664850991141,40,tcbtr,0.0829664851,0.0829664851
    0.14016453615592928,26,mlyas,-0.3598354638,0.3598354638
    0.43436632265162967,38,efcsm,-0.06563367735,0.06563367735
    0.4097725083991255,35,mlyas,-0.0902274916,0.0902274916
    0.6379834519420476,26,mlyas,0.1379834519,0.1379834519



Modify accepts conditions, there are two ways:


```python
df_mod_2.modify("values = 0",condition = "new_column < 0")
```

    gawk: warning: escape sequence `\/' treated as plain `/'
    gawk: warning: escape sequence `\/' treated as plain `/'





    values,some_ints,name,new_column,abs_new_column
    0.8633713864104114,21,mlyas,0.3633713864,0.3633713864
    0.7797461486214806,32,efcsm,0.2797461486,0.2797461486
    0.9415640935512127,24,tcbtr,0.4415640936,0.4415640936
    0.7678670658611503,44,efcsm,0.2678670659,0.2678670659
    0.8223095493965592,2,bgmqd,0.3223095494,0.3223095494
    0,31,bgmqd,-0.4316711131,0.4316711131
    0.717887788740719,44,mlyas,0.2178877887,0.2178877887
    0.6559538612897098,49,efcsm,0.1559538613,0.1559538613
    0,44,tcbtr,-0.4107234555,0.4107234555
    0.7338088959472877,36,tcbtr,0.2338088959,0.2338088959
    0.701592457357365,9,mlyas,0.2015924574,0.2015924574
    0,11,lmqgd,-0.4566170155,0.4566170155
    0,12,bgmqd,-0.1702572745,0.1702572745
    0,31,mlyas,-0.3988244124,0.3988244124
    0.8235585667750851,7,efcsm,0.3235585668,0.3235585668
    0.5829664850991141,40,tcbtr,0.0829664851,0.0829664851
    0,26,mlyas,-0.3598354638,0.3598354638
    0,38,efcsm,-0.06563367735,0.06563367735
    0,35,mlyas,-0.0902274916,0.0902274916
    0.6379834519420476,26,mlyas,0.1379834519,0.1379834519




```python
conditional_equation = ad.Conditional_equation()
conditional_equation.condition = "new_column < 0"
conditional_equation.equation = "values = 0"
df_mod_2.modify(conditional_equation)
```

    gawk: warning: escape sequence `\/' treated as plain `/'
    gawk: warning: escape sequence `\/' treated as plain `/'





    values,some_ints,name,new_column,abs_new_column
    0.8633713864104114,21,mlyas,0.3633713864,0.3633713864
    0.7797461486214806,32,efcsm,0.2797461486,0.2797461486
    0.9415640935512127,24,tcbtr,0.4415640936,0.4415640936
    0.7678670658611503,44,efcsm,0.2678670659,0.2678670659
    0.8223095493965592,2,bgmqd,0.3223095494,0.3223095494
    0,31,bgmqd,-0.4316711131,0.4316711131
    0.717887788740719,44,mlyas,0.2178877887,0.2178877887
    0.6559538612897098,49,efcsm,0.1559538613,0.1559538613
    0,44,tcbtr,-0.4107234555,0.4107234555
    0.7338088959472877,36,tcbtr,0.2338088959,0.2338088959
    0.701592457357365,9,mlyas,0.2015924574,0.2015924574
    0,11,lmqgd,-0.4566170155,0.4566170155
    0,12,bgmqd,-0.1702572745,0.1702572745
    0,31,mlyas,-0.3988244124,0.3988244124
    0.8235585667750851,7,efcsm,0.3235585668,0.3235585668
    0.5829664850991141,40,tcbtr,0.0829664851,0.0829664851
    0,26,mlyas,-0.3598354638,0.3598354638
    0,38,efcsm,-0.06563367735,0.06563367735
    0,35,mlyas,-0.0902274916,0.0902274916
    0.6379834519420476,26,mlyas,0.1379834519,0.1379834519



A future update of the library will allow to include several conditional equations in the same modify statement

# add_index


```python
df_mod = df.add_index()
df_mod
```




    index,values,some_ints,name
    0,0.8633713864104114,21,mlyas
    1,0.7797461486214806,32,efcsm
    2,0.9415640935512127,24,tcbtr
    3,0.7678670658611503,44,efcsm
    4,0.8223095493965592,2,bgmqd
    5,0.06832888693954564,31,bgmqd
    6,0.717887788740719,44,mlyas
    7,0.6559538612897098,49,efcsm
    8,0.08927654448880817,44,tcbtr
    9,0.7338088959472877,36,tcbtr
    10,0.701592457357365,9,mlyas
    11,0.04338298448626843,11,lmqgd
    12,0.3297427254572507,12,bgmqd
    13,0.1011755876260031,31,mlyas
    14,0.8235585667750851,7,efcsm
    15,0.5829664850991141,40,tcbtr
    16,0.14016453615592928,26,mlyas
    17,0.43436632265162967,38,efcsm
    18,0.4097725083991255,35,mlyas
    19,0.6379834519420476,26,mlyas



## sort_by


```python
df_mod.sort_by("values")
```




    index,values,some_ints,name
    11,0.04338298448626843,11,lmqgd
    5,0.06832888693954564,31,bgmqd
    8,0.08927654448880817,44,tcbtr
    13,0.1011755876260031,31,mlyas
    16,0.14016453615592928,26,mlyas
    12,0.3297427254572507,12,bgmqd
    18,0.4097725083991255,35,mlyas
    17,0.43436632265162967,38,efcsm
    15,0.5829664850991141,40,tcbtr
    19,0.6379834519420476,26,mlyas
    7,0.6559538612897098,49,efcsm
    10,0.701592457357365,9,mlyas
    6,0.717887788740719,44,mlyas
    9,0.7338088959472877,36,tcbtr
    3,0.7678670658611503,44,efcsm
    1,0.7797461486214806,32,efcsm
    4,0.8223095493965592,2,bgmqd
    14,0.8235585667750851,7,efcsm
    0,0.8633713864104114,21,mlyas
    2,0.9415640935512127,24,tcbtr



## to_pandas


```python
pdf = df_mod.to_pandas()
pdf
```




<div>
<style scoped>
    .dataframe tbody tr th:only-of-type {
        vertical-align: middle;
    }

    .dataframe tbody tr th {
        vertical-align: top;
    }

    .dataframe thead th {
        text-align: right;
    }
</style>
<table border="1" class="dataframe">
  <thead>
    <tr style="text-align: right;">
      <th></th>
      <th>index</th>
      <th>values</th>
      <th>some_ints</th>
      <th>name</th>
    </tr>
  </thead>
  <tbody>
    <tr>
      <th>0</th>
      <td>0</td>
      <td>0.863371</td>
      <td>21</td>
      <td>mlyas</td>
    </tr>
    <tr>
      <th>1</th>
      <td>1</td>
      <td>0.779746</td>
      <td>32</td>
      <td>efcsm</td>
    </tr>
    <tr>
      <th>2</th>
      <td>2</td>
      <td>0.941564</td>
      <td>24</td>
      <td>tcbtr</td>
    </tr>
    <tr>
      <th>3</th>
      <td>3</td>
      <td>0.767867</td>
      <td>44</td>
      <td>efcsm</td>
    </tr>
    <tr>
      <th>4</th>
      <td>4</td>
      <td>0.822310</td>
      <td>2</td>
      <td>bgmqd</td>
    </tr>
    <tr>
      <th>5</th>
      <td>5</td>
      <td>0.068329</td>
      <td>31</td>
      <td>bgmqd</td>
    </tr>
    <tr>
      <th>6</th>
      <td>6</td>
      <td>0.717888</td>
      <td>44</td>
      <td>mlyas</td>
    </tr>
    <tr>
      <th>7</th>
      <td>7</td>
      <td>0.655954</td>
      <td>49</td>
      <td>efcsm</td>
    </tr>
    <tr>
      <th>8</th>
      <td>8</td>
      <td>0.089277</td>
      <td>44</td>
      <td>tcbtr</td>
    </tr>
    <tr>
      <th>9</th>
      <td>9</td>
      <td>0.733809</td>
      <td>36</td>
      <td>tcbtr</td>
    </tr>
    <tr>
      <th>10</th>
      <td>10</td>
      <td>0.701592</td>
      <td>9</td>
      <td>mlyas</td>
    </tr>
    <tr>
      <th>11</th>
      <td>11</td>
      <td>0.043383</td>
      <td>11</td>
      <td>lmqgd</td>
    </tr>
    <tr>
      <th>12</th>
      <td>12</td>
      <td>0.329743</td>
      <td>12</td>
      <td>bgmqd</td>
    </tr>
    <tr>
      <th>13</th>
      <td>13</td>
      <td>0.101176</td>
      <td>31</td>
      <td>mlyas</td>
    </tr>
    <tr>
      <th>14</th>
      <td>14</td>
      <td>0.823559</td>
      <td>7</td>
      <td>efcsm</td>
    </tr>
    <tr>
      <th>15</th>
      <td>15</td>
      <td>0.582966</td>
      <td>40</td>
      <td>tcbtr</td>
    </tr>
    <tr>
      <th>16</th>
      <td>16</td>
      <td>0.140165</td>
      <td>26</td>
      <td>mlyas</td>
    </tr>
    <tr>
      <th>17</th>
      <td>17</td>
      <td>0.434366</td>
      <td>38</td>
      <td>efcsm</td>
    </tr>
    <tr>
      <th>18</th>
      <td>18</td>
      <td>0.409773</td>
      <td>35</td>
      <td>mlyas</td>
    </tr>
    <tr>
      <th>19</th>
      <td>19</td>
      <td>0.637983</td>
      <td>26</td>
      <td>mlyas</td>
    </tr>
  </tbody>
</table>
</div>



## to_numpy_dataframe


```python
ndf = df_mod.to_npd()
print(ndf)
print(ndf.shape)
```

        index    values  some_ints   name
    0       0  0.863371         21  mlyas
    1       1  0.779746         32  efcsm
    2       2  0.941564         24  tcbtr
    3       3  0.767867         44  efcsm
    4       4  0.822310          2  bgmqd
    5       5  0.068329         31  bgmqd
    6       6  0.717888         44  mlyas
    7       7  0.655954         49  efcsm
    8       8  0.089277         44  tcbtr
    9       9  0.733809         36  tcbtr
    10     10  0.701592          9  mlyas
    11     11  0.043383         11  lmqgd
    12     12  0.329743         12  bgmqd
    13     13  0.101176         31  mlyas
    14     14  0.823559          7  efcsm
    15     15  0.582966         40  tcbtr
    16     16  0.140165         26  mlyas
    17     17  0.434366         38  efcsm
    18     18  0.409773         35  mlyas
    19     19  0.637983         26  mlyas
    (20, 4)


## to_csv


```python
path_output = os.path.expanduser("~") + "/.tmp/example_mod.csv"
df_mod.to_csv(path_output)
```

# For future development

```
add_rows(n)
keep_na = False
rename

```

# Internal gawk command example (where command):

```

    function is_digit_field(field){
        if (field ~ /^[\\+-]?[0-9]+$|^[\\+-]*[0-9]*[\\.]?[0-9]+$|^[\\+-]*[0-9]*[\\.]?[0-9]+[eE]?[\\+-]?[0-9]+$|#N\/A|#N\/A|N\/A|#NA|-1.#IND|-1.#QNAN|-NaN|-nan|1.#IND|1.#QNAN|<NA>|<na>|NA|NULL|NaN|n\/a|nan|null||Nan|-Nan/){
            return 1
        }else{
            return 0
        }
    }

    function needs_quotes(field){
    #postgres_standard: delimiter character, the QUOTE character, the NULL string, a carriage return, or line feed character, t

        regex = "(" FS ")+|(\\n)+|(" input_quote ")+|\r+"
        if (field ~ regex){
            return 1
        }else{
            return 0
        }
    }

    function transform_field(field,column){
        if (is_first_command && !is_last_command && original_level_simplicity_csv != 2){
            gsub(/\n/,delimiter_internal_notation "n" delimiter_internal_notation,field)
            gsub(FS,delimiter_internal_notation "d" delimiter_internal_notation,field)
            gsub(input_quote, delimiter_internal_notation "q" delimiter_internal_notation, field)
            gsub("\r", delimiter_internal_notation "r" delimiter_internal_notation, field)
        }
        if (is_last_command && !is_first_command  && original_level_simplicity_csv != 2){
            gsub(delimiter_internal_notation "n" delimiter_internal_notation,"\n",field)
            gsub(delimiter_internal_notation "d" delimiter_internal_notation,FS,field)
            gsub(delimiter_internal_notation "q" delimiter_internal_notation,input_quote, field)
            gsub(delimiter_internal_notation "r" delimiter_internal_notation,"\r", field)
        }
        if (is_digit_field(field) || (level_simplicity_csv == 2 && (!is_last_command || original_level_simplicity_csv == 2))){
            if (!is_digit_field()){
                field = transform_string(field,column)
                if (input_quote != output_quote){
                    gsub(input_quote,output_quote,field)
                }
            }else{
                return transform_digit(field,column)
            }
            return field
        }else{
            field = transform_string(field,column)
            if (quotes_have_been_removed){
                if (full_string_quoting){
                    return output_quote field output_quote
                }else{
                    if (needs_quotes(field) && minimal_string_quoting || field == delimiter_internal_notation "NULL" delimiter_internal_notation){
                        if (field == delimiter_internal_notation "NULL" delimiter_internal_notation){
                            gsub(delimiter_internal_notation "NULL" delimiter_internal_notation,"NULL",field)
                        }
                        return output_quote field output_quote
                    }else{
                        return field
                    }
                }
            }else{
                return field
            }
        }

    }



    function print_field(field,column){


        field = transform_field(field,column)

        if (FNR == NR && find_unique){
            unique[field] = 1
        }else{
            if (print_fields){
                output_separator = OFS
                if (i == max_col() && !add_new_column){
                    output_separator = ORS
                }
                if (i == min_col()){
                    if (add_index){
                        if (!save){
                            printf("%s" output_separator,print_line_number() + index_based_on)
                        }else{
                            printf("%s" output_separator,print_line_number() + index_based_on) > path_output
                        }

                    }
                }
                if (!save){
                    printf "%s" output_separator,field
                }else{
                    printf "%s" output_separator,field > path_output
                }

            }
        }
    }


    function print_line(line){
        line = transform_line(line)
        if (print_fields){
            if (add_index){
                if (!save){
                    printf("%s" OFS,print_line_number() + index_based_on)
                }else{
                    printf("%s" OFS,print_line_number() + index_based_on) > path_output
                }

            }
            if (input_quote != output_quote){
                gsub(input_quote,output_quote,line)
            }

            if (!save){
                if (sort){
                    sort_command = "sort -t'" OFS "' --parallel " num_cores " -nk" sort_column
                    printf "%s" ORS,line | sort_command
                }else{
                    printf "%s" ORS,line
                }
            }else{
                printf "%s" ORS,line > path_output
            }
        }
    }

    function print_line_number(){
        if (output_header){
            return FNR-records_skipped - 2
        }else{
            return FNR-records_skipped - 1
        }
    }

    function line_number(){
        if (header){
            return FNR-records_skipped - 1
        }else{
            return FNR-records_skipped
        }

    }

    function print_header(){
        if (add_index){
            field = transform_field("index",1)
            if (!save){
                printf("%s" OFS,field)
            }else{
                printf("%s" OFS,field) > path_output
            }

        }
        if (fields_based_code){
            for (i=min_col();i<=max_col();i++) {
                if ((number_files_input == 1 || input_file_rows) || (input_file_cols && v[i])){
                    if (is_first_command && !is_last_command && level_simplicity_csv != 2){
                        gsub(/\n/,delimiter_internal_notation "n" delimiter_internal_notation,$i)
                        gsub(FS,delimiter_internal_notation "d" delimiter_internal_notation,$i)
                        gsub(input_quote, delimiter_internal_notation "q" delimiter_internal_notation, $i)
                        gsub("\r", delimiter_internal_notation "r" delimiter_internal_notation, $i)
                    }
                    if (is_last_command && !is_first_command  && level_simplicity_csv != 2){
                        gsub(delimiter_internal_notation "n" delimiter_internal_notation,"\n",$i)
                        gsub(delimiter_internal_notation "d" delimiter_internal_notation,FS,$i)
                        gsub(delimiter_internal_notation "q" delimiter_internal_notation,input_quote, fldStr)
                        gsub(delimiter_internal_notation "r" delimiter_internal_notation,"\r", $i)
                    }
                    output_separator = OFS
                    if (i == max_col() && !add_new_column){
                        output_separator = ORS
                    }
                    if (!save){
                        printf "%s" output_separator,transform_header($i,i)
                    }else{
                        printf "%s" output_separator,transform_header($i,i) > path_output
                    }
                }

            }
            add_column()
        }else{
            gsub(input_quote,output_quote,$0)
            if (!save){
                printf "%s" ORS,$0
            }else{
                printf "%s" ORS,$0 > path_output
            }
            add_column()

        }

    }

    function min_col(){
        if (1 > col_start){
            return 1
        }else{
            return col_start
        }
    }

    function max_col(){
        if (col_end == INF){
            return NF
        }else{
            if (NF < col_end){
                return NF
            }else{
                return col_end
            }
        }
    }

    function add_column(){
        if (add_new_column){
            if (line_number() == 0){
                printf "%s" ORS,name_new_column
            }else{
                printf "%s" ORS,""
            }
        }

    }

    function transform_header(field,column){
        return field
    }




    #################################
    #################################


    function transform_column(field,column){

    return field
    }


    function transform_digit(field,column){
    field = transform_column(field,column)

    return field
    }


    function transform_string(field,column){
    field = transform_column(field,column)

    return field
    }

    function transform_line(line){

    return line
    }

        function condition(){
        statement = 1
        statement = ($3 ~ /^"?crlsb"?$/)
        return statement
        }

    BEGIN {
        PREC=100
        OFMT="%.10g"
        CONVFMT="%.10g"

        is_first_command = 0
        is_last_command = 0


        delimiter_internal_notation = ":"
        if (FS == delimiter_internal_notation){
            delimiter_internal_notation = "#"
        }

        input_quote = "\""
        output_quote = "\""

        level_simplicity_csv = 2

        FS =","

        OFS=","


        original_level_simplicity_csv = 0

        if (level_simplicity_csv <= 1){
            FPAT="([^" FS "]*)|(" input_quote "([^" input_quote "]|" input_quote input_quote ")+" input_quote ")"
        }


        records_skipped = 0

        minimal_string_quoting = 1
        full_string_quoting = !minimal_string_quoting

        is_unix_input = 1
        is_unix_output = 1

        if (is_unix_input){
        RS = "\n"
        }else{
        RS = "\r\n"
        }

        if (is_unix_output){
        ORS = "\n"
        }else{
        ORS = "\r\n"
        }
        null_input_string = "NULL"
        null_output_string = ""

        header = 1
        output_header = 1

        if (!header){
            output_header = 0
        }

        add_index = 0
        index_based_on = 0

        line_based_code = 0
        fields_based_code = !line_based_code

        col_start = 1
        col_end = INF

        row_start = 1
        row_end = INF

        number_files_input = 1
        input_file_rows = 1
        input_file_cols = !input_file_rows

        find_unique = 0

        print_fields = 1

        save = 0
        path_output = ""

        sort = 0
        sort_column = 1
        num_cores = 4
        sort_in_parallel = 1

        calculate_shape = 0

        check_complexity = 0

        add_new_column = 0
        name_new_column = ""

        if (check_complexity){
            has_maximum_complexity = 0
            print_fields = 0
        }

        quotes_have_been_removed = 0
        number_fields = 0
        continue_next_line = 0
    }



    {
        if (!calculate_shape){

            if (check_complexity || number_files_input == 1){
                if (check_complexity){
                    if (line_number() == 0){
                        number_fields = max_col()
                        has_maximum_complexity = 0
                    }else{
                        if (max_col() < number_fields){
                            has_maximum_complexity = 1
                            exit
                        }
                    }
                }else{
                    if (line_number() == 0 && header){
                        number_fields = NF
                        if (output_header){
                            print_header()
                        }
                    }else{
                        if (fields_based_code){
                            if (line_number() >= row_start){
                                for (i=min_col();i<=max_col();i++) {
                                    if (condition()){
                                        print_field($i,i)
                                    }
                                }
                                i=min_col()
                                if (min_col() == max_col() && $i == ""){
                                    print(":n:")
                                }
                                add_column()
                            }
                        }else{
                            if (line_number() >= row_start){
                            if (condition()){
                                print_line($0)
                            }

                            }
                        }
                        if (row_end != INF && line_number() > row_end){
                        exit
                        }
                    }
                }
            }else{
                if (FNR == NR){
                    v[$0] = 1

                }else{
                    if (FNR!=NR && FNR == 1){
                        records_skipped = 0
                    }
                    if (line_number() == 0 && header){
                        number_fields = max_col()
                        if (output_header){
                            print_header()
                        }
                    }else{
                        if (fields_based_code){
                            if (line_number() >= row_start){
                                for (i=min_col();i<=max_col();i++) {
                                if (condition()){
                                    field = $i
                                    if (input_file_rows && v[line_number()]){
                                        print_field(field,i)
                                    }else{
                                        if (input_file_cols && v[i]){
                                            print_field(field,i)
                                        }
                                    }
                                }
                                }
                                i=min_col()
                                if (min_col() == max_col() && $i == ""){
                                    print(":n:")
                                }
                                add_column()
                            }
                        }else{
                            if (line_number() >= row_start){
                            if (condition()){
                                if (input_file_rows && v[line_number()]){
                                    print_line($0)
                                }

                            }

                            }
                        }
                        if (row_end != INF && line_number() > row_end){
                        exit
                        }
                    }
                }


            }
        }

    }


    END{
        if (find_unique){
            for (key in unique){
                print(key)
            }
        }
        if (calculate_shape){
            print print_line_number()
            print NF
        }
        if (check_complexity){
            print has_maximum_complexity
        }


    }
    ```
