import webbrowser
from pathlib import Path

html_file = Path("index.html").resolve()

webbrowser.open(html_file.as_uri())