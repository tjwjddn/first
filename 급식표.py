import requests
import xmltodict
import pandas as pd
import streamlit as st
import streamlit.components.v1 as components

st.set_page_config(
    page_title='구암고 급식표',
    page_icon='🍽',
    layout = 'wide',
    initial_sidebar_state="collapsed"

)
menu = st.sidebar.selectbox('오늘의 급식', options=['하루','기간'])


# st.write(학교)
# st.write(급식일자)


if menu == '하루':
    급식일자 = st.sidebar.text_input('급식일자를 선택하세요')
    btn = st.sidebar.button('확인')
    if btn:
        url = f'https://open.neis.go.kr/hub/mealServiceDietInfo?KEY=b90d79811c0244188bac999ee6e4ea63&ATPT_OFCDC_SC_CODE=D10&SD_SCHUL_CODE=7240056&MLSV_YMD={급식일자}'

        response = requests.get(url)
        response = response.content
        xmlObject = xmltodict.parse(response)
        dict_data = xmlObject['mealServiceDietInfo']
        df = pd.DataFrame(dict_data)
        df = df['row']



        components.html(df['DDISH_NM'], height=200)

if menu == '기간':
    급식시작일자 = st.sidebar.text_input('급식시작일자를 선택하세요')
    급식종료일자 = st.sidebar.text_input('급식일자를 입력하세요')
    # st.write(학교)
    # st.write(급식일자)
    btn = st.sidebar.button('확인')

    if btn:
        url = f'''https://open.neis.go.kr/hub/mealServiceDietInfo?KEY=b90d79811c0244188bac999ee6e4ea63&ATPT_OFCDC_SC_CODE=D10&SD_SCHUL_CODE=7240056&MLSV_FROM_YMD={급식시작일자}&MLSV_TO_YMD={급식종료일자}'''
        response = requests.get(url)
        response = response.content
        xmlObject = xmltodict.parse(response)


        dict_data = xmlObject['mealServiceDietInfo']['row']
        df = pd.DataFrame(dict_data)

        #st.write(df)

        for i in range(len(df)):
            components.html(df['DDISH_NM'][i], height=200)