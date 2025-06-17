
# 🐞 Custom ML Debuggers

A collection of custom debugging utilities for machine learning projects to help identify and visualize common issues during model development.

## Tools

* 🔍 NaN Detector
* 📊 Classifier Plots

### 📊 Classifier Plots
Visualization utilities for classification model debugging.
- NaN value detection
- Confusion matrix plots
- Learning curve plots
## Quick Start

```python
from my_debuggers import nan_detector, create_clf_plots
```
# Detect NaN values
```python
nan_detector = nan_detector(df)
# detects NaN values in a DataFrame
```
`df: pandas.DataFrame`

# Generate classification plots
```python
create_clf_plots(model, X_train, X_val, y_train, y_val,model_name='Model', y_pred=None)
# Creates confusion matrix and learning curve plots for classification models
```
---
## Installation

```bash
pip install -r requirements.txt
```

**Optional: Create a virtual environment:**(eg. [`miniconda`](https://www.anaconda.com/docs/getting-started/miniconda/install))

---
## Contributing

Feel free to add new debugging utilities or improve existing ones. Each tool should be self-contained and well-documented.

---
## License
This project is licensed under the MIT License.