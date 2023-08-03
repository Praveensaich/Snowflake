import streamlit
import pandas
streamlit.title("Snowflake")
streamlit.header("SQL")
streamlit.text("Praveen sai ch")
streamlit.text("Dabagardens, 30-1-29, Visakhapatnam")
my_fruit_list = pandas.read_csv("https://uni-lab-files.s3.us-west-2.amazonaws.com/dabw/fruit_macros.txt")
streamlit.dataframe(my_fruit_list)
