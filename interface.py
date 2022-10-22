from flask import Flask,jsonify,render_template,request
from project_app.utils import medical
import config

app=Flask(__name__)
@app.route('/')
def sachin():
    return "hello"
@app.route('/result')
def result():
    Input=request.form
    print('input',Input)
    age=Input['age']
    sex=Input['sex']
    bmi=Input['bmi']
    children=Input['children']
    smoker=Input['smoker']
    region=Input['region']
    med=medical(age,sex,bmi,children,smoker,region)
    charges=med.get_predicted()
    print(charges)
    return jsonify({'msg':f'predicted charges is {charges}'})
if __name__=="__main__":
    app.run(host="0.0.0.0",port=config.PORT_NUMBER,debug=False)