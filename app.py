from flask import Flask, render_template, request
import pickle
import pandas as pd

app = Flask(__name__)

model = pickle.load(open("model.pkl", "rb"))

@app.route('/')
def home():
    return render_template("index.html")

@app.route('/predict', methods=['POST'])
def predict():
    try:
        form_data = request.form

        experience = int(form_data['experience'])
        education = form_data['education']
        jobrole = form_data['jobrole']
        location = form_data['location']
        country = form_data['country']

        input_data = pd.DataFrame({
            'Experience': [experience],
            'Education': [education],
            'JobRole': [jobrole],
            'Location': [location],
            'Country': [country]
        })

        annual_salary = model.predict(input_data)[0]
        monthly_salary = annual_salary / 12

        return render_template(
            "index.html",
            prediction_text=f"Monthly: ${monthly_salary:,.0f} | Annual: ${annual_salary:,.0f}",
            form_data=form_data
        )

    except Exception as e:
        return render_template("index.html", prediction_text=f"Error: {str(e)}")

if __name__ == "__main__":
    app.run(debug=True)