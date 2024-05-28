from hdnhd_utils import *


def label_image(img):
    """
    Creates and returns a copy of the image, labeled as either Hot Dog or Not Hot Dog
    based off of the results from GCP Vision API.
    :param img: a string that is either the URL or filename for the image
    :return: a copy of the image labeled as either Hot Dog or Not Hot Dog
    """
    # TODO: replace pass with your code
    # Prompt user for input and have scan images which in which a pillow image is created and labels based on API are formed
    imgbytes = load_image_bytes(input(f'Enter a URL or filename of an Image:'))
    labels = detect_image_labels(imgbytes)
    img = create_pillow_img(imgbytes)

    #declare what the acceptable labels are
    top_text = str('Hot Dog')
    bottom_text = str('Not Hot Dog')


    img_width, img_height = img.size

    try:
        # compute the size of the top text when drawn
        if any(label['description'] == 'Hot dog' for label in labels):
            top_text_size_width, top_text_size_height = text_rect_size(top_text, font=ImageFont.truetype('ariblk.ttf', 22))
            # print(f'Top text size: {top_text_size_width, top_text_size_height}')
            top_text_x = img_width / 2 - top_text_size_width / 2
            img = add_text_to_img(img, top_text, color="white", bgcolor="green", pos=(top_text_x, 0))
            print(img)

        # compute the size of the bottom text when drawn
        else:
            bottom_text_size_width, bottom_text_height = text_rect_size(bottom_text,font=ImageFont.truetype('ariblk.ttf', 22))

            bottom_text_x = img_width / 2 - bottom_text_size_width / 2
            bottom_text_y = img_height - bottom_text_height

            img = add_text_to_img(img, bottom_text, color="white", bgcolor="red", pos=(bottom_text_x, bottom_text_y))
            print(img)
    finally:
        return img

def main():
    """
    Main function that runs the program.
    """
    # URLs for some sample images to try
    # NOTE: the TAs may use other images for testing your program
    # Hot Dog
    # img = 'https://upload.wikimedia.org/wikipedia/commons/b/b1/Hot_dog_with_mustard.png'
    # Not Hot Dog (Pizza)
    # img = 'https://render.fineartamerica.com/images/rendered/default/poster/8/10/break/images/artworkimages/medium/1/pizza-slice-diane-diederich.jpg'
    # The image below is an example of a hot dog that is not labeled as a hot dog
    # since your program relies on GCP Vision API, which is not perfect,
    # such an image will be (mis-)labeled as Not Hot Dog by your program
    # that is the expected behavior, you don't need to build your own better hot dog detector ;)
    # img = 'https://i.kinja-img.com/gawker-media/image/upload/s--6RyJpgBM--/c_scale,f_auto,fl_progressive,q_80,w_800/tmlwln8revg44xz4f0tj.jpg'
    img = label_image('img')
    img.show()
    # TODO: your code to read the URL/filename from the user
    # TODO: and then call label_image
    # TODO: and then finally show the image returned by the call to label_image

if __name__ == "__main__":
    main()
