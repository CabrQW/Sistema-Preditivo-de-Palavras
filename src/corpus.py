import re
from pathlib import Path


def carregar_corpus(caminho: str) -> str:

    return Path(caminho).read_text(encoding="utf-8")


def normalizar_texto(texto: str) -> str:


    texto = texto.lower()

  
    texto = re.sub(r"[^a-záàâãéêíóôõúüç0-9\s]", " ", texto)


    texto = re.sub(r"\s+", " ", texto)

    return texto.strip()


def tokenizar(texto: str) -> list[str]:

    return texto.split()


def preparar_corpus(caminho: str) -> list[str]:

    texto = carregar_corpus(caminho)
    texto = normalizar_texto(texto)

    return tokenizar(texto)