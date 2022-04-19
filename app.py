import pandas as pd
import streamlit as st
import plotly.express as px
import matplotlib.pyplot as plt
from pandas_profiling import ProfileReport
from streamlit_pandas_profiling import st_profile_report

#Webaap title
st.markdown("# **Bacteroides project for meta-analysis**")
st.markdown('''
### This web application is designed to view the articles realted to ___Bacteroides___ and ___probiot*___ in [Scopus](https://www.scopus.com) online database.\
**Credit:** App built in `Python` + `Streamlit` by [Dr. Muhammad Aammar Tufail](https://www.researchgate.net/profile/Muhammad-Tufail-22)
---
''')

# loading dataset csv file
with st.sidebar.header('upload your cvs data'):
    uploaded_file = st.sidebar.file_uploader("Upload your input CSV file", type=["csv"])
    st.sidebar.markdown("""
[Example CSV input file](https://raw.githubusercontent.com/dataprofessor/data/master/delaney_solubility_with_descriptors.csv)
""")
# prepare plotting

if uploaded_file is not None:
    @st.cache
    def load_csv():
        csv = pd.read_csv(uploaded_file)
        return csv

    df = load_csv()
    pr = ProfileReport(df, explorative=True)
    st.header('**Input DataFrame summary**')
    st.write(df.describe())
    st.header('**Line Chart showing articles per year**')

    # #multiselect
    # year = df['year'].unique()
    # year_selected = st.multiselect("Select year of publication", year)
    # mask_year = df['year'].isin(year_selected)
    # df = df[year_selected]

    st.write(px.histogram(df, x='year',color="year")) 
    st.header('**Input DataFrame**')
    st.write(df)
    st.write('---')
    st.header('**Pandas Profiling Report**')
    st_profile_report(pr)
else:
    st.info('Awaiting for CSV file to be uploaded.')
    if st.button('Press to use Example Dataset'):
        # Example data
        @st.cache
        def load_data():
            a = pd.read_csv("data.csv")
            return a
        df = load_data()
        pr = ProfileReport(df, explorative=True)
        st.header('**Input DataFrame**')
        st.write(df)
        st.write('---')
        st.header('**Pandas Profiling Report**')
        st_profile_report(pr)

