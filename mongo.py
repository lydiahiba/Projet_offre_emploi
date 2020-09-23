from flask import Flask, render_template, url_for, redirect, flash,jsonify,request
from flask_pymongo import PyMongo
# from flask_wtf import FlaskForm
# from wtforms import StringField, SubmitField

app = Flask(__name__)

app.config['MONGO_DBNAME'] = 'Indeed'
app.config['MONGO_URI'] = 'mongodb://localhost:27017/job_applications'

mongo = PyMongo(app)
job=mongo.db.Indeed


@app.route('/')
def index():
    return render_template('index.html')


@app.route('/search', methods=['POST'])
def get_offers():
    job = mongo.db.Indeed
    output = []
    for s in job.find({"Title": { "$regex": str(request.form["Title_field"]) }, "Company":  { "$regex": str(request.form['skills_field'])}}):
        output.append({'Title' : s['Title'], 'Description' : s['Description'],'Links': s['Links']})
    return render_template('result.html', outputs= output)

# @app.route('/My_Application', methods=['POST'])
# def Application():
#     return render_template('application.html',)

if __name__ == "__main":
    app.run(debug=True,host='0.0.0.0')