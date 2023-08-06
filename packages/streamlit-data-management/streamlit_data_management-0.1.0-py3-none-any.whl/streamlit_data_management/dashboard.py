import streamlit as st
import plotly.graph_objects as go
import pandas as pd

import base64
import io

import arrow

class Components:
	def __init__(self,name):
		self.name = name
		st.set_page_config(
			page_title=f"{self.name} Data Management System",
			page_icon="📊",
			layout="wide",
			)
	def header(self):
		st.title(f"{self.name} Data Management System")
	def footer(self):
		st.write("---")
		st.markdown(f"[*Provost & Pritchard Consulting Group - 2023*](https://provostandpritchard.com/)")

	def month_picker(self,start_year,end_year):
		if st.checkbox("Single Month"):
			month = st.selectbox('Month',[arrow.get(i,"M").format('MMMM') for i in range(1,13)])
			year = st.selectbox('Year',range(start_year,end_year))
			return arrow.get(f"{year}-{month}","YYYY-M")



def export_df(df,file_name,index=True,header=True):
	towrite = io.BytesIO()
	downloaded_file = df.to_excel(towrite, encoding='utf-8', index=index, header=header)
	towrite.seek(0)  # reset pointer
	b64 = base64.b64encode(towrite.read()).decode()  # some strings
	linko= f'<a href="data:application/vnd.openxmlformats-officedocument.spreadsheetml.sheet;base64,{b64}" download="{file_name}">Download excel file</a>'
	# return linko
	st.markdown(linko, unsafe_allow_html=True)


def show_pdf(file_path):
	with open(file_path,"rb") as f:
		base64_pdf = base64.b64encode(f.read()).decode('utf-8')
		pdf_display = f'<iframe src="data:application/pdf;base64,{base64_pdf}" width="800" height="800" type="application/pdf"></iframe>'		
		st.markdown(pdf_display, unsafe_allow_html=True)


def download_pdf(file_path,file_name,label):
		
	with open(file_path, "rb") as pdf_file:
		PDFbyte = pdf_file.read()

	st.download_button(label=label, 
			data=PDFbyte,
			file_name=f"{file_name}.pdf",
			mime='application/octet-stream')


def convert_date(df,col):
	df[col] = df[col].pipe(pd.to_datetime)
	return df

class Table:
	# def __init__(self,client,table_name):
	def __init__(self,table_name):
		"""
		client: supabase connection
		table_name: table name of supabase table
		"""
		# self.client = client
		self.client = st.session_state['client']
		
		self.table_name = table_name
		self.refresh()
	
	def __repr__(self) -> str:
		return f"Table Name = {self.table_name}"
	
	def refresh(self):
		self.df = pd.DataFrame(self.client.table(self.table_name).select('*').execute().data)
	
	def append(self,data):
		"""
		data; dict {"client":"Aliso"}
		"""
		self.client.table(self.table_name).insert(data).execute()
		self.refresh()

	def edit(self,data,locator):
		"""
		data: dict {"client":"Aliso"}
		locator: list ["id",1]
		"""
		self.client.table(self.table_name).update(data).eq(locator).execute()
		self.refresh()

	def delete(self,locator):
		"""
		locator: list ["id",1]
		"""
		self.client.table(self.table_name).delete().eq(locator).execute()
		self.refresh()