from flask import Flask, render_template,jsonify

app = Flask(__name__)

JOBS =[
  {
    'id':1,
    'title': 'Data Analyst',
    'location': 'Bengaluru,India',
    'salary': 'Rs.10000000'
  },
  {
    'id':2,
    'title': 'Data Scientist',
    'location':'Delhi,India',
    'salary': 'Rs.15000000'
  },
  {
    'id':3,
    'title': 'FrontEnd Engineer',
    'location':'Remote' ,
    'salary': 'Rs.15000000'
  },
  {
    'id':4,
    'title': 'Backend Engineer',
    'location':'San Fransico,USA' ,
    'salary': '$.12000000'
    }
    
  
]

@app.route("/")

def hello_jovian():
  #return "Hello, World !!!"
  return render_template('home.html',jobs=JOBS, 
  company_name='Jovian')

@app.route("/api/jobs")

def list_jobs():
  return jsonify(JOBS)

if __name__=="__main__":
  #print("I am inside the if now") 
  app.run(host='0.0.0.0',debug=True)