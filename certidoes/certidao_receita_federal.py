import io
from fastapi.responses import StreamingResponse

def emitir_auto_pdf_receita_federal(cpf: str) -> io.BytesIO:
    pdf_str = """%PDF-1.4
1 0 obj<</Type/Catalog/Pages 2 0 R>>endobj
2 0 obj<</Type/Pages/Count 1/Kids[3 0 R]>>endobj
3 0 obj<</Type/Page/MediaBox[0 0 612 792]/Parent 2 0 R/Contents 4 0 R/Resources<</ProcSet[/PDF/Text]/Font<</F1 5 0 R>>>>>>endobj
4 0 obj<</Length 55>>stream
BT
/F1 24 Tf
100 700 Td
(Certidão Receita Federal) Tj
ET
endstream
5 0 obj<</Type/Font/Subtype/Type1/Name/F1/BaseFont/Helvetica/Encoding/MacRomanEncoding>>endobj
xref
0 6
0000000000 65535 f
0000000009 00000 n
0000000074 00000 n
0000000120 00000 n
0000000250 00000 n
0000000310 00000 n
trailer<</Size 6/Root 1 0 R>>
startxref
390
%%EOF"""
    # Converte para bytes usando latin-1 (é compatível com muitos acentos)
    pdf_bytes = pdf_str.encode('latin-1')
    return io.BytesIO(pdf_bytes)
