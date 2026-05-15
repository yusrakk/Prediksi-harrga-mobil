import joblib
import pickle

# Load model dan extract feature names
model = joblib.load('car_price_prediction_model.joblib')
model_columns = model.feature_names_in_

print("Model features:")
print(model_columns)
print(f"\nTotal: {len(model_columns)} features")

# Save ke pkl
pickle.dump(model_columns, open('model_columns.pkl', 'wb'))
print("\nmodel_columns.pkl updated!")
