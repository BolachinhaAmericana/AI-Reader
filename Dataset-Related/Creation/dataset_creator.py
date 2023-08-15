import os
import cairocffi as cairo
import random

from PIL import Image, ImageDraw, ImageOps

import essentials as e

FONTS = {'Concetta Kalvani': 'A',
         'Grechen Fuemen': 'B',
         'Meddon': 'C',
         'Princess Sofia': 'D',
         'Schoolbell': 'E',
         'Splash': 'F',
         'Vtks Garota Bonita': 'G',
         'Vtks legal': 'H',
         'Vtks Relaxing Blaze': 'I',
         'Dekko': 'J',
         'WindSong': 'K',
                }

DATA_PATH = 'dataset.csv'


if not os.path.exists('./Data'):
    os.makedirs('./Data')

def distort_text(text_list, disorganization, max_distortion, font_name, output_name, x, y):
    '''
    Creates image of text with distortion
    text_list 
    '''
    surface = cairo.ImageSurface(cairo.FORMAT_ARGB32, x, y)
    ctx = cairo.Context(surface)
    
    ctx.set_source_rgb(1, 1, 1)
    ctx.paint()

    offset_y = 50

    word_bboxes = []

    for text in text_list:
        lines = text.split('\n')
        offset_x = 0

        for line in lines:
            char_offset_x = offset_x
            word_bbox = None

            for char in line:
                char_distortion = max_distortion * random.random()
                angle = (random.random() - 0.5) * char_distortion * 60
                x_offset_change = (random.random() - 0.5) * char_distortion * 10
                y_offset_change = (random.random() - 0.5) * char_distortion * 10
                font_size = 30 + y_offset_change * 0.5

                font_face = cairo.ToyFontFace(font_name, cairo.FONT_SLANT_NORMAL, cairo.FONT_WEIGHT_NORMAL)

                ctx.set_font_face(font_face)
                ctx.set_source_rgba(0, 0, 0, 1 - char_distortion * 0.7)
                ctx.set_font_size(font_size)
                ctx.rotate(angle * (3.14 / 180.0))
                ctx.move_to(char_offset_x + x_offset_change + 0, offset_y + y_offset_change)
                ctx.show_text(char)
                char_offset_x += ctx.text_extents(char)[2]
                ctx.rotate(-angle * (3.14 / 180.0))

                char_bbox = ctx.text_extents(char)

                if word_bbox is None:
                    word_bbox = (int(char_offset_x + char_bbox[0]), int(offset_y + char_bbox[1]), 
                                 int(char_offset_x + char_bbox[2]), int(offset_y + char_bbox[3]))
                else:
                    word_bbox = (int(word_bbox[0]), int(min(word_bbox[1], offset_y + char_bbox[1])), 
                                 int(char_offset_x + char_bbox[2]), int(max(word_bbox[3], offset_y + char_bbox[3])))

            word_bboxes.append(word_bbox)
    surface.write_to_png(f"{output_name}")

    return word_bboxes

df = e.file_reader_to_list(DATA_PATH)
words, lines, abv = e.get_words_and_abrevisions(df)

saved_lines = lines
lines.sort()
sorted_lines = lines

dir_name_1 = e.get_dir_name_1()

def get_images(start_batch, end_batch, depth_one_index):
    os.system('touch words.txt')
    for i in enumerate(sorted_lines[start_batch:end_batch]): # para cada items da lista sorted
        #print(i)
        d1 = dir_name_1[depth_one_index]
        for font_name, font_id in FONTS.items():
            if not os.path.exists(f'./Data/{d1}/{d1}-0{i[0]}{font_id}'):
                os.makedirs(f'./Data/{d1}/{d1}-0{i[0]}{font_id}')
            if not os.path.exists(f'Crop_Data/{d1}/{d1}-0{i[0]}{font_id}'):
                os.makedirs(f'Crop_Data/{d1}/{d1}-0{i[0]}{font_id}')
            for i2 in enumerate(i[1]):

                word = i2[1]
                final_path = f'./Data/{d1}/{d1}-0{i[0]}{font_id}/{d1}-0{i[0]}{font_id}-00-0{i2[0]}.png'
                bboxes = distort_text([word], 0.5, 0.075, font_name, final_path, 1000, 500)
                    
                
                final_name = f'{d1}-0{i[0]}{font_id}-00-0{i2[0]}' # manter


                image = Image.open(final_path)
                #draw = ImageDraw.Draw(image)
                bbox = bboxes[-1]
                b1 = bbox[0] - 50 # inicio_X
                b2 = bbox[1] 
                b3 = bbox[2] # Fim_X
                b4 = bbox[3] - 10

                try:
                    os.mkdir(f'./Crop_Data')
                except:
                    pass
                
                inv_img = ImageOps.invert(image)
                bounding_box = inv_img.getbbox()
                roi = image.crop(bounding_box)

                roi.save(f'./Crop_Data/{d1}/{d1}-0{i[0]}{font_id}/{d1}-0{i[0]}{font_id}-00-0{i2[0]}.png')

                # ficheiro .txt
                os.system(f'echo {final_name} ok 170 {b1} {b2} {b3} {b4} AT {word} >> words.txt')

char_lists = []
for x in range(33):
    depth_one_index = x
    start_batch = depth_one_index * 50
    end_batch = start_batch + 50
    get_images(start_batch, end_batch, depth_one_index)
    bounding_boxes = distort_text(['', 'Testing'], 1, 0.1, 'Dekko', 'test', 1000, 1000)

