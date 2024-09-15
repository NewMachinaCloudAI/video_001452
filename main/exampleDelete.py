import time
from pinecone import Pinecone, ServerlessSpec

pc = Pinecone(
    api_key="YOUR-API-KEY"
)

# Get python object reference to Index
index = pc.Index("my-index")

# Delete vectors with id equal to 'A' and 'B'
index.delete(ids=["A", "B"])

# Fetch all of hte original vectors
results = index.fetch(["A", "B", "C", "D"])

# Print the results from fetch operation
print( results )