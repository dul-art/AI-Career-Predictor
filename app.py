from flask import Flask, render_template, request
import pickle


app = Flask(__name__)


model = pickle.load(open("career_model.pkl","rb"))
print("Model loaded")


career_encoder = pickle.load(open("career_encoder.pkl","rb"))
print("Encoder loaded")

print("Encoder classes:", career_encoder.classes_)
@app.route("/")
def home():
    return render_template("index.html")


@app.route("/predict", methods=["POST"])
def predict():

    # get values from HTML form
    python_skill = int(request.form["Python"])
    java = int(request.form["Java"])
    sql = int(request.form["SQL"])
    communication = int(request.form["Communication"])
    leadership = int(request.form["Leadership"])
    mathematics = int(request.form["Mathematics"])
    experience = int(request.form["Experience"])
    education = int(request.form["Education"])


    # create model input
    data = [[
        python_skill,
        java,
        sql,
        communication,
        leadership,
        mathematics,
        experience,
        education
    ]]


    prediction_number = model.predict(data)[0]

    print("Prediction number:", prediction_number)


    career_names = {
    0:"Data Scientist",
    1:"Network Engineer",
    2:"Software Engineer",
    3:"AI Engineer",
    4:"Cyber Security Analyst",
    5:"Cloud Engineer",
    6:"Data Analyst"
}
    prediction = career_names[int(prediction_number)]


    print("Prediction career:", prediction)


    return render_template(
        "result.html",
        career=prediction
    )




if __name__ == "__main__":
    app.run(host="0.0.0.0", port=10000)