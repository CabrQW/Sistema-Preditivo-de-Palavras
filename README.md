# Sistema Preditivo de Palavras

## Análise Exploratória de Dados – Exercício-Programa

Sistema inteligente de autocompletação de texto desenvolvido em Python utilizando conceitos de probabilidade condicional, N-grams, Teorema de Bayes e Laplace Smoothing.

O objetivo do projeto é analisar uma frase fornecida pelo usuário e sugerir a próxima palavra mais provável, apresentando também uma porcentagem de confiança para a previsão.

---

## 1. Objetivo

O projeto tem como objetivo desenvolver um modelo probabilístico capaz de prever a próxima palavra de uma frase.

Por exemplo:

```text
Entrada:
o aluno estudou

Sugestão:
para
```

O modelo utiliza informações obtidas a partir de um corpus textual para calcular a probabilidade de diferentes palavras aparecerem depois de determinado contexto.

---

## 2. Tecnologias utilizadas

- Python 3.10+
- Pytest
- Programação Orientada a Objetos
- Type Hints
- Probabilidade Condicional
- N-grams
- Laplace Smoothing
- Teorema de Bayes

---

## 3. Estrutura do projeto

```text
sistema-preditivo-palavras/
│
├── src/
│   ├── __init__.py
│   ├── corpus.py
│   ├── modelo.py
│   └── main.py
│
├── data/
│   └── corpus.txt
│
├── tests/
│   └── test_modelo.py
│
├── README.md
├── requirements.txt
└── pytest.ini
```

### `src/corpus.py`

Responsável pelo processamento do corpus.

São realizadas as seguintes etapas:

1. Leitura do arquivo;
2. Conversão para letras minúsculas;
3. Remoção de caracteres especiais;
4. Remoção de espaços duplicados;
5. Separação do texto em tokens.

### `src/modelo.py`

Contém a implementação do modelo probabilístico.

O arquivo realiza:

- Contagem das palavras;
- Construção dos bigramas;
- Construção dos trigramas;
- Cálculo das probabilidades;
- Aplicação de Laplace Smoothing;
- Predição da próxima palavra.

### `src/main.py`

Responsável pela interação com o usuário.

O programa solicita uma frase e apresenta:

```text
Sugestão: palavra
Confiança: XX.XX%
```

### `data/corpus.txt`

Contém os textos utilizados pelo modelo para aprender as relações entre as palavras.

### `tests/test_modelo.py`

Contém testes automatizados para verificar o funcionamento do modelo.

---

## 4. N-grams

O sistema utiliza dois tipos de N-grams.

### Bigramas

Um bigrama é formado por duas palavras consecutivas.

Exemplo:

```text
o aluno
aluno estudou
estudou para
para a
a prova
```

Nesse caso, podemos calcular:

```text
P(aluno | o)
```

Ou seja, a probabilidade de aparecer a palavra `aluno` depois da palavra `o`.

### Trigramas

Um trigrama é formado por três palavras consecutivas.

Exemplo:

```text
o aluno estudou
aluno estudou para
estudou para a
para a prova
```

Podemos calcular:

```text
P(prova | para, a)
```

Isso permite utilizar um contexto maior para realizar a previsão.

---

## 5. Probabilidade Condicional

A previsão utiliza o conceito de probabilidade condicional.

Para os bigramas:

```text
P(Wn | Wn-1)
```

Para os trigramas:

```text
P(Wn | Wn-2, Wn-1)
```

A ideia é verificar quais palavras possuem maior probabilidade de aparecer depois do contexto informado pelo usuário.

---

## 6. Teorema de Bayes

O exercício propõe a utilização do Teorema de Bayes:

```text
P(Wn | Contexto) =
P(Contexto | Wn) * P(Wn) / P(Contexto)
```

Na implementação, a previsão utiliza probabilidades condicionais obtidas a partir das frequências dos N-grams.

Dessa forma, o modelo utiliza as informações observadas no corpus para estimar a probabilidade da próxima palavra.

---

## 7. Laplace Smoothing

Um dos problemas de modelos probabilísticos baseados em frequência é a ocorrência de probabilidades iguais a zero.

Por exemplo, caso uma determinada combinação de palavras não apareça no corpus:

```text
P(palavra | contexto) = 0
```

Para evitar esse problema, foi utilizado o Laplace Smoothing.

A fórmula utilizada é:

```text
P(w | contexto) =
(C(contexto, w) + 1) /
(C(contexto) + V)
```

Onde:

- `C(contexto, w)` = quantidade de ocorrências da combinação;
- `C(contexto)` = quantidade de ocorrências do contexto;
- `V` = tamanho do vocabulário.

O acréscimo de `1` permite que palavras que ainda não apareceram naquele contexto recebam uma pequena probabilidade em vez de zero.

---

## 8. Funcionamento

Para executar o sistema, abra o terminal na pasta principal do projeto.

Execute:

```bash
python src/main.py
```

O sistema solicitará uma frase:

```text
Digite uma frase:
```

Exemplo:

```text
o aluno estudou
```

O programa apresentará:

```text
Resultado:
Sugestão: para
Confiança: XX.XX%
```

A palavra e a confiança dependem do conteúdo e das frequências existentes no corpus.

---

## 9. Executando os testes

Instale as dependências:

```bash
pip install -r requirements.txt
```

Depois execute:

```bash
python -m pytest
```

Resultado esperado:

```text
5 passed
```

Os testes verificam:

- Existência do vocabulário;
- Cálculo de probabilidades;
- Funcionamento dos bigramas;
- Funcionamento dos trigramas;
- Geração de uma previsão;
- Valor válido para a confiança.

---

## 10. Tratamento de palavras desconhecidas

O modelo utiliza Laplace Smoothing para evitar probabilidades nulas.

Quando uma combinação de palavras não aparece no corpus, o modelo não simplesmente retorna zero.

Isso permite que o algoritmo continue realizando uma previsão mesmo diante de contextos que não foram observados durante a construção do corpus.

---

## 11. Limitações

O modelo possui algumas limitações.

A qualidade das previsões depende diretamente da qualidade e do tamanho do corpus utilizado.

Como o projeto utiliza um corpus relativamente pequeno, algumas frases podem apresentar previsões pouco precisas.

Além disso, o modelo não possui compreensão semântica da linguagem. Ele realiza as previsões com base principalmente nas frequências e relações estatísticas observadas no texto.

---

## 12. Possíveis melhorias

Como trabalhos futuros, o sistema poderia receber:

- Corpus maior;
- Mais tipos de N-grams;
- Tratamento de palavras desconhecidas;
- Interface gráfica;
- API para utilização do modelo;
- Comparação entre diferentes técnicas de suavização;
- Métricas mais completas de avaliação;
- Modelos de linguagem mais avançados.

---

## 13. Conclusão

O projeto demonstra a aplicação prática de conceitos de probabilidade e análise de dados na construção de um sistema preditivo.

Através da utilização de N-grams, probabilidades condicionais e Laplace Smoothing, foi desenvolvido um modelo capaz de analisar um contexto textual e estimar qual palavra possui maior probabilidade de aparecer em seguida.

O desenvolvimento também permitiu aplicar conceitos de limpeza de dados, contagem de frequências, modelagem probabilística, modularização, testes automatizados e documentação de software.