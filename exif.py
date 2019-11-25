#Developed with code form Jayson DeLancey and  he deserves all credit
#https://developer.here.com/blog/getting-started-with-geocoding-exif-image-metadata-in-python3

#prints the exif data for a photo

from PIL import Image
from PIL.ExifTags import TAGS, GPSTAGS

photo = "myphoto.jpg"


#Get the label data of the exif dictionary
#Note, it works with just the exif, but this populates with human readable labels
def get_labeled_exif(exif):
    labeled = {}
    for (key, val) in exif.items():
        labeled[TAGS.get(key)] = val

    return labeled

#Get the exif data in the raw form
def get_exif(filename):
    image = Image.open(filename)
    image.verify()
    return image._getexif()

exif = get_exif(photo)
labeled = get_labeled_exif(exif)

for x, y in labeled.items():
	print(x, y)
