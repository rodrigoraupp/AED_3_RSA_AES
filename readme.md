**Enunciado do problema**

Como criptoanalista no Biuro Szyfrów, você interceptou uma mensagem cifrada, criptografada com AES 256 bits, cuja chave foi criptografada utilizando uma chave pública RSA. Você tem acesso tanto a mensagem cifrada como a chave cifrada. Sabe ainda que provavelmente foi utilizado o programa openssl para realizar ambas encriptações.

Sua tarefa é obter a mensagem cifrada. 

Ao concluir a tarefa, submeta os procedimentos adotados que permitam replicar o processo, bem como a senha e a mensagem originais, em um único arquivo PDF.

A nota deste trabalho comporá a nota de trabalhos da disciplina. Será avaliado da seguinte forma:

- Nota máxima para os trabalhos corretos entregues até o dia 12/12;
- 85% da nota máxima para trabalhos corretos entregues até o dia 15/12;
- Cada trabalho correto entregue até 12/12 receberá até 2,0 pontos adicionais. Este bônus de 2 pontos será dividido pelo número de trabalhos corretos entregues pela turma.

## 1.Introdução 

O trabalho proposto envolve três arquivos interceptados usando técnicas de criptografia conhecidas. Os arquivos contam com um texto cifrado em AES-256 bits, a chave que descriptografa esse texto mas que está criptografado por RSA, cuja chave pública usada é o terceiro arquivo. É sabido que o programa OpenSSL foi provavelmente utilizado para realizar as encriptações. A partir de todos esses dados deverá ser feita a criptoanálise e quebra da mensagem cifrada. 

## 2.*Walkthrough* da Criptoanálise 

É possível acessar tanto os arquivos interceptados quanto documentos e códigos utilizados para decifrar a mensagem no link a seguir. Os algoritmos estão todo codificados na linguagem Python. 

<https://github.com/rodrigoraupp/AED_3_RSA_AES> 

O primeiro passo consiste em desmembrar a chave pública afim de formular a chave privada. Para isso, foi retirado da chave pública os números N e E que a compõem. São eles: 

N=1827700881180020961087568768788024747837552898711832066633012170617731396283665548738830421 

E= 65537 

Em seguida, foi necessário fatorar o número N para adquirir os dois números primos que multiplicados geram o número N. O site Alpertron.com foi utilizado, tomando cerca de uma hora para concluir a fatoração. Os números P e Q encontrados foram: 

P= 1371293089587387292180481293784036793076837889 

Q= 1332830227949273521465367319234277279439624789 

Obtidos os números primos, o próximo passo é gerar a chave privada. A partir do algoritmo encontrado no arquivo gerachaveprivada.py, foi possível encontrar a seguinte chave: 

```
-----BEGIN RSA PRIVATE KEY----- 

MIHBAgEAAiYOWxON4VVOCjgECz38THnFRTqJY2gENjwnu266/sg0yYw6BiggVQID 

AQABAiYKAICuQInrtojyoFaOm0XYIPS4gdMeNj3C5uWo2IfKGNERZ8+4AQITPX2s 

M0jDhgm4ndB+ijBfokJuAQITO8QkAkcydrUiO+qEJlMfWe2aVQITFVxIq3AFa9SI 

q1m3+20ea5FEAQITL1bOxtcqC4ixkw/QmKKiZJKk+QITA+HQAN0Pyy+LQVUdHZPk 

Xcku+Q== 

-----END RSA PRIVATE KEY-----
```

Logo após formular a chave privada, foi possível utilizar o programa OpenSSL para decifrar a chave AES criptografada. A versão do programa para descriptografar a senha é 1.1.1, utilizada sem problemas. O seguinte comando foi introduzido: 

```openssl rsautl -decrypt -inkey private.pem -in key.cipher -out chaveaes.txt```

Revelando a seguinte chave AES: 

```6AYwFJffIFVVpYkCUFf4Jw== ```

Em seguida que a chave foi descriptografada, foram várias as tentativas de utilizar novamente o programa OpenSSL, dessa vez para decifrar o texto em questão utilizando a chave AES. Porém, todas as tentativas foram frustradas mesmo ao testar os vários parâmetros que o programa coloca à disposição. Para enfim decifrar o texto secreto, foi utilizada então uma build de versão anterior (1.1.0 para Windows). O comando correto para descriptografar o texto usado é: 

openssl aes-256-cbc -salt -a -d -in ciphertext.enc -out MENSAGEM.txt 

Inserido o comando, o programa pediu para introduzir a senha/chave AES, concluindo o processo de quebra da mensagem. 

##    3.O Texto Decifrado 

O texto foi então revelado: trata-se do telegrama do ministro exterior da Alemanha, Arthur Zimmerman, enviado no auge da Primeira Guerra Mundial diretamente para o embaixador alemão no México, Heinrich von Eckardt. 

“We intend to begin on the first of February unrestricted submarine warfare. We shall endeavor in spite of this to keep the United States of America neutral. In the event of this not succeeding, we make Mexico a proposal of alliance on the following basis: make war together, make peace together, generous financial support and an understanding on our part that Mexico is to reconquer the lost territory in Texas, New Mexico, and Arizona. The settlement in detail is left to you. You will inform the President of the above most secretly as soon as the outbreak of war with the United States of America is certain and add the suggestion that he should, on his own initiative, invite Japan to immediate adherence and at the same time mediate between Japan and ourselves. Please call the President's attention to the fact that the ruthless employment of our submarines now offers the prospect of compelling England in a few months to make peace.

  

Signed, ZIMMERMANN.” 
