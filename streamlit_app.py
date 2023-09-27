import streamlit
import pandas

streamlit.title("Pokepedia")
streamlit.header("First generation starters")
streamlit.text("🌩️ Pikachu*")
streamlit.text("🔥 Charmander")
streamlit.text("🍀 Bulbasaur")
streamlit.text("💧 Squirtle")

streamlit.title("Smoothie table")
my_fruit_list = pandas.read_csv("https://uni-lab-files.s3.us-west-2.amazonaws.com/dabw/fruit_macros.txt")
streamlit.dataframe(my_fruit_list)
