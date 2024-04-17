from django.shortcuts import render
from django.http import HttpResponse
from .models import Template
from .forms import TemplateForm

from django.db import models
from PIL import Image, ImageDraw, ImageFont
from datetime import datetime
import os




def get_file_choices():
    file_choices = []
    folder_path = './img/'
    for file_name in os.listdir(folder_path):
        if os.path.isfile(os.path.join(folder_path, file_name)):
            file_choices.append(file_name)
    return file_choices

def get_font_choices():
    file_choices = []
    folder_path = './fonts/'
    for file_name in os.listdir(folder_path):
        if os.path.isfile(os.path.join(folder_path, file_name)):
            file_choices.append(file_name)
    return file_choices

def generate_image(templates, font, data):
        # data = {
        #     "full_name": "Dilshodbek Donaboyev",
        #     "given_date": ['24','15', 'aprel'],
        #     "reference_number": 50,
        #     "start_date": ['24','02', 'aprel'],
        #     "end_date": ['24', '15', 'aprel']
        # }
        
        image = Image.open(f'img/{templates}')
        d = ImageDraw.Draw(image)
        font = ImageFont.truetype(f'fonts/{font}', 44)
        if templates == 'img-1.jpg':
            coordinate = {
                "full_name": (295,410),
                "given_date_top": [(49,310), (137,315), (207, 315)],
                "reference_number_top": (709, 322),
                "start_date": [(464,734),(555,735),(627,735)],
                "end_date": [(464,761),(555,761),(627,765)],
                "given_date_bottom": [ (459,993), (564,995), (643,996)],
                "reference_number_bottom":  (493,1018),
            }
            for key, val in data.items():
                text = val
                if key == 'given_date':
                    for i in ("top", "bottom"):                    
                        text_pos = coordinate[f"{key}_{i}"]
                        color = (36,27,113)
                        for kr in range(len(text)):
                            d.text((text_pos[kr][0]+1,text_pos[kr][1]), text=text[kr], fill=color, font=font)
                            d.text((text_pos[kr][0],text_pos[kr][1]+1), text=text[kr], fill=color, font=font)
                        
                elif key == 'reference_number':
                    for i in ("top", "bottom"):                    
                        text_pos = coordinate[f"{key}_{i}"]
                        color = (36,27,113)
                        p_1 = (text_pos[0]+1,text_pos[1])
                        p_2 = (text_pos[0],text_pos[1]+1)
                        
                        d.text(p_1, text=str(text), fill=color, font=font)
                        d.text(p_2, text=str(text), fill=color, font=font)
                elif key == 'start_date' or key == 'end_date':
                    text_pos = coordinate[key]
                    color = (36,27,113)
                    for kr in range(len(text)):
                            d.text((text_pos[kr][0]+1,text_pos[kr][1]), text=text[kr], fill=color, font=font)
                            d.text((text_pos[kr][0],text_pos[kr][1]+1), text=text[kr], fill=color, font=font)
                else:
                    text_pos = coordinate[key]
                    color = (36,27,113)
                    d.text((text_pos[0]+1,text_pos[1]), text=text, fill=color, font=font)
                    d.text((text_pos[0],text_pos[1]+1), text=text, fill=color, font=font)

            image.save(f"./images/tayyor.png")
    
    

def template_test(request):
    file_names = get_file_choices()
    font_names = get_font_choices()

    if request.method == 'POST':
        data = request.POST
        d = {
            'full_name': data['full_name'],
            "given_date": data['given_date'].split(','),
            "reference_number": data['reference_number'],
            "start_date": data['start_date'].split(','),
            "end_date": data['end_date'].split(",")
        }

        font = data['font']
        template = data['template']

        generate_image(template,font,d)    
    

    return render(request, 'index.html', {
        "file_names": file_names,
        "font_names": font_names
    })
