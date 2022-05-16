This is a flask app for returning "word count" data for a given text.

# Setup

The following instructions assume you already have docker installed and setup.
If you do not already have it installed, [get docker](https://docs.docker.com/get-docker/).

Run the following in order, in your terminal.

`docker build --tag nate-docker .`

`docker run -d -p 5000:3000 nate-docker`

Now going to http://localhost:5000 will open up the app.

# Using the app

When the app is up and running, the page at `/` will have a text input box, a drop down 
with a options on how to sort the result, and a button to submit the data to the server 
for processing.

if the text is a url to a web page, the app will attempt to get the text content of the 
web page and return the `word count` data.

You can also provide raw text to the input box and the response will be the `word count` 
data for the given text.

# Running tests

To run the tests for this app, first install all the requirements in the `requirements.txt` 
file with the following code in your terminal. (This assumes you have virtualenv installed) Run the following;

### Create a virtual environment

`virtualenv venv -p python3.6`

`source venv/bin/activate`

### Install the requirements

`pip install -r requirements.txt`

Then run the tests with the following code to get both the test results and 
test coverage report.

`python -m pytest --cov=tests`