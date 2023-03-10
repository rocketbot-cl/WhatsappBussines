# Whatsapp Business
  
Módulo para se conectar à api Whatsapp Business e enviar mensagens de texto ou templates  

*Read this in other languages: [English](Manual_WhatsappBusiness.md), [Español](Manual_WhatsappBusiness.es.md), [Português](Manual_WhatsappBusiness.pr.md)*
  
![banner](/docs/imgs/Banner_WhatsappBusiness.png)
## Como instalar este módulo
  
A instalação pode ser:
1. Manual: Faça o download do arquivo .zip e descompacte-o na pasta de módulos. O nome da pasta deve ser o mesmo que o nome do módulo e dentro dela deve ter os seguintes arquivos e pastas: \__init__.py, package.json, docs, exemplo e libs. Se você tiver o aplicativo aberto, atualize o navegador para poder usar o novo módulo.
2. Automático: Ao entrar no Rocketbot Studio na margem direita, você encontrará a seção **Adicionamentos**, selecione **Instalar Modos**, encontre o módulo desejado e pressione instalar. 




## Como usar este módulo
Para utilizar este módulo, é necessária a seguinte configuração:
1. __Log in__ ou __register__ em https://developers.facebook.com/
2. vá para suas aplicações em https://developers.facebook.com/apps/
3. Criar um novo aplicativo. Deve ser uma aplicação comercial. Na página seguinte, escolha o nome, o e-mail do administrador e a conta comercial à qual o aplicativo estará vinculado.
4. Ao criar o aplicativo, você será redirecionado para a página do aplicativo, que estará no modo Desenvolvimento. Nesta página, selecione o botão __Configure__ no aplicativo Whatsapp e depois selecione __API Configuration__. Ao clicar em Continuar, você receberá um número de teste para enviar mensagens e até 5 contatos que você pode adicionar para receber as mensagens de teste.
5. Na página Quick Start, clique em __Start usando a API__. 
6. Tanto na aplicação de desenvolvimento quanto na de produção, só é possível enviar mensagens que incluam texto para conversas que tenham sido iniciadas pelo usuário. Se a conversa for iniciada pela empresa, você deverá enviar modelos que tenham sido aprovados pela META. Para mais informações, consulte o seguinte link: https://developers.facebook.com/docs/whatsapp/api/messages/message-templates
7. Na página de Primeiros Passos, você verá um token de acesso temporário para usar o API. Esta ficha tem uma duração de 24 horas. Se você quiser usar o API por mais tempo, deverá solicitar um token de acesso permanente (ver ponto 12).
8. Nesta seção você terá acesso ao número de teste Whatsapp e às configurações do número do destinatário. Você também tem o identificador do número de telefone. Tanto isto como a ficha serão necessários para poder se conectar através do módulo no modo desenvolvedor.
9. Tente associar um destinatário e envie do módulo o modelo padrão hello_world com o idioma en_US. Se tudo funcionar corretamente, você receberá uma mensagem Whatsapp com o texto "Hello World!
10. Uma vez testados, você pode criar seus próprios modelos que precisam ser aprovados pelo META e enviá-los através do módulo. Para mais informações sobre os modelos, consulte o seguinte link: https://developers.facebook.com/docs/whatsapp/api/messages/message-templates
11. Uma vez testada a API, você precisará adicionar um número de telefone para sua empresa a fim de poder enviar mensagens a seus clientes. Clique no botão no passo 5 __Adicionar número de telefone__ e siga os passos para criar o perfil Whatsapp Business. Uma vez adicionado, salvo o identificador do número de telefone, estes dados serão necessários para poder se conectar através do módulo.
12. Uma vez adicionado um número de telefone, você precisa configurar o aplicativo para entrar no modo produtivo e gerar um token de acesso permanente. Para fazer isso, vá para a página do aplicativo em https://developers.facebook.com/apps/ e selecione o aplicativo que você criou. Na página do aplicativo, selecione o botão "Configurar" no aplicativo Whatsapp e depois "Configurações Básicas".
13. Aí você deve fornecer um __Privacy Policy URL__ como obrigatório e o resto dos campos como opcional. No final clique em __Salvar mudanças__.
14. Com tudo configurado, o aplicativo está pronto para ir para o modo Ativo. Para fazer isso, vá para o topo do site e mova o seletor de Desenvolvimento para o Active. 
15. Receba uma ficha permanente: Para fazer isso, é necessário ter uma conta Meta trading. Vá para https://business.facebook.com/ e no menu à esquerda selecione sua empresa, e clique na roda de configuração, depois em Business Settings. Na nova janela, clique em System Users e adicione uma nova janela.
16. Aceite a mensagem na janela que se abre e depois selecione um nome para seu novo usuário. Sob a função você deve colocar Administrator.
17. Ao criar o usuário, clique no botão __Adicionar Ativos__. Na janela que se abre selecione Apps, então marque o App que você criou e ative a opção __Manage App__, depois Salve as mudanças.
18. Ao atribuir o bem, clique em __Gerar novo token__. Selecione seu aplicativo e verifique todas as permissões da lista (Nem todas são necessárias, mas se mais integrações Rocketbot forem adicionadas no futuro, você poderá usar o mesmo token). Clique em __Generar ficha__. Este será o símbolo permanente que você pode usar para se autenticar no módulo.


## Descrição do comando

### Configurar o servidor
  
Configura a API do Whatsapp para poder executar comandos
|Parâmetros|Descrição|exemplo|
| --- | --- | --- |
|API KEY|API KEY obtida em https//developers.facebook.com/|api-key|
|Identificador de número de telefone|Identificador de número de telefone obtido em https//developers.facebook.com/|116787907958900|
|Atribuir resultado a variável|Variável onde o resultado será salvo|Variável|

### Enviar mensagem de texto ou template
  
Envia uma mensagem de texto ou de um template para um número de Whatsapp
|Parâmetros|Descrição|exemplo|
| --- | --- | --- |
|Número de Whatsapp|Número de Whatsapp para o qual a mensagem será enviada|55111222333|
|Template e código de idioma|Todelo de mensagem e código de idioma que será enviado para o número de Whatsapp.|hello_world, pt_BR|
|Mensagem|Mensagem que será enviada para o número de Whatsapp|Olá, como você está?|
|Assign result to a variable|Variable where the result will be saved|Variable|
