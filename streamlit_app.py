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

# Print results.
for row in df.itertuples():
    st.write(f"{row.col_0} has a :{row.channels}:")