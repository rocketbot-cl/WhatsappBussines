



# Whatsapp Business
  
This module allows you to connect to the Whatsapp Business API and send text or template messages.  

*Read this in other languages: [English](Manual_WhatsappBusiness.md), [Português](Manual_WhatsappBusiness.pr.md), [Español](Manual_WhatsappBusiness.es.md)*
  
![banner](imgs/Banner_WhatsappBusiness.jpg)
## How to install this module
  
To install the module in Rocketbot Studio, it can be done in two ways:
1. Manual: __Download__ the .zip file and unzip it in the modules folder. The folder name must be the same as the module and inside it must have the following files and folders: \__init__.py, package.json, docs, example and libs. If you have the application open, refresh your browser to be able to use the new module.
2. Automatic: When entering Rocketbot Studio on the right margin you will find the **Addons** section, select **Install Mods**, search for the desired module and press install.  

## How to use this module
To use this module, you must complete the following setup:
1. __Login__ or __Sign up__ at https://developers.facebook.com/
2. Go to your Apps at https://developers.facebook.com/apps/ and click the Create App button.
3. Connect the business portfolio, which is the Facebook business account to which the App will be linked. Click Next.
4. On the next page What do you want your app to do? choose the Other option from the Looking for something else? section. Click Next.
5. Select the Business app type and click Next.
6. Choose the name, administrator email, and Business Account to which the App will be linked. Click Create, and you will be asked to enter your password to finish. When you create the App, you will be redirected to the App page, which will be in Development mode.
7. On this page, select the __Setup__ button in the Whatsapp app and then click __Start using the API__ under API Settings. You will be given a test number to send messages and up to 5 
contacts that you can add to receive test messages. In both the development and production App, you can only send messages that include text to conversations that have been started by the user. If the conversation is started by the company, you must send templates that have been approved by META. For more information, check the following link: https://developers.facebook.com/docs/whatsapp/api/messages/message-templates
8. On the API Settings page, you will see a temporary access token to use the API. This token lasts for 24 hours. If you want to use the API for longer, you must request a permanent access token (See point 13). 9. In Step 1 of this page you will have access to the WhatsApp test number and the recipient number settings. You also have the Phone Number Identifier. Both this data and the token will be necessary to be able to connect through the module in developer mode.
10. Try to associate a recipient and send from the module the default template hello_world with the 
language en_US. If everything works correctly, you will receive a WhatsApp message with the text "Hello World!".
11. Once you have verified the operation, you can create your own templates that need to be approved by META and send them through the module. For more information about the templates, check the following link: https://developers.facebook.com/docs/whatsapp/api/messages/message-templates
12. Once you have verified the operation of the API, you must add a phone number for your company to be able to send messages to your clients. In step 5 of the API Configuration page, click on the __Add phone number__ button and follow the steps to create the WhatsApp Business profile. Once added, save the Phone Number Identifier, this information will be necessary to be able to connect through the module.
13. Once you have added a phone number, you need to configure the application to go into production mode and generate a permanent access token. To do this, you must go to the App page at 
https://developers.facebook.com/apps/ and select the App you created. On the App page, select the "Basic" option in App Configuration.
14. There you must provide a mandatory __Privacy Policy URL__ and the rest of the fields as optional. When you finish, click on __Save changes__.
15. With everything already configured, the app is ready to go into Active mode. To do this, go to the top of the web and move the Development selector to Active.
16. Get a permanent token: To do this, you must have a Meta business account. Go to https://business.facebook.com/ and in the menu on the left select your company, and click on the configuration wheel, then on Business Settings. In the new window go to Users > System Users and add a new user.
17. Accept the message in the window that opens and then select a name for your new user. In Role you must put Administrator.
18. When creating the user, click on the __Assign assets__ button. In the window that will open, select Apps, then select the App you 
created and activate the __Manage App__ option, then Save changes.
19. When assigning the asset, click on __Generate new token__. Select your App, in __Token expiration__ choose __Never__ and check all the permissions on the list (not all of them are necessary but if more integrations are added to Rocketbot in the future you will be able to use the same credential). Click on __Generate token__. This will be the permanent token that you can use to authenticate to the module.


## Description of the commands

### Configure server
  
Configure the Whatsapp API to be able to execute commands
|Parameters|Description|example|
| --- | --- | --- |
|API KEY|API KEY obtained in https//developers.facebook.com/|api-key|
|Phone number identifier|Phone number identifier obtained in https//developers.facebook.com/|116787907958900|
|Assign result to a variable|Variable where the result will be saved|Variable|

### Send text message or template
  
Sends a text message or from a template to a Whatsapp number
|Parameters|Description|example|
| --- | --- | --- |
|Whatsapp number|Whatsapp number to which the message will be sent|5551112222|
|Template and language code|Message template and language code that will be sent to the Whatsapp number.|hello_world, en_US|
|Template Params|Optional. Specify the parameter(s) using a list ['1param', '2param']|['1param', '2param']|
|Message|Message that will be sent to the Whatsapp number|Hello, how are you?|
|Assign result to a variable|Variable where the result will be saved|Variable|
