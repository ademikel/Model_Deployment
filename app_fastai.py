import uvicorn as uv
from fastapi import FastAPI as API
from heart import heart
import pickle as pkl

app = API()
pkl_in = open('Heart_Classfier.pkl', 'rb')
clf = pkl.load(pkl_in)

@app.get('/')
def index():
  return {'message' : 'Hello, Mike'}

@app.get('/welcome')
def get_name(name: str):
  return {f'Welcome To My First Deployment Project: {name}'}

@app.post('/predict')
def predict_heart_disease(data:heart):
  data = data.dict()
  print(data)
  print('-Predict Heart Disease-')

  age = data['age']
  sex = data['sex']
  cp = data['cp']
  trestbps = data['trestbps']
  chol = data['chol']
  fbs = data['fbs']
  restecg = data['restecg']
  thalach = data['thalach']
  exang = data['exang']
  oldpeak = data['oldpeak']
  slope = data['slope']
  ca = data['ca']
  thal = data['thal']

  prediction = clf.predict([[age, sex, cp, trestbps, chol, fbs, restecg, thalach, exang, oldpeak, slope, ca, thal]])

  if (prediction[0] > 0.5):
    prediction = 'Heart Disease'
  else:
    prediction = 'No Heart Disease'

  return {'prediction': prediction}

if __name__ == '__main__':
  uv.run(app, host = '127.0.0.1', port = 8000)
# uvicorn app_fastai:app --reload