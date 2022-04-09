from flask import Flask , render_template , request , redirect, flash,url_for
import pickle
import numpy as np


app = Flask(__name__)

filename = 'cancer_prediction_pickle'
model = pickle.load(open(filename,'rb'))

@app.route('/')
def home():
    return render_template('index.html')

@app.route('/predict',methods=['GET','POST'])
def predict():
    if request.method == "POST":
        radius_mean = float(request.form['radius_mean'])
        perimeter_mean  = float(request.form['perimeter_mean'])
        area_mean = float(request.form['area_mean'])
        concavity_mean = float(request.form['concavity_mean'])
        concave_points_mean = float(request.form['concave_points_mean'])
        radius_worst = float(request.form['radius_worst'])
        perimeter_worst = float(request.form['perimeter_worst'])
        area_worst = float(request.form['area_worst'])
        concavity_worst = float(request.form['concavity_worst'])
        concave_points_worst = float(request.form['concave_points_worst'])
        # Validation Checkpoint
        if (radius_mean < 4 or radius_mean > 28 or
        perimeter_mean < 43 or perimeter_mean > 190 or
        area_mean < 143 or area_mean > 2550 or
        concavity_mean < 0 or concavity_mean > 0.5 or
        concave_points_mean < 0 or concave_points_mean > 0.3 or     
        radius_worst < 7 or radius_worst > 36 or    
        perimeter_worst < 50 or perimeter_worst > 252 or   
        area_worst < 185 or area_worst > 4254 or   
        concavity_mean < 0 or concavity_mean > 1.25 or   
        concave_points_worst < 0 or concave_points_worst > 0.3 
        ):
            flash('Invalid password provided', 'warning')
            return render_template('index.html')
        
        data = np.array([[radius_mean,perimeter_mean,area_mean ,concavity_mean,concave_points_mean,radius_worst,perimeter_worst, area_worst,concavity_worst,concave_points_worst]])
        my_prediction = model.predict(data)
        # return template after clicking analyze button.
        return render_template('index.html',
        radius_mean=str(radius_mean),
        perimeter_mean = str(perimeter_mean),
        area_mean = str(area_mean),
        concavity_mean = str(concavity_mean),
        concave_points_mean = str( concave_points_mean),
        radius_worst = str(radius_worst),
        perimeter_worst = str(perimeter_worst),
        area_worst = str(area_worst),
        concavity_worst = str(concavity_worst),
        concave_points_worst = str(concave_points_worst),
        prediction=my_prediction)

        


if __name__ == '__main__':
    app.secret_key = '1234'
    app.run(debug=True)