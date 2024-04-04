# Projeto Conteinerização

Este projeto consiste na aplicação do módulo anterior mas agora conteinerizado:

O sistema verifica se alguma transação seguida foi realizada em alguma outra unidade federativa(estado) a partir da última UF utilizada.

Execute o comando `make build` para construir as imagens mas sem as instanciar.

Caso queira executar a aplicação e os seus conteiners execute o comando `make run`.

Mesmo que não tenha executado o comando `make build` antes, o comando `make run` funcionará e fará o build das imagens automaticamente antes.

As transções geradas pelo producer estão no arquivo `transactions.json`.

O arquivo/link com número da conta passível de fraude vai estar disponível para download no minio e no console.
