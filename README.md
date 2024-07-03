
# Men's T20 International Cricket Score Predictor

This project aims to predict scores in Men's T20 International cricket matches using machine learning models. Different factors are used to predict the score lincluding batting team, bowling team, current score, last 5 over score, current run rate, ball left, wicket left and venue. The final model is deployed using a Streamlit application, providing an accessible interface for score predictions.

## Steps Involved
- Data Collection (Kaggle)
- Data Preparation( takes 5-6 hours)
- Data Preprocessing
- Model Selection and Training
- Model Evaluation
- Pipeline Creation
- Saving the model using pickle
- Created Streamlit app
- Uploaded to Github



## Dependencies

- pandas
- numpy
- scikit-learn 1.3.2
- xgboost 1.6.2
- streamlit
- pickle
## Installation

Install all project requirements 

```bash
  pip install -r requirements.txt
```
    
Run the command to see the demo

```bash
  streamlit run app.py
```
## Authors

- [@Debopam-Pritam2014](https://www.github.com/Debopam-Pritam2014)


![Logo](https://miro.medium.com/v2/resize:fit:300/1*k1JyI844F7VW2UWkIxTS6Q.jpeg)

## Features

- **High Accuracy:** Achieves 99% R² score on training data and 98% R² score on testing data.
- **Comprehensive Data Handling:** Converts detailed ball-by-ball data from YAML files into Pandas DataFrames.
- **Effective Preprocessing:** Utilizes ColumnTransformer for one-hot encoding of categorical variables and MinMaxScaler for scaling numerical features.
- **Model Selection:** Compares multiple machine learning models, with XGBoost being the best performer.
- **Pipeline Integration:** Combines preprocessing steps and the XGBoost model into a single pipeline for streamlined processing.
- **Model Saving:** Saves the trained model and preprocessing pipeline using pickle for easy reuse and deployment.
- **User-Friendly Deployment:** Deploys the model using a Streamlit application, providing a simple interface for making score predictions.



### Challenges I Faced and How I Overcame Them

- **Data Format:** Working with data in YAML format presented a challenge due to its complexity and non-tabular structure. Implemented a script to parse and convert YAML files into a structured Pandas DataFrame, ensuring data was ready for preprocessing and modeling.

- **Data Extraction Time:** Extracting and processing the required data from YAML files took significantly longer than anticipated. Sequentially performed steps to get the required data for model building.

- **Model Selection:** Experimenting with multiple machine learning models to find the best performer was time-consuming and resource-intensive. Implemented a systematic approach to evaluate and compare models based on performance metrics such as R² score, focusing on XGBoost due to its superior performance.

- **Deployment Complexity:** Deploying the machine learning model into a user-friendly application required integrating multiple components and ensuring smooth functionality. Developed a Streamlit application that encapsulated the model and provided an intuitive interface for users to input data and receive predictions, simplifying the deployment process.

- **Data Preprocessing:** Handling categorical variables and numerical scaling posed challenges in ensuring data consistency and model readiness. Utilized ColumnTransformer for categorical encoding and MinMaxScaler for numerical scaling within a pipeline, streamlining preprocessing steps and enhancing model robustness.

## Acknowledgements

 - [Dataset link kaggle](https://www.kaggle.com/datasets/veeralakrishna/cricsheet-a-retrosheet-for-cricket?select=t20s)
 - [YAML to Pandas Dataframe](https://stackoverflow.com/questions/54259207/how-to-denormalize-yaml-for-pandas-dataframe)


## Feedback

If you have any feedback, please reach out to me at debopamdeycse19@gmail.com

