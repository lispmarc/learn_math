# learn_math

Python package containing two modules 
- waves
- wave_plot

### waves
Allows you to generate linear combination of sinusodal functions
### waves_plot
Plots different functions depending on one variable
## Installation

Download this project directory. In the project directory (the directory containing setup.py) install the package by executing

```bash
python setup.py install
```

## Usage

```python
# Using waves
from learn_math import waves,waves_plot
wave_length=10
wave_phase=3
wave_function=generate(wave_length,wave_phase)

## Assume that f1 and f2 are wave functions
## Return a wave function that is the sum of f1 and f2
f=add(f1,f2)
## Plot the wave function
wave_plot(f)
python -m factorial 4
```
