# Introduction 
Design package for the company Envidan A/S intended for use with matplotlib and seaborn
- Hardcoded palettes and colormaps with company design colors
- Envidan logo in print and web form

# Getting Started
## Installation
You can install this package using
```
pip install ed_design
```
## Dependencies
Software dependencices are:
```
matplotlib
numpy
```

## Use
### Palettes and colormaps for matplotlib and seaborn
```
from ed_design import Colors

colors = Colors()
colors.show_palette('all')

palette = colors.get_palette('blues')  # Use with categorical variabels
cmap = colors.get_palette('BlGr')  # Use with continous variabels
```

### Envidan logo
```
from ed_design import ed_logo
logo = ed_logo('print')
```

# Build and Test
TODO:
- Implementation of a matplotlib setup file to fix visualization style in plots
- Implement Satoshi font

# Contribute
Only employees in Envidan has access to the repository

# Author
Martin Vidkjær, mav@envidan.dk
