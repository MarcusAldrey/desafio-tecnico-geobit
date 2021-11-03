# desafio-tecnico-geobit
Desafio técnico da empresa Geobit

## API
A API está disponível `/api/v1/`

A rota `/api/v1/persons` retorna todas as pessoas no banco de dados ordenada por idade (decrescente), podendo receber o sexo como parâmetro para filtrar.

Ex:
`/api/v1/persons?sexo=F`
`/api/v1/persons?sexo=M`

A rota `/api/v1/femalemereen` retorna todas as pessoas que possuem sexo feminino e cidade Mereen.
