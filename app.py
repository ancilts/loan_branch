from flask import Flask,render_template,request
import pickle

app = Flask(__name__)

@app.route('/')
def hello():
    return render_template('index.html')

@app.route('/prediction', methods = ['POST'])
def predict():
    if request.method == 'POST':
        Yearly_Income = float(request.form['Yearly_Income'])
        Total_Unpaid_CL = float(request.form['Total_Unpaid_CL'])
        Unpaid_Amount = float(request.form['Unpaid_Amount'])
        Account_Open = float(request.form['Account_Open'])
        Debt_to_Income = float(request.form['Debt_to_Income'])
        Lend_Amount = float(request.form['Lend_Amount'])
        Sub_GGGrade = float(request.form['Sub_GGGrade'])

        features = [[Yearly_Income, Total_Unpaid_CL, Unpaid_Amount, Account_Open, Debt_to_Income, Lend_Amount, Sub_GGGrade]]
        print(features)
        model = pickle.load(open('model.pkl', 'rb'))
            
        prediction = model.predict(features)
        print(prediction)
        
        defaulter_mapping = {0: 'Non-Defaulter', 1: 'Defaulter'}
        predicted_result = defaulter_mapping[prediction[0]]

    return render_template("prediction.html", result=predicted_result)


if __name__ == '__main__':
    app.run()