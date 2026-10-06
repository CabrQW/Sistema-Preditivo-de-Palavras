from collections import Counter, defaultdict
from typing import Optional


class ModeloPreditivo:


    def __init__(self, tokens: list[str]) -> None:
        self.tokens = tokens

        self.vocabulario = set(tokens)

        self.frequencia_palavras = Counter(tokens)

        self.bigrams: Counter[tuple[str, str]] = Counter()
        self.trigrams: Counter[tuple[str, str, str]] = Counter()

        self.contextos_bigramas: Counter[str] = Counter()
        self.contextos_trigramas: Counter[tuple[str, str]] = Counter()

        self._construir_modelo()

    def _construir_modelo(self) -> None:


        for i in range(len(self.tokens) - 1):
            palavra_atual = self.tokens[i]
            proxima_palavra = self.tokens[i + 1]

            self.bigrams[(palavra_atual, proxima_palavra)] += 1
            self.contextos_bigramas[palavra_atual] += 1

        for i in range(len(self.tokens) - 2):
            palavra1 = self.tokens[i]
            palavra2 = self.tokens[i + 1]
            palavra3 = self.tokens[i + 2]

            self.trigrams[(palavra1, palavra2, palavra3)] += 1
            self.contextos_trigramas[(palavra1, palavra2)] += 1

    def probabilidade_bigram(
        self,
        contexto: str,
        palavra: str
    ) -> float:


        frequencia_bigram = self.bigrams[(contexto, palavra)]
        frequencia_contexto = self.contextos_bigramas[contexto]

        tamanho_vocabulario = len(self.vocabulario)

        return (
            (frequencia_bigram + 1)
            / (frequencia_contexto + tamanho_vocabulario)
        )

    def probabilidade_trigram(
        self,
        contexto1: str,
        contexto2: str,
        palavra: str
    ) -> float:

        frequencia_trigram = self.trigrams[
            (contexto1, contexto2, palavra)
        ]

        frequencia_contexto = self.contextos_trigramas[
            (contexto1, contexto2)
        ]

        tamanho_vocabulario = len(self.vocabulario)

        return (
            (frequencia_trigram + 1)
            / (frequencia_contexto + tamanho_vocabulario)
        )

    def prever(
        self,
        contexto: str
    ) -> Optional[tuple[str, float]]:
     

        palavras = contexto.lower().split()

        if not palavras:
            return None

        candidatos = list(self.vocabulario)

        probabilidades = {}

        if len(palavras) >= 2:

            contexto1 = palavras[-2]
            contexto2 = palavras[-1]

            for candidato in candidatos:
                probabilidade = self.probabilidade_trigram(
                    contexto1,
                    contexto2,
                    candidato
                )

                probabilidades[candidato] = probabilidade

        else:

            contexto1 = palavras[-1]

            for candidato in candidatos:
                probabilidade = self.probabilidade_bigram(
                    contexto1,
                    candidato
                )

                probabilidades[candidato] = probabilidade

        palavra_escolhida = max(
            probabilidades,
            key=probabilidades.get
        )

        probabilidade = probabilidades[palavra_escolhida]


        soma = sum(probabilidades.values())

        if soma > 0:
            confianca = probabilidade / soma
        else:
            confianca = 0.0

        return palavra_escolhida, confianca