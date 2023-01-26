# alto - an accessibility browser add-on

![alto logo](chrome-extension/icons/128x128.png)

## Add-on Installation Instructions

1. Download the .ZIP file of the code.

![The Bigger Picture GitHub repository with code options opened and "Download ZIP" highlighted in red](https://user-images.githubusercontent.com/69097387/214959076-09f1fb13-69f6-470b-ac3d-4520ee35a954.png)

2. Open the Chrome browser and go to the extensions page, either by typing chrome://extensions/ into the address bar and hitting enter, or clicking on the extensions icon on the top right menu bar.

![Google Chrome extensions page, with link in the address bar and extensions icon highlighted in red](https://user-images.githubusercontent.com/69097387/214959401-12da7774-1b40-440a-8d1e-164bf340f260.png)

3. Enable Developer Mode by clicking the toggle switch in the top right corner of the page.

![Google Chrome extensions page, with Developer Mode toggle highlighted in red](https://user-images.githubusercontent.com/69097387/214959582-6da3ba75-ec7a-46b1-ad9c-07c14e976158.png)

4. Click the "Load Unpacked" button and select the `chrome-extension` folder from the folder that you downloaded in step 1.

![Google Chrome extensions page, with Load Unpacked button and the chrome-extension folder in File Explorer highlighted in red](https://user-images.githubusercontent.com/69097387/214960799-a6f7143d-00d6-44d0-9159-bbde7a1834fa.png)

5. Chrome will now install the extension and you should see it listed on the extensions page.

![Google Chrome extensions page, with alto extension highlighted in red](https://user-images.githubusercontent.com/69097387/214961073-664fdd7b-7db7-4347-8f47-9b9be9973e7e.png)

6. To use the extension, click on the extension icon in the browser toolbar and pin it.

![Google Chrome extensions page, with alto pin option in the extensions menu highlighted](https://user-images.githubusercontent.com/69097387/214961486-7c31ad8a-4eb2-405d-b52c-2b6cb95eeb31.png)

Congratulations, you have successfully installed the alto browser add-on!
Note: The alto add-on icon is where you can access the options menu.

## Quick Start

1. Go to any website with images (e.g.[Pexels](https://www.pexels.com/)).
2. The first five images originally lacking in alt text should have alt text generated provided the setting has been enabled in the alto popup options menu.
3. For images still lacking in alt text, you can right-click the image and select the option "Generate alt text for all images" in the context menu to generate the alt text.

![Four images of cherry blossoms, with one darkened with the context menu opened. The option "Generate alt text for all images" is highlighted in red](https://user-images.githubusercontent.com/69097387/214961995-76673fa1-5b19-4f8c-a21e-baabbf842183.png)


## Backend Installation Instructions:
1. Run the command pipenv install to install the necessary dependencies for the project.
2. Obtain the .env file from another developer. This file should contain the necessary environment variables for the project, such as the API keys and endpoint URLs for the cognitive service instance.
3. To test locally, run the main.py script in the image-caption-service directory to start the service.
4. To test remotely, deploy the Azure Function using VSCode. This will allow the service to be accessed remotely through an HTTP trigger.
5. Test the Azure Function using the remote URL provided by Azure. This will allow you to verify that the function is working correctly and that the image-caption-service is able to generate captions for images as expected.
