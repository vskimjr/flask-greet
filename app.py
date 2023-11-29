from flask import Flask

app = Flask(__name__)

@app.get('/welcome')
def welcome():
    """ Returns "welcome" """

    return """
    <html>
        <body>
            <h1>welcome</h1>
        </body>
    </html>
    """
@app.get('/welcome/home')
def welcome_home():
    """ Returns "welcome home" """

    return """
    <html>
        <body>
            <h1>welcome home</h1>
        </body>
    </html>
    """

@app.get('/welcome/back')
def welcome_back():
    """ Returns "welcome back" """

    return """
    <html>
        <body>
            <h1>welcome back</h1>
        </body>
    </html>
    """