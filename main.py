import streamlit as st

st.set_page_config(page_title="Andrej Karpathy Chat Bot", page_icon=":robot:")
st.header('Andrej Karpathy Bot')

col1, col2 = st.columns(2)



with col1:
    st.markdown("Our chatbot provides a comprehensive guide to all of Andrej \
                Karpathy's videos on deep learning. Whether you're new to the field or\
                an experienced practitioner, our chatbot will help you navigate through \
                the complexities of deep learning and artificial intelligence. \
                Our chatbot attempts to answer any queries you might have regarding \
                this [playlist](https://www.youtube.com/playlist?list=PLAqhIrjkxbuWI23v9cThsA9GvCAUhRvKZ).")


st.markdown("## Enter Your Query")

def get_text():
    input_text = st.text_area(label="Query", label_visibility='collapsed', placeholder="Your Query...", key="query_input")
    return input_text

query = get_text()

if query:
    st.write(query)