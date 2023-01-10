# chrome-extension-template
![favicon-128x128](https://user-images.githubusercontent.com/58629614/211460652-ccfcf7be-0f83-4170-9404-0a23475a3a07.png)

To install the backend image-caption-service locally, follow these steps:

1. Run the command pipenv install to install the necessary dependencies for the project.
2. Obtain the .env file from another developer. This file should contain the necessary environment variables for the project, such as the API keys and endpoint URLs for the cognitive service instance.
3. To test locally, run the main.py script in the image-caption-service directory to start the service.
4. To test remotely, deploy the Azure Function using VSCode. This will allow the service to be accessed remotely through an HTTP trigger.
5. Test the Azure Function using the remote URL provided by Azure. This will allow you to verify that the function is working correctly and that the image-caption-service is able to generate captions for images as expected.

To install the Chrome extension locally, follow these steps:

1. Download the repository. You will install from the chrome-extension folder.
2. Open the Chrome browser and go to the extensions page by typing chrome://extensions/ into the address bar and hitting enter.
3. Enable Developer Mode by clicking the toggle switch in the top right corner of the page.
4. Click the "Load Unpacked" button and select the extension file that you downloaded in step 1.
5. Chrome will now install the extension and you should see it listed on the extensions page.
6. To use the extension, click on the extension icon in the browser toolbar.
