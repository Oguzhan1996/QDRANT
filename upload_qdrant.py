import pickle
from qdrant_client import QdrantClient
from qdrant_client.http.models import PointStruct
import uuid

# Load image embeddings from pickle file
with open('image_embeddings.pkl', 'rb') as f:
    image_embeddings = pickle.load(f)

print(f"Loaded {len(image_embeddings)} image embeddings.")

# Initialize Qdrant client
client = QdrantClient(host="localhost", port=6333)

# Define a new collection name
new_collection_name = "oguzhan_collection"

# Ensure the new collection is created
try:
    client.create_collection(
        collection_name=new_collection_name,
        vectors_config={"size": 512, "distance": "Cosine"}
    )
    print(f"Collection '{new_collection_name}' created successfully.")
except Exception as e:
    print(f"Collection '{new_collection_name}' already exists or error in creation: {e}")

# Function to generate a unique integer ID
def generate_unique_id():
    return int(uuid.uuid4().int & (1<<64)-1)

# Upserting points to the new collection
for index, (image_path, embedding) in enumerate(image_embeddings):
    try:
        unique_id = generate_unique_id()  # Generate a unique integer ID
        point = PointStruct(
            id=unique_id,  # Use the generated unique ID
            vector=embedding.tolist(),
            payload={"original_id": image_path, "path": image_path}  # Include original ID in the payload
        )

        # Perform the upsert operation
        client.upsert(collection_name=new_collection_name, points=[point])
        print(f"Upsert successful for {image_path}")

    except Exception as e:
        print(f"Error during upsert for {image_path}: {e}")

print("Finished upserting points to the new collection.")
