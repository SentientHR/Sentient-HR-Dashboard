import streamlit as st
from load_data import load_data
from gpt_insights import generate_strategic_insights

staffing_hours, recruitment_data, client_centres, ontario_centres, financial_forecast = load_data()

st.title("Sentient HR Strategic Forecasting Dashboard")

if st.button('Generate Monthly Staffing Insights'):
    monthly_hours = staffing_hours.groupby('Date')['Hours Filled'].sum().reset_index()
    current_month_hours = monthly_hours.iloc[-1]['Hours Filled']
    forecasted_hours_prompt = f"""
    Current month hours filled: {current_month_hours}
    Historical monthly average: {monthly_hours['Hours Filled'].mean():.0f}
    Identify explicitly top 5 childcare centres to call based on staffing shortfall, historical ordering, and potential revenue. Provide explicit messaging aligned with Sentient Synergy's warm, professional style.
    """
    insights = generate_strategic_insights(forecasted_hours_prompt)
    st.write("### Strategic Recommendations:", insights)