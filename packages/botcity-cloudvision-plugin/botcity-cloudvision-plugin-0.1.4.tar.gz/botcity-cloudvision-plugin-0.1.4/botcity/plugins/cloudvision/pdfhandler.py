from typing import List

import pypdfium2


def pdf_to_image(filepath: str, resolution: int = 72, **kwargs) -> List:
    """Converts a PDF to a list PIL Image objects

    Args:
        filepath (str): The PDF file path.
        resolution (int, optional): The resolution to use when converting the PDF to image.
            Defaults to 72.

    Returns:
        List: List of Image objects being one for each page of the PDF.
    """
    pages = []
    with pypdfium2.PdfDocument(input_data=filepath) as pdf:
        for page_num in range(len(pdf)):
            page = pdf.get_page(page_num)
            pil_image = page.render_topil(scale=resolution / 72, **kwargs)
            pages.append(pil_image)
    return pages
