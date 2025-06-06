# 🤖DIABETES CLASSIFIER

```python
NextJS + FastAPI + Sklearn
```

![Banner](/assets/wallpaper.png)

## 🍭OVERVIEW

Through a web-based graphical interface, the program allows users to input diagnostic measurements and, using a pre-trained machine learning model, determines whether they are likely to have diabetes or not.

## 👾MACHINE LEARNING MODEL

The `machine learning model` is trained using a dataset from [Kaggle](https://www.kaggle.com/datasets/mathchi/diabetes-data-set). This dataset is originally from the National Institute of Diabetes and Digestive and Kidney Diseases.

**Measurements used:**

- Pregnancies: Number of times pregnant
- Glucose: Plasma glucose concentration a 2 hours in an oral glucose tolerance test
- BloodPressure: Diastolic blood pressure (mm Hg)
- SkinThickness: Triceps skin fold thickness (mm)
- Insulin: 2-Hour serum insulin (mu U/ml)
- BMI: Body mass index (weight in kg/(height in m)^2)
- DiabetesPedigreeFunction: Diabetes pedigree function
- Age: Age (years)

**The output can be `1` (likely to have diabetes) or `0` (not likely to have diabetes)**

### ⚙️IMPLEMENTATION

The program uses `pandas` library to load and handle the diabetes dataset, and `scikit-learn (sklearn)` to train the machine learning model. Specifically, it uses the **Random Forest algorithm** to predict whether a person is likely to have diabetes. The script uses _cross-validation strategy, and performs a randomized search_ over several hyperparameter combinations to find the best model settings. It evaluates the model using the F1-macro. Once the best configuration is found, it retrains the Random Forest model on the full dataset using these optimized parameters. Finally, the trained model is saved to a .pkl file using the `joblib` library.

## 🚀GUI (GRAPHICAL USER INTERFACE) + API

![WEB GUI PICTURE](/assets/preview.png)

The web interface is built using the **JavaScript** framework `NextJS` along with the `Tailwind CSS` framework for styling. The API, which handles communication between the user interface and the machine learning model, is developed using `FastAPI` — a modern and high-performance **Python** web framework.