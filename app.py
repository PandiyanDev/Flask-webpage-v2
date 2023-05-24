from flask import Flask, render_template, jsonify

JOBS = [{
  'id': 1,
  'title': 'Data Scientist',
  'location': 'Delhi, India',
  'Salary': 'Rs. 15,00,000'
}, {
  'id': 2,
  'title': 'Data Analyst',
  'location': 'Bangaluru, India',
  'Salary': 'Rs. 10,00,000'
}, {
  'id': 3,
  'title': 'Frontend Engineer',
  'location': 'Remote'
}, {
  'id': 4,
  'title': 'Backend Engineer',
  'location': 'San Francisco, USA',
  'Salary': '$120,000'
}, {
  'id': 5,
  'title': 'Data Scientist',
  'location': 'London, UK',
  'Salary': '£1,00,000'
}]

app = Flask(__name__)


@app.route("/")
def hello_world():
  return render_template('home.html', jobs=JOBS, company_name='Jovian')

@app.route('/api/jobs')
def list_json():
  return jsonify(JOBS)


if __name__ == '__main__':
  app.run(host='0.0.0.0', debug=True)
