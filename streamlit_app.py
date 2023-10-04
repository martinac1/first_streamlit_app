import streamlit
import pandas
import requests
import snowflake.connector
from urllib.error import URLError

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

# Create repeatable code block (function)
def get_fruityvice_data(this_fruit_choice):
    fruityvice_response = requests.get("https://fruityvice.com/api/fruit/" + this_fruit_choice)
    fruityvice_normalized = pandas.json_normalize(fruityvice_response.json())
    return fruityvice_normalized

# New section to display fruityvice api response
streamlit.header("Fruityvice Fruit Advice!")
try:
  fruit_choice = streamlit.text_input('What fruit would you like information about?')
  if not fruit_choice:
    streamlit.error("Please select a fruit to get information.")
  else:
    back_from_function = get_fruityvice_data(fruit_choice)
    streamlit.dataframe(back_from_function)

except URLError as e:
  streamlit.error()

streamlit.header("The fruit load list contains:")
def get_fruit_load_list():
    with my_cnx.cursor() as my_cur:
        #my_cur.execute("SELECT CURRENT_USER(), CURRENT_ACCOUNT(), CURRENT_REGION()")
        my_cur.execute("select * from pc_rivery_db.public.fruit_load_list")
        return my_cur.fetchall()

# Add button to load the fruit
if streamlit.button('Get Fruit Load List'):
    my_cnx = snowflake.connector.connect(**streamlit.secrets["snowflake"])
    my_data_rows = get_fruit_load_list()
    streamlit.dataframe(my_data_rows)

# Don't run whilst we troubleshoot
streamlit.stop()

add_my_fruit = streamlit.text_input("What fruit would you like to add?")
streamlit.write('Thanks for adding ', add_my_fruit)

# Try to add row
my_cur.execute("insert into pc_rivery_db.public.fruit_load_list values ('from streamlit')")
