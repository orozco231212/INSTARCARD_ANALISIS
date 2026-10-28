import nbformat
from nbclient import NotebookClient

nb_path = "notebooks/00_entorno.ipynb"
with open(nb_path, encoding="utf-8") as f:
    nb = nbformat.read(f, as_version=4)

client = NotebookClient(nb, timeout=600, kernel_name="python3")
client.execute()
print("Notebook executed successfully")
