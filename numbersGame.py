from flask import Flask, render_template, request, session, flash, redirect
import random
app = Flask(__name__)
app.secret_key = "secretKey"
def setSession():
    session['number'] = random.randrange(0,101)

@app.route('/')
def index():
    if session['number'] == None:
        setSession()
    else:
        pass
    print session['number']
    return render_template('index.html')

@app.route('/guess', methods=['POST'])
def guess():
    guess = request.form['guess']
    if request.method == 'POST':
        numGuess = int(guess)
        if  numGuess == session['number']:
            flash(str(numGuess) + ' was the number!', 'success')
        elif numGuess > session['number']:
            flash('Too High', 'error')
        else:
            flash('Too Low', 'error')
    return redirect('/')

@app.route('/restart', methods=['GET', 'POST'])
def restart():
    setSession()
    return redirect('/')
app.run(debug=True)
