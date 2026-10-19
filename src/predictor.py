import joblib
import pandas as pd

model = joblib.load("./models/ipo_model.pkl")
scaler = joblib.load("./models/scaler.pkl")

features = [
    "Issue_Size(crores)",
    "QIB",
    "HNI",
    "Total",
    "Year",
    "Month"
]

issue_size = float(input("Issue size (in crores): "))
qib = float(input("QIB subscription (x): "))
hni = float(input("HNI subscription (x): "))
total = float(input("Total subscription ratio (x): "))
year = int(input("IPO year (e.g. 2026): "))
month = int(input("IPO month (1-12): "))

new_ipo = pd.DataFrame([{
    "Issue_Size(crores)": issue_size,
    "QIB": qib,
    "HNI": hni,
    "Total": total,
    "Year": year,
    "Month": month
}])

new_ipo = new_ipo[features]

new_ipo_scaled = scaler.transform(new_ipo)

predicted_gain = model.predict(new_ipo_scaled)[0]

print(f"Predicted gains: {predicted_gain:.2f} %")