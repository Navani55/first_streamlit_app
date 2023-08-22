
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
streamlit.dataframe(my_fruit_list)

#Let's put a pick list here so they can pick the fruit they want to include 
streamlit.multiselect("Pick some fruits:",list(my_fruit-list.index))

#display the table on the page
streamlit.dataframe(my_fruit_list)

