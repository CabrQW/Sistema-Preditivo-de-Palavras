from src.modelo import ModeloPreditivo


def criar_modelo():
    tokens = """
    o aluno estudou para a prova
    o aluno estudou matemática
    o aluno estudou programação
    o professor ensinou matemática
    o professor ensinou programação
    a prova de matemática foi difícil
    a prova de programação foi difícil
    """.lower().split()

    return ModeloPreditivo(tokens)


def test_modelo_possui_vocabulario():
    modelo = criar_modelo()

    assert len(modelo.vocabulario) > 0


def test_probabilidade_bigram():
    modelo = criar_modelo()

    probabilidade = modelo.probabilidade_bigram(
        "estudou",
        "para"
    )

    assert probabilidade > 0


def test_probabilidade_trigram():
    modelo = criar_modelo()

    probabilidade = modelo.probabilidade_trigram(
        "a",
        "prova",
        "de"
    )

    assert probabilidade > 0


def test_previsao_retorna_palavra():
    modelo = criar_modelo()

    resultado = modelo.prever(
        "o aluno estudou"
    )

    assert resultado is not None


def test_confianca_entre_zero_e_um():
    modelo = criar_modelo()

    resultado = modelo.prever(
        "o aluno estudou"
    )

    assert resultado is not None

    palavra, confianca = resultado

    assert isinstance(palavra, str)
    assert 0 <= confianca <= 1