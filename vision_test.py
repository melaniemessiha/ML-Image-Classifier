from hdnhd_utils import *
from pprint import pprint

imgbytes = load_image_bytes("C:\Users\12395\OneDrive\Documents\hwm.png")
labels = detect_image_labels(imgbytes)
pprint(labels)



