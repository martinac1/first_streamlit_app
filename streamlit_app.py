import streamlit
import pandas

streamlit.title("Pokepedia")
streamlit.header("First generation starters")
streamlit.text("🌩️ Pikachu*")
streamlit.text("🔥 Charmander")
streamlit.text("🍀 Bulbasaur")
streamlit.text("💧 Squirtle")
streamlit.text("*There are two games where you can get Pikachu as your first Pokemon:")
streamlit.text("Pokemon Yellow: Which came out shortly after the Pokemon Anime hit the US.")
streamlit.text("Pokemon Let's Go Pikachu: the Pokemon Yellow Remake for the Nintendo Switch.")

streamlit.title("🍏🍑 Smoothie table 🍓🍒")
my_fruit_list = pandas.read_csv("https://uni-lab-files.s3.us-west-2.amazonaws.com/dabw/fruit_macros.txt")
my_fruit_list = my_fruit_list.set_index('Fruit')

# Let's put a pick list here so they can pick the fruit they want to include, with example
fruits_selected = streamlit.multiselect("Pick some fruits:", list(my_fruit_list.index), ['Avocado', 'Strawberries'])
fruits_to_show = my_fruit_list.loc[fruits_selected]

# Display the table on the page.
streamlit.dataframe(fruits_to_show)

# New section to display fruityvice api response
import requests
fruityvice_response = requests.get("https://fruityvice.com/api/fruit/watermelon")
streamlit.header("Fruityvice Fruit Advice!")
streamlit.text(fruityvice_response.json())

