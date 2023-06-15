import streamlit as st
import pandas as pd
import numpy as np
from st_on_hover_tabs import on_hover_tabs
import matplotlib.pyplot as plt
import altair as alt
import plotly.express as px

st.set_page_config(page_title="Capstone Project Bayu Setiawan", layout="wide")

st.markdown("<style>" + open("./style.css").read() + "</style>", unsafe_allow_html=True)
st.markdown("""---""")
# Data Process

def highlight_rows(x):
    if x['Negara'] == 'Indonesia':
        return ['background-color : #4DD0E1']*2
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
final_data2.rename(columns = {'meat_total':'Konsumsi Daging Merah', 'country_name':'Negara'}, inplace=True)
final_data2 = final_data2[["Negara","Konsumsi Daging Merah"]]
final_data2.index = np.arange(1, len(final_data2) + 1)
final_data2 = final_data2.iloc[np.r_[0:4, -8:0]]
line = pd.DataFrame({"Negara": "", "Konsumsi Daging Merah": ""}, index=[5])
final_data2 = pd.concat([final_data2, line], ignore_index=False)
final_data2 = final_data2.sort_index()
final_data2 = final_data2.rename(index={5: ''})
final_data2 = final_data2.style.apply(highlight_rows, axis = 1)

final_data3 = final_data.sort_values(
    by=["hospital_bed"], ignore_index=True, ascending=False
)
final_data3.rename(columns = {'hospital_bed':'Ketersediaan Fasilitas Kesehatan', 'country_name':'Negara'}, inplace=True)
final_data3 = final_data3[["Negara", "Ketersediaan Fasilitas Kesehatan"]]
final_data3.index = np.arange(1, len(final_data3) + 1)
final_data3 = final_data3.iloc[np.r_[0:4, -8:0]]
line = pd.DataFrame({"Negara": "", "Ketersediaan Fasilitas Kesehatan": ""}, index=[5])
final_data3 = pd.concat([final_data3, line], ignore_index=False)
final_data3 = final_data3.sort_index()
final_data3 = final_data3.rename(index={5: ''})
final_data3 = final_data3.style.apply(highlight_rows, axis = 1)

final_data4 = final_data.sort_values(
    by=["mortality"], ignore_index=True, ascending=False
)
final_data4.rename(columns = {'mortality':'Tingkat Mortalitas', 'country_name':'Negara'}, inplace=True)
final_data4 = final_data4[["Negara","Tingkat Mortalitas"]]
final_data4.index = np.arange(1, len(final_data4) + 1)
final_data4 = final_data4.iloc[np.r_[0:4, -8:0]]
line = pd.DataFrame({"Negara": "", "Tingkat Mortalitas": ""}, index=[5])
final_data4 = pd.concat([final_data4, line], ignore_index=False)
final_data4 = final_data4.sort_index()
final_data4 = final_data4.rename(index={5: ''})
final_data4 = final_data4.style.apply(highlight_rows, axis = 1)

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
    st.header("Pendahuluan")
    col1, col2 = st.columns([4, 2])
    with st.container():
        with col1:
            st.write("Daging adalah sumber nutrisi yang penting yaitu protein, zat besi, seng, dan vitamin B12. Namun banyak media maupun tulisan di media sosial memberitakan mengenai daging merah yang dapat menaikkan risiko kanker, di berbagai jurnal, kemenkes maupun WHO (Organisasi Kesehatan Dunia). WHO mengatakan bahwa daging merah sebagai penyebab kanker (Grup 2a karsinogen) dan daging olahan sebagai penyebab 'pasti' kanker (kelompok 1 karsinogen). Istilah 'daging merah' termasuk daging sapi, daging sapi muda, babi, domba, dan kambing. Daging olahan mengacu pada daging yang telah melalui pengasinan, pengawetan, fermentasi, pengasapan, atau proses lain yang bertujuan untuk meningkatkan rasa atau meningkatkan daya tahan.")
            st.subheader("Hipotesis")
            st.write(" Berdasarkan informasi yang telah diperoleh, untuk sementara kita ambil hipotesis bahwa semakin banyak daging merah yang dikonsumsi maka semakin tinggi risiko kanker yang akan dialami oleh setiap individu.")        
        with col2:
            st.image('https://www.freeiconspng.com/uploads/meat-png-0.png')
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
    
    st.header("Analisis Data")
    col1, col2 = st.columns([3, 1])
    with st.container():
        with col1:
            fig = px.scatter(
                x=final_data["mortality"],
                y=final_data["meat_total"],
                trendline="ols",
                text=final_data["country_name"],
                width=900,
                height=600,
            )
            fig.update_layout(
                xaxis_title="Mortalitas (%)",
                yaxis_title="Konsumsi Daging (Kg/kapita per tahun)",
                uniformtext_mode='hide',
            )
            fig.update_traces(
                hovertemplate="Negara: %{text} <br>Mortalitas: %{x} % <br>Konsumsi Daging: %{y} Kg/kapita per tahun",
                marker_size=8,
            )
            st.write(fig)
        with col2:
            "1. Berdasarkan pola data, konsumsi daging merah yang lebih tinggi justru mengurangi risiko terkena penyakit kanker maupun cvd."
            "2. Terdapat 4 Negara dengan konsumsi daging merah yang tinggi jika dibandingkan dengan negara lain yaitu Argentina, Australia, Khazakstan dan Brazil."
            "3. Dari keempat negara dengan jumlah konsumsi daging merah terbanyak. terdapat 3 negara yang tidak mengikuti pola dikarenakan konsumsi daging merah yang terlalu banyak"
            "3. Indonesia sendiri malah berada di posisi nomor 2 terbawah dalam konsumsi daging merah dan nomor 4 negara dengan mortality rate tinggi dari data yang dianalisis."
    st.markdown("""---""")
    col1, col2, col3 = st.columns(3)
    col1.metric("Konsumsi per Hari", "70g")
    col1.metric("Konsumsi per Tahun", "2.55kg")
    col2.write("Rock, C.L., Thomson, C.A., Sullivan, K.R., Howe, C.L., Kushi, L.H., Caan, B.J., Neuhouser, M.L., Bandera, E.V., Wang, Y., Robien, K. and Basen‐Engquist, K.M., 2022. American Cancer Society nutrition and physical activity guideline for cancer survivors. CA: A Cancer Journal for Clinicians, 72(3), pp.230-262.")
    col3.write("Aulawi, T., 2013. Hubungan konsumsi daging merah dan gaya hidup terhadap risiko kanker kolon. Kutubkhanah, 16(1), pp.37-45.")
    st.markdown("""---""")

    col1, col2 = st.columns([1, 3])
    with st.container():
        with col2:
            fig = px.scatter(
                x=final_data["mortality"],
                y=final_data["hospital_bed"],
                trendline="ols",
                text=final_data["country_name"],
                width=900,
                height=600,
            )
            fig.update_layout(
                xaxis_title="Mortalitas (%)",
                yaxis_title="Fasilitas Kesehatan (per 1000 individu)",
            )
            fig.update_traces(
                hovertemplate="Negara: %{text} <br>Mortalitas: %{x} % <br>Fasilitas Kesehatan: %{y} per 1000 individu",
                marker_size=8,
            )
            st.write(fig)
        with col1:
            "1. Australia, Argentina dan Brazil dapat mengatasi kenaikan risiko akibat konsumsi daging merah yang banyak dikarenakan jumlah fasilitas Kesehatan yang memadai. Sehingga mortality ratenya masih di atas median dan mengikuti pola jumlah fasilitas kesehatan dan tingkat mortalitas."
            "2. Untuk Khazakstan meskipun jumlah fasilitas Kesehatan banyak namun tingkat mortalitasnya cukup tinggi sehingga tidak sesuai dengan pola. hal ini dimungkinkan terjadi karena konsumsi daging merah yang terlalu banyak maupun terdapat faktor yang belum teridentifikasi seperti rusia yang tingkat mortalitasnya tinggi meskipun terdapat fasilitas kesehatan yang memadai."
            "3. Indonesia sendiri jumlah fasilitas kesehatannya sedikit jika dibandingan jumlah penduduk Indonesia yang banyak."
    st.markdown("""---""")

    st.header("Kesimpulan dan Solusi")
    "1. Berdasarkan data konsumsi daging merah yang semakin tinggi justru mengurangi resiko kanker selama konsumsinya tidak melebihi batas wajar. Ini dikarenakan daging merah kaya protein dan vitamin yang baik untuk menjaga kesehatan tubuh."
    "2. Memang benar menurut penelitian daging merah dapat meningkatkan risiko kanker, namun hal itu terjadi jika terlalu banyak dikonsumsi. Menurut pedoman dari Rock et al., jumlah daging merah yang direkomendasikan untuk orang sehat adalah 500 g/minggu atau 70 g/hari."
    "3. Posisi Indonesia sendiri berada di posisi dua dengan konsumsi daging merah paling sedikit yaitu hanya 1.04 Kg per kapita per tahun dan berada di posisi nomor 4 tingkat mortalitas tertinggi dari data."
    "4. Pemberitaan mengenai peningkatan resiko kanker dan cvd akibat konsumsi daging merah di Indonesia kurang tepat untuk diimplementasikan. Seharusnya malah sebaliknya yaitu anjuran untuk mengkonsumsi daging merah yang kaya protein untuk memenuhi kebutuhan gizi yang baik namun tetap memberikan anjuran agar tidak melebihi batas konsumsi."
    "5. Pemerintah juga perlu meningkatkan kapasitas fasilitas Kesehatan untuk mengimbangi konsumsi daging untuk menghindari hal hal yang tidak diinginkan mengingat Indonesia berada di nomor 8 terbawah mengenai ketersediaan fasilitas Kesehatan."

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
