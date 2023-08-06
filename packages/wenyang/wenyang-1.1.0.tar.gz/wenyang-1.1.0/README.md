# wenyang
A Python package example

steps:
1. Give your package a unique name {package.name} in PyPI. You can check with `pip search`.
1. Create a new repository {package.name} on github as https://github.com/{github.username}/{package.name}
1. `git clone https://github.com/{github.username}/{package.name}` then you will get folder {package.name} as the {root}
1. Change directory into {root}
1. Create README.md for the package if you did not init your repository with a README.md
1. Read https://packaging.python.org/tutorials/packaging-projects/
1. Create empty package as {package.name}
1. Create setup.py
1. Generate distribution packages
1. `python3 -m pip install --upgrade setuptools wheel`
1. `python3 setup.py sdist bdist_wheel`
1. Upload the distribution archives
1. `python3 -m pip install --upgrade twine`
1. `python3 -m twine upload --skip-existing dist/*`
1. Check the package on https://pypi.org/project/{package.name}/

references:
1. https://github.com/pypa/sampleproject
1. [Github-flavored Markdown](https://guides.github.com/features/mastering-markdown/)
