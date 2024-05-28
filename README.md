# Machine-Learning-Hot-Dog-Not-Hot-Dog-Image-Classifier
This Python program utilizes the Google Cloud Platform Vision API to label images as either "Hot Dog" or "Not Hot Dog." It takes a user-provided image URL or filename, sends it to the Vision API for analysis, and then displays the labeled image.

# How it works:
User Input: The program prompts the user to enter the URL or filename of an image.
Image Loading: The load_image_bytes() function retrieves the image data from the provided URL or filename.
Label Detection: The detect_image_labels() function uses the GCP Vision API to analyze the image and return a list of detected labels.

# Image Labeling:
The code checks if the detected labels contain "Hot dog". If it does, the image is labeled as "Hot Dog" with a green background.
If "Hot dog" is not found, the image is labeled as "Not Hot Dog" with a red background.
Image Display: The labeled image is displayed using the show() method from the Pillow library.

# Requirements:
Python 3.x
Pillow library (pip install pillow)
Google Cloud Platform account with Vision API enabled

# Instructions:
Install the required libraries: pip install pillow
Enable the Vision API in your Google Cloud Platform project: https://cloud.google.com/vision/docs/
Set up your Google Cloud Platform credentials following the instructions here: https://cloud.google.com/docs/authentication/getting-started
Run the Python script. You will be prompted to enter an image URL or filename.

# Example Usage:
Enter a URL or filename of an Image: (user input)
Note: Utilize the images provided in the repository. They are great examples for this project. I would reccomend downloading them and copy/paste the file path for user input.
The program will analyze the image and display the labeled image as "Hot Dog."

# Limitations:
This program relies on the accuracy of the GCP Vision API. The API may not always correctly identify hot dogs in all images.
The labels are static and do not adapt to different image sizes.

# Future Improvements:
Implement more robust image labeling techniques for improved accuracy.
Allow users to customize the labels and text styles.
Integrate with other image processing libraries for more advanced functionalities.
This code serves as a basic example of using the GCP Vision API for image labeling. It can be further extended and modified to suit your specific needs.

