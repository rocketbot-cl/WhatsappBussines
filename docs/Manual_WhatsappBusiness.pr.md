



# Whatsapp Business
  
Este módulo permite que você se conecte à API do WhatsApp Business e envie mensagens de texto ou modelos.  

*Read this in other languages: [English](Manual_WhatsappBusiness.md), [Português](Manual_WhatsappBusiness.pr.md), [Español](Manual_WhatsappBusiness.es.md)*
  
![banner](imgs/Banner_WhatsappBusiness.jpg)
## Como instalar este módulo
  
Para instalar o módulo no Rocketbot Studio, pode ser feito de duas formas:
1. Manual: __Baixe__ o arquivo .zip e descompacte-o na pasta módulos. O nome da pasta deve ser o mesmo do módulo e dentro dela devem ter os seguintes arquivos e pastas: \__init__.py, package.json, docs, example e libs. Se você tiver o aplicativo aberto, atualize seu navegador para poder usar o novo módulo.
2. Automático: Ao entrar no Rocketbot Studio na margem direita você encontrará a seção **Addons**, selecione **Install Mods**, procure o módulo desejado e aperte instalar.  



## Como usar este módulo
Para utilizar este módulo, deve-se fazer a seguinte configuração:
1. __Login__ ou __register__ em https://developers.facebook.com/
2. Acesse seus aplicativos em https://developers.facebook.com/apps/ e clique no botão Criar aplicativo.
3. Conecte a carteira comercial, que é a conta comercial do Facebook à qual o App estará vinculado. Clique em próximo.
4. Na próxima página, o que você deseja que seu aplicativo faça? escolha a opção Outro em Você está procurando outra coisa? Clique em próximo.
5. Selecione o tipo de aplicativo Business e clique em Avançar.
6. Escolha o nome, e-mail do administrador e conta comercial à qual o aplicativo será vinculado. Clique em Criar e será solicitado que você insira sua senha para finalizar. Ao criar o App, você será redirecionado para a página dele, que estará em modo Desenvolvimento.
7. Nesta página, selecione o botão __Configurar__ no aplicativo Whatsapp e depois em Configurações da API clique em __Começar a usar a API__. 
Você receberá um número de teste para enviar mensagens e até 5 contatos que poderá adicionar para receber as mensagens de teste. Tanto no App em desenvolvimento quanto em produção, você só pode enviar mensagens que incluam texto para conversas iniciadas pelo usuário. Caso a conversa seja iniciada pela empresa, você deverá enviar modelos que tenham sido aprovados pela META. Para mais informações consulte o seguinte link: https://developers.facebook.com/docs/whatsapp/api/messages/message-templates
8. Na página Configurações da API você verá um token de acesso temporário para usar a API. Este token dura 24 horas. Se quiser utilizar a API por mais tempo, deverá solicitar um token de acesso permanente (ver ponto 13).
9. No Passo 1 desta página você terá acesso ao número de teste do Whatsapp e às configurações do número do destinatário. Você também tem o identificador do número de telefone. Tanto esta informação quanto o token serão necessários para poder conectar-se através do módulo no 
modo de desenvolvedor.
10. Tente associar um destinatário e enviar do módulo o modelo padrão hello_world com o idioma en_US. Se tudo funcionar corretamente, você receberá uma mensagem no WhatsApp com o texto “Olá, Mundo!”.
11. Depois de funcionar, você pode criar seus próprios templates que precisam ser aprovados pelo META e enviá-los através do módulo. Para mais informações sobre templates, confira o seguinte link: https://developers.facebook.com/docs/whatsapp/api/messages/message-templates
12. Depois de verificar se a API funciona, você precisará adicionar um número de telefone da sua empresa para poder enviar mensagens aos seus clientes. No passo 5 da página Configuração da API, clique no botão __Adicionar número de telefone__ e siga os passos para criar o perfil do WhatsApp Business. Uma vez adicionado, salve o Identificador do Número de Telefone, esta informação será necessária para poder se conectar através do módulo.
13. Adicionado um número de telefone, resta configurar o 
aplicativo para entrar em modo produtivo e gerar um token de acesso permanente. Para fazer isso, você deve ir até a página do App em https://developers.facebook.com/apps/ e selecionar o App que você criou. Na página do aplicativo, selecione a opção "Básico" nas configurações do aplicativo.
14. Lá você deve fornecer um __URL da Política de Privacidade__ obrigatório e o restante dos campos opcionalmente. Ao terminar, clique em __Salvar alterações__.
15. Com tudo já configurado, o app está pronto para entrar no modo Ativo. Para fazer isso, vá até o topo de tudo no site e mova o seletor Desenvolvimento para Ativo.
16. Obtenha token permanente: Para fazer isso, você deve ter uma conta de negociação Meta. Acesse https://business.facebook.com/ e no menu à esquerda selecione sua empresa, e clique na roda de configuração e depois em Configuração empresarial. Na nova janela vá para Usuários > Usuários do Sistema e adicione um novo usuário.
17. Aceite a mensagem na janela que se abre e selecione 
um nome para o seu novo usuário. Em Função você deve colocar Administrador.
18. Ao criar o usuário, clique no botão __Assign Assets__. Na janela que se abrirá, selecione Apps, marque o App que você criou e ative a opção __Gerenciar App__, depois Salve as alterações.
19. Ao atribuir o ativo, clique em __Gerar novo token__. Selecione seu App, em __Token Expiration__ escolha __Nunca__ e verifique todas as permissões da lista (nem todas são necessárias, mas se mais integrações forem adicionadas ao Rocketbot no futuro você poderá usar a mesma credencial). Clique em __Gerar token__. Este será o token permanente que você pode usar para autenticar no módulo.

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
|Parâmetros do modelo|Opcional. Indique o(s) parâmetro(s) usando uma lista ['1param', '2param']|['1param', '2param']|
|Mensagem|Mensagem que será enviada para o número de Whatsapp|Olá, como você está?|
|Assign result to a variable|Variable where the result will be saved|Variable|
