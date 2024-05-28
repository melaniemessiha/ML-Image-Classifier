# DO NOT CHANGE THE CODE IN THIS FILE
# YOU ARE NOT SUBMITTING THIS FILE WITH YOUR SOLUTION
from PIL import Image, ImageDraw, ImageFont
from pprint import pformat
from io import BytesIO

# the cache for the image labels
_image_labels_cache = {}


def cached(cachefile):
    """
    A function that creates a decorator which will use "cachefile" for caching the results of the decorated function "fn".
    """
    # This function is a lightly-edited version of the one found at
    # https://datascience.blog.wzb.eu/2016/08/12/a-tip-for-the-impatient-simple-caching-with-python-pickle-and-decorators/,
    # last access 12/1/2022
    import os
    import pickle

    def decorator(fn):  # define a decorator for a function "fn"
        global _image_labels_cache
        # load the cachefile if it exists
        if os.path.exists(cachefile):  # if the cache file exists, load it
            with open(cachefile, 'rb') as f:
                _image_labels_cache = pickle.load(f)

        def wrapped(*args, **kwargs):  # define a wrapper that will finally call "fn" with all arguments
            import hashlib
            # if cache exists and the image is in the cache -> return the cached labels
            global _image_labels_cache
            hashed_arg = ''
            # args[0] is either a string or bytes
            if isinstance(args[0], bytes):
                hashed_arg = hashlib.sha256(args[0]).hexdigest()
            else:
                hashed_arg = hashlib.sha256(args[0].encode()).hexdigest()

            if _image_labels_cache != {} and hashed_arg in _image_labels_cache:
                # print(f'using cached result from {cachefile}')
                return _image_labels_cache[hashed_arg]

            # else
            # execute the function with all arguments passed
            res = fn(*args, **kwargs)

            # store the result in the cache
            _image_labels_cache[hashed_arg] = res

            # write to cache file
            with open(cachefile, 'wb') as cachehandle:
                # print("saving result to cache '%s'" % cachefile)
                pickle.dump(_image_labels_cache, cachehandle)

            return res

        return wrapped

    return decorator  # return this "customized" decorator that uses "cachefile"


@cached('labels_cache.pkl')
def detect_image_labels(img):
    """
    Gets the labels from GCP Vision API for the given image
    :param img: either the image bytes or a string that is the URL or filename for an image

    :return: the list of dictionaries containing the labels
    """

    # ---------------------------------------------------------------
    # that's right Pyton has nested functions
    # the anot_to_dict function can only be called from
    # within the detect_image_labels function

    def anot_to_dict(anot):
        """
        Converts the given GCP annotation result type to a dictionary
        :param anot: the GCP annotation result type object
        :return: a dictionary containing the annotation
        """
        return {'mid': anot.mid, 'description': anot.description, 'score': anot.score, 'topicality': anot.topicality}

    # end nested function
    # ---------------------------------------------------------------

    # rest of the body of the detect_image_labels function
    from google.cloud import vision

    # determine if the function was called with bytes, a URL, or a filename
    imgbytes = None
    if type(img) is bytes:
        imgbytes = img
    else:
        imgbytes = load_image_bytes(img)

    # create the GCP client
    client = vision.ImageAnnotatorClient()

    # create the GCP image object
    image = vision.Image(content=imgbytes)

    # get the labels from GCP
    response = client.label_detection(image=image)

    # convert the GCP labels to a list of dictionaries
    return [anot_to_dict(label) for label in response.label_annotations]


def format_text(text, columns):
    """
    Returns a copy of text that will not span more than the specified number of columns
    :param text: the text
    :param columns: the maximum number of columns
    :return: the formatted text
    """
    # format the text to fit the specified columns
    import re
    text = re.sub('[()\']', '', pformat(text, width=columns))
    text = re.sub('\n ', '\n', text)
    return text


def text_rect_size(text, font, draw=None):
    """
    Returns the size of the rectangle to be used to
    draw as the background for the text
    :param text: the text to be displayed
    :param font: the font to be used
    :param draw: an ImageDraw.Draw object
    :return: the size of the rectangle to be used to draw as the background for the text
    """
    if draw is None:
        dummy_img = Image.new('RGB', (0, 0), (255, 255, 255, 0))
        draw = ImageDraw.Draw(dummy_img)
        (width, height) = draw.multiline_textsize(text, font=font)
        del draw
    else:
        (width, height) = draw.multiline_textsize(text, font=font)
    return width * 1.1, height * 1.3


def add_text_to_img(img, text, pos=(0, 0), color=(0, 0, 0), bgcolor=(255, 255, 255, 128),
                    columns=60,
                    font=ImageFont.truetype('ariblk.ttf', 22)):
    """
    Creates and returns a copy of the image with the specified text displayed on it
    :param img: the (Pillow) image
    :param text: the text to display
    :param pos: a 2 tuple containing the xpos, and ypos of the text
    :param color: the fill color of the text
    :param bgcolor: the background color of the box behind the text
    :param columns: the max number of columns for the text
    :param font: the font to use
    :return: a copy of the image with the specified text displayed on it
    """

    # make a blank image for the text, initialized to transparent text color
    txt_img = Image.new('RGBA', img.size, (255, 255, 255, 0))
    draw = ImageDraw.Draw(txt_img)

    # format the text
    text = format_text(text, columns)
    # get the size of the text drawn in the specified font
    (text_width, text_height) = ImageDraw.Draw(img).multiline_textsize(text, font=font)

    # compute positions and box size
    (xpos, ypos) = pos
    rwidth = text_width * 1.1
    rheight = text_height * 1.4
    text_xpos = xpos + (rwidth - text_width) / 2
    text_ypos = ypos + (rheight - text_height) / 2

    # draw the rectangle (slightly larger) than the text
    draw.rectangle([xpos, ypos, xpos + rwidth, ypos + rheight], fill=bgcolor)

    # draw the text on top of the rectangle
    draw.multiline_text((text_xpos, text_ypos), text, font=font, fill=color)

    del draw  # clean up the ImageDraw object
    return Image.alpha_composite(img.convert('RGBA'), txt_img)


def create_pillow_img(imgbytes):
    """
    Creates and returns a Pillow image from the given image bytes
    :param imgbytes: the bytes of the image
    """
    return Image.open(BytesIO(imgbytes))


def load_image_bytes(img):
    """
    Loads and returns the image either from a URL or a file
    :param img: string that is either the URL or file
    :return:
    """

    # ---------------------------------------------------------------
    # that's right Pyton has nested functions
    # these two functions, load_image_bytes_from_url and load_image_bytes_from_file,
    # can only be called from within the load_image_bytes function
    def load_image_bytes_from_url(imgurl):
        """
        Loads and returns the bytes of the image from the specified url
        :param imgurl: the url
        """
        import requests
        resp = requests.get(imgurl)
        imgbytes = resp.content
        return imgbytes

    def load_image_bytes_from_file(filename):
        """
        Loads and returns the bytes of the image from the specified file
        :param filename: the name of the file
        Based on
           https://docs.aws.amazon.com/rekognition/latest/dg/example4.html,
           last access 10/3/2017
        """
        with open(filename, 'rb') as imgfile:
            return imgfile.read()

    # end nested functions
    # ---------------------------------------------------------------

    # this is the actual code of the load_image_bytes function
    if img.lower().startswith('http'):
        return load_image_bytes_from_url(img)
    else:
        return load_image_bytes_from_file(img)
