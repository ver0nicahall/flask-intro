"""Greeting Flask app."""

from random import choice

from flask import Flask, request

# "__name__" is a special Python variable for the name of the current module
# Flask wants to know this to know what any imported things are relative to.
app = Flask(__name__)

AWESOMENESS = [
    'awesome', 'terrific', 'fantastic', 'neato', 'fantabulous', 'wowza',
    'oh-so-not-meh', 'brilliant', 'ducky', 'coolio', 'incredible',
    'wonderful', 'smashing', 'lovely']

INSULTS = ['stupid', 'annoying', 'silly', 'lazy']


@app.route('/')
def start_here():
    """Home page."""  

    return """<!doctype html>
                <body>
                <h1>Hi! This is the home page</h1>
                <a href="/hello">Go there!</a>
                </body>
              </html>"""


@app.route('/hello')
def say_hello():
    """Say hello and prompt for user's name."""

    return """
    <!doctype html>
    <html>
      <head>
        <title>Hi There!</title>
      </head>
      <body>
        <h1>Hi There!</h1>
        <form action="/greet">
          Greet:<br/>
          <input type="text" name="person">
          <select name="awesomeness">
            <option value=""></option>
            <option value="awesome">awesome</option>
            <option value="terrific">terrific</option>
            <option value="fantastic">fantastic</option>
            <option value="neato">neato</option>
            <option value="fantabulous">fantabulous</option>
            <option value="wowza">wowza</option>
            <option value="oh-so-not-meh">oh-so-not-meh</option>
            <option value="brilliant">brilliant</option>
            <option value="ducky">ducky</option>
            <option value="coolio">coolio</option>
            <option value="incredible">incredible</option>
            <option value="wondeful">wonderful</option>
            <option value="smashing">smashing</option>
            <option value="lovely">lovely</option>
          </select>
          <input type="submit" value="Submit">
          <br/>
        </form>
        <form action="/diss">
          Insult:<br/>
          <input type="text" name="person">
          <select name="insult">
            <option value=""></option>
            <option value="silly">silly</option>
            <option value="lazy">lazy</option>
            <option value="annoying">annoying</option>
            <option value="stupid">stupid</option>
          </select>
          <input type="submit" value="Submit">
          <br/>
        </form>
      </body>
    </html>
    """


@app.route('/greet')
def greet_person():
    """Get user by name."""

    player = request.args.get("person")
    AWESOMENESS = request.args.get("awesomeness")

    compliment = AWESOMENESS

    return f"""
    <!doctype html>
    <html>
      <head>
        <title>A Compliment</title>
      </head>
      <body>
        <h1>Hi, {player}! I think you're {compliment}!</h1>
        <a href="/hello">Go back</a>
      </body>
    </html>
    """

    
@app.route('/diss')
def diss():
    """Insult user by name."""

    player = request.args.get("person")
    insult = request.args.get("insult")

    return f"""
    <!doctype html>
    <html>
      <head>
        <title>An Insult</title>
      </head>
      <body>
        <h1>Hi, {player}! I think you're {insult}!</h1>
        <a href="/hello">Go back</a>
      </body>
    </html>
    """

if __name__ == '__main__':
    # debug=True gives us error messages in the browser and also "reloads"
    # our web app if we change the code.
    app.run(debug=False, host="0.0.0.0")
