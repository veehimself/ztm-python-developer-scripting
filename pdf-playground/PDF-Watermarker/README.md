# PDF-Watermarker
### simple program that adds watermark to the provided pdf
---
#### variables
```python
pdf_path = Path("super.pdf") # pdf with content
watermark_path = Path("wtr.pdf") # pdf with watermark
pdf_result = Path("watermarkedsuper.pdf") # output pdf
# make sure you provide path for these and Path from pathlib handles paths
```
#### function call
```python
watermark(
    pdf_path,
    watermark_path,
    pdf_result,
)
# fourth argument determines what all pages should be watermarked 
# by default it is set to "ALL" but it can be altered to list of numbers that acts as page_indices for watermarking
```
[PyPDF2 Documentation for reference](https://pypdf2.readthedocs.io/en/3.0.0/user/add-watermark.html#watermark-underlay)
#### how to run 

```sh
python pdfwatermarker.py
```
---
make sure the virtual environment on the root of the repo is activated and `PyPDF2` is installed
