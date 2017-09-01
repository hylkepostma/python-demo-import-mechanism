# Activate venv
venv\Scripts\activate.ps1

# Install dependencies
pip install wheel
pip install twine

# Create some distributions
python setup.py sdist --formats=gztar,zip bdist_wheel

# To upload with twine to PyPI use:
# twine upload dist/*

# Deactivate venv
deactivate