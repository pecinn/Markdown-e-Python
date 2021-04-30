import glob

file_list = glob.glob(
    'E:/MeusProjetos/Projeto-Markdown/Markdown-e-Python/venv/docs/files/*.md*')
print(file_list)

my_list = []

path = "E:/MeusProjetos/Projeto-Markdown/Markdown-e-Python/venv/docs/files/*.md*"
for file in glob.glob(path):
    print(file)
    my_list.append(file)

print(my_list[2])
