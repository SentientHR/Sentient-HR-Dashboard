import pandas as pd

def load_data():
    staffing_hours = pd.read_csv('data/Sentient_Staffing_Hours_Historical.csv')
    recruitment_data = pd.read_csv('data/Sentient_Educator_Recruitment_Retention.csv')
    client_centres = pd.read_csv('data/Sentient_Client_Centre_List.csv')
    ontario_centres = pd.read_excel('data/child_care_facilities_open_data_april_2025.xlsx')
    financial_forecast = pd.read_excel('data/Corrected_36-month_forecast.xlsx')
    
    return staffing_hours, recruitment_data, client_centres, ontario_centres, financial_forecast