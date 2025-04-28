from flask import Flask, render_template
app = Flask(__name__)

@app.route("/")
def hello():
    return render_template('index.html')

@app.route("/about")
def rishabh():
    name = 'rishabh'
    return render_template('about.html', namefortemp=name) 
# name (ye wala part templet me jata hai ise dusre file se access karte hai) = name (ye wala part python ke program se uthaya jata hai)


#app.run() this will work
app.run(debug=True) #debug=True relodes the changes automatically