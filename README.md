## String Formatting

```
%s - String (or any object with a string representation, like numbers)

%d - Integers

%f - Floating point numbers

%.<number of digits>f - Floating point numbers with a fixed amount of digits to the right of the dot.

%x/%X - Integers in hex representation (lowercase/uppercase)
```

## DataFrames

```
import pandas as pd
```
Can be used to create tabular data from:

- Dictionaries:
>```
>dict = {
>    'key1': ['val1', 'val2', 'val3'],
>    'key2': ['val1', 'val2', 'val3']
>}
>
>df = pd.DataFrame(dict)
>print(df)
>```
>Output:
>```
>        city                 fav_movie   first    last  score
>0  New York             The Outsiders   Chris   Smith     90
>1    Boston  Pirates of the Carribean   Tommy    Bart     85
>2   Pheonix              Harry Potter    alex  Trebek     99
>3  Istanbul                       Elf  Jarrod  Subway     78
>```