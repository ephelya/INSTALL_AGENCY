import os

def create_main_files(base_path):
    files = {
        "index.html": """
            <!DOCTYPE html>
            <html lang="{lang}">
            <head>
                <meta charset="UTF-8">
                <meta name="viewport" content="width=device-width, initial-scale=1.0">
                <title>{title}</title>
            </head>
            <body>
                <div id="root"></div>
                <script src="index.js"></script>
            </body>
            </html>
        """
    }

    for file_path, content in files.items():
        full_path = os.path.join(base_path, file_path)
        os.makedirs(os.path.dirname(full_path), exist_ok=True)
        with open(full_path, 'w') as f:
            f.write(content)
        print(f"File created: {full_path}")
