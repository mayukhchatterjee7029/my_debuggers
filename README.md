
# 🐞 Custom ML Debuggers

A collection of custom debugging utilities for machine learning projects to help identify and visualize common issues during model development.

## Tools

### 🔍 NaN Detector
Utility for detecting NaN values in pandas DataFrames.
- NaN value detection

### 📊 Classifier Plots
Visualization utilities for classification model debugging.
- Confusion matrix plots
- Learning curve plots

---
## 🧑🏻‍💻 Quick Start

```python
from my_debuggers import nan_detector, create_clf_plots
```
## 🔍 Detect NaN values
```python
nan_detector = nan_detector(df) # df is a pandas DataFrame
# detects NaN values in a DataFrame
```

## 📊 Generate classification plots
```python
create_clf_plots(model, X_train, X_val, y_train, y_val, model_name='Model', y_pred=None)
# Creates confusion matrix and learning curve plots for classification models
```
---
## 🛠️ Installation
**(Optional) Create a virtual environment**(eg. [`miniconda`](https://www.anaconda.com/docs/getting-started/miniconda/install))

```bash
pip install -r requirements.txt
```

---
## 🙏🏻 Contributing

Feel free to add new debugging utilities or improve existing ones. Each tool should be self-contained and well-documented.

## 📃 License
This project is licensed under the MIT License.

---
⭐ If you found this project helpful, please consider giving it a star!