<a name="readme-top"></a>
# StockChecker
This Python program makes use of the [RealStonks API][RealStonksAPI] available on the [RapidAPI][RapidAPI] website to fetch information on specified NASDAQ stock symbols.  It was built and tested on Python version 3.11.1.

# Table of Contents
* [Installation](#installation)
* [Setup](#setup)
* [Execute](#execute)

# Installation

**Pyenv**
* Install Pyenv on your machine, [github.com/pyenv-win/pyenv-win](https://github.com/pyenv-win/pyenv-win).
* Use Pyenv to install Python version 3.11.1.
  ```
  pyenv install 3.11.1
  ```

**Pipenv**
* Install Pipenv on your machine, [pipenv.pypa.io/en/latest](https://pipenv.pypa.io/en/latest/#install-pipenv-today).

**StockChecker**
* Clone this repo onto your machine.
  ```
  git clone git@github.com:luis-delatorre/StockChecker.git
  ```
* Navigate into the StockChecker directory.

* Use Pipenv to create a virtual environment and install required packages.
  ```
  pipenv install --skip-lock --dev
  ```
  * **Note:** If the required Python version does not exist on your machine, Pipenv will use Pyenv to install it.  It will prompt  you first.

<p align="right">(<a href="#readme-top">back to top</a>)</p>


# Setup
**RapidAPI Account**
* To use APIs from the [RapidAPI][RapidAPI] site, you need to have an account setup with them.  Their service is free to use.
* After you have an account with them, search for and subscribe to the [RealStonks API][RealStonksAPI].
  * This will provide you with an `X-RapidAPI-Host` and `X-RapidAPI-Key`.

**Environment Variables**
* In the project's root directory, create a `.env` file.
* Enter the following variables into the file.  Replace values with data from RapidAPI.
  ```
  API_HOST=realstonks.p.rapidapi.com
  API_KEY=<replace_with_rapid_api_key>
  ```
<p align="right">(<a href="#readme-top">back to top</a>)</p>


# Execute
**Run Program**
```
pipenv run python StockChecker.py AAPL
```

**Run Tests**
```
pipenv run python -m pytest -rA tests/
```

<!-- Reference Links --> 
[RapidAPI]: https://rapidapi.com/hub
[RealStonksAPI]: https://rapidapi.com/amansharma2910/api/realstonks/

<p align="right">(<a href="#readme-top">back to top</a>)</p>