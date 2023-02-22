from abydos.phonetic import RussellIndex
import pandas as pd
import streamlit as st
from functionforDownloadButtons import download_button

def _max_width_():
    max_width_str = f"max-width: 1800px;"
    st.markdown(
        f"""
    <style>
    .reportview-container .main .block-container{{
        {max_width_str}
    }}
    </style>    
    """,
        unsafe_allow_html=True,
    )

st.set_page_config(page_icon="✂️", page_title="Lookalike record check")


c2, c3 = st.columns([6, 1])


with c2:
    c31, c32 = st.columns([12, 2])
    with c31:
        st.caption("")
        st.title("Email Check")
    with c32:
        st.image(
            "images/logo.png",
            width=200,
        )

uploaded_file = st.file_uploader(
    " ",
    key="1",
    help="To activate 'wide mode', go to the hamburger menu > Settings > turn on 'wide mode'",
)

if uploaded_file is not None:
    df = pd.read_csv(uploaded_file)
    uploaded_file.seek(0)


    file_container = st.expander("Check your uploaded .csv")
    file_container.write(df)


else:
    st.info(
        f"""
            👆 Upload a .csv file first. Sample to try: [biostats.csv](https://people.sc.fsu.edu/~jburkardt/data/csv/biostats.csv)
            """
    )

    st.stop()

encode_list = []
re = RussellIndex()

def find_lookAlikeImages(column_name):

    for index, rows in df.iterrows():
        encode_ = re.encode(rows[column_name])
        encode_list.append(encode_)

    df['Encode-scores'] = encode_list
    duplicates = df[df.duplicated(subset=['Encode-scores'], keep=False)]
    return duplicates


form = st.form(key="annotation")
with form:

    column_name = st.selectbox(
        "Column name:", list(df.columns)
    )
    submitted = st.form_submit_button(label="Submit")

result = pd.DataFrame()
if submitted:

    result = find_lookAlikeImages(column_name)
    c29, c30, c31 = st.columns([1, 1, 2])

    with c29:
        CSVButton = download_button(
            result,
            "FlaggedFile.csv",
            "Download to CSV",
        )



#a = re.encode("nidugrssk@gmail.com")
#b = re.encode("nida_ugur_sisik@gmail.com")


