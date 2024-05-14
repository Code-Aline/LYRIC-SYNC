LYRIC SYNC
===========

## Essa é a versão inicial. 

 🚨Antes de rodar o programa peço:🚨

✦instale no prompt de comando:

    python -m nltk.downloader all
✦Instale o ffmpeg seguindo as instruções:

    https://phoenixnap.com/kb/ffmpeg-windows

✦Start

    python main.py

## Para teste
Para teste de PDF, fique a vontade se quiser ultilizar o arquivo dentro da pasta de arquivos.

E pra transcrição deixo minha sugestão: https://www.youtube.com/watch?v=UEcyz0Q6bs8&t

**Mas fique a vontade em testar como desejar.**

## Sobre o desenvolvimento

**Funcionamento do projeto e implementações das funcionalidades solicitadas:**

**Análise de sentimento:** Foi implementado na área de contato. O usuário escreve na caixa de texto os comentários que deseja em relação ao site e, então, o texto da área comentada é traduzido para inglês para poder ser analisado pela biblioteca do NLTK.

**Transcrição de vídeo:** Optei por fazer a transcrição de vídeo partindo de um link da plataforma do YouTube, que é uma plataforma muito utilizada e de fácil acesso. Nessa transcrição, o programa recebe o link e faz o download do vídeo e depois faz a extração de seu áudio para finalmente realizar a transcrição.

**Consumo de conteúdo não estruturado:** Neste projeto, decidi incluir inicialmente o consumo de arquivos em PDF, para realizar as traduções de seu conteúdo do inglês para o português.

