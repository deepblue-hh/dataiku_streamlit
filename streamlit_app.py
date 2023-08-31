# # streamlit_app.py

# import streamlit as st

# # Initialize connection.
# conn = st.experimental_connection('snowpark')

# # Perform query.
# df = conn.query('SELECT * from ROBYN_NEW_SNOW_ALLOCATED_CSV_COPY;', ttl=600)

# # Print results.
# for row in df.itertuples():
#     st.write(f"{row.col_0} has a :{row.solID}:")

# streamlit_app.py

import streamlit as st

# Initialize connection.
conn = st.experimental_connection('snowpark')

# Load the table as a dataframe using the Snowpark Session.
@st.cache_data
def load_table():
    with conn.safe_session() as session:
        return session.table('ROBYN_NEW_SNOW_ALLOCATED_CSV_COPY').to_pandas()

df = load_table()

import pandas as pd
import matplotlib.pyplot as plt

# Load the data
data = df

# Create a figure with two subplots
fig, (ax1, ax2) = plt.subplots(1, 2, figsize=(12, 6))

# Create the first pie chart
ax1.pie(data['histSpendAllShare'], labels=data['channels'], autopct='%1.1f%%')
ax1.set_title('histSpendAllShare')

# Create the second pie chart
ax2.pie(data['optmSpendShareUnit'], labels=data['channels'], autopct='%1.1f%%')
ax2.set_title('optmSpendShareUnit')

# Create the Streamlit app
st.title('My Streamlit App')
st.write(fig)
