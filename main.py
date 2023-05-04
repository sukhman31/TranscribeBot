import streamlit as st
from langchain.text_splitter import RecursiveCharacterTextSplitter
from langchain.document_loaders import TextLoader
from langchain.vectorstores import Chroma
from langchain import PromptTemplate, LLMChain, OpenAI


loader = TextLoader('video_transcription/final_file')
docs = loader.load()
text_splitter = RecursiveCharacterTextSplitter(chunk_size=1000,chunk_overlap=0)
docs = text_splitter.split_documents(docs)
db = Chroma.from_documents(docs)

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
    ans = db.similarity_search(query,k=1)
    ans = ans[0].page_content
    llm = OpenAI(temperature=0)
    template="""Please use the following context to answer questions.
    Context: {ans}
    Question: {query}
    Answer:"""

    prompt = PromptTemplate(template=template, input_variables=["ans","query"])
    llm_chain = LLMChain(prompt=prompt, llm=llm)
    st.write(llm_chain.predict(ans = ans, query = query))