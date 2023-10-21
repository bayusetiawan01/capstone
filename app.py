import streamlit as st
import pandas as pd
import numpy as np
from st_on_hover_tabs import on_hover_tabs
import matplotlib.pyplot as plt
import altair as alt
import plotly.express as px

st.set_page_config(page_title="Project Bayu Setiawan", layout="wide")

st.markdown("<style>" + open("./style.css").read() + "</style>", unsafe_allow_html=True)
st.markdown("""---""")
# Data Process


def highlight_rows(x):
    if x["Negara"] == "Indonesia":
        return ["background-color : #4DD0E1"] * 2
    else:
        return [None, None]


disease = pd.read_csv("Disease Percentage.csv")
beef_consumption = pd.read_csv("Beef 2017.csv")
sheep_consumption = pd.read_csv("Sheep 2017.csv")
hospital_bed = pd.read_csv("Hospital Bed.csv")
final_data = pd.read_csv("Final Data.csv")
final_data2 = final_data.sort_values(
    by=["meat_total"], ignore_index=True, ascending=False
)
final_data2.rename(
    columns={"meat_total": "Konsumsi Daging Merah", "country_name": "Negara"},
    inplace=True,
)
final_data2 = final_data2[["Negara", "Konsumsi Daging Merah"]]
final_data2.index = np.arange(1, len(final_data2) + 1)
final_data2 = final_data2.iloc[np.r_[0:4, -8:0]]
line = pd.DataFrame({"Negara": "", "Konsumsi Daging Merah": ""}, index=[5])
final_data2 = pd.concat([final_data2, line], ignore_index=False)
final_data2 = final_data2.sort_index()
final_data2 = final_data2.rename(index={5: ""})
final_data2 = final_data2.style.apply(highlight_rows, axis=1)

final_data3 = final_data.sort_values(
    by=["hospital_bed"], ignore_index=True, ascending=False
)
final_data3.rename(
    columns={
        "hospital_bed": "Ketersediaan Fasilitas Kesehatan",
        "country_name": "Negara",
    },
    inplace=True,
)
final_data3 = final_data3[["Negara", "Ketersediaan Fasilitas Kesehatan"]]
final_data3.index = np.arange(1, len(final_data3) + 1)
final_data3 = final_data3.iloc[np.r_[0:4, -8:0]]
line = pd.DataFrame({"Negara": "", "Ketersediaan Fasilitas Kesehatan": ""}, index=[5])
final_data3 = pd.concat([final_data3, line], ignore_index=False)
final_data3 = final_data3.sort_index()
final_data3 = final_data3.rename(index={5: ""})
final_data3 = final_data3.style.apply(highlight_rows, axis=1)

final_data4 = final_data.sort_values(
    by=["mortality"], ignore_index=True, ascending=False
)
final_data4.rename(
    columns={"mortality": "Tingkat Mortalitas", "country_name": "Negara"}, inplace=True
)
final_data4 = final_data4[["Negara", "Tingkat Mortalitas"]]
final_data4.index = np.arange(1, len(final_data4) + 1)
final_data4 = final_data4.iloc[np.r_[0:4, -8:0]]
line = pd.DataFrame({"Negara": "", "Tingkat Mortalitas": ""}, index=[5])
final_data4 = pd.concat([final_data4, line], ignore_index=False)
final_data4 = final_data4.sort_index()
final_data4 = final_data4.rename(index={5: ""})
final_data4 = final_data4.style.apply(highlight_rows, axis=1)

# Data Process End
st.title("Analisis Pengaruh Konsumsi Daging Merah Terhadap Peningkatan Risiko Penyakit")
st.subheader(
    "Kasus CVD (Cardiovascular Disease), Kanker, CRD (Chronic Respiratory Diseases), dan Diabetes"
)
st.write("Oleh Bayu Setiawan")
st.markdown("""---""")
with st.sidebar:
    tabs = on_hover_tabs(
        tabName=["Data Analytics", "Raw Data", "Processed Data"],
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

elif tabs == "Data Analytics":
    st.header("Pendahuluan")
    col1, col2, col3 = st.columns([2, 2, 2])
    with st.container():
        with col2:
            st.write(
                "Daging adalah sumber nutrisi yang penting yaitu protein, zat besi, seng, dan vitamin B12. Namun banyak media maupun tulisan di media sosial memberitakan mengenai daging merah yang dapat menaikkan risiko kanker, di berbagai jurnal, kemenkes maupun WHO (Organisasi Kesehatan Dunia). WHO mengatakan bahwa daging merah sebagai penyebab kanker (Grup 2a karsinogen) dan daging olahan sebagai penyebab 'pasti' kanker (kelompok 1 karsinogen). Istilah 'daging merah' termasuk daging sapi, daging sapi muda, babi, domba, dan kambing. Daging olahan mengacu pada daging yang telah melalui pengasinan, pengawetan, fermentasi, pengasapan, atau proses lain yang bertujuan untuk meningkatkan rasa atau meningkatkan daya tahan."
                "Banyak pemberitaan di media yang menyatakan jika konsumsi daging merah yang terlalu banyak dapat meningkatkan risiko kanker"
            )
        with col1:
            st.image("https://www.freeiconspng.com/uploads/meat-png-0.png")
        with col3:
            st.image("Screenshot 2023-10-20 193559.png")
    st.subheader("Hipotesis")
    st.write(
        " Berdasarkan informasi yang telah diperoleh, untuk sementara kita ambil hipotesis bahwa semakin banyak daging merah yang dikonsumsi maka semakin tinggi risiko kanker yang akan dialami oleh setiap individu."
    )
    st.markdown("""---""")

    st.header("Data yang digunakan")
    col1, col2, col3 = st.columns([1, 1, 1])
    with st.container():
        with col1:
            st.table(final_data2)
        with col2:
            st.table(final_data3)
        with col3:
            st.table(final_data4)
    st.markdown("""---""")

    col1, col2 = st.columns([1, 1])
    with st.container():
        with col1:
            fig = px.choropleth(
                final_data,
                locations="location",
                locationmode="ISO-3",
                color="meat_total",
                hover_name="country_name",
                color_continuous_scale=px.colors.sequential.Blues,
                width=700,
            )
            fig.update_layout(
                coloraxis_colorbar=dict(
                    title="Konsumsi Daging Kg/kapita",
                    tickvals=[10, 20, 30, 40],
                    ticktext=["Rendah", "Cukup Rendah", "Cukup Tinggi", "Tinggi"],
                    dtick=4,
                ),
            )
            st.write(fig)
        with col2:
            fig = px.choropleth(
                disease,
                locations="Country Code",
                locationmode="ISO-3",
                color="2017",
                hover_name="Country Name",
                color_continuous_scale=px.colors.sequential.Blues,
                width=700,
            )
            fig.update_layout(
                coloraxis_colorbar=dict(
                    title="Tingkat Mortalitas %",
                    tickvals=[10, 22, 37, 50],
                    ticktext=["Rendah", "Cukup Rendah", "Cukup Tinggi", "Tinggi"],
                    dtick=4,
                ),
            )
            st.write(fig)

    st.header("Analisis Data")
    col1, col2 = st.columns([3, 1])
    with st.container():
        with col1:
            fig = px.scatter(
                final_data,
                x="mortality",
                y="meat_total",
                trendline="lowess",
                trendline_options=dict(frac=1),
                custom_data=["country_name", "mortality", "meat_total"],
                width=900,
                height=600,
            )
            fig.update_layout(
                xaxis_title="Mortalitas (%)",
                yaxis_title="Konsumsi Daging (Kg/kapita per tahun)",
            )
            fig.update_traces(
                hovertemplate="Negara: %{customdata[0]}<br>Mortalitas: %{customdata[1]} % <br>Konsumsi Daging: %{y} Kg/kapita per tahun",
                marker_size=final_data.marker1,
                marker_color=final_data.color1,
            )
            st.write(fig)

        with col2:
            "Berdasarkan pola data, konsumsi daging merah yang lebih tinggi justru mengurangi risiko terkena penyakit kanker maupun cvd."
            ":red[1]. Dari kelima negara dengan jumlah konsumsi daging merah terbanyak. terdapat 4 negara yang tidak mengikuti pola dikarenakan konsumsi daging merah yang terlalu banyak"
            ":blue[2]. Indonesia sendiri malah berada di posisi nomor 3 terbawah dalam konsumsi daging merah dan nomor 4 negara dengan mortality rate tinggi dari data yang dianalisis."
            ":green[3]. Australia sebagai salah satu negara dengan konsumsi daging terbanyak tetap menjaga tingkat kesehatan penduduknya dengan teknologi pengolahan daging dan teknologi kesehatan"
    st.markdown("""---""")
    col1, col2, col3 = st.columns(3)
    col1.metric("Konsumsi per Hari", "70g")
    col2.metric("Konsumsi per Tahun", "2.55kg")
    st.markdown("""---""")

    col1, col2 = st.columns([1, 3])
    with st.container():
        with col2:
            fig = px.scatter(
                data_frame=final_data,
                x="mortality",
                y="hospital_bed",
                trendline="lowess",
                trendline_options=dict(frac=1),
                custom_data=["country_name", "mortality", "hospital_bed"],
                width=900,
                height=600,
            )
            fig.update_layout(
                xaxis_title="Mortalitas (%)",
                yaxis_title="Fasilitas Kesehatan (per 1000 individu)",
            )
            fig.update_traces(
                hovertemplate="Negara: %{customdata[0]} <br>Mortalitas: %{customdata[1]} % <br>Fasilitas Kesehatan: %{customdata[2]} per 1000 individu",
                marker_size=final_data.marker2,
                marker_color=final_data.color2,
            )
            st.write(fig)
        with col1:
            "Terdapat beberapa negara yang tidak mengikuti pola dimana jika jumlah fasilitas kesehatan memadai maka risiko kematian akibat kanker juga berkurang."
            ":red[1]. Argentina dan Khazakstan memiliki jumlah fasilitas kesehatan yang memadai namun tingkat mortalitasnya relatif tinggi, berhubungan dengan data sebelumnya hal ini bisa diakibatkan konsumsi daging kedua negara tersebut terlalu tinggi."
            ":red[2]. Untuk rusia dan ukraina meskipun konsumsi daging tidak terlalu tinggi namun bisa diakibatkan oleh gaya hidup tidak sehat yang lain seperti konsumsi alkohol"
            ":blue[3]. Indonesia sendiri jumlah fasilitas kesehatannya sedikit jika dibandingan jumlah penduduk Indonesia yang banyak."
            "Jadi faktor konsumsi daging merah terhadap risiko kanker dapat terlihat juga pada dataset lain yang menyebabkan adanya pencilan pada data."
    st.markdown("""---""")

    st.header("Kesimpulan dan Solusi")
    "1. Berdasarkan data konsumsi daging merah yang semakin tinggi justru mengurangi risiko kanker selama konsumsinya tidak melebihi batas wajar."
    "2. Batas Konsumsi daging merah yang direkomendasikan untuk orang sehat adalah 2.55kg/tahun atau 70 g/hari sesuai dengan pedoman Nutrisi dari Rock dkk."
    "3. Posisi Indonesia sendiri berada di posisi tiga dengan konsumsi daging merah paling sedikit yaitu hanya 1.04 Kg per kapita per tahun dan berada di posisi nomor 4 tingkat mortalitas tertinggi dari data."
    "4. Untuk indonesia seharusnya lebih dianjurkan untuk mengkonsumsi daging merah lebih banyak untuk kebutuhan gizi"

elif tabs == "Processed Data":
    st.header("Dataset yang telah diproses")
    st.dataframe(final_data)
    st.write(
        "Dataset dibersihkan dengan mengjilangkan bagian yang tidak terpakai terlebih dahulu. Tahun 2017 merupakan tahun dimana hampir setiap negara memiliki data yang dibutuhkan dan merupakan tahun yang paling baru, Sehingga digunakanlah data tahun 2017."
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
