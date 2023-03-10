## How to use this module
To use this module, you must perform the following configuration:
1. __Log in__ or __register__ at https://developers.facebook.com/
2. Go to your Apps at https://developers.facebook.com/apps/
3. Create a new App. It must be a Business App. On the next page, choose the name, the administrator's email and the Business Account to which the App will be linked.
4. When creating the App, you will be redirected to the App page, which will be in Development mode. On this page, select in the Whatsapp app the __Configure__ button and then __API Configuration__. When you click Continue, you will be given a test number to send messages and up to 5 contacts that you can add to receive the test messages.
5. On the Quick Start page, click __Start using the API__. 
6. In both the development and production App, you can only send messages that include text to conversations that have been initiated by the user. If the conversation is initiated by the company, you must send templates that have been approved by META. For more information check the following link: https://developers.facebook.com/docs/whatsapp/api/messages/message-templates
7. On the Getting Started page, you will see a temporary access token to use the API. This token lasts for 24 hours. If you want to use the API for a longer period of time, you must request a permanent access token (See point 12).
8. In this section you will have access to the Whatsapp test number and recipient number settings. You also have the phone number identifier. Both this data and the token will be required to connect through the module in developer mode.
9. Try to associate a recipient and send from the module the default hello_world template with the en_US language. If everything works correctly, you will receive a Whatsapp message with the text "Hello World!".
10. Once you have checked the operation, you can create your own templates that need to be approved by META and send them through the module. For more information about the templates, check the following link: https://developers.facebook.com/docs/whatsapp/api/messages/message-templates
11. Once you have tested the API functionality, you will need to add a phone number of your company to be able to send messages to your customers. Click on the button in step 5 __Add phone number__ and follow the steps to create the Whatsapp Business profile. Once added, save the phone number identifier, this data will be necessary to be able to connect through the module.
12. Once you have a phone number added, it remains to configure the application to switch to productive mode and generate a permanent access token. To do this, go to the App page at https://developers.facebook.com/apps/ and select the App you created. On the App page, select the "Configure" button in the Whatsapp app and then "Basic Settings".
13. There you must provide a __Privacy Policy URL__ as mandatory and the rest of the fields as optional. At the end click on __Save changes__.
14. With everything configured, the app is ready to go to Active mode. To do this go to the top of the web and move the Development selector to Active. 
15. Get a permanent token: To do this you must have a Meta trading account. Go to https://business.facebook.com/ and in the left menu select your company, and click on the configuration wheel, then Business Settings. In the new window click on System users and add a new one.
16. Accept the message in the window that opens and then select a name for your new user. Under Role you should put Administrator.
17. When creating the user click on the __Add assets__ button. In the window that will open select Apps, then check the App you created and activate the option __Manage App__, then Save the changes.
18. When assigning the asset, click on __Generate new token__. Select your App and check all permissions from the list (They are not all required but if more integrations are added to Rocketbot in the future you will be able to use the same token). Click on __Generate token__. This will be the permanent token that you will be able to use to authenticate in the module.

---

## Como usar este módulo
Para utilizar este módulo, se debe realizar la siguiente configuración:
1. __Inicia sesión__ o __regístrate__ en https://developers.facebook.com/
2. Ve a tus Apps en https://developers.facebook.com/apps/
3. Crea una nueva App. Debe ser de tipo Negocio. En la página siguiente, elije el nombre, el correo del administrador y la Cuenta comercial a la que se vinculará la App.
4. Al crear la App, se te redirigirá a la página de la misma, la cual se encontrará en modo Desarrollo. En esta página, selecciona en la app Whatsapp el botón __Configurar__ y luego __Configuración de la API__. Al hacer click en Continuar, se te otorgará un número de prueba para enviar mensajes y hasta 5 contactos que puedes agregar para recibir los mensajes de prueba.
5. En la página de Inicio rápido, haz click en __Empezar a usar la API__. 
6. Tanto en la App en desarrollo como en producción, sólo puedes enviar mensajes que incluyen texto a conversaciones que hayan sido iniciadas por el usuario. Si la conversación es iniciada por la empresa, deberás enviar plantillas que hayan sido aprobadas por META. Para más información revisa el siguiente link: https://developers.facebook.com/docs/whatsapp/api/messages/message-templates
7. En la página de Primeros pasos, verás un token de acceso temporal para usar la API. Este token tiene una duración de 24 horas. Si quieres usar la API por más tiempo, debes solicitar un token de acceso permanente (Ver punto 12).
8. En esta sección tendrás acceso al número de prueba de Whatsapp y a la configuración de los números de destinatario. También tienes el Identificador de número de teléfono. Tanto este dato como el token serán necesarios para poder conectarte a través del módulo en modo desarrollador.
9. Prueba asociar un destinatario y enviar desde el módulo la plantilla por defecto hello_world con el lenguaje en_US. Si todo funciona correctamente, recibirás un mensaje de Whatsapp con el texto "Hello World!".
10. Una vez comprobado el funcionamiento, puedes crear tus propias plantillas que necesitan ser aprobadas por META y enviarlas a través del módulo. Para más información sobre las plantillas, revisa el siguiente link: https://developers.facebook.com/docs/whatsapp/api/messages/message-templates
11. Una vez que hayas comprobado el funcionamiento de la API, deberás agregar un número de teléfono de tu empresa para poder enviar mensajes a tus clientes. Haz click en el botón del paso 5 __Agregar número de teléfono__ y sigue los pasos para crear el perfil de Whatsapp Business. Una vez agregado, guarda el Identificador de número de teléfono, este dato será necesario para poder conectarte a través del módulo.
12. Al tener un número de teléfono agregado, queda configurar la aplicación para pasar al modo productivo y generar un token de acceso permanente. Para esto, debes ir a la página de la App en https://developers.facebook.com/apps/ y seleccionar la App que creaste. En la página de la App, selecciona en la app Whatsapp el botón "Configurar" y luego "Configuración básica".
13. Allí deberás otorgar una __URL de la Política de privacidad__ de forma obligatoria y el resto de campos de forma opcional. Al finalizar haz click en __Guardar cambios__.
14. Con todo ya configurado, la app está lista para pasar al modo Activo. Para ello ve hacia arriba de todo en la web y mueve el selector de Desarrollo a Activo. 
15. Obtener token permanente: Para ello debes tener una cuenta comercial de Meta. Ingresa a https://business.facebook.com/ y en el menú de la izquierda selecciona tu empresa, y haz click en la rueda de configuración, luego en Configuración de negocio. En la nueva ventana haz click en Usuarios del sistema y agrega uno nuevo.
16. Acepta el mensaje de la ventana que se abre y luego selecciona un nombre para tu nuevo usuario. En Rol debes colocar Administrador.
17. Al crear el usuario haz click en el botón __Agregar activos__. En la ventana que se abrirá selecciona Apps, luego marca la App que creaste y activa la opción __Administrar App__, luego Guarda los cambios.
18. Al asignar el activo, haz click en __Generar nuevo token__. Selecciona tu App y marca todos los permisos de la lista (No son todos necesarios pero si en un futuro se agregan más integraciones en Rocketbot podrás utilizar la misma credencial). Haz click en __Generar token__. Este será el token permanente que podrás utilizar para autenticarte en el módulo.

---

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

