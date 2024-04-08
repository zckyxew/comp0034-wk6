from flask import current_app as app
from flask import render_template

@app.route('/', methods=['GET'])
def index():
    """
    Returns a HTML page, based on the template.
    """
    return render_template('index.html')
