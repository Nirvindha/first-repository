from flask import Flask, render_template
app=Flask(__name__)
JOBS=[
  {
    'id':1,'title':'Data Scientist','location':'Chennai,India','salary':'Rs.20,00,000'
  },
  {
    'id':2,'title':'Data Analyst','location':'Mumbai.India','salary':'Rs.10,00,000'
  },
{
    'id':3,'title':'Front-End developer','location':'Delhi,India','salary':'Rs.15,00,000'
  }
]
@app.route("/")
def hello_nir():
  return render_template('home.html',jobs=JOBS)
@app.route("/api/jobs")
def list_jobs():
  return jsonify(JOBS)
if __name__=='__main__':
  app.run(host='0.0.0.0',debug=True)