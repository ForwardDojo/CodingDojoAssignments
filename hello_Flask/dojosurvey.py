from flask import Flask, render_template, request, redirect, session
app = Flask(__name__)

app.secret_key= "/hello"

@app.route('/')
def index():
    return render_template("index3.html")


@app.route('/create', methods= ['POST'])
def create():
    name = request.form['name']
    location= request.form['Dojo_Location']
    language= request.form['Favorite_Language']
    message= request.form['message']
    print(request.form)
    print(name)
    print(location)
    print(language)

    session['name'] = name
    session['Dojo_Location']= location
    session['Favorite_Language']= language
    session['message']= message
    return redirect('/result')

@app.route('/result', methods= ['GET'])
def result():
    
    return render_template('result.html')


if __name__=="__main__":
    app.run(debug=True)


