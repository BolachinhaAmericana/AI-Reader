import random
import cairocffi as cairo



def distort_text(text_list, disorganization, max_distortion, font_index, output_name):
    ''' Creates Image With Text'''
    font_family = list(approved_fonts.values())[font_index]
    surface = cairo.ImageSurface(cairo.FORMAT_ARGB32, 300, 100)
    ctx = cairo.Context(surface)
    ctx.set_source_rgb(1, 1, 1)
    ctx.paint()

    offset_y = 0

    for text in text_list:
        lines = text.split('\n')
        offset_x = (random.random() - 0.5) * disorganization * 100

        for line in lines:
            offset_x += (random.random() - 0.5) * disorganization * 50
            char_offset_x = offset_x

            for char in line:
                char_distortion = max_distortion * random.random()
                angle = (random.random() - 0.5) * char_distortion * 60
                x_offset_change = (random.random() - 0.5) * char_distortion * 10
                y_offset_change = (random.random() - 0.5) * char_distortion * 10
                font_size = 24 + y_offset_change * 0.5


                #font_path = "~/Downloads/SedgwickAveDisplay-Regular.ttf"

                font_face = cairo.ToyFontFace(font_family, cairo.FONT_SLANT_NORMAL, cairo.FONT_WEIGHT_BOLD)
                #font_face = cairo.ToyFontFace.createFromFtFace(cairo.ft_font_create_for_file(font_path), 0)
                ctx.set_font_face(font_face)

                #ctx.select_font_face(font_path, cairo.FONT_SLANT_NORMAL, cairo.FONT_WEIGHT_BOLD)
                ctx.set_font_size(font_size)
                ctx.set_source_rgba(0, 0, 0, 1 - char_distortion * 0.7)
                ctx.move_to(char_offset_x + x_offset_change + 50, offset_y + y_offset_change)
                ctx.rotate(angle * (3.14 / 180.0))
                ctx.show_text(char)
                ctx.rotate(-angle * (3.14 / 180.0))

                char_offset_x += ctx.text_extents(char)[2]

            offset_y += 30 + (random.random() - 0.5) * disorganization * 20

        offset_y += 30




    # Save the image
    surface.write_to_png(f"{output_name}.png")





FONTS = {'A': 'Kaushan Script',
         'B': 'Felipa',
         'C': 'Kristi',
         'D': 'Dancing Script',
         'E': 'Kaushan Script',
         'F': 'La Belle Aurore',
         'G': 'Marck Script',
         'H': 'Miss Fajardose',
         'I': 'Pacifico',
         'J': 'Parisienne',
         'K': 'Princess Sofia',
         'L': 'Satisfy',
         'M': 'Schoolbell',
         'N': 'Sofia',
         'O': 'Tangerine',
         'P': 'WindSong',
         'Q': 'Yellowtail'
         }

OLD_FONTS = {1: 'bedtime stories',
             2: 'PWsignaturefont',
             3: 'Splash',
             4: 'Concetta Kalvani',
             5: 'Douglas Adams Hand',
             6: 'Meddon',
             7: 'Vtks Academy',
             8: 'Vtks legal',
             9: 'Vtks Relaxing Blaze',
             10: 'Dekko',
             11: 'Nothing You Could Do'
             }

for key, values in OLD_FONTS.items():
    
    #print(key, values)
    #distort_text(['', "Hello Class, My name is Hector"], 00, 0, key - 1, values)
    pass


'''
List of characters in data

"
'['+', ',', '-', '.', '/', '0', '1', '2', '3', '4', '7', 'A', 'B', 'C', 'D', 'E', 'F', 'G', 'H', 'I', 'J', 'K', 'L', 'M', 'N', 'O', 'P', 'Q', 'R', 'S', 'T', 'U', 'V', 'W', 'X', 'Y', 'Z', 'a', 'b', 'c', 'd', 'e', 'f', 'g', 'h', 'i', 'j', 'k', 'l', 'm', 'n', 'o', 'p', 'q', 'r', 's', 't', 'u', 'v', 'w', 'x', 'y', 'z', 'É', 'Ñ', 'á', 'â', 'ã', 'ç', 'è', 'é', 'ê', 'í', 'ñ', 'ó', 'ô', 'õ', 'ö', 'ú', 'ü']'
"

'''

#all fonts for testing
font_dict = {1: 'bedtime stories',
             2: 'Concetta Kalvani',
             3: 'Dekko',
             4: 'Douglas Adams Hand',
             5: 'Fuzzy Blubbles',
             6: 'Grechen Fuemen',
             7: 'Libertango',
             8: 'Vtks legal',
             9: 'Vtks Relaxing Blaze',
             10: 'Splash',
             11: 'Nothing You Could Do',
             12: 'PWsignaturefont',
             13: 'Reenie Beanie',
             14: 'Oooh Baby',
             15: 'Meddon',
             16: 'Vtks Garota Bonita',
             17: 'Vtks Academy',
             18: 'Kaushan Script',
             19: 'Felipa',
             20: 'Kristi',
             21: 'Dancing Script',
             22: 'Kaushan Script',
             23: 'La Belle Aurore',
             24: 'Marck Script',
             25: 'Miss Fajardose',
             26: 'Pacifico',
             27: 'Parisienne',
             28: 'Princess Sofia',
             29: 'Satisfy',
             30: 'Schoolbell',
             31: 'Sofia',
             32: 'Tangerine',
             33: 'WindSong',
             34: 'Yellowtail',
             }
approved_fonts = {1: 'Concetta Kalvani',
                  2: 'Dancing Script',
                  3: 'Dekko',
                  4: 'Felipa',
                  5: 'Grechen Fuemen',
                  6: 'Kaushan Script',
                  7: 'Kristi',
                  8: 'La Belle Aurore',
                  9: 'Marck Script',
                  10: 'Meddon',
                  11: 'Miss Fajardose',
                  12: 'Vtks Relaxing Blaze',
                  13: 'Splash',
                  14: 'Nothing You Could Do',
                  15: 'Oooh Baby',
                  16: 'Pacifico',
                  17: 'Parisienne',
                  18: 'Princess Sofia',
                  19: 'Satisfy',
                  20: 'Schoolbell',
                  21: 'Sofia',
                  22: 'Tangerine',
                  23: 'WindSong',
                  24: 'Yellowtail',
                  25: 'Reenie Beanie',
                  26: 'Vtks Garota Bonita',
                  27: 'Vtks legal',
                  }
chosen_fonts = {1: 'Concetta Kalvani',
                2: 'Grechen Fuemen',
                3: 'Meddon',
                4: 'Princess Sofia',
                5: 'Schoolbell',
                6: 'Splash',
                7: 'Vtks Garota Bonita',
                8: 'Vtks legal',
                9: 'Vtks Relaxing Blaze',
                10: 'Dekko',
                11: 'WindSong',
                }

for key, font in font_dict.items():
    ''' testing all fonts with all characters'''
    #distort_text(['', "['+', ',', '-', '.', '/', '0', '1', '2', '3', '4', '7', 'A', 'B', 'C', 'D', 'E', 'F', 'G', 'H', 'I', 'J', 'K', 'L', 'M', 'N', 'O', 'P', 'Q', 'R', 'S', 'T', 'U', 'V', 'W', 'X', 'Y', 'Z', 'a', 'b', 'c', 'd', 'e', 'f', 'g', 'h', 'i', 'j', 'k', 'l', 'm', 'n', 'o', 'p', 'q', 'r', 's', 't', 'u', 'v', 'w', 'x', 'y', 'z', 'É', 'Ñ', 'á', 'â', 'ã', 'ç', 'è', 'é', 'ê', 'í', 'ñ', 'ó', 'ô', 'õ', 'ö', 'ú', 'ü']"], 0, 0, key - 1, font)
    
    if key in chosen_fonts.keys():
        distort_text(['', "Font_Test"], 0, 0, key - 1, font)
        #print(key, font)