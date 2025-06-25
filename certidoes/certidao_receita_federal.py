import io
from fastapi.responses import StreamingResponse

def emitir_auto_pdf_receita_federal(cpf: str) -> io.BytesIO:
    # Simulação de geração de PDF
    pdf_content = b"%PDF-1.4\n1 0 obj<</Type/Catalog/Pages 2 0 R>>endobj\n2 0 obj<</Type/Pages/Count 1/Kids[3 0 R]>>endobj\n3 0 obj<</Type/Page/MediaBox[0 0 612 792]/Parent 2 0 R/Contents 4 0 R/Resources<</ProcSet[/PDF/Text]/Font<</F1 5 0 R>>>>>>endobj\n4 0 obj<</Length 55>>stream\nBT\n/F1 24 Tf\n100 700 Td\n(Certidão Receita Federal) Tj\nET\nendstream\n5 0 obj<</Type/Font/Subtype/Type1/Name/F1/BaseFont/Helvetica/Encoding/MacRomanEncoding>>endobj\nxref\n0 6\n0000000000 65535 f\n0000000009 00000 n\n0000000074 00000 n\n0000000120 00000 n\n0000000250 00000 n\n0000000310 00000 n\ntrailer<</Size 6/Root 1 0 R>>startxref\n390\n%%EOF"
    return io.BytesIO(pdf_content)
