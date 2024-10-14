from PIL import Image, ImageOps, ImageFilter, ImageEnhance
# загрузили изображение из файла, используйте open()функцию в Imageмодуле
im = Image.open("zebra.JPG")

# атрибуты экземпляра для проверки содержимого файла:
# Атрибут format определяет источник изображения. Если изображение не было считано из файла,
# ему присваивается значение None. Атрибут size — это 2-кортеж, содержащий ширину и высоту (в пикселях).
# Атрибут mode определяет количество и названия полос на изображении, а также тип и глубину пикселей.
# Обычные режимы — «L» (яркость) для изображений в оттенках серого, «RGB» для полноцветных изображений
# и «CMYK» для допечатных изображений.
#
# Если файл не может быть открыт, OSError возникает исключение.

print(im.format, im.size, im.mode)
# отобразим изображение, которое мы только что загрузили

im.show()

# Разделение и слияние полос

r, g, b = im.split()
im = Image.merge("RGB", (b, g, r))

im.show()

# содержит методы для resize()и rotate()изображения. Первый принимает кортеж, дающий новый размер,
# второй — угол в градусах против часовой стрелки
out = im.resize((400, 400))
out.show()


out = im.rotate(45)
out.show()
# Транспонирование изображения
out = im.transpose(Image.Transpose.FLIP_LEFT_RIGHT)
out = im.transpose(Image.Transpose.FLIP_TOP_BOTTOM)
out = im.transpose(Image.Transpose.ROTATE_90)
out = im.transpose(Image.Transpose.ROTATE_180)
out = im.transpose(Image.Transpose.ROTATE_270)


out.show()


# Применение фильтров
out = im.filter(ImageFilter.DETAIL)

out.show()
# Улучшение изображений
enh = ImageEnhance.Contrast(im)
enh.enhance(1.3).show("80% more contrast")

im.show()

