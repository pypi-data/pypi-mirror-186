# Bunzbar

## System requirements
+ Linux system with X.Org display server

## Installation

### Install Python package

First of all you need to install the bunzbar python module.
After installing python and pip, use one of the following options to install it.

+ pip
```bash
pip install bunzbar
```
+ from source
```bash
pip install build twine
git clone https://gitlab.com/02742/bunzbar.git
cd bunzbar && python3 -m build
pip install dist/*.whl --force-reinstall
```

### Add `~/.local/bin` to your `$PATH`
```bash
export PATH=~/.local/bin:${PATH}
echo "export PATH=~/.local/bin:${PATH}" >> ~/.bashrc
```


### Add `~/.local/bin/bunzbar -d &` to your `~/.xinitrc` file
```bash
bunzbar -d
```

## Configuration
You can toggle an info in the bar with the following command:
```bash
bunzbar -it <toogle_name>
```
To get a list of these names simply execute:
```bash
bunzbar -il
```
If you want to change an option in the config file you can do that using:
```bash
bunzbar -cs <config_option> <value>
```
Again you can list the available config options using:
```bash
bunzbar -cl
```


## Links

+ [gitlab](https://gitlab.com/02742/bunzbar/)
+ [pypi](https://pypi.org/project/bunzbar/)
