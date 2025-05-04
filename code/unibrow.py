'''
Solution unibrow.py
'''
import pandas as pd
import streamlit as st
import pandaslib as pl

st.title("UniBrow")
st.caption("The Universal data browser")

# Upload section
uploaded = st.file_uploader("Upload your data file here", type=["csv", "xlsx", "json"])

if uploaded:
    # Extract file extension
    file_ext = pl.get_file_extension(uploaded.name)

    # Load the file into a DataFrame
    df = pl.load_file(uploaded, file_ext)

    # Column selection
    st.subheader("Select Columns to Display")
    all_cols = pl.get_column_names(df)
    selected_cols = st.multiselect("Choose one or more columns:", options=all_cols, default=all_cols)

    # Optional filter toggle
    filter_enabled = st.checkbox("Would you like to filter the rows?")

    if filter_enabled:
        st.subheader("Apply Filter to a Text Column")
        col1, col2 = st.columns(2)
        
        text_cols = pl.get_columns_of_type(df, 'object')
        selected_col = col1.selectbox("Select a column to filter by", options=text_cols)

        if selected_col:
            values = pl.get_unique_values(df, selected_col)
            selected_value = col2.selectbox("Choose a value to match", options=values)
            filtered_df = df[df[selected_col] == selected_value][selected_cols]
        else:
            filtered_df = df[selected_cols]
    else:
        filtered_df = df[selected_cols]

    # Display filtered data
    st.subheader("Filtered Data")
    st.dataframe(filtered_df)

    # Display summary statistics
    st.subheader("Summary Statistics")
    st.dataframe(filtered_df.describe())

