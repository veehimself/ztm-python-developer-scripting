from PIL import Image

img = Image.open('./Pokedex/pikachu.jpg')

print(img.size)
print(img.mode)
print(img.format)


filtered_img = img.convert('L')

filtered_img.save('greyscalepikachu.png','png')
filtered_img.show()
crooked = filtered_img.rotate(90)
crooked.save('upsidedownpikachu.png','png')
resize = filtered_img.resize((300,300))
resize.save('resizepikachu.png','png')
box = (100,100,400,400)
region = filtered_img.crop(box)
region.save('croppikachu.png','png')

