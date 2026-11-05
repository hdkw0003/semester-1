from image import Image

testy = Image.read("test.pgm")
testy.create_pixels(10, 10, 30)
testy._write_pixels("4")
