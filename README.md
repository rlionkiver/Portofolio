# EDA and Modeling Project

This project is designed to perform exploratory data analysis (EDA), feature engineering, and model training using a dataset related to client and pricing information.

## Project Structure

- **data/**
  - **raw/**: Contains the original datasets.
    - `clean_data_after_eda.csv`: The cleaned dataset after EDA.
    - `client_data.csv`: Client-related data for analysis and modeling.
    - `price_data.csv`: Pricing information relevant to the analysis.
  - **processed/**: Intended for storing processed datasets after feature engineering.

- **notebooks/**: Contains Jupyter notebooks for analysis.
  - `EDA_and_Modeling.ipynb`: A notebook for performing EDA, feature engineering, and model training.

- **src/**: Contains source code for the project.
  - `__init__.py`: Marks the directory as a Python package.
  - `utils.py`: Utility functions for loading data and common tasks.
  - `feature_engineering.py`: Contains the `create_features` function for feature creation.
  - `modeling.py`: Contains functions for training and evaluating machine learning models.

- **requirements.txt**: Lists the dependencies required for the project.

## Setup Instructions

1. Clone the repository to your local machine.
2. Navigate to the project directory.
3. Install the required dependencies using:
   ```
   pip install -r requirements.txt
   ```

## Usage Guidelines

- Use the Jupyter notebook `EDA_and_Modeling.ipynb` for performing EDA and model training.
- Modify the source code in the `src/` directory as needed for custom feature engineering and modeling approaches.
- Processed datasets can be saved in the `data/processed/` directory after feature engineering.

## License

This project is licensed under the MIT License.