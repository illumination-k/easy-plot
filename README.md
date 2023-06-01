# easy-plot

The CLI tool to plot biological data easily

## Installation

```
pip install git+https://github.com/illumination-k/easy-plot.git
```

## Multisample plot

Plot boxplot and swarmplot with tukey-hsd test.

```bash
easy-plot multisample -i ./examples/multisample.csv -o ./examples/multisample.png
```

### Example data

[multisample.csv](examples/multisample.csv)

### Example image

![multisample](examples/multisample.png)

## Two sample plot

Plot boxplot and swarmplot with t-test_welch test.

```bash
easyplot twosample -i ./examples/twosample.csv -o ./examples/twosample.png --test t-test_welch --test-text simple
```

### Example Data

[twosample.csv](examples/twosample.csv)

### Example Image

![twosample](examples/twosample.png)
