Codes taken from:
https://engineering.upside.com/a-beginners-guide-to-optimizing-pandas-code-for-speed-c09ef2c6a4d6

These codes show how can we speed up the same code using Pandas DataFrames

We’ll review the efficiency of several methodologies for applying a function to a Pandas DataFrame, from slowest to fastest:
1. Crude looping over DataFrame rows using indices
    CrudeLopping_1.py

2. Looping with iterrows()
    IterrowsLooping_2.py
    
3. Looping with apply()
    ApplyLooping.py
    
4. Vectorization with Pandas series
    SeriesLooping_4.py
    
5. Vectorization with NumPy arrays
    NumpyLooping_5.py
