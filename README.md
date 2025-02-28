# Wealth_Wise

A comprehensive financial education and planning platform designed specifically for women, helping them take control of their financial future through education, tools, and portfolio tracking.

## Features 🌟

### 1. Financial Education Hub 📚
- Basic financial concepts
- Investment fundamentals
- Real success stories from women investors
- Interactive learning modules

### 2. Financial Calculators 🧮
- **SIP Calculator**: Plan your systematic investment plans
  - Calculate future value of investments
  - Visualize returns through interactive charts
  - Adjust parameters in real-time

- **EMI Calculator**: Manage loan planning
  - Calculate monthly loan payments
  - Understand interest breakdowns
  - View payment distribution charts

### 3. Portfolio Tracker 📊
- Track investment performance
- View asset allocation
- Monitor top performers
- Real-time portfolio valuation

## Technology Stack 💻

- **Frontend & Backend**: Streamlit
- **Data Processing**: Pandas
- **Visualization**: Plotly
- **Styling**: Custom CSS

## Project Structure 📁

```
├── .streamlit/
│   └── config.toml         # Streamlit configuration
├── data/
│   ├── education_content.json  # Educational content
│   └── stock_data.csv         # Sample portfolio data
├── styles/
│   └── custom.css         # Custom styling
├── utils/
│   ├── calculators.py     # Financial calculation utilities
│   └── portfolio.py       # Portfolio management utilities
└── main.py               # Main application file
```

## Setup Instructions 🚀

1. Ensure you have Python 3.11+ installed
2. Install required packages:
   ```bash
   pip install streamlit pandas plotly
   ```

3. Run the application:
   ```bash
   streamlit run main.py
   ```

4. Access the application at `http://localhost:5000`

## Usage Guidelines 📝

1. **Navigation**: Use the sidebar to switch between different sections
2. **Calculators**: 
   - Enter your inputs in the provided fields
   - Click calculate to see results
   - Interact with charts for detailed insights
3. **Portfolio Tracker**:
   - View your portfolio summary
   - Check asset allocation
   - Monitor performance metrics

## Contributing 🤝

Feel free to fork this project and submit pull requests for improvements. Some areas for potential enhancement:

- Additional financial calculators
- More educational content
- Enhanced visualization features
- Integration with real-time market data

## License 📄

This project is licensed under the MIT License - see the LICENSE file for details.

---

Built with 💝 for women's financial empowerment
