from pandas.tseries.offsets import BusinessDay


class Defaults:
    convention = "ACT360"
    notional = 1000000.0
    stub = "SHORTFRONT"
    stub_length = "SHORT"
    modifier = "MF"
    payment_lag = 2
    payment_lag_specific = {
        "IRS": 2,
        "FXSwap": 0,
        "SBS": 2,
        "NonMtmXCS": 2,
        "Swap": 2,
    }
    calendar = BusinessDay()
    interpolation = "log_linear"
    frequency = "Q"
    frequency_months = {
        "M": 1,
        "B": 2,
        "Q": 3,
        "T": 4,
        "S": 6,
        "A": 12,
        "Z": 1e8,
    }
    eom = False
    fx_swap_base = "foreign"
    tag = "v"
    headers = {
        "type": "Type",
        "u_acc_start": "Unadj Acc Start",
        "u_acc_end": "Unadj Acc End",
        "a_acc_start": "Acc Start",
        "a_acc_end": "Acc End",
        "payment": "Payment",
        "convention": "Convention",
        "dcf": "DCF",
        "df": "DF",
        "notional": "Notional",
        "rate": "Rate",
        "spread": "Spread",
        "npv": "NPV",
        "cashflow": "Cashflow",
    }