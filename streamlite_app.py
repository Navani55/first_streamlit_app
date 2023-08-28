
import streamlit

streamlit.title('My Moms new Healthy Diner')
streamlit.header('Breakfast Favourites')
streamlit.text('🥣 Omega 3 & Blueberry Oatmetal')
streamlit.text('🥗 kale,spinach & Rocket smoothe')
streamlit.text('🐔Hard-Boiled Free-Range Egg ')
streamlit.text('🥑🍞 Avacado Toast')

streamlit.header('🍌🥭 Build Your Own Fruit Smoothie 🥝🍇')

import pandas 
my_fruit_list = pandas.read_csv("https://uni-lab-files.s3.us-west-2.amazonaws.com/dabw/fruit_macros.txt")
my_fruit_list=my_fruit_list.set_index('Fruit')

#Let's put a pick list here so they can pick the fruit they want to include 
fruits_selected=streamlit.multiselect("Pick some fruits:",list(my_fruit_list.index),['Avocado','Strawberries'])
fruits_to_show=my_fruit_list.loc[fruits_selected]

#display the table on the page
streamlit.dataframe(fruits_to_show)

streamlit.header('Fruity Fruit Advice')
fruit_choice=streamlit.text.input('What fruit would you like information about?','Kiwi')
streamlit.write('The user entered',fruit_choice)
import requests
fruityvice_response = requests.get("https://fruityvice.com/api/fruit/" + fruit_choice)


# normalize the json 
fruityvice_normalized = pandas.json_normalize(fruityvice_response.json())
# put the normalised json into a dataframe
streamlit.dataframe(fruityvice_normalized)


