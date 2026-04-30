# anotações de fundamentos da programação 

# TIPOS DE DADOS EM PYTHON
1. string
2. number-int
3. number-float
4. boolean

# OPERADORES MATEMÁTICOS - BÁSICOS
+ -> adição
- -> subtração
* -> multiplicação
/ -> divisão

# OPERADORES LÓGICOS
and->e-> Se duas condições forem verdadeiras, o resultado é verdadeiro.
or->ou-> Se pelo menos uma condição é verdadeira, o resultado é verdadeiro.
not-> Ele altera o valor booleano da condição.

# MÉTODOS EM PYTHON
1. print() -> Exibe informações no terminal
2. input() -> Capturar uma informação no terminal

# FORMAT EM PYTHON

# Estrutura condicional
``if (se)`` -> verifica se uma condição é true (verdadeira) - Se for, ele executa o código
``elif (senão se)`` -> é usado para testar várias condições. Ele só executa se todas as condições anteriores forem falsas
``else (senão)`` -> executa o código se a condição if for false (falsa)

# LAÇOS DE REPETIÇÃO
É um recurso de programação que permite executar um conjunto de comando várias vezes. Também são chamados de loop, laços de repetição ou iteração
``for``-> Utilizamos quando sabemos quantas vezes queremos repetir algo
Sintáxe:
fpr variável in range (início, fim):
    comandos
``range()``-> Método que aceita geração de números
``início``-> É inclusivo. É o primeiro número a ser usado.
``fim``-> É exclusivo. O número utilizado é o anterior a esse.
## Escopo das variáveis
``Escopo Local``-> A ela só pode ser acessada dentro da estrutura que ela foi criada.
``Escopo Global``-> A Variável pode ser acessada por todo mundo.

## Variações das variáveis
Variável em memória -> É declara quando você não pretende utilizar essa variável em outros cenários.
Variável contadora -> É utilizada para uma lógica onde a repetição irá ser alterada.

``While``-> É utilizado quando não sabemos quantas vezes o programa vai repetir. Ele repete enquanto uma condição for verdadeira.
Sintáxe:
while :condicao;
    comandos

# CONVERSÃO DE TIPOS DE PYTHON
1. int() -> A gente vai incluir qual variável/dado deveremos converter para número inteiro
2. float() -> A gente vai incluir qual variável/dado deveremos converter para número decimal
3. str() -> A gente vai incluir qual variável/dado deveremos converter para texto  

# Boas Práticas
1. Qualquer variável em python utiliza o padrão de case snake_case ou recentemente o cammelCase.
2. Se você observar alguma estrutura tipo nome(), 90% de chance de ser uma função.
3. Python não tem constante, porém utilizamos o padrão case UPPERCASE, para simular que aquela variável não pode ser alterada.