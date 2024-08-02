import streamlit as st
from datetime import datetime, timedelta
import pandas as pd

# Sample data for customers
data = {
    'customer_id': list(range(1, 21)),
    'name': ['Arun', 'Balaji', 'Chitra', 'Devi', 'Eswaran', 'Fathima', 'Gopal', 'Hema', 'Indira', 'Jagan', 
             'Kumar', 'Lakshmi', 'Mohan', 'Nalini', 'Omprakash', 'Priya', 'Quincy', 'Ravi', 'Selvi', 'Thiru'],
    'membership_start_date': ['2023-01-01', '2023-03-15', '2023-06-01', '2023-07-20', '2023-02-10', 
                              '2023-05-25', '2023-08-30', '2023-01-15', '2023-04-22', '2023-09-05',
                              '2023-02-28', '2023-06-18', '2023-03-10', '2023-07-01', '2023-10-10',
                              '2023-01-25', '2023-04-05', '2023-08-01', '2023-11-15', '2023-03-20'],
    'membership_plan': ['12 months', '6 months', '12 months', '6 months', '12 months', 
                        '6 months', '12 months', '6 months', '12 months', '6 months',
                        '12 months', '6 months', '12 months', '6 months', '12 months', 
                        '6 months', '12 months', '6 months', '12 months', '6 months']
}

# Create a DataFrame
df = pd.DataFrame(data)

# Function to calculate expiry date and renewal month
def calculate_membership_dates(start_date, plan):
    start_date = datetime.strptime(start_date, '%Y-%m-%d')
    if '12' in plan:
        expiry_date = start_date + timedelta(days=365)
        renewal_month = (start_date + timedelta(days=365)).strftime('%B')
    elif '6' in plan:
        expiry_date = start_date + timedelta(days=182)
        renewal_month = (start_date + timedelta(days=182)).strftime('%B')
    return expiry_date.strftime('%Y-%m-%d'), renewal_month

# Streamlit app
st.set_page_config(page_title="Gym Membership Tracker")

# Centering the image using Streamlit's image function and some HTML
st.markdown(
    """
    <style>
    .centered {
        display: flex;
        justify-content: center;
        align-items: center;
        margin-bottom: 20px;
    }
    </style>
    """,
    unsafe_allow_html=True
)

st.markdown('<div class="centered">', unsafe_allow_html=True)
st.image("logo.png", width=150)
st.markdown('</div>', unsafe_allow_html=True)

st.title("Gym Membership Tracker")

customer_id_input = st.text_input("Enter Customer ID:")

if customer_id_input:
    try:
        customer_id = int(customer_id_input)
        customer = df[df['customer_id'] == customer_id]
        if not customer.empty:
            name = customer.iloc[0]['name']
            start_date = customer.iloc[0]['membership_start_date']
            plan = customer.iloc[0]['membership_plan']
            expiry_date, renewal_month = calculate_membership_dates(start_date, plan)
            
            st.write(f"**Customer Name:** {name}")
            st.write(f"**Membership Start Date:** {start_date}")
            st.write(f"**Membership Expiry Date:** {expiry_date}")
            st.write(f"**Renewal Month:** {renewal_month}")
        else:
            st.write("Customer ID not found.")
    except ValueError:
        st.write("Invalid Customer ID. Please enter a number.")
