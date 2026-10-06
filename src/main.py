from pathlib import Path

from corpus import preparar_corpus
from modelo import ModeloPreditivo


def main() -> None:

    caminho_corpus = (
        Path(__file__).parent.parent / "data" / "corpus.txt"
    )

    tokens = preparar_corpus(str(caminho_corpus))

    modelo = ModeloPreditivo(tokens)

    print("=" * 50)
    print("       SISTEMA PREDITIVO DE PALAVRAS")
    print("=" * 50)

    frase = input("\nDigite uma frase: ")

    resultado = modelo.prever(frase)

    if resultado is None:
        print("Não foi possível realizar a predição.")
        return

    palavra, confianca = resultado

    print("\nResultado:")
    print(f"Sugestão: {palavra}")
    print(f"Confiança: {confianca * 100:.2f}%")


if __name__ == "__main__":
    main()