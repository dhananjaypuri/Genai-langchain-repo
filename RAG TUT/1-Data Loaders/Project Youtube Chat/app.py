from youtube_transcript_api import YouTubeTranscriptApi, TranscriptsDisabled
from langchain_openai import OpenAIEmbeddings, ChatOpenAI
from langchain_community.vectorstores import FAISS
from langchain_core.prompts import PromptTemplate
from langchain_text_splitters import RecursiveCharacterTextSplitter
from dotenv import load_dotenv

load_dotenv();
## Document Loading

video_id = "AOQyRiwydyo";

embeddings = OpenAIEmbeddings();
llm = ChatOpenAI(model="gpt-4.1-nano", temperature="0.7");

template = "Based on given context : {contt} , answer the following query : {query}. And if you are not aware just say I dont know .";
prompt = PromptTemplate(template=template, input_variables=["contt", "query"]);
ytt = YouTubeTranscriptApi();
transcript = ytt.fetch(video_id);

complete_transcript = "";

for doc in transcript:
    complete_transcript = complete_transcript + doc.text;

## Chunking
splitter = RecursiveCharacterTextSplitter(chunk_size=1000, chunk_overlap=200);

chunks = splitter.split_text(complete_transcript);

print(len(chunks));

## Embedding and storing to vector store

vector_stores = FAISS.from_texts(chunks, embedding=embeddings);


retreiver = vector_stores.as_retriever(search_type="similarity", search_kwargs={'k': 4});

query = "what are prompt templates in langchain";

context_docs = retreiver.invoke("what are prompt templates in langchain");

complete_context = "";

for context in context_docs:
    complete_context = complete_context + context.page_content;

chain = prompt | llm;

result = chain.invoke({"contt": complete_context, "query": query });

print(result.content);