from ast import mod
from langchain_openai import OpenAIEmbeddings
from dotenv import load_dotenv
from pandas.core.internals.blocks import new_block
from sklearn.metrics.pairwise import cosine_similarity
import numpy as np

load_dotenv()

document = [
    "Diwali is the Hindu festival of lights symbolizing good’s triumph over evil, celebrated with diyas, fireworks, sweets, and family gatherings.",
    "Holi, the festival of colors, celebrates the arrival of spring, joy, and the victory of good over evil with vibrant powders and music.",
    "Lohri is a Punjabi harvest festival marking winter’s end, featuring bonfires, singing, dancing, and sharing traditional foods with community spirit.",
    "Dussehra marks Lord Rama’s victory over demon Ravana, symbolizing the triumph of good over evil, celebrated with plays, effigies, and festivities."
];

query = "Tell me about Holi";

embedding = OpenAIEmbeddings(model="text-embedding-3-small", dimensions=32);

user_query = embedding.embed_query(query);

print(str(user_query));

document_embedding = embedding.embed_documents(document);

print(str(document_embedding));

result = cosine_similarity([user_query], document_embedding)[0];

index , score = sorted(list(enumerate(result)), key=lambda x: x[1])[-1];

print(document[index]);