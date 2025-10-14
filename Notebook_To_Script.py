#!/usr/bin/env python3
import nbformat
import sys
from pathlib import Path


def notebook_to_python(notebook_path, output_path=None):
    """
    Converts a Jupyter notebook (.ipynb) to a Python script (.py).
    Parameters:
        notebook_path (str or Path): Path to the input Jupyter notebook file.
        output_path (str or Path, optional): Path to the output Python script file.
            If None, the output file will have the same name as the notebook with a .py extension.
    Returns:
        None
    Side Effects:
        Writes the extracted code cells from the notebook to the specified Python script file.
        Prints a confirmation message upon successful conversion.
    Notes:
        - Only code cells are extracted; markdown and other cell types are ignored.
        - Comments within code cells are preserved.
    """
    notebook_path = Path(notebook_path)

    # Default output: same name with .py extension
    if output_path is None:
        output_path = notebook_path.with_suffix(".py")

    # Load the notebook
    nb = nbformat.read(notebook_path, as_version=4)

    with open(output_path, "w", encoding="utf-8") as f:
        for cell in nb.cells:
            if cell.cell_type == "code":
                f.write(cell.source + "\n\n")  # preserves comments inside code

    print(f"✅ Notebook converted to Python script: {output_path}")


if __name__ == "__main__":
    if len(sys.argv) < 2:
        print("Usage: python nb_to_py.py <notebook.ipynb> [output.py]")
        sys.exit(1)

    notebook_file = sys.argv[1]
    output_file = sys.argv[2] if len(sys.argv) > 2 else None

    notebook_to_python(notebook_file, output_file)
