# Get application

Download the zipped file and unzip it. The name of the executable is *tiped*.

* Download [here](https://github.com/GimmyR/tiped-2.0-download/blob/main/tiped-ubuntu-22.04.tar.xz) for Ubuntu 22.04.
* Download [here](./dist/tiped-windows-11.zip) for Windows 11.

# For developers

## Prerequisites

* **Python** version **3.11**
* **PyQt** version **5.15**

## Run project

* For Linux and Mac users, run command `python3 tiped.py` in the directory of the project.
* For Windows users, run command `py tiped.py` in the directory of the project.

## Build an app for your operating system

You need to install **PyInstaller**.

Then run command `pyinstaller --noconsole tiped.py` in the directory of the project.

Don't forget to copy the **images** directory in the same directory of your executable (usually in *dist/tiped/*)