# Twitter Bot
Uma automação no Twitter que responde ou curte tweets que contenham palavras ou frases específicas definidas pelo usuário

[![NPM](https://img.shields.io/apm/l/react?style=plastic)](https://github.com/bigpedrolucas/TwitterBot-Python/blob/master/LICENSE)

## Como funciona
Num arquivo .txt, o usuário insere quantas palavras e frases quiser, formatadas uma embaixo da outra. Nesse arquivo, um caractere especial antes de cada palavra vai definir o que o robô fará com o tweet que contenha ela. Por exemplo, se eu quiser responder um tweet que contenha a frase "eu amo tecnologia", no meu arquivo .txt, eu colocarei um "r=" antes dessa frase (r="Eu amo tecnologia"). A minha frase de resposta virá precedida de um "-" (-Eu também amo tecnologia!).

![img1](https://github.com/bigpedrolucas/TwitterBot-Python/blob/master/images/img1.png)

Após a leitura do arquivo .txt, as frases serão separadas de acordo com o seu propósito, e, o usuário, após digitar o nome do arquivo a ser aberto e as suas 4 chaves de autenticação da API do Twitter, poderá setar o robô para fazer as duas ações (curtir e responder) ou apenas uma.

![img2](https://github.com/bigpedrolucas/TwitterBot-Python/blob/master/images/img2.png)
![img3](https://github.com/bigpedrolucas/TwitterBot-Python/blob/master/images/img3.png)



