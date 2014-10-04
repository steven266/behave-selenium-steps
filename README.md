behave-selenium-steps
=====================

Common steps for website functionality tests


Usage
------

Just copy the features directory into your project. Add some *.feature files and change the settings.py file.
To run the tests, simply call 'behave' inside of the feature directory

Features are written in [Gherkin Syntax](https://github.com/cucumber/cucumber/wiki/Gherkin).
You can add new step-definitions in the steps.py file. Feel free to contribute to this repository!

Have a look at the example.feature file for examples.


Installation and configuration
------

Besides 'behave' and 'selenium' you will also need to install phantomjs or any other driver compatible with selenium
(see [Selenium WebDriver](http://docs.seleniumhq.org/projects/webdriver/)).


Additional information
------

* [Behave](http://pythonhosted.org/behave/)
* [Gherkin](https://github.com/cucumber/cucumber/wiki/Gherkin)
* [Selenium with Python](http://selenium-python.readthedocs.org/en/latest/)
* [Selenium](http://docs.seleniumhq.org/)