import glob
import markdown
from flask import Flask

file_list = glob.glob(
    'E:/MeusProjetos/Projeto-Markdown/Markdown-e-Python/venv/docs/files/*.md*')
print(file_list)

lista = []

path = "E:/MeusProjetos/Projeto-Markdown/Markdown-e-Python/venv/docs/files/*.md"
app = Flask(__name__)

for file in glob.glob(path):
    arquivo = open(file, 'r')
    mark = arquivo.read()
    html = markdown.markdown(mark)
    lista.append(html)
    print(file)
    print(html)


@app.route('/')
def raiz():
    return '{}'.format(lista)


app.run(debug=True)
