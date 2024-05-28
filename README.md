# Machine-Learning-Hot-Dog-Not-Hot-Dog-Image-Classifier
This Python program utilizes the Google Cloud Platform Vision API to label images as either "Hot Dog" or "Not Hot Dog." It takes a user-provided image URL or filename, sends it to the Vision API for analysis, and then displays the labeled image.

# How it works:
User Input: The program prompts the user to enter the URL or filename of an image.<br>
Image Loading: The load_image_bytes() function retrieves the image data from the provided URL or filename.<br>
Label Detection: The detect_image_labels() function uses the GCP Vision API to analyze the image and return a list of detected labels.<br>

# Image Labeling:
The code checks if the detected labels contain "Hot dog". If it does, the image is labeled as "Hot Dog" with a green background.<br>
If "Hot dog" is not found, the image is labeled as "Not Hot Dog" with a red background.<br>
Image Display: The labeled image is displayed using the show() method from the Pillow library.<br>

# Requirements:
Python 3.x<br>
Pillow library (pip install pillow)<br>
Google Cloud Platform account with Vision API enabled<br>

# Instructions:
Install the required libraries: pip install pillow<br>
Enable the Vision API in your Google Cloud Platform project: https://cloud.google.com/vision/docs/<br>
Set up your Google Cloud Platform credentials following the instructions here: https://cloud.google.com/docs/authentication/getting-started<br>
Run the Python script. You will be prompted to enter an image URL or filename.<br>

# Functionality Explained
label_image(filename): This function takes a single parameter, filename, which is a string representing the filename of the image. It uses the hdnhd_utils.detect_image_labels() function to get a list of dictionaries containing information about the objects detected in the image by Google Cloud Vision. The code will then determine if the image contains a hot dog or not by searching the list of dictionaries. If a hot dog is detected, centered text with a green background and white text saying "Hot Dog" should be added at the top of the image. Otherwise, centered text with a red background and white text saying "Not Hot Dog" should be added at the bottom of the image.<br>

main(): Implement the code to prompt the user for a local (on the disc) JPG (JPEG) or PNG file or the URL to a JPG (JPEG) or PNG file. Display the image with either "Hot Dog" or "Not Hot Dog" displayed in the appropriate place/color on the image, depending on whether Google Cloud Vision detects a hot dog in the image. Exit the program with exit code 1 if the user has not selected a file.
Whether a hot dog exists in the image must come from the code written that correctly checks the results from hdnhd_utils.detect_image_labels().<br>

# Example Usage:
Enter a URL or filename of an Image: (user input)<br>
Note: Utilize the images provided in the repository. They are great examples for this project. I would reccomend downloading them and copy/paste the file path for user input.<br>
The program will analyze the image and display the labeled image as "Hot Dog."<br>

# Limitations:
This program relies on the accuracy of the GCP Vision API. The API may not always correctly identify hot dogs in all images.<br>
The labels are static and do not adapt to different image sizes.<br>

# Future Improvements:
Implement more robust image labeling techniques for improved accuracy.<br>
Allow users to customize the labels and text styles.<br>
Integrate with other image processing libraries for more advanced functionalities.<br>
This code serves as a basic example of using the GCP Vision API for image labeling. It can be further extended and modified to suit your specific needs.<br>

