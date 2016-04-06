# takes in a number of parameters regarding the tumblr page to be scraped
# outputs a csv containing the urls of the pictures of puppies

import urllib.request
import re
import csv
import io
import struct

page_low = 510
page_high = 1974
url = "http://puppiesarecute.tumblr.com/"
pattern = "<img src=\"([a-zA-z0-9:/._]*?)\" width=\"400\" border=\"0\">"
dest = 'raw_dog_1.txt'


def getImageInfo(data):
    data = data
    size = len(data)
    #print(size)
    height = -1
    width = -1
    content_type = ''

    # handle GIFs
    if (size >= 10) and data[:6] in (b'GIF87a', b'GIF89a'):
        # Check to see if content_type is correct
        content_type = 'image/gif'
        w, h = struct.unpack(b"<HH", data[6:10])
        width = int(w)
        height = int(h)

    # See PNG 2. Edition spec (http://www.w3.org/TR/PNG/)
    # Bytes 0-7 are below, 4-byte chunk length, then 'IHDR'
    # and finally the 4-byte width, height
    elif ((size >= 24) and data.startswith(b'\211PNG\r\n\032\n')
          and (data[12:16] == b'IHDR')):
        content_type = 'image/png'
        w, h = struct.unpack(b">LL", data[16:24])
        width = int(w)
        height = int(h)

    # Maybe this is for an older PNG version.
    elif (size >= 16) and data.startswith(b'\211PNG\r\n\032\n'):
        # Check to see if we have the right content type
        content_type = 'image/png'
        w, h = struct.unpack(b">LL", data[8:16])
        width = int(w)
        height = int(h)

    # handle JPEGs
    elif (size >= 2) and data.startswith(b'\377\330'):
        content_type = 'image/jpeg'
        jpeg = io.BytesIO(data)
        jpeg.read(2)
        b = jpeg.read(1)
        try:
            while (b and ord(b) != 0xDA):
                while (ord(b) != 0xFF): b = jpeg.read(1)
                while (ord(b) == 0xFF): b = jpeg.read(1)
                if (ord(b) >= 0xC0 and ord(b) <= 0xC3):
                    jpeg.read(3)
                    h, w = struct.unpack(b">HH", jpeg.read(4))
                    break
                else:
                    jpeg.read(int(struct.unpack(b">H", jpeg.read(2))[0])-2)
                b = jpeg.read(1)
            width = int(w)
            height = int(h)
        except struct.error:
            pass
        except ValueError:
            pass

    return content_type, width, height

def scrape(url, pattern, page_low, page_high, dest):
  count = 0
  with open(dest, 'w', newline='') as out_file:
    writer = csv.writer(out_file)
    for i in range(page_low, page_high + 1):
      with urllib.request.urlopen(url + "page/" + str(i)) as response:
        html = str(response.read())
        matches = re.findall(pattern, html)
        for match in matches:
          with urllib.request.urlopen(match) as res:
            content_type, width, height = (getImageInfo(res.read()))
            if width >= height:
              writer.writerow([match])
              count += 1
      print("finished " + str(i) + " pages, total puppies: " + str(count))
