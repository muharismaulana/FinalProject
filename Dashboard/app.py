from flask import Flask, render_template, request
import pickle
import pandas as pd

app = Flask(__name__)

# predict

@app.route('/', methods=['POST','GET'])
def home():
    return render_template('home.html')

@app.route('/appRecord', methods=['POST','GET'])
def apprecord():
    return render_template('apprecord.html')

@app.route('/credRecord', methods=['POST','GET'])
def crerecord():
    return render_template('credrecord.html')

@app.route('/about', methods=['POST','GET'])
def about():
    return render_template('about.html')


@app.route('/highlight', methods=['POST','GET'])
def highlight():
    return render_template('highlight.html')

@app.route('/predict', methods=['POST','GET'])
def predict():
    return render_template('predict.html')

# result

@app.route('/result', methods=['POST','GET'])
def result():
    if request.method == 'POST':
        input = request.form

        df_predict= pd.DataFrame({
            'CODE_GENDER':[input['gender']],
            'FLAG_OWN_CAR':[input['car']],
            'FLAG_OWN_REALTY':[input['property']],
            'AMT_INCOME_TOTAL':[input['amountIncome']],
            'NAME_INCOME_TYPE':[input['typeIncome']],
            'NAME_EDUCATION_TYPE':[input['education']],
            'NAME_FAMILY_STATUS':[input['family']],
            'NAME_HOUSING_TYPE':[input['housing']],
            'DAYS_BIRTH':[input['age']],
            'FLAG_PHONE':[input['phone']],
            'FLAG_EMAIL':[input['email']]
        })

        prediksi = model.predict_proba(df_predict)[0][1]

        if prediksi>0.099691:
            quality='GOOD'
            textColor = 'green'
        else:
            quality='BAD'
            textColor = 'red'

        return render_template('result.html',data=input, pred=quality, prob="%.2f" % round(prediksi, 2), textPred = textColor)

if __name__ == '__main__':
    filename='C:\\Users\\Aris\\Documents\\Jupyter Purwa\\Final Project\\ModelFinal.sav'
    model=pickle.load(open(filename,'rb'))
    app.run(debug=True)