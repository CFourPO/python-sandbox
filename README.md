## String Formatting

```
%s - String (or any object with a string representation, like numbers)

%d - Integers

%f - Floating point numbers

%.<number of digits>f - Floating point numbers with a fixed amount of digits to the right of the dot.

%x/%X - Integers in hex representation (lowercase/uppercase)
```

## Dictionary

```
dict = [
    key: value,
    key: value
]
```

## Numpy

```
import numpy as np

h = [2, 3, 4]
w = [4, 6, 8]

np_h = np.array(h)
np_w = np.array(w)

w_to_h = np_w / np_h

print(w_to_h)
```



## DataFrames

```
import pandas as pd
```
Can be used to create tabular data from various sources.

#### Create DataFrame from Dictionary:

>```
>dict = {
>    'key1': ['val1', 'val2', 'val3'],
>    'key2': ['val1', 'val2', 'val3']
>}
>
>df = pd.DataFrame(dict)
>print(df)
>
>"""
>Output:
>
>        city                 fav_movie   first    last  score
>0  New York             The Outsiders   Chris   Smith     90
>1    Boston  Pirates of the Carribean   Tommy    Bart     85
>2   Pheonix              Harry Potter    alex  Trebek     99
>3  Istanbul                       Elf  Jarrod  Subway     78
>"""
>```

#### Create DataFrame from CSV:

>```
>df = pd.read_csv('file.csv')
>```

#### Accessing Rows (Observations):

>```
># select row
>row  = df[0]
>
># select first 4 rows
>rows = df[0:4]
>
># create dataframe with specific columns
>show_cols = df[['column_1', 'column_2']]
>```