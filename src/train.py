from sklearn.linear_model import LinearRegression
from sklearn.preprocessing import StandardScaler
from sklearn.metrics import mean_absolute_error, mean_squared_error, r2_score
from sklearn.model_selection import train_test_split
import pandas as pd
import joblib

df = pd.read_excel("./data/ipo_cleaned.xlsx")

# print(df.shape)

x = df.drop(columns = ['Date', 'List Price', 'Listing Gain', "Day", "Month","RII","Offer Price",])
y = df['Listing Gain']

# print(x.head(4))
# print(x.shape)
# print(y.shape)

#splitting data 80-20
X_train, X_test, y_train, y_test = train_test_split(
    x, y,
    test_size=0.20,
    random_state=42,
)

scaler = StandardScaler()
X_train_scaled = scaler.fit_transform(X_train)
X_test_scaled = scaler.transform(X_test)


model = LinearRegression()
model.fit(X_train_scaled, y_train)

#saving the models and scaller to pkl(serialised[byte stream])
joblib.dump(model, "./models/ipo_model.pkl")
joblib.dump(scaler, "./models/scaler.pkl")

print("Training completed and model saved to Models/ipo_model")


y_pred = model.predict(X_test_scaled)

print("Model predictions complete")

#calc the errors

mae = mean_absolute_error(y_test, y_pred)
mse = mean_squared_error(y_test, y_pred)
r2 = r2_score(y_test, y_pred)

print(f"mae : {mae:.2f}")
print(f"mse : {mse:.2f}")
print(f"r2 : {r2:.2f}")

feature_names = [
    "Issue_Size(crores)",
    "QIB",
    "HNI",
    "Total",   
    "Year",
]

importance = pd.DataFrame({
    "Features": feature_names,
    "Coefficients": model.coef_
})

importance['Absolute Coefficients'] = importance["Coefficients"].abs()

importance = importance.sort_values(
    by="Absolute Coefficients",
    ascending=False
)

print(importance.to_string(index=False))