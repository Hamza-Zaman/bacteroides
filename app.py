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
[Example CSV input file](https://github.com/AammarTufail/bacteroides/blob/main/data.csv)
""")
# prepare plotting
st.title("Data f Publication")
df1 = pd.read_csv('count_year.csv')
st.write(df1)
# st.write(df.head())
# st.write(df.columns)
# # summary stat
st.write(df1.describe())
# data management
year_option = df1['year'].unique().tolist()
year = st.selectbox("which year should we plot?", year_option, 0)
# df1 = df1[df1['year']== year]
# plotting
fig = px.scatter(df1, x= 'year', y ='num_of_pubs', size='num_of_pubs', color='num_of_pubs', hover_name='year',
                size_max=40,range_y=[5,300], range_x=[1990,2024],
                animation_frame='year', animation_group='year')
fig1 = px.bar(df1, x= 'year', y ='num_of_pubs', color='year', hover_name='year',
                range_y=[5,10], range_x=[1990,2024],
                animation_frame='year', animation_group='year')
fig.update_layout(width=800, height=600)
st.write(fig)
st.write(fig1)     

if uploaded_file is not None:
    @st.cache
    def load_csv():
        csv = pd.read_csv(uploaded_file)
        return csv
    df = load_csv()
    #other profile reporting
    pr = ProfileReport(df, explorative=True)
    st.header('**Input DataFrame summary**')
    st.write(df.describe())
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

