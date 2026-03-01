from youtube_transcript_api import YouTubeTranscriptApi
from langchain_openai import ChatOpenAI , OpenAIEmbeddings
from dotenv import load_dotenv
from langchain_community.vectorstores import FAISS
from langchain_text_splitters import RecursiveCharacterTextSplitter
from langchain_core.prompts import PromptTemplate

load_dotenv()

model = ChatOpenAI(model="gpt-4.1-nano", temperature=0.7);
embedding = OpenAIEmbeddings();

video_id = "bL92ALSZ2Cg";

# UrsmFxEIp5k
# bL92ALSZ2Cg

def translate(text, lang):
    
    prompt = PromptTemplate(template="Translate the text : {text} to new language : {newlang}", input_variables=["text", "newlang"]);
    chain = prompt | model;

    result = chain.invoke({"text": text, "newlang": lang});

    return result.content;

def splitter(transcript):
    spl = RecursiveCharacterTextSplitter(chunk_size=1000, chunk_overlap=200);
    chunks = spl.split_text(transcript);
    return chunks;

def generate_transcript(video_id, translate_to):
    
    ytt = YouTubeTranscriptApi();

    try:

        transcript_list = ytt.list(video_id=video_id);
        transcript_list = list(transcript_list);
        final_transcript = "";

        if len(transcript_list) == 1:
            print("Only one Transcript is available for this video .");

            print(f"Language : {transcript_list[0].language} | Language Code : {transcript_list[0].language_code} | Is_translatable : {transcript_list[0].is_translatable}");
        
            if transcript_list[0].language_code == translate_to and transcript_list[0].is_translatable:
                text = transcript_list[0].fetch();
                
                final_transcript = " ".join(t.text for t in text);
            
            else:

                text = transcript_list[0].fetch();

                text = " ".join(t.text for t in text);

                final_transcript = translate(text, translate_to);

        else:
            print("Below are the transcripts available for the video .");
            found = False;
            for transcript in transcript_list:
                print(f"Language : {transcript.language} | Language Code : {transcript.language_code} | Is_translatable : {transcript.is_translatable}");
                if transcript.language_code == translate_to and transcript.is_translatable:
                    text = transcript.fetch();
                    final_transcript = " ".join(t.text for t in text);
                    found = True
                    break;
            if not found:
                first = transcript_list[0]
                text = first.fetch();

                text = " ".join(t.text for t in text);
                final_transcript = translate(text, translate_to);

    
    except Exception as e:

        print(str(e));
        exit();
    return final_transcript;


if __name__ == "__main__":

    ## Document ingestion / Document Loading
    final_transcript = generate_transcript(video_id, "fr");

    # print(final_transcript);

    ## Text Splitting / Chunking
    chunks = splitter(final_transcript);

    # print(len(chunks));

    ## Store to vector Store
    vector_store = FAISS.from_texts(texts=chunks, embedding=embedding);

    ## Retreival
    context = "";
    query = "How can we load text and pdf files ? ?"

    retreiver = vector_store.as_retriever(search_type="similarity", search_kwargs={"k": 2});

    docs = retreiver.invoke(query)
    
    for doc in docs:
        context = context + doc.page_content;

    # print(context);
    ## Augmentation

    template = "Based on the context : {context}. Answer the query : {query}. If you dont know anything , simply say i dont know.";

    prompt = PromptTemplate(template=template, input_variables=["context", "query"]);

    ## Generation

    chain = prompt | model;

    result = chain.invoke({"context": context, "query": query});

    print(result.content);