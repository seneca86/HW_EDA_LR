## Homework: exploratory data analysis and linear regression

### Instructions

* You will provide a main.py file; it is critical that the code runs (i.e. if I press the "Run" button there should be no error message)

* You do not need to write text, just code; please `print` important results (otherwise they are executed but do not get printed)

* You may interact with your friends but DO NOT copy code: if I detect errors that have been copy pasted and that are suspiciously similar across different submission the grade will be penalized

(1) Import `seaborn`, `pandas`, and `numpy`, plus the following:

```python
import matplotlib as mpl
import matplotlib.pyplot as plt
```

(2) From `seaborn`, load the dataset `mpg`, which stands for "miles per gallon", with the following command:

```python
df = sns.load_dataset("mpg")
```

This dataset contains information of a number of vehicles.

(3) Check which are the columns of the dataset.

(4) Add a column named `l100km` which are the liters that each car consumes per one hundred kilometers; you will start with `mpg` and apply a transformation.

Note that one miles is equal to `1.60934` km and one gallon equal to `3.78541` liters. 

(5) Count how many cars have which number of cylinders by using `value_counts()`.

(6) Copy the `LeastSquares` function we defined in class into your code.

(7) Remove the rows containing `nans` in columns `l100km` and `horsepower`, which will play the role of `x` and `y` in our linear regression model

(8) Calculate the `slope` and the `intercept` of the relationship between power and consumption; print the results

(9) Print the data (you do not need to print the results) with `seaborn`; you may used the following code but you will need to fill out the `...`: 

```python
from pathlib import Path
Path('plots').mkdir(parents=True, exist_ok=True)
mpl.rcParams["figure.dpi"] = 300
sns.set_theme()
scatter1 = sns.relplot(
    data=...,
    x=...,
    y=...,
    style=None,
    hue="cylinders",
    markers=None,
    kind="scatter",
    col=None,
)
scatter1.savefig("plots/scatter.png")
plt.clf()
```