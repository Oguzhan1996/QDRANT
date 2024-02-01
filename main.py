from transformers import CLIPProcessor, CLIPModel
import matplotlib.pyplot as plt
import matplotlib.image as mpimg
from qdrant_client import QdrantClient
import numpy as np
import torch

# Initialize the CLIP model and processor
model_name = "openai/clip-vit-base-patch32"
device = "cuda" if torch.cuda.is_available() else "cpu"
model = CLIPModel.from_pretrained(model_name).to(device)
processor = CLIPProcessor.from_pretrained(model_name)

# Initialize Qdrant client
client = QdrantClient(host="localhost", port=6333)
collection_name = "oguzhan_collection"

def find_relevant_images(text_query, client, collection_name):
    # Convert text query to embedding
    inputs = processor(text=text_query, return_tensors="pt")
    inputs = {k: v.to(device) for k, v in inputs.items()}
    with torch.no_grad():
        text_features = model.get_text_features(**inputs)
    text_embedding = text_features.cpu().numpy()[0]

    # Search in Qdrant
    search_results = client.search(
        collection_name=collection_name,
        query_vector=text_embedding.tolist(),
        limit=10
    )

    # Retrieve images based on search results
    # Adjust this line according to the actual structure of the search result
    image_paths = [hit.payload['path'] for hit in search_results]

    return image_paths

'''for hit in search_results:
    print(hit)
    break'''


def display_images(image_paths):
    # Set up the matplotlib figure and axes
    fig, axes = plt.subplots(nrows=1, ncols=len(image_paths), figsize=(20, 10))
    if not isinstance(axes, np.ndarray):
        axes = [axes]
    for ax, image_path in zip(axes, image_paths):
        img = mpimg.imread(image_path)
        ax.imshow(img)
        ax.axis('off')  # Hide axes
    plt.show()

# Example usage
text_query = "red cat"
relevant_images_paths = find_relevant_images(text_query, client, collection_name)
display_images(relevant_images_paths)
