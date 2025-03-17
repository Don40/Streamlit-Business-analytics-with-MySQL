import mysql.connector
#pip install mysql-connector-python
import streamlit as st

conn = mysql.connector.connect(
host="46.202.164.177",
port="3306",
user="streamlit_vps_user",
passwd="vps_streamlit",
db="my_streamlit")

c = conn.cursor()


def view_all_data():
	c.execute('SELECT * FROM customers order by id asc')
	data = c.fetchall()
	return data

def view_all_departments():
	c.execute('SELECT Department FROM customers')
	data = c.fetchmany
	return data
