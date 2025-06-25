from fastapi import FastAPI, HTTPException
from fastapi.responses import StreamingResponse
from pydantic import BaseModel, Field
from typing import Optional
import re

# Importar as funções de certidão
from certidoes.certidao_receita_federal import (
    emitir_auto_pdf_receita_federal,
)
from certidoes.certidao_pref_sorriso import (
    emitir_via_botao_pref_sorriso,
)
from certidoes.certidao_cndt import (
    emitir_com_dados_cndt,
)

app = FastAPI(
    title="API de Certidões",
    description="API para emissão de diversas certidões, classificadas em três grupos.",
    version="1.0.0"
)

# Modelos de requisição
class Grupo1Request(BaseModel):
    cpf: str = Field(..., regex=r"^\d{11}$", description="CPF com 11 dígitos numéricos.")

class Grupo2Request(BaseModel):
    cpf: str = Field(..., regex=r"^\d{11}$", description="CPF com 11 dígitos numéricos.")

class Grupo3Request(BaseModel):
    cpf: Optional[str] = Field(None, regex=r"^\d{11}$", description="CPF com 11 dígitos numéricos.")
    cnpj: Optional[str] = Field(None, regex=r"^\d{14}$", description="CNPJ com 14 dígitos numéricos.")

# Grupo 1: Auto-PDF
@app.get("/certidoes/receita_federal", summary="Emitir Certidão da Receita Federal (Auto-PDF)")
async def get_certidao_receita_federal(cpf: str):
    if not re.fullmatch(r"\d{11}", cpf):
        raise HTTPException(status_code=400, detail="CPF inválido. Deve conter 11 dígitos numéricos.")
    
    pdf_stream = emitir_auto_pdf_receita_federal(cpf)
    return StreamingResponse(pdf_stream, media_type="application/pdf", 
                             headers={"Content-Disposition": f"attachment; filename=certidao_receita_federal_{cpf}.pdf"})

# Grupo 2: Botão "Imprimir"
@app.post("/certidoes/pref_sorriso", summary="Emitir Certidão da Prefeitura de Sorriso (Botão 'Imprimir')")
async def post_certidao_pref_sorriso(request: Grupo2Request):
    pdf_stream = emitir_via_botao_pref_sorriso(request.cpf)
    return StreamingResponse(pdf_stream, media_type="application/pdf", 
                             headers={"Content-Disposition": f"attachment; filename=certidao_pref_sorriso_{request.cpf}.pdf"})

# Grupo 3: Formulário Extra
@app.post("/certidoes/cndt", summary="Emitir Certidão Negativa de Débitos Trabalhistas (Formulário Extra)")
async def post_certidao_cndt(request: Grupo3Request):
    pdf_stream = emitir_com_dados_cndt(request)
    return StreamingResponse(pdf_stream, media_type="application/pdf", 
                             headers={"Content-Disposition": f"attachment; filename=certidao_cndt_{request.cpf}.pdf"})
