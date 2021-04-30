from flask import Flask
import markdown
import pandas as pd
from glob import glob

arquivo = open('docs/aulas.md', 'r')
mark = arquivo.read()
html5 = markdown.markdown(mark)
app = Flask(__name__)
print(html5)


@app.route('/')
def raiz():
    return html5


app.run(debug=True)
