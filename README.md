✦ LYRIC SYNC
===========
O projeto LYRIC SYNC surgiu de uma ideia que acredita em uma abordagem inclusiva para tornar o aprendizado da língua inglesa uma experiência diferenciada e acessível.

# Informações do projeto: 

## Sobre o desenvolvimento

### **Funcionamento do projeto e implementações das funcionalidades solicitadas:**

**Análise de sentimento:** Foi implementado na área de contato. O usuário escreve na caixa de texto os comentários que deseja em relação ao site e, então, o texto da área comentada é traduzido para inglês para poder ser analisado pela biblioteca do NLTK, retornando uma mensagem de agradecimento de acordo com a analise do seu conteudo, podendo ser positiva, negativa ou neutra.

**Transcrição de vídeo:** Optei por fazer a transcrição de vídeo partindo de um link da plataforma do YouTube, que é uma plataforma muito utilizada e de fácil acesso. Nessa transcrição, o programa recebe o link e faz o download do vídeo, depois faz a extração de seu áudio para finalmente realizar a transcrição, que será mostrada na tela.

**Consumo de conteúdo não estruturado:** Neste projeto, decidi incluir inicialmente o consumo de arquivos em PDF, para realizar as traduções de seu conteúdo do inglês para o português, fazendo a extração do texto no arquivo, seguida pela tradução que tambem será mostrada na tela.

## Tecnologias ultilizadas
 
 - Python
   - Flask
 - HTML
 - CSS

## 🚨Como rodar o projeto:🚨
 
 
 ✦Ambiente recomendado para uso será o: Visual Studio Code

 
 ✦Clone o projeto `git clone https://github.com/Code-Aline/Projeto-IA-do-alem`


✦Instale no prompt de comando:    

    pip install -r requirements.txt

    python -m nltk.downloader all
    
✦Instale o ffmpeg seguindo as instruções:

    https://phoenixnap.com/kb/ffmpeg-windows
    
✦Start

    python main.py

   
## Para realizção de testes:
Para teste da funcionalidade de tradução de PDF, fique a vontade se quiser ultilizar o arquivo dentro da pasta de arquivos.

Para transcrição de video deixo minha sugestão: https://www.youtube.com/watch?v=UEcyz0Q6bs8&t
 - Recomendo que faça a escolha de videos mais curtos devido ao tempo de processamento.

Para a analise de sentimentos, deixo os exemplos mais basicos e o resultado que cada um deve retornar:
 - Estou muito satisfeita com o site `Retorna a mensagem positiva!`
 - Estou decepcionada com o tempo de demora do site `Retorna a mensagem negativa!`

**Mas fique a vontade em testar como desejar.**

