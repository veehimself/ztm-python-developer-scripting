from pathlib import Path
from typing import Union, Literal, List

from PyPDF2 import PdfWriter,PdfReader

def watermark(
        content_pdf:Path,
        watermark_path:Path,
        result_path:Path,
        page_indices:Union[Literal["ALL"],List[int]]="ALL"
    ):
    reader = PdfReader(content_pdf)

    if page_indices == "ALL":
        page_indices=list(range(0,len(reader.pages)))

    writer = PdfWriter()
    for index in page_indices:
        content_page = reader.pages[index]
        mediabox = content_page.mediabox
        reader_watermark = PdfReader(watermark_path)
        image_page = reader_watermark.pages[0]
        image_page.merge_page(content_page)
        image_page.mediabox = mediabox
        writer.add_page(image_page)

    with open(result_path,"wb") as fp:
        writer.write(fp)
    print("PDF watermarked")

pdf_path = Path("super.pdf")
watermark_path = Path("wtr.pdf")
pdf_result = Path("watermarkedsuper.pdf")

watermark(
    pdf_path,
    watermark_path,
    pdf_result,
)
