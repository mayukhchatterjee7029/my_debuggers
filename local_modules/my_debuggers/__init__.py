"""
ML Debugging utilities package.
"""

## Import other debuggers in this way
from .nan_detector import nan_detector
from .plot_clf import create_clf_plots

# Version info
__version__ = "0.1.0"
__author__ = "Mayukh Chatterjee"

# What gets imported with "from my_debuggers import *"

## list structure
__all__ = [
    'nan_detector',
    'create_clf_plots',
]
