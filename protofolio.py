import pandas as pd
import numpy as np

class Portfolio:
    def __init__(self):
        self.portfolio_data = pd.read_csv('data/stock_data.csv')
    
    def get_portfolio_value(self):
        return self.portfolio_data['current_value'].sum()
    
    def get_portfolio_returns(self):
        total_investment = self.portfolio_data['investment_amount'].sum()
        current_value = self.portfolio_data['current_value'].sum()
        return ((current_value - total_investment) / total_investment) * 100
    
    def get_asset_allocation(self):
        return self.portfolio_data.groupby('asset_type')['current_value'].sum()
    
    def get_top_performers(self):
        return self.portfolio_data.nlargest(5, 'returns_percentage')
