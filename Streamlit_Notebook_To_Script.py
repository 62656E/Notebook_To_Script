import streamlit as st
from pathlib import Path
import nbformat
import sys
import streamlit.web.bootstrap as st_bootstrap

st.title("📓 Notebook → Python Script Converter")
st.write("""
Upload one or more Jupyter Notebooks, and this app will convert them to Python scripts.
Only code cells are kept (in-cell comments preserved), and markdown is removed.
""")

# Upload notebooks (multiple allowed)
uploaded_files = st.file_uploader(
    "Choose one or more .ipynb files", type="ipynb", accept_multiple_files=True)

if uploaded_files:
    for uploaded_file in uploaded_files:
        nb = nbformat.read(uploaded_file, as_version=4)

        # Automatically generate output filename with _clean suffix
        output_name = Path(uploaded_file.name).stem + "_clean.py"
        output_path = Path(output_name)

        # Write code cells only
        with open(output_path, "w", encoding="utf-8") as f:
            for cell in nb.cells:
                if cell.cell_type == "code":
                    f.write(cell.source + "\n\n")

        st.success(f"✅ Converted: {uploaded_file.name} → {output_name}")

        # Show preview of first 20 lines
        st.subheader("Preview (first 20 lines):")
        preview_lines = open(
            output_path, "r", encoding="utf-8").read().splitlines()[:20]
        st.code("\n".join(preview_lines), language="python")

        # Provide download button
        st.download_button(
            label="Download Python Script",
            data=open(output_path, "r", encoding="utf-8").read(),
            file_name=output_name,
            mime="text/x-python"
        )

