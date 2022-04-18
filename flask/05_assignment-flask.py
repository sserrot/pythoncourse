'''
Assignment #5

1. Add / modify code ONLY between the marked areas (i.e. "Place code below")
2. Run the associated test harness for a basic check on completeness. A successful run of the test cases does not guarantee accuracy or fulfillment of the requirements. Please do not submit your work if test cases fail.
3. To run unit tests simply use the below command after filling in all of the code:
    python 05_assignment.py
  
4. Unless explicitly stated, please do not import any additional libraries but feel free to use built-in Python packages
5. Submissions must be a Python file and not a notebook file (i.e *.ipynb)
6. Do not use global variables
7. Make sure your work is committed to your master branch

http://flask.pocoo.org/docs/1.0/quickstart/

Using the flask web server, load the HTML form contained in the variable main_page. The form should load at route '/'.
The user should then be able to enter a number and click Calculate at which time the browser will submit
an HTTP POST to the web server. The web server will then capture the post, extract the number entered
and display the number multiplied by 5 on the browser.

Hint: The HTML in main_page needs a modification in the text input. The modification should be done using regular expressions(regex)
'''
# ------ Place code below here \/ \/ \/ ------
from flask import Flask, request, render_template

app = Flask(__name__)


# Index Initialized

@app.route('/')
def index():
    return render_template('index.html')


# calculations for input numbers


@app.route('/calc', methods=['GET', 'POST'])
def calculate():
    if request.method == 'POST':
        number = int(request.form['input_number'])
        calculated_number = number * 5
    return render_template('calculate.html', calculated_number=calculated_number)


if __name__ == "__main__":
    app.run(host='0.0.0.0', port=5001, debug=True)
