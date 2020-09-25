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
def index(outputs=None):
    print(outputs)
    return render_template('index.html', outputs=outputs)

@app.route('/search')
def search():
    job = mongo.db.Indeed
    title=request.args.get('title',0,type=str) # c'est la valeurs par défault si on récup rien ça retourne 0 
    job=request.args.get('skills',1,type=str)
    output = list(job.find({"Title": { "$regex":title },}, projection={'_id': False}))
    # for s in job.find({"Title": { "$regex": str(request.form["Title_field"]) }, "Skills":  { "$regex": str(request.form['skills_field'])}}):
    #     output.append({'Title' : s['Title'], 'Description' : s['Description'],'Links': s['Links']})
    results= jsonify({'result' : output})
    return results

# @app.route('/My_Application', methods=['POST'])
# def Application():
#     return render_template('application.html',)

if __name__ == "__main__":
    app.run(debug=True,host='0.0.0.0')