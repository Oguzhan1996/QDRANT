# Text2Image Search System

## System Architecture Overview

This system is designed to perform semantic image retrieval based on textual queries. Utilizing the CLIP (Contrastive Language-Image Pretraining) model, it generates embeddings for text queries and images within a dataset, allowing for effective and efficient similarity searches.

### Backend Components

#### Embed_images.py

- **Description**: Manages the generation of embeddings for the dataset images using the CLIP model.
- **Functionality**: Encodes images into embeddings which are stored for later search comparisons.

#### Upload_qdrant.py

- **Description**: Responsible for uploading the generated embeddings and image metadata into the Qdrant vector database.
- **Functionality**: Ensures embeddings are stored in Qdrant, ready for similarity searches.

#### Main.py

- **Description**: Acts as the central API endpoint for the system.
- **Functionality**: Handles user text queries, performs vector searches in Qdrant, and returns the most relevant image results.

#### FAST_API.py

- **Description**: Provides a FastAPI server setup to serve the Text2Image search functionality over a REST API.
- **Functionality**: Interfaces with `main.py` to accept queries and return image results through HTTP requests.

### Frontend

A minimalistic frontend that allows users to enter text queries and displays relevant image results fetched from the backend.

### Setup and Run Instructions

#### Installation

# Text2ImageSearch

## Installation

Clone this repository to your desired location:

```bash
git clone https://github.com/Oguzhan1996/Text2ImageSearch.git


Navigate to the project directory and install the required Python packages:

cd Text2ImageSearch
pip install -r requirements.txt


    Ensure Qdrant is running. If not, start your Qdrant instance as per the official documentation.

Running the Application

Generate and Upload Image Embeddings:

python embed_images.py
python upload_qdrant.py


python embed_images.py
python upload_qdrant.py

    Start the FastAPI server:

uvicorn FAST_API:app --reload


The server will be available at http://127.0.0.1:8000. Use endpoints like /search/?query=<your-query> to perform searches.
