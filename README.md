# Least Squares Analysis

## Authors:

1. Carlos Andres Gallego Montoya
2. Gustavo Adolfo Perez Perez
3. Sebastian Pedraza Rendon

## Introduction:

This project is a collaborative effort aimed at applying numerical analysis techniques, specifically the **Least Squares Method**, to real-world problems. The project consists of three main components:

1. **Theoretical Foundation**: An in-depth explanation of the Least Squares Method, including its mathematical derivation and practical applications.
2. **Real-world Examples**: Application of the method to two scenarios:
   - **Plant Growth**: Modeling plant height based on watering frequency.
   - **Air Quality**: Analyzing PM2.5 pollution levels over time in Medellín, Colombia.
3. **Implementation and Analysis**: 
   - A Python implementation of the Least Squares Method to analyze air quality data from the Belén neighborhood.
   - Visualization of the data and regression models.
   - Evaluation of model performance using MSE and RMSE, and a discussion of results, limitations, and improvements.

This repository combines theoretical insights with practical coding to demonstrate the power of numerical methods in solving real-world problems.

## Project Structure

```
├─ report
    ├─ Gallego Montoya- Pedraza Rendón- Pérez Pérez.pdf
    └─ Gallego Montoya- Pedraza Rendón- Pérez Pérez.tex
├─ src
    ├─ data
        └─ belén,-medellín-air-quality.py
    ├─ method
        └─ least_squares_analysis.py
    └─ results
        ├─ air_quality_least_squares.pdf
        └─ air_quality_least_squares.tex
├─ .gitignore
├─ README.md
└─ requirements.txt
```

- `report/`: Contains the report with the final PDF file about the theory about the assignments given.
- `requirements.txt`: Contains the dependencies needed to run the project.
- `src/method/`: Contains the Python script implementing Least Squares Method.

## Report

Inside the `report/` directory, you will find the PDF file and the native .tex file for latex, that contain the report with the final PDF file about the assignments given.

1. **`Gallego Montoya- Pedraza Rendón- Pérez Pérez.pdf`**
2. **`Gallego Montoya- Pedraza Rendón- Pérez Pérez.tex`**

## Getting Started

### Prerequisites

- **Python 3.8+** (It's recommended to have at least Python 3.8)
- **git** (if you are pulling the project from a Git repository)

### Setting Up a Virtual Environment

Although a virtual environment is not included in the repository (as it's ignored in `.gitignore`), you can easily create one. This ensures that all dependencies are installed in an isolated environment, preventing version conflicts with other projects.

1. **Create the virtual environment:**
   
   ```bash
   python3 -m venv venv
   ```
   This command creates a new virtual environment named venv in the project root directory.

2. **Activate the virtual environment:**

    On macOS/Linux:
    ```bash
    source venv/bin/activate
    ```
    On Windows:
    ```bash
    venv\Scripts\activate
    ```
    After this, you should see the environment name (e.g., (venv)) at the beginning of your terminal prompt, indicating that you are working inside the virtual environment.

### Installing Dependencies

With the virtual environment activated, run:
```bash
    pip install -r requirements.txt
```
This will install all the necessary dependencies (e.g., numpy, scipy) required to run the code.

### Running the Method

Inside the `src/method` directory, you will find the Python file that contain the code for Least Squares Method.

1. **`least_squares_analysis.py`**

You can run them directly, for example:
```bash
    python src/methods/least_squares_analysis.py
```

### Results about tests
Inside the `src/results` directory, the document provides a detailed analysis of air quality data using the Least Squares Method. Key aspects covered in the document include:

1. **Model Interpretation**: The linear regression model derived from PM2.5 concentration data is explained, with coefficients and error metrics (MSE and RMSE) discussed in detail.
2. **Quality of Fit**: A discussion on the limitations of the linear model, considering the variability in the dataset, and the potential for improved accuracy using alternative approaches.
3. **Visualization**: A clear graphical representation of the observed data points alongside the regression line, with annotations for key metrics.
4. **Recommendations**: Suggestions for enhancing the analysis, such as incorporating additional variables or exploring non-linear models.

The document combines mathematical rigor and practical application to demonstrate how numerical methods can be applied to environmental data analysis.