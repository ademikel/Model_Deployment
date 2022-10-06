import uvicorn
from fastapi import FastAPI as API

app = API()

@app.get('/')
def index():
  return {'message' : 'Hello, Mike'}

@app.get('/Welcome')
def get_name(name: str):
  return {f'Welcome To My First Deployment Project: {name}'}

if __name__ == '__main__':
  uvicorn.run(app, host = '127.0.0.1', port = 8000)
# uvicorn main:app --reload