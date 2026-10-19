# IPO Listing Gain Predictor

A small Python project that trains a linear regression model to estimate an IPO's listing gain from its issue size, subscription figures, and listing date.

> **Note:** This is an experimental prediction project, not financial advice. Predictions are estimates based on the available historical data and should not be used as the sole basis for investment decisions.

## Project contents

```text
data/
  ipo.xlsx                 # Source IPO data
  ipo_cleaned.xlsx         # Cleaned data with date features
models/
  ipo_model.pkl            # Trained regression model
  scaler.pkl               # Feature scaler used by the model
src/
  data_preprocessing.py    # Cleans source data
  feature_engineering.py   # Extracts year, month, and day from dates
  train.py                 # Trains and evaluates the model
  predictor.py             # Prompts for an IPO and predicts its gain
```

The repository also contains `ipo_model1.pkl` and `scaler1.pkl`; the current training and prediction scripts use `ipo_model.pkl` and `scaler.pkl`.

## Requirements

- Python 3
- `pandas`
- `openpyxl`
- `scikit-learn`
- `joblib`
- `numpy`

Install the dependencies in your active Python environment:

```bash
python -m pip install pandas openpyxl scikit-learn joblib numpy
```

## Prepare and train

Run these commands from the project root so the scripts can find the `data/` and `models/` directories:

```bash
python src/data_preprocessing.py
python src/feature_engineering.py
python src/train.py
```

The preprocessing script reads `data/ipo.xlsx`, removes unused columns, fills missing subscription values with their column medians, and drops rows without a list price or listing gain. Feature engineering adds `Year`, `Month`, and `Day` based on the `Date` column. Training uses the cleaned workbook, fits a `StandardScaler` and `LinearRegression` model, and saves the model and scaler under `models/`. It also prints MAE, MSE, R², and the absolute model coefficients.

The training target is `Listing Gain`. The predictor accepts these inputs:

| Input | Meaning |
| --- | --- |
| Issue size (in crores) | IPO issue size |
| QIB subscription (x) | Qualified institutional buyer subscription multiple |
| HNI subscription (x) | High-net-worth individual subscription multiple |
| Total subscription ratio (x) | Overall subscription multiple |
| IPO year | Calendar year of the IPO |
| IPO month | Month number from 1 to 12 |

## Make a prediction

From the project root, run:

```bash
python src/predictor.py
```

Enter the requested values when prompted. The script prints the estimated listing gain as a percentage. The corresponding trained model and scaler must exist in `models/`; run the preparation and training steps first if they are missing or you want to retrain.
