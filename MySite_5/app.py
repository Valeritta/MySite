from flask import Flask,  render_template, redirect, request, flash, session, url_for
from users import Users
add=Users()
app=Flask(__name__)
app.secret_key='lolpowerfcefer'

@app.route('/logout')
@app.route('/')
def home():
    session['key']=False
    return render_template('index.html')

@app.route('/about')
def about():
    return render_template('about.html')

@app.route('/photos')
def photos():
    return render_template('photos.html')

@app.route('/reg')
def reg():
    return render_template('reg.html')

@app.route('/authorization')
def authorization():
    return render_template('authorization.html')

@app.route('/create_akk', methods=['POST'])
def create_akk():
    res=add.reg(request.form)
    if res==True:
        session['key']=True
        return redirect(url_for('authoriz_user'))
    return redirect(url_for('reg'))

@app.route('/authoriz_user')
def authoriz_user():
    if session['key']==True:
        return render_template('1.html')
    else:
        return redirect(url_for('reg'))
    

if (__name__=="__main__"):
    app.debug = True
    app.run()