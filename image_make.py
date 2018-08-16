from PIL import Image, ImageDraw, ImageFont, ImageFilter
import os

#configuration
width=64
height=width
back_ground_color=(255,255,255)
font_size=40
font_color=(0,0,0)
path_dir = "font/"


def get_offset(ch, font, canvas_size):
    font_size = font.getsize(ch)
    font_offset = font.getoffset(ch)
    offset_x = canvas_size/2 - font_size[0]/2 - font_offset[0]/2
    offset_y = canvas_size/2 - font_size[1]/2 - font_offset[1]/2
    return [offset_x, offset_y]

def draw_char(font,ch):
    im = Image.new ( "RGB", (width,height), back_ground_color )
    draw = ImageDraw.Draw (im)
    unicode_font = ImageFont.truetype(path_dir + font + ".ttf", font_size)
    offset_x, offset_y = get_offset(ch, unicode_font, width)
    draw.text ( (offset_x,offset_y), ch, font=unicode_font, fill=font_color )
    im.save("font/save/" + font + "_" + str(s[ch]) + ".png")


text = list("다람쥐헌쳇바퀴에타고파")
num = [i for i in range(len(text))]
s = dict(zip(text,num))
print(s)


file_list = os.listdir(path_dir)
print(file_list)

font_list = []
for font in file_list:
    font_list.append(font[:-4])

for font in font_list:
    print(font)
    for char in text:
        # draw_char(font,char)

        try:
            draw_char(font,char)
        except:
            break

print("finish")