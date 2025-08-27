# annuity_data.py
athene_products = [
    {"name": "AccuMax 7", "type": "Fixed Indexed Annuity", "min_premium": 10000, "max_premium": 1000000,
     "issue_ages": "0-83", "withdrawal_charge_years": 7, "free_withdrawal": "Greater of 10% Accumulated Value or 10% Premium",
     "rates": {"7-Yr PtP S&P 500 (Par Rate)": {"low_band": 0.88, "high_band": 0.93},
               "7-Yr PtP AIMAX (Par Rate)": {"low_band": 3.65, "high_band": 3.85},
               "7-Yr PtP CAPE (Par Rate)": {"low_band": 4.35, "high_band": 4.60},
               "7-Yr Annual Sum S&P (Par Rate)": {"low_band": 0.80, "high_band": 0.85, "floor": -0.10},
               "1-Yr PtP AIMAX (Par Rate)": {"low_band": 1.50, "high_band": 1.60},
               "1-Yr PtP CAPE (Par Rate)": {"low_band": 1.45, "high_band": 1.55},
               "Fixed": {"low_band": 0.0345, "high_band": 0.0375}},
     "features": ["Terminal Illness Waiver (not CA)", "Confinement Waiver (not CA)", "MVA (not CA)", "Death Benefit: Greater of Interim Value or Min Guaranteed"],
     "state_availability": "All except NY; variations in CA"},
    {"name": "MaxRate 7", "type": "Multi-Year Guaranteed Annuity", "min_premium": 10000, "max_premium": 1000000,
     "issue_ages": "0-83", "rates": {"Fixed": 0.045}, "features": ["10% Free Withdrawal", "Confinement/Terminal Waivers"]},
    # Add more from below
]

company_highlights = {
    "assets": 363300000000,  # $363.3B GAAP assets
    "liabilities": 337500000000,  # $337.5B
    "equity": 16400000000,  # $16.4B shareholders' equity
    "ratings": {"S&P": "A+ (Jan 2024)", "Fitch": "A+ (Sep 2024)", "AM Best": "A+ (Jun 2024)", "Moody's": "A1 (Sep 2024)"}
}