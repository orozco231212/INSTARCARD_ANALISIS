import json, sys
from pathlib import Path

nb_path = Path(__file__).resolve().parent / "instacart-analisis" / "notebooks" / "00_entorno.ipynb"
if not nb_path.exists():
    print(f"No se encontro el notebook en: {nb_path}")
    sys.exit(1)

with open(nb_path, encoding='utf-8') as f:
    nb = json.load(f)
ns = {}
for i, cell in enumerate(nb['cells']):
    if cell['cell_type'] == 'code':
        src = ''.join(cell['source'])
        print(f"--- Executing cell {i} (id={cell.get('id')}) ---")
        try:
            exec(compile(src, f"cell_{i}", 'exec'), ns)
            print("OK")
        except Exception as e:
            import traceback
            traceback.print_exc()
            print("FAILED")
            break