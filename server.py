from flask_app import app
from flask_app.controllers import surveys_controller



if __name__=="__main__":
    app.run(debug=True)


























#from flask import Flask, render_template, session, request, redirect

#app = Flask (__name__)

#app.secret_key= "llave"


#@app.route('/')
#def index():
#    return render_template('index.html')


#@app.route('/results', methods=['POST'])
#def Procesando():
#    print(request.form)

#    #GUARDAMOS EN SESION
#    session['name'] = request.form['name']
#    session['location'] = request.form['location']
#    session['language'] = request.form['language']
#    session['comment'] = request.form['comment']

#    #return "Procesando información"
#    return redirect('/results') #redirect nos lleva a la nueva URL 


#@app.route('/results')
#def exito():
#    return render_template('results.html')


#if __name__=="__main__":
#    app.run(debug=True)