import numpy as np

def calculate_sip(monthly_investment, expected_return, time_period):
    """Calculate SIP returns"""
    r = expected_return/100/12
    n = time_period * 12
    
    future_value = monthly_investment * ((1 + r) * ((1 + r)**n - 1)/r)
    total_investment = monthly_investment * n
    returns = future_value - total_investment
    
    return {
        'future_value': round(future_value, 2),
        'total_investment': round(total_investment, 2),
        'returns': round(returns, 2)
    }

def calculate_emi(principal, rate, tenure):
    """Calculate EMI for loans"""
    r = rate/100/12
    n = tenure * 12
    
    emi = principal * r * (1 + r)**n/((1 + r)**n - 1)
    total_payment = emi * n
    total_interest = total_payment - principal
    
    return {
        'emi': round(emi, 2),
        'total_payment': round(total_payment, 2),
        'total_interest': round(total_interest, 2)
    }
