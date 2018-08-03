from flask import Flask, render_template, session
app = Flask(__name__)  

app.secret_key= "/counterhello"

@app.route('/')         
def index():
    count = 1
    if "num" not in session:
        session['num']=1
    else: session 'num' = session 'num'+1

#   email= request.form['email']

#     print(request.form)

#     session['name'] = name

    return render_template("index5.html")

if __name__=="__main__":
    app.run(debug=True)

