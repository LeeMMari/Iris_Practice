# -*- coding:utf-8 -*-
import streamlit as st
import pandas as pd
import matplotlib.pyplot as plt
import plotly.express as px
import seaborn as sns

def run_eda_app():

    st.subheader("탐색적 자료 분석 페이지!")

    iris_df = pd.read_csv('data/iris.csv')
    # st.dataframe(iris_df)

    submenu = st.sidebar.selectbox("서브메뉴", ['기술통계량', '그래프'])
    if submenu == "기술통계량":
        st.dataframe(iris_df)

        with st.expander("Data Types"):
            result = pd.DataFrame(iris_df.dtypes).transpose()
            result.index = ["데이터타입"]
            st.dataframe(result)

        with st.expander("기술 통계량"):
            result2 = pd.DataFrame(iris_df.describe()).transpose()
            st.dataframe(result2)

        with st.expander("타겟분포"):
            result3 = iris_df['species'].value_counts()
            st.dataframe(result3)

    elif submenu == "그래프":
        st.subheader("plots")
        iris_df["e"] = iris_df["sepal_width"]/100
        fig1 = px.scatter(iris_df,
                          x = 'sepal_width',
                          y = 'sepal_length',
                          color = 'species',
                          error_x="e",
                          error_y="e",
                          title = 'Scatter Plot')
        st.plotly_chart(fig1)

        col1, col2 = st.columns(2)
        with col1:
            # st.subheader("컬럼1")
            with st.expander("박스플롯!!"):
                fig, ax = plt.subplots()
                sns.boxplot(iris_df, x = 'species', y = 'sepal_length', 
                            palette = sns.color_palette("pastel"),
                             saturation = 50, 
                             width = 0.7,  
                             fliersize = 5, ax = ax)
                st.pyplot(fig) 
                
        with col2:
            # st.subheader("컬럼2")
            with st.expander("히스토그램 by matplotlib"):
                fig, ax = plt.subplots()
                sns.histplot(iris_df['sepal_length'], kde=True)
                st.pyplot(fig) 
 
    else:    
        st.write("저 아님")
