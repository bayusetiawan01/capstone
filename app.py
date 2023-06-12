import streamlit as st
import pandas as pd
import numpy as np
from lorem_text import lorem
from st_on_hover_tabs import on_hover_tabs
import matplotlib.pyplot as plt
import altair as alt
import plotly.express as px

st.set_page_config(page_title="Capstone Project Bayu Setiawan", layout="wide")

st.markdown("<style>" + open("./style.css").read() + "</style>", unsafe_allow_html=True)
st.markdown("""---""")
# Data Process
disease = pd.read_csv("Disease Percentage.csv")
beef_consumption = pd.read_csv("Beef 2017.csv")
sheep_consumption = pd.read_csv("Sheep 2017.csv")
hospital_bed = pd.read_csv("Hospital Bed.csv")
final_data = pd.read_csv("Final Data.csv")
final_data2 = final_data.sort_values(
    by=["meat_total"], ignore_index=True, ascending=False
)
final_data3 = final_data.sort_values(
    by=["hospital_bed"], ignore_index=True, ascending=False
)

# Data Process End
st.title("Analisis Pengaruh Konsumsi Daging Merah Terhadap Peningkatan Risiko Penyakit")
st.subheader(
    "Kasus CVD (Cardiovascular Disease), Kanker, CRD (Chronic Respiratory Diseases), dan Diabetes"
)
st.write("Oleh Bayu Setiawan")
st.markdown("""---""")
with st.sidebar:
    tabs = on_hover_tabs(
        tabName=["Dashboard", "Raw Data", "Processed Data"],
        iconName=["dashboard", "receipt_long", "description"],
    )

if tabs == "Raw Data":
    st.subheader(
        "Mortalitas akibat CVD, kanker, diabetes atau CRD antara usia tepat 30 dan 70 tahun"
    )
    st.write(
        "Mortalitas akibat CVD, kanker, diabetes, atau CRD adalah persentase orang berusia 30 tahun yang akan meninggal sebelum usia ke-70 karena penyakit kardiovaskular, kanker, diabetes, atau penyakit pernapasan kronis. dengan asumsi bahwa dia akan mengalami tingkat kematian saat ini di setiap usia dan dia tidak akan meninggal karena penyebab kematian lainnya (misalnya cedera atau HIV/AIDS)."
        " Karena tidak ada data khusus kanker saja atau CVD saja maka yang digunakan adalah mortalitas akibat semua penyakit yang disebutkan di atas."
    )
    st.caption("sumber : https://data.worldbank.org/indicator/SH.DYN.NCOM.ZS")
    st.dataframe(disease)

    st.markdown("""---""")
    st.subheader("Konsumsi Daging Sapi dan Kambing (Kg/Kapita per Tahun)")
    st.write(
        "Indikator ini disajikan untuk daging sapi dan daging sapi muda, babi, unggas, dan domba. Konsumsi daging diukur dalam ribuan ton berat karkas (kecuali unggas yang dinyatakan sebagai berat siap masak) dan dalam kilogram berat eceran per kapita. Faktor konversi berat karkas menjadi berat eceran adalah: 0,7 untuk daging sapi dan daging sapi muda, 0,78 untuk daging babi, dan 0,88 untuk daging domba dan daging unggas."
        " Data yang digunakan hanya data daging sapi dan kambing berdasarkan definisi daging merah yang menyebabkan CVD dan meningkatkan risiko Kanker"
    )
    st.caption(
        "sumber : https://www.oecd-ilibrary.org/agriculture-and-food/meat-consumption/indicator/english_fa290fd0-en"
    )
    st.dataframe(beef_consumption)
    st.dataframe(sheep_consumption)

    st.markdown("""---""")
    st.subheader("Tempat tidur rumah sakit (per 1.000 orang)")
    st.write(
        "Tempat tidur rumah sakit termasuk tempat tidur rawat inap yang tersedia di rumah sakit umum, swasta, umum, dan khusus serta pusat rehabilitasi. Dalam kebanyakan kasus, tempat tidur untuk perawatan akut dan kronis sudah termasuk."
    )
    st.caption("sumber : https://data.worldbank.org/indicator/SH.MED.BEDS.ZS")
    st.dataframe(hospital_bed)

elif tabs == "Dashboard":
    st.header("Analisis Data")
    col1, col2 = st.columns([3, 1])
    data = np.random.randn(10, 1)
    with st.container():
        with col1:
            fig = px.scatter(
                x=final_data["mortality"],
                y=final_data["meat_total"],
                trendline="ols",
                text=final_data["country_name"],
            )
            fig.update_layout(
                xaxis_title="Mortalitas",
                yaxis_title="Konsumsi Daging",
            )
            fig.update_traces(
                hovertemplate="Negara: %{text} <br>Mortalitas: %{x} <br>Konsumsi Daging: %{y}"
            )
            st.write(fig)
        with col2:
            st.write(lorem.paragraph())
    st.markdown("""---""")
    col1, col2 = st.columns([1, 1])
    with st.container():
        with col1:
            st.table(final_data2[["country_name", "meat_total"]].head(10))
        with col2:
            st.table(final_data2[["country_name", "meat_total"]].tail(10))
    st.markdown("""---""")

    st.header("Penjelasan Data")
    col1, col2 = st.columns([3, 1])
    data = np.random.randn(10, 1)
    with st.container():
        with col1:
            fig = px.scatter(
                x=final_data["mortality"],
                y=final_data["hospital_bed"],
                trendline="ols",
                text=final_data["country_name"],
            )
            fig.update_layout(
                xaxis_title="Mortalitas",
                yaxis_title="Fasilitas Kesehatan",
            )
            fig.update_traces(
                hovertemplate="Negara: %{text} <br>Mortalitas: %{x} <br>Fasilitas Kesehatan: %{y}",
            )
            st.write(fig)
        with col2:
            st.write(lorem.paragraph())
    st.markdown("""---""")
    col1, col2 = st.columns([1, 1])
    with st.container():
        with col1:
            st.table(final_data3[["country_name", "hospital_bed"]].head(10))
        with col2:
            st.table(final_data3[["country_name", "hospital_bed"]].tail(10))
    st.markdown("""---""")

    st.header("Kesimpulan dan Solusi")
    st.write(lorem.paragraph())

elif tabs == "Processed Data":
    st.header("Dataset yang telah diproses")
    st.dataframe(final_data)
    st.write(
        "Dataset dibersihkan dengan mengjilangkan bagian yang tidak terpakai terlebih dahulu. Karena tahun diaman ketersediaan data cukup lengkap adalah pada tahun 2017 maka data yang diambil hanya data pada tahun 2017."
        " Kemudian dilakukan join tabel berdasarkan kesesuaian kode negara dan tidak semua negara memiliki data konsumsi daging sehingga menyisakan beberapa negara."
        " Setelah dilakukan join tabel terdapat beberapa negara yang duplikat dan memiliki nilai yang sama sehingga langsung saja digunakan perintah 'DISTINCT' pada query MySQL."
        " Kemudian untuk mengatasi nilai null digunakan data satu tahun sebelumnya kecuali nigeria yang data terakhirnya tahun 2004 dan Filipina yang data tahun terakhirnya 2014"
        " Query yang digunakan adalah sebagai berikut:"
    )
    code = """
    CREATE TABLE final_data AS
    SELECT DISTINCT 
	    dp.`Country Name` AS country_name,
	    b.LOCATION AS location,
	    b.`TIME` AS `time`,
	    b.Value AS beef,
	    s.Value AS sheep,
	    b.Value + s.Value AS meat_total,
	    dp.`2017` AS mortality,
	    CASE
		    WHEN hb.`2016` IS NULL AND hb.`2017` IS NULL AND hb.`2014` IS NULL THEN hb.`2004` #Nigeria
		    WHEN hb.`2016` IS NULL AND hb.`2017` IS NULL THEN hb.`2014` #Philipine
		    WHEN hb.`2017` IS NULL THEN hb.`2016`
		    ELSE hb.`2017`
	    END AS hospital_bed
    FROM beef b
    JOIN sheep s 
    ON s.LOCATION = b.LOCATION
    JOIN disease_percentage dp
    ON s.LOCATION = dp.`Country Code`
    JOIN hospital_bed hb
    ON s.LOCATION = hb.`Country Code`
    """
    st.code(code, language="SQL")
