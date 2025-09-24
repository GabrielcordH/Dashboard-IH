import streamlit as st
import pandas as pd
import openpyxl

@st.cache_data  
def carregar_dados():
    url = "https://www.sspds.ce.gov.br/wp-content/uploads/sites/24/2025/03/CVLI_2009-2024.xlsx"

    df = pd.read_excel(url)
    return df

def main():
    st.title("CVLI Detalhado (2009-2024) — SSPDS/CE")

    df = carregar_dados()
    st.subheader("Visão geral dos dados")
    st.dataframe(df.head(20))

if __name__ == "__main__":
    main()