"""
LISWA - Lab Instrument Service & Warranty Analytics
Simulated service ticket dataset generator.

Schema:
- ticket_id
- instrument_type
- region
- issue_category
- open_date
- close_date
- sla_target_hours
- actual_resolution_hours
- engineer_id
- warranty_status
- repeat_ticket
- cost
- sla_breached (derived)
"""

import numpy as np
import pandas as pd
from faker import Faker
from datetime import timedelta

fake = Faker()
np.random.seed(42)

N = 2000

instrument_types = ["Mass Spectrometer", "Sequencer", "PCR Analyzer", "Chromatograph", "Microscope"]
# Mass Spec and Sequencer are complex/specialized -> longer repair, more parts delays
instrument_weights = [0.25, 0.20, 0.25, 0.20, 0.10]

regions = ["North America", "Europe", "APAC", "Latin America", "India"]
# India and Latin America simulate regional understaffing -> worse SLA performance
region_weights = [0.30, 0.25, 0.20, 0.10, 0.15]

issue_categories = ["Hardware", "Software", "Calibration"]
issue_weights = [0.55, 0.25, 0.20]

warranty_statuses = ["In-Warranty", "Out-of-Warranty"]

sla_target_map = {
    "Hardware": 48,
    "Software": 24,
    "Calibration": 72,
}

# base repair-time multipliers by instrument (complex instruments take longer)
instrument_delay_factor = {
    "Mass Spectrometer": 1.6,
    "Sequencer": 1.5,
    "PCR Analyzer": 1.0,
    "Chromatograph": 1.1,
    "Microscope": 0.8,
}

# regional delay factor (parts logistics / staffing)
region_delay_factor = {
    "North America": 0.9,
    "Europe": 1.0,
    "APAC": 1.1,
    "Latin America": 1.4,
    "India": 1.3,
}

rows = []
open_dates_pool = pd.date_range("2024-01-01", "2025-12-31", freq="D")

for i in range(1, N + 1):
    instrument = np.random.choice(instrument_types, p=instrument_weights)
    region = np.random.choice(regions, p=region_weights)
    issue = np.random.choice(issue_categories, p=issue_weights)
    warranty = np.random.choice(warranty_statuses, p=[0.65, 0.35])

    sla_target = sla_target_map[issue]

    # simulate actual resolution hours with noise, skewed by instrument + region factors
    base_hours = sla_target * np.random.uniform(0.5, 1.3)
    delay_factor = instrument_delay_factor[instrument] * region_delay_factor[region]
    actual_hours = round(base_hours * delay_factor + np.random.normal(0, 5), 1)
    actual_hours = max(1.0, actual_hours)

    open_date = pd.Timestamp(np.random.choice(open_dates_pool)) + timedelta(
        hours=int(np.random.randint(0, 24))
    )
    close_date = open_date + timedelta(hours=actual_hours)

    engineer_id = f"ENG-{np.random.randint(1, 61):03d}"

    # repeat ticket: instruments with higher delay factor have a higher chance of repeat failure
    repeat_prob = 0.08 * delay_factor
    repeat_ticket = np.random.rand() < min(repeat_prob, 0.35)

    # cost: base cost by issue type + instrument complexity + warranty status (warranty covers most cost)
    base_cost = {"Hardware": 450, "Software": 120, "Calibration": 200}[issue]
    cost = base_cost * instrument_delay_factor[instrument] * np.random.uniform(0.8, 1.4)
    if warranty == "Out-of-Warranty":
        cost *= 1.5
    cost = round(cost, 2)

    rows.append(
        {
            "ticket_id": f"TCK-{i:05d}",
            "instrument_type": instrument,
            "region": region,
            "issue_category": issue,
            "open_date": open_date.strftime("%Y-%m-%d %H:%M"),
            "close_date": close_date.strftime("%Y-%m-%d %H:%M"),
            "sla_target_hours": sla_target,
            "actual_resolution_hours": actual_hours,
            "engineer_id": engineer_id,
            "warranty_status": warranty,
            "repeat_ticket": repeat_ticket,
            "cost_usd": cost,
        }
    )

df = pd.DataFrame(rows)
df["sla_breached"] = df["actual_resolution_hours"] > df["sla_target_hours"]

df.to_csv("/home/claude/liswa_service_tickets.csv", index=False)
print(f"Generated {len(df)} rows")
print(df.head(10).to_string())
print("\nSLA breach rate overall: {:.1%}".format(df["sla_breached"].mean()))
print("\nSLA breach rate by region:")
print(df.groupby("region")["sla_breached"].mean().sort_values(ascending=False))
print("\nSLA breach rate by instrument type:")
print(df.groupby("instrument_type")["sla_breached"].mean().sort_values(ascending=False))
print("\nRepeat ticket rate overall: {:.1%}".format(df["repeat_ticket"].mean()))