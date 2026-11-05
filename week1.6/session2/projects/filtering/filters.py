from image import Image
img = Image()

img.read_pgm("./images/feep.pgm")

for row in range(1, img.height - 1):
    for col in range(1, img.width - 1):
        