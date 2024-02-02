from fastapi import FastAPI, HTTPException
from fastapi.staticfiles import StaticFiles
from typing import List
from main import find_relevant_images  # Ensure this is correctly importing your function

from fastapi.responses import HTMLResponse

app = FastAPI()

# Mount the 'Bilder' directory as a static files route
app.mount("/bilder", StaticFiles(directory="Bilder"), name="bilder")

@app.get("/search/")
async def search_images(query: str) -> List[str]:
    try:
        image_paths = find_relevant_images(query)
        # Convert local paths to URLs
        # Assuming image_paths contains file paths with backslashes
        # Assuming image_paths contains file paths with backslashes
        # Assuming `image_paths` contains file paths that use backslashes
        image_urls = ["/bilder/" + "/".join(path.split('\\')[1:]) for path in image_paths]




        return image_urls
    except Exception as e:
        raise HTTPException(status_code=500, detail=str(e))


@app.get("/show-images/")
async def show_images(query: str):
    image_paths = await search_images(query)
    images_html = "".join([f"<img src='{path}' style='width:200px;' />" for path in image_paths])
    return HTMLResponse(f"<html><body>{images_html}</body></html>")