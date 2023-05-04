<a name="readme-top"></a>
# StockChecker
This Python program makes use of the [RealStonks API][RealStonksAPI] available on the [RapidAPI][RapidAPI] website to fetch information on specified NASDAQ stock symbols.  It was built and tested on Python version 3.11.1.

# Table of Contents
* Installation
* Setup
* Execute

# Installation

**Pyenv**
* Install Pyenv on your machine, [github.com/pyenv-win/pyenv-win](https://github.com/pyenv-win/pyenv-win).
* Use Pyenv to install Python version 3.11.1.
  > pyenv install 3.11.1

**Pipenv**
* Install Pipenv on your machine, [pipenv.pypa.io/en/latest](https://pipenv.pypa.io/en/latest/#install-pipenv-today).

**StockChecker**
* Clone this repo onto your machine.
  > git clone git@github.com:luis-delatorre/StockChecker.git
* Navigate into the StockChecker directory.
* Use Pyenv to set Python 3.11.1 as your local python version.
  > pyenv local 3.11.1
* Use Pipenv to create a virtual environment with the compatible Python version.
  ```
  pipenv --python 3.11.1
  pipenv install --skip-lock --dev
  ```


# Setup
**RapidAPI Account**
* To use APIs from the [RapidAPI][RapidAPI] site, you need to have an account setup with them.  Their service is free to use.
* After you have an account with them, search for and subscribe to the [RealStonks API][RealStonksAPI].
  * This will provide you with a `X-RapidAPI-Key`.

**Environment Variables**
* In the project's root directory, create a `.env` file.
* Enter the following variables into the file.  Replace values with data from RapidAPI.
```
API_KEY=<replace_with_rapid_api_key>
API_HOST=<replace_with_rapid_api_host>
```  

# Execute
**Run Program**
> pipenv run python StockChecker.py AAPL

**Run Tests**
> pipenv run python -m pytest tests/

<!-- Reference Links --> 
[RapidAPI]: https://rapidapi.com/hub
[RealStonksAPI]: https://rapidapi.com/amansharma2910/api/realstonks/

