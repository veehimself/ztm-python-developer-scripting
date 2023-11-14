from PIL import Image

img = Image.open('./Pokedex/pikachu.jpg')

print(img.size)
print(img.mode)
print(img.format)


filtered_img = img.convert('L')

filtered_img.save('greyscalepikachu.png','png')
