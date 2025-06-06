from fastapi import FastAPI
from fastapi.middleware.cors import CORSMiddleware
from pydantic import BaseModel, Field

import joblib
import numpy

model = joblib.load("../mlmodel/ml_model_random_forest_diabetes.pkl")

app = FastAPI()

app.add_middleware(
    CORSMiddleware,
    allow_origins="*",
    allow_credentials=True,
    allow_methods=["*"],
    allow_headers=["*"],
)


class BodyRequest(BaseModel):
    Pregnancies: int = Field(title="Number of times pregnant")
    Glucose: int = Field(
        title="Plasma glucose concentration a 2 hours in an oral glucose tolerance test"
    )
    BloodPressure: int = Field(title="Diastolic blood pressure (mm Hg)")
    SkinThickness: int = Field(title="Triceps skin fold thickness (mm)")
    Insulin: int = Field(title="2-Hour serum insulin (mu U/ml)")
    BMI: float = Field(title="Body mass index (weight in kg/(height in m)^2)")
    DiabetesPedigreeFunction: float = Field(title="Diabetes pedigree function")
    Age: int = Field(gt=0, title="Age (years)")


@app.post("/predict")
def prediction(data: BodyRequest):
    numpy_data_array = numpy.array(
        [
            [
                data.Pregnancies,
                data.Glucose,
                data.BloodPressure,
                data.SkinThickness,
                data.Insulin,
                data.BMI,
                data.DiabetesPedigreeFunction,
                data.Age,
            ]
        ]
    )

    prediction = model.predict(numpy_data_array)

    return {"prediction": int(prediction[0])}

@app.get("/")
def connection():
    return {"connection": "connected"}