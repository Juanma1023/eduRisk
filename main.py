from preprocessing import load_data
from metrics import compute_metrics
from risk_model import compute_risk
from alerts import generate_alerts

df = load_data("sample_edurisk_1000.csv")
df = compute_metrics(df)
df = compute_risk(df)
df = generate_alerts(df)

print(df)
