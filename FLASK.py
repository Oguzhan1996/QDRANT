from flask import Flask, render_template_string, request
from main import find_relevant_images  

app = Flask(__name__, static_folder='Bilder')

@app.route('/', methods=['GET', 'POST'])
def index():
    if request.method == 'POST':
        query = request.form.get('query')
        image_paths = find_relevant_images(query)
        # Generate the full URLs for each image
        image_urls = [f"/{path}" for path in image_paths]
        return render_template_string('''
            <html>
                <head>
                    <title>Image Search</title>
                </head>
                <body>
                    <form action="/" method="post">
                        <input type="text" name="query" />
                        <input type="submit" value="Search" />
                    </form>
                    {% for url in image_urls %}
                        <img src="{{ url }}" style="max-width:100%;" />
                    {% endfor %}
                </body>
            </html>
        ''', image_urls=image_urls)
    return render_template_string('''
        <html>
            <head>
                <title>Image Search</title>
            </head>
            <body>
                <form action="/" method="post">
                    <input type="text" name="query" />
                    <input type="submit" value="Search" />
                </form>
            </body>
        </html>
    ''')

if __name__ == '__main__':
    app.run(debug=True)
