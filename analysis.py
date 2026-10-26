from pathlib import Path
import numpy as np
import pandas as pd
import matplotlib.pyplot as plt

ROOT = Path(__file__).resolve().parent
DATA = ROOT / "data" / "hourly_operations_synthetic.csv"
OUT = ROOT / "outputs"
OUT.mkdir(exist_ok=True)

df = pd.read_csv(DATA)
print(f"Rows: {len(df):,}")
print("Missing values by column:")
print(df.isna().sum().to_string())

# Practice assumption only; replace with validated local operating standards for real use.
ORDERS_PER_STAFF_PROXY = 12
MIN_STAFF_PROXY = 2
df["recommended_staff_proxy"] = np.ceil(df["orders"] / ORDERS_PER_STAFF_PROXY).astype(int).clip(lower=MIN_STAFF_PROXY)
df["staff_gap"] = df["actual_staff"] - df["recommended_staff_proxy"]
df["peak_flag"] = df["orders"] >= df["orders"].quantile(0.75)

hourly = df.groupby("hour", as_index=False).agg(
    avg_orders=("orders", "mean"), avg_sales_usd=("sales_usd", "mean"),
    avg_actual_staff=("actual_staff", "mean"),
    avg_service_time_min=("avg_service_time_min", "mean"),
    avg_late_order_rate=("late_order_rate", "mean"),
    below_proxy_share=("staff_gap", lambda x: (x < 0).mean()))
hourly.to_csv(OUT / "hourly_summary.csv", index=False)

weekday = df.groupby("day_of_week", as_index=False).agg(
    avg_orders=("orders", "mean"), avg_sales_usd=("sales_usd", "mean"),
    avg_actual_staff=("actual_staff", "mean"),
    avg_service_time_min=("avg_service_time_min", "mean"),
    avg_late_order_rate=("late_order_rate", "mean"),
    below_proxy_share=("staff_gap", lambda x: (x < 0).mean()))
order = ["Monday","Tuesday","Wednesday","Thursday","Friday","Saturday","Sunday"]
weekday["day_of_week"] = pd.Categorical(weekday["day_of_week"], categories=order, ordered=True)
weekday = weekday.sort_values("day_of_week")
weekday.to_csv(OUT / "day_of_week_summary.csv", index=False)

peak = df.groupby("peak_flag", as_index=False).agg(
    periods=("orders", "size"), avg_orders=("orders", "mean"),
    avg_actual_staff=("actual_staff", "mean"),
    avg_service_time_min=("avg_service_time_min", "mean"),
    avg_late_order_rate=("late_order_rate", "mean"),
    below_proxy_share=("staff_gap", lambda x: (x < 0).mean()))
peak["period_type"] = peak["peak_flag"].map({True:"Top-quartile demand periods",False:"Other periods"})
peak.to_csv(OUT / "peak_vs_nonpeak_summary.csv", index=False)

plt.figure(figsize=(9,5))
plt.plot(hourly.hour, hourly.avg_orders, marker="o")
plt.xticks(range(10,24)); plt.xlabel("Hour"); plt.ylabel("Average orders per hour")
plt.title("Average Hourly Demand — Synthetic Practice Data"); plt.grid(alpha=.25); plt.tight_layout()
plt.savefig(OUT / "hourly_demand.png", dpi=150); plt.close()

plt.figure(figsize=(9,5))
plt.plot(hourly.hour, hourly.avg_actual_staff, marker="o", label="Average actual staff")
plt.plot(hourly.hour, np.ceil(hourly.avg_orders/ORDERS_PER_STAFF_PROXY), marker="s", label="Simple staffing proxy")
plt.xticks(range(10,24)); plt.xlabel("Hour"); plt.ylabel("Staff / proxy")
plt.title("Staffing Coverage Proxy by Hour — Synthetic Data"); plt.legend(); plt.grid(alpha=.25); plt.tight_layout()
plt.savefig(OUT / "staffing_coverage.png", dpi=150); plt.close()
print("Done. Reminder: the data is synthetic and the staffing proxy is only an illustrative assumption.")
