# Basic AI Model for Solar Power Potential Estimation

## Project Description

This project, developed during a FTL Ethiopia Python Hackathon , focuses on leveraging Artificial Intelligence to contribute to **SDG 7: Affordable and Clean Energy** and **SDG 13: Climate Action**. We have built a basic AI model to estimate the solar power potential for specific locations based on environmental and geographical data. The goal is to provide a tool that can help individuals, businesses, and potentially governments make more informed decisions about investing in solar energy.

## The Problem

Estimating the amount of solar energy a location can receive is crucial for the effective deployment of solar panels. This potential is influenced by various factors, including geographical position, time of year, and prevailing weather conditions. Accurately predicting this can optimize solar installations and accelerate the adoption of clean energy.

## Our Solution

We developed a Machine Learning model, specifically a **Random Forest Regressor**, to analyze a combination of historical climate data and geographical information to estimate the expected solar irradiance (a measure of solar power potential) at a given point.

While this is a basic prototype, the model has shown promising results in predicting solar potential based on the available data.

## Dataset

The model was trained using the **Climate Change Dataset 2020-2024** from Kaggle, which includes various meteorological and geographical features. To address the limited number of original data points, we employed a basic synthetic data generation technique to augment the dataset and improve the model's training.


## Key Features (Prototype)

Our current prototype demonstrates the core functionality:

* **Data Processing Pipeline:** Includes steps for handling missing data (imputation) and preparing data for the model.
* **Trained AI Model:** A Random Forest Regressor capable of estimating solar potential.
* **Basic Estimation Logic:** The model can take input data and output a solar irradiance estimate.
* ** Simple User Interface:** An interface (to be built using Django) to allow users to input data and view the estimated solar potential.

## Technologies Used

* Python
* pandas (for data handling)
* numpy (for numerical operations)
* scikit-learn (for the AI model and evaluation)
* joblib (for saving/loading the model)
* Django(Website Development)

## Setup and Running the Project



1.  **Clone the Repository:**
    ```bash
    git clone https://github.com/FasikaBelayneh/Basic-AI-Model-for-Solar-Power-Potential-Estimation-.git
    cd Basic-AI-Model-for-Solar-Power-Potential-Estimation-
    ```
2.  **Set up a Python Environment:**
    
    ```bash
    # Using conda
    conda create -n solar_env python=3.x
    conda activate solar_env
    ```
    *(Or using venv)*
    ```bash
    python -m venv venv
    # On Windows
    .\venv\Scripts\activate
    # On macOS/Linux
    source venv/bin/activate
    ```

 **Install Dependencies:**
    ```bash
    pip install pandas numpy scikit-learn joblib [your chosen interface framework, e.g., Django]
    ```
4.  **Obtain the Dataset:**
    The dataset can be Accessed on Kaggle and also a simple synthetic data is generated.
    
5.  **Run the Model Training Script:**
    
    ```bash
    python Solar-Power-Potential-Estimation/Basic-AI-Model-for-Solar-Power-Potential-Estimation.py # Example script name
    ```
    *(Make sure your script saves the model as `solar_potential_model.pkl`)*




## Contributing



If you'd like to contribute to this project, please fork the repository and create a pull request with your suggested changes.



