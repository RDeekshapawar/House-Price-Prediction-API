# Bengaluru House Price Prediction API

A Flask REST API scaffold for serving a trained Bengaluru house-price model.

## Important: add your trained model

This ZIP does **not** include your existing trained model because it was not attached to this chat. Copy your trained model file into this folder and name it:

`house_price_model.joblib`

If your model has another filename, either rename it or set the `MODEL_PATH` environment variable.

## Expected input schema

The API currently sends these columns to the model:

- `location` (lowercase string)
- `total_sqft` (number)
- `bath` (number)
- `bhk` (number of bedrooms)

This matches a common Bengaluru house-price dataset workflow. Your saved model must have been trained to accept these exact feature names and this preprocessing. If you trained with `bedrooms` instead of `bhk`, or used a preprocessing pipeline, adapt `app.py` accordingly.

## Run locally on macOS

```bash
cd house_price_prediction_api
python3 -m venv .venv
source .venv/bin/activate
python -m pip install -r requirements.txt
python app.py
```

Open:
- http://127.0.0.1:5000/
- http://127.0.0.1:5000/health

Test a prediction in a second terminal:

```bash
curl -X POST http://127.0.0.1:5000/predict \
  -H "Content-Type: application/json" \
  -d '{"location":"Whitefield","total_sqft":1200,"bedrooms":2,"bath":2}'
```

## Deploy on Render

1. Push this folder and your model file to a GitHub repository.
2. In Render, choose **New + → Web Service** and connect the repository.
3. Build command: `pip install -r requirements.txt`
4. Start command: `gunicorn app:app`
5. Deploy and check `https://YOUR-SERVICE.onrender.com/health`.

The included `render.yaml` can also be used as a Render Blueprint configuration.

## Model compatibility

The pinned scikit-learn version is a starting point, not a guarantee. Pick the same scikit-learn version used when saving the model whenever possible. If the model was trained using another version, re-export it in a compatible environment or update the dependency pin. Do not load joblib/pickle model files from untrusted sources.
