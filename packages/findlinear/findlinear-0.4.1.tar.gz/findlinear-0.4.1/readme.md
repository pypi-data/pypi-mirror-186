# findlinear: Determining the linear segments of data with Bayesian model comparison

`findlinear` is a Python module for finding the linear segment given a curve or dataset with `x` and `y`. 

## How does it work?
It uses the idea of Bayesian model comparison and calculate the evidence of each possible segment of curve being linear. 
After calculating the evidence of each segment, it detects the global maximum, or uses the `findpeaks` library to find the local maxima of evidence, from which the user can choose the relevant linear segment (e.g. that with the largest evidence, or that with the largest slope when the data consists of multiple linear segments).

## Installation
For users, type in terminal
```
> pip install findlinear
```

For developers, create a virtual environment and then type 
```
> git clone https://git.ecdf.ed.ac.uk/s1856140/findlinear.git
> cd findlinear 
> poetry install --with dev 
```

## Quickstart
Data `x` is a list or a 1D Numpy array, sorted ascendingly; the data `y` is a list or a Numpy array, with each row being one replicate of measurement.
```
>>> from findlinear.findlinear import findlinear, get_example_data
>>> x, y = get_example_data()
>>> fl = findlinear(x, y)
>>> fl.find_all()
>>> fl.plot()
>>> fl.get_argmax()
>>> fl.get_peaks()
```

## Documentation
Detailed documentation is available soon.

## Citation
A preprint is coming soon.
