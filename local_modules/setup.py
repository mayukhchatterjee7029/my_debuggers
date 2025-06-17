from setuptools import setup, find_packages

setup(
    name="my-debuggers",
    version="0.1.0",
    description="ML debugging utilities",
    author="Your Name",
    packages=find_packages(),
    install_requires=[
        'pandas>=1.0.0',
        'numpy>=1.18.0',
        'matplotlib>=3.0.0',
        'seaborn>=0.11.0',
        'scikit-learn>=1.0.0',
    ],
    python_requires='>=3.7',
)
