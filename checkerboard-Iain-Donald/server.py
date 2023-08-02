from flask import Flask, render_template  # Import Flask to allow us to create our app
app = Flask(__name__)    # Create a new instance of the Flask class called "app"

@app.route('/<x>/<y>')
def printPage(x: int, y: int):
    x = int(x)
    y = int(y)
    return render_template('index.html', x = x, y = y) 

if __name__=="__main__":   # Ensure this file is being run directly and not from a different module    
    app.run(debug=True)    # Run the app in debug mode.
