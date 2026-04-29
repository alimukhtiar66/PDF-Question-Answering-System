import streamlit as st
from Pdf_QA_System import extract_text, cosine_search


st.title("PDF Question Answering System")

uploaded_file = st.file_uploader("Upload PDF", type="pdf")

if uploaded_file is not None:

    st.success("PDF uploaded!")

    if "text" not in st.session_state:
        st.session_state.text = extract_text(uploaded_file)

    query = st.text_input("Ask question")

    if st.button("Search"):
        if query:
            answer = cosine_search(query, st.session_state.text)

            st.subheader("Answer:")
            st.write(answer)
        else:
            st.warning("Please enter a question")