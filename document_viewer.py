import fitz  # PyMuPDF
import streamlit as st


def preview_document(file_path):
    """
    Display the first page of a PDF.
    """

    doc = fitz.open(file_path)

    page = doc.load_page(0)

    pix = page.get_pixmap(matrix=fitz.Matrix(2, 2))

    image = pix.tobytes("png")

    st.image(
        image,
        caption="Document Preview",
        use_container_width=True
    )

    doc.close()
