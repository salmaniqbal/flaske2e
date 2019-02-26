## Running the website as dokcer container

1. Run the following command to build the docker image
Make sure you are in the `web` directory

`$ docker build -t myapp:1.0 .`

2. Run the following command to run the image

`$ docker run -d -p 5000:5000 myapp:1.0`

3. Access the website by navigating to

`http://127.0.0.1:5000`

## Running UI tests

### Pre-requsisites 
1. In order to run the UI tests using selenium, install selenium on your machine using the following:

`$ pip install -U selenium`

2. Install pytest, instructions are [here](https://docs.pytest.org/en/latest/getting-started.html) 
3. More information on Selenium can be found on the official [website](https://pypi.org/project/selenium/)
4. These tests use the Chrome web driver to interact with the browser. This driver is included in the repository's root directory and the tests reference it from that location.

### Running the Tests

1. Ensure that the docker container is running, see instructions in the first section of this file.

2. Go to the root folder and run
`$ py.test`

This will run the two tests in `test_browser.py` & `test_flaskapp.py`

There are many ways of running selenium UI tests this is one way of doing See the python selenium documentation [here](https://selenium-python.readthedocs.io/) for more information.

