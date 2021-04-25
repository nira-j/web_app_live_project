from flask import Flask
from flask.templating import render_template
from flask import request
import pandas as pd

app=Flask("myapp")

@app.route("/")
def home():
    return render_template("index.html")

@app.route("/out", methods=['POST'])
def output():
    req_value = request.form.get("xl_data")
    ds = pd.read_excel("emp_salary.xlsx")
    ds['salary'] = ds['salary'] + int(req_value)
    output = 'C:\\Users\\niraj\\Desktop\\web_app_live_project\\output.xlsx'
    ds.to_excel(output)

    stat="Data has been updated and saved directory C:/Users/niraj/Desktop/web_app_live_project"

    return render_template("index.html", status=stat )

app.run(debug=True)