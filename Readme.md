## Calorie Predictor
Calorie Predictor is a machine learning web application that estimates an individual's daily calorie requirements based on personal, physical, activity, and dietary attributes. The application uses an Artificial Neural Network (ANN) trained on health and lifestyle data to generate calorie predictions in real time.

## Features 
1. Predicts daily calorie requirements instantly
2. ANN-based regression model built with PyTorch
3. Real-time predictions through a web interface
4. Input preprocessing using StandardScaler
5. Supports physical activity and dietary habit analysis
6. Simple and user-friendly interface

## Tech Stack
- Python
- Pytorch
- NumPy
- Pandas
- Flask 
- HTML, Taiwind CSS, JavaScript 
- Scikit-learn

## How it works
- Enter personal details such as age, gender, height, weight, and BMI.
- Select activity and dietary preferences.
- Input data is preprocessed using a trained StandardScaler.
- The ANN model analyzes the features.
- Predicted daily calorie requirement is displayed instantly.

## Model Description
* Input Features
    1. Age
    2. Gender
    3. Height
    4. Weight
    5. BMI
    6. Activity-related features
    7. Diet-related features
* Accuracy
    1. Train accuracy - 99% 
    2. R2 score - 0.99
* Neural Network Structure
    1. Input Layer (14 Features)
    2. Hidden Layer (64 Neurons, ReLU)
    3. Hidden Layer (32 Neurons, ReLU)
    4. Output Layer (1 Neuron) 
* Optimizer - torch.optim.Adam(model.parameters(), lr=0.001)
* Loss function - torch.nn.MSELoss()
* Batch size = 32, Epochs = 100

## Project Setup
Clone the repository
```bash
git clone https://github.com/Tanmeiii/calorie-predictor.git
```
Move into the project directory
```bash
cd calorie-predictor
```
Install Dependencies
```bash
pip install -r requirements.txt
```
Run the application
```bash
python app.py
```

## Folder Structure
```bash
CALORIEPREDICTOR/
├── assets/
│   └── diet_calorie_intake.csv      # Dataset
│   └── calorie_predictor_ANN.ipynb  # Actual model                 
|          
├── static/
│   └── script.js 
│   └── style.css
|
├── templates/
│   └── index.html                   # Frontend
│
├── app.py                           # Backend
├── model_loader.py                  # ANN model with same architecture as notebook
├── scaler.pkl      
├── model.pth                        # Weights taken from model with best training results
├── requirements.txt                 
│
└── README.md                 
```

## Author
GitHub: https://github.com/Tanmeiii