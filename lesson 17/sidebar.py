import streamlit as st

st.sidebar.header("Sidebar")

st.sidebar.write("this is a sidebar")

st.sidebar.selectbox("chose an option",["Oprion 1","option 2","option3"])
st.sidebar.radio("Go to ",["Home","settings"])