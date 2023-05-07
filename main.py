import streamlit as st
from langchain.vectorstores import DeepLake
from langchain import PromptTemplate, LLMChain
from langchain.llms import OpenAI
from langchain.embeddings.openai import OpenAIEmbeddings


embeddings = OpenAIEmbeddings()
db = DeepLake(dataset_path="./my_deeplake/", embedding_function=embeddings, read_only=True)

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
    ans = db.similarity_search(query,k=5)
    context = ""
    for i in range(5):
        context += ans[i].page_content
        context += "\n"
    llm = OpenAI(temperature=0)
    template="""Please use the following context to answer questions.
    Context: {context}
    Question: {query}
    Answer:"""

    prompt = PromptTemplate(template=template, input_variables=["context","query"])
    llm_chain = LLMChain(prompt=prompt, llm=llm)
    st.write(llm_chain.predict(context = context, query = query))