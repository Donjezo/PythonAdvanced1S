import streamlit as st


if st.button("Click me"):
    st.write("buttoni eshte klikuar")


if st.checkbox("check me to show some text"):
    st.write("you're seeing this text bescause you checkd the checkbox")



user_input =  st.text_input("Enter some text")

st.write("you enterd: ", user_input)


age = st.number_input("enter age",min_value=0,max_value=100)

st.write(f"you age is {age}")

message3= st.text_area("Enter a message")

st.write("you have enterd ", message3)

choice = st.radio("Pick one",["ai","python adv","code 1"])

if st.button("Success"):
    st.success("Operatin was succesful")



try:
    1/0

except Exception as e:
    st.exception(e)








