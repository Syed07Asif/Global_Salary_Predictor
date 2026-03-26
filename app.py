from flask import Flask, render_template, request, make_response
import pickle
import pandas as pd
import os

app = Flask(__name__)

app.config['TEMPLATES_AUTO_RELOAD'] = True
app.config['SEND_FILE_MAX_AGE_DEFAULT'] = 0
model = pickle.load(open("model.pkl", "rb"))

@app.after_request
def add_header(response):
    response.headers["Cache-Control"] = "no-cache, no-store, must-revalidate"
    response.headers["Pragma"] = "no-cache"
    response.headers["Expires"] = "0"
    return response

@app.route('/')
def home():
    return render_template("index.html")

@app.route('/predict', methods=['POST'])
def predict():
    form_data = request.form

    input_data = pd.DataFrame({
        'Experience': [int(form_data['experience'])],
        'Education': [form_data['education']],
        'JobRole': [form_data['jobrole']],
        'Location': [form_data['location']],
        'Country': [form_data['country']]
    })

    annual = model.predict(input_data)[0]
    monthly = annual / 12

    return render_template(
        "index.html",
        prediction_text=f"Monthly: ${monthly:,.0f} | Annual: ${annual:,.0f}",
        form_data=form_data
    )

if __name__ == "__main__":
    app.run(host="0.0.0.0", port=5000, debug=True)