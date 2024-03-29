# -*- coding: utf-8 -*-
"""day073.ipynb

Automatically generated by Colaboratory.

Original file is located at
    https://colab.research.google.com/drive/1sFPwvACHbe7cJVhtL0G4hLPACXGDKyO6
"""

import pandas as pd
df = pd.read_csv("salaries_by_college_major.csv")
df.head()
df.shape
print(df.columns)
df.isna()
df.tail()
clean_df = df.dropna()
clean_df.shape

max_start_salary_ind = int(clean_df["Starting Median Salary"].idxmax())
print(f"Highest median starting salary:"
      f"{clean_df['Undergraduate Major'][max_start_salary_ind]} "
      f"{int(clean_df['Starting Median Salary'].max())}")

max_mid_salary_ind = int(clean_df["Mid-Career Median Salary"].idxmax())
print(f"Highest Mid-Carrer median starting salary:"
      f"{clean_df['Undergraduate Major'][max_mid_salary_ind]} "
      f"{int(clean_df['Mid-Career Median Salary'].max())}")

min_start_salary_ind = int(clean_df["Starting Median Salary"].idxmin())
print(f"Lowest median starting salary:"
      f"{clean_df['Undergraduate Major'][min_start_salary_ind]} "
      f"{int(clean_df['Starting Median Salary'].min())}")

min_mid_salary_ind = int(clean_df["Mid-Career Median Salary"].idxmin())
print(f"Lowest Mid-Carrer median starting salary:"
      f"{clean_df['Undergraduate Major'][min_mid_salary_ind]} "
      f"{int(clean_df['Mid-Career Median Salary'].min())}")

spread_col = clean_df['Mid-Career 90th Percentile Salary'] - clean_df['Mid-Career 10th Percentile Salary']
clean_df.insert(1, 'Spread', spread_col)

clean_df

low_risk_major = clean_df.sort_values('Spread')
low_risk_major[['Undergraduate Major', 'Spread']].head()

high_potential = clean_df.sort_values('Mid-Career 90th Percentile Salary', ascending=False)
high_potential[['Undergraduate Major', 'Mid-Career 90th Percentile Salary']].head()

high_risk = clean_df.sort_values('Spread', ascending=False)
high_risk[['Undergraduate Major', 'Spread']].head()

clean_df.groupby('Group').count()

pd.options.display.float_format = '{:,.2f}'.format
clean_df.groupby('Group').mean()



# UPDATED DATA 2023



import requests
from bs4 import BeautifulSoup

DATA_URL = "https://www.payscale.com/college-salary-report/majors-that-pay-you-back/bachelors"
PAGE_NUMBERS = 32

def process_page(index):
  if index == 1:
    response = requests.get(DATA_URL)
  else:
    response = requests.get(DATA_URL+ "/page/" + f"{index}")
  response.raise_for_status()
  soup = BeautifulSoup(response.text, "html.parser")

  headers_raw = soup.select(".data-table__header")
  headers = [header.get_text() for header in headers_raw]

  rows_raw = soup.select(".data-table__row")
  row_list = [row.select(".data-table__cell .data-table__value") for row in rows_raw]
  row_dict = {}
  for row in row_list:
    row_content = [ entry.get_text() for entry in row ]
    for i, cell in enumerate(row_content):
      if "$" in cell:
        row_content[i] = int(cell.replace("$", '').replace(",", ""))
    row_dict[f"{row[0].get_text()}"] = row_content

  df_current = pd.DataFrame.from_dict(row_dict, orient="index", columns=headers)
  return df_current

data_list = [ process_page(i) for i in range(1, 33)]

current_data = pd.concat(data_list)

current_data

num_data = current_data[["Major", "Early Career Pay", "Mid-Career Pay"]]
num_data.groupby('Major').count()

pd.options.display.float_format = '{:,.2f}'.format
num_data.groupby('Major').mean().sort_values("Early Career Pay", ascending=False)