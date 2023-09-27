import streamlit
import pandas

streamlit.title("Pokepedia")
streamlit.header("First generation starters")
streamlit.text("🌩️ Pikachu*")
streamlit.text("🔥 Charmander")
streamlit.text("🍀 Bulbasaur")
streamlit.text("💧 Squirtle")
streamlit.text("*There are two games where you can get Pikachu as your first Pokemon. Pokemon Yellow: Which came out shortly after the Pokemon Anime hit the US. Pokemon Let's Go Pikachu: the Pokemon Yellow Remake for the Nintendo Switch.")

streamlit.title("🍏🍑 Smoothie table 🍓🍒")
my_fruit_list = pandas.read_csv("https://uni-lab-files.s3.us-west-2.amazonaws.com/dabw/fruit_macros.txt")
streamlit.dataframe(my_fruit_list)
