import os
from pathlib import Path
from PIL import Image, ImageChops

EMPTY_IMG = Image.open("./empty_64x64.png")


def remove_second_skin_layer(skin_img: Image.Image) -> Image.Image:
    skin_converted = skin_img.convert('RGBA')
    MASK_IMG = Image.open("./skintemplate_masked_alpha.png")
    MASK_IMG_converted = MASK_IMG.convert('RGBA')
    masked_img = ImageChops.multiply(skin_converted, MASK_IMG_converted)
    return masked_img

def clean_skin(skin: Image.Image) -> Image.Image:
    ''' Takes a 64x64 skin and cleans it (removes second layer). '''
    if skin.size == (64, 64):
        cleaned_skin = remove_second_skin_layer(skin)
        save_path =f"cleaned_skins/{skin}"
        cleaned_skin.save(save_path)
        return cleaned_skin
    else:
        print("Wrong size, skipping.")