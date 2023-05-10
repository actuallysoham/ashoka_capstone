import streamlit as st
import streamlit.components.v1 as components
import pandas as pd
import numpy as np

st.title('Twitter Friend Recommender')


def load_data(nrows):
    data = pd.read_excel('recommendations/day1.xlsx', nrows=nrows)
    return data



data = load_data(10000)
st.write(data)

# username input: TODO - fix lowercase
username_input = st.text_input('Enter your Twitter username')

df = pd.read_csv('ashoka_users.csv')
select_users = list(df['username'])

if username_input in select_users:
	st.write('Congrats, you are part of the study')
	#reccs = list(data[data['username'] == username_input])
	reccs = list(data.loc[data['username'] == username_input].values[0][2:])
	print(reccs)
	

	tab1, tab2, tab3, tab4, tab5, tab6, tab7 = st.tabs(["Day 1", "Day 2", "Day 3", "Day 4", "Day 5", "Day 6", "Day 7"])
	with tab1:
	   st.header("Day 1")
	   st.write(reccs)
	   st.markdown(f'''<a href='https://forms.gle/uVw3K1n7d5XSqWC38'>Link to Survey (Day 1)</a>''',unsafe_allow_html=True)

	with tab2:
	   st.header("Day 2")
	   st.write(reccs)

	with tab3:
	   st.header("Day 3")
	   st.write(reccs)

	with tab4:
	   st.header("Day 4")
	   st.write(reccs)

	with tab5:
	   st.header("Day 5")
	   st.write(reccs)

	with tab6:
	   st.header("Day 6")
	   st.write(reccs)

	with tab7:
	   st.header("Day 7")
	   st.write(reccs)

elif len(username_input)>1 and username_input not in select_users:
	st.write('Sorry, you are not a part of this study')





