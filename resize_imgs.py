from PIL import Image
import glob

img_path = r"C:\Users\shakt\sample images\ben-benjamin-79wo3zOy-5M-unsplash.jpg"

im = Image.open(img_path)
print('{}'.format(im.format))
print('size {}'.format(im.size))
print('image mode {}'.format(im.mode))
im.show()

image_list = []
resized_images = []
for filename in glob.glob(r'C:\Users\shakt\sample images\*.jpg'):
  print(filename)
  img = Image.open(filename)
  image_list.append(img)

for image in image_list:
  img_ = image.resize((600,600))
  resized_images.append(img_)

for (i, new) in enumerate(resized_images):
  new.save('{}{}{}'.format(r'C:\Users\shakt\sample images', i+1, '.jpg'))
