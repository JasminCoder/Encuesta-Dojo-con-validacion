from flask import render_template, redirect, request
from flask_app import app
from flask_app.models.surveys import Survey

#ruta raiz
@app.route('/')
def index():
    return render_template('index.html')



@app.route('/create/survey', methods=['POST'])
def create_survey():
    if Survey.is_valid(request.form):
        Survey.save(request.form)
        return redirect('/results')
    return redirect('/')




#ruta resultados
@app.route('/results')
def results():
    survey = Survey.get_survey()
    return render_template('results.html', encuesta = survey)