import torch
from transformers import CLIPProcessor, CLIPModel
from PIL import Image
from pathlib import Path
import pickle


# Initialize CLIP model
device = "cuda" if torch.cuda.is_available() else "cpu"
model = CLIPModel.from_pretrained("openai/clip-vit-base-patch32").to(device)
processor = CLIPProcessor.from_pretrained("openai/clip-vit-base-patch32")

# Function to generate embedding
def generate_embedding(image_path):
    image = Image.open(image_path).convert("RGB")
    inputs = processor(images=image, return_tensors="pt")
    inputs = {k: v.to(device) for k, v in inputs.items()}
    with torch.no_grad():
        outputs = model.get_image_features(**inputs)
    return outputs.cpu().numpy()[0]

# Directory containing images
image_folder = "Bilder"
image_embeddings = []

# Process each image and store its embedding
for image_file in Path(image_folder).rglob('*.[pj][np][g]'):
    embedding = generate_embedding(str(image_file))
    image_embeddings.append((str(image_file), embedding))
    
with open('image_embeddings.pkl', 'wb') as f:
    pickle.dump(image_embeddings, f)
    


