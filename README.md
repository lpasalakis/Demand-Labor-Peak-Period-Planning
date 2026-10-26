# Demand, Labor, and Peak-Period Planning

## Project overview

This project explores how hourly demand patterns can inform staffing and
peak-period planning in a quick-service restaurant. **All data is
synthetic practice data**, not records from a real employer.

## Business question

When does demand peak, and where might staffing schedules need a closer
review to balance service performance and labor efficiency?

## Dataset

-   File: `data/hourly_operations_synthetic.csv`
-   12 weeks of hourly observations, 10:00--23:00, 1,176 rows
-   Includes orders, sales, scheduled/actual staff, orders per labor
    hour, simulated service time, late-order rate, and estimated waste
    rate.

## Tools

Python, pandas, NumPy, Matplotlib. CSV summaries can also be opened in
Excel or imported into Tableau.

## Method

1.  Summarize orders and service indicators by hour and weekday.
2.  Define the top quartile of hourly orders as high-demand periods.
3.  Create an illustrative staffing proxy: `ceil(orders / 12)`, with a
    minimum of two staff.
4.  Compare actual staff with the proxy. A negative gap means actual
    staffing is below this simple proxy, not proof that a shift was
    understaffed.
5.  Develop recommendations and document limitations.

## Example findings from the generated sample

-   Average demand: **23.4 orders/hour**.
-   Three highest average-demand hours: **19:00, 18:00, 13:00**.
-   Three highest average-demand days: **Saturday, Friday, Sunday**.
-   Average service time: **3.24 minutes**.
-   **0.8%** of periods fall below the simple staffing proxy; this is
    **0.0%** during top-quartile demand periods and **1.0%** during
    other periods.

These findings describe only this generated dataset. Do not present them
as actual business results.

## Recommendations to test

1.  Review staffing and prep readiness before recurring high-demand
    windows.
2.  Test staggered shift starts so coverage overlaps more near
    lunch/dinner peaks and less during slower periods.
3.  Monitor orders per labor hour alongside service time and late-order
    rate; do not optimize labor productivity in isolation.
4.  Validate the staffing proxy against local standards, order
    complexity, delivery mix, breaks, and actual task requirements.
5.  Compare similar weekdays over several weeks before and after any
    schedule change, accounting for promotions, holidays, and unusual
    events.

## Limitations

-   Synthetic data is not representative of a particular restaurant.
-   Service, late-order, and waste measures are simulated.
-   One staff per 12 orders is an illustrative assumption, not an
    industry standard or validated staffing requirement.
-   Correlation does not establish causation.
-   No actual labor savings or real-world impact is claimed.

## Run it

Install dependencies with
`python -m pip install pandas numpy matplotlib`, then run
`python analysis.py` from this folder.

## Portfolio description

**Demand, Labor, and Peak-Period Planning (Python, pandas, data
visualization)** --- Analyzed 12 weeks of synthetic hourly restaurant
operations data to identify demand peaks, compare staffing coverage with
an explicit planning proxy, and develop testable recommendations for
shift staggering, prep readiness, and service-level monitoring.
