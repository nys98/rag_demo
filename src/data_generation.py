import random
import pandas as pd

def generate_data(n=200):
    sites = ["New York", "Chicago", "Dallas", "LA", "Boston", "Seattle", "Denver", "Buffalo", "Tampa", "Atlanta"]
    issues = ["oil degradation", "coolant leak", "motor vibration", "fuel contamination", "Cloudy oil", "High Precipitates in Fuel", "oil becoming worse quality"]
    repairs = [
        "low repair frequency",
        "moderate repair frequency",
        "high repair costs",
        "high repair frequency"
    ]

    rows = []

    for i in range(n):
        rows.append({
            "asset_id": f"GEN{i:03d}",
            "site": random.choice(sites),
            "health_score": round(random.uniform(0, 2), 2),
            "issue": random.choice(issues),
            "repairs": random.choice(repairs)
        })

    return pd.DataFrame(rows)


if __name__ == "__main__":
    df = generate_data()
    df.to_csv("data/synthetic_generator_data.csv", index=False)