import cv2
from PIL import ImageFont, ImageDraw, Image  
import numpy as np 

#inputs
name = 'John Dome akegjbwgek'     #Gotta take name from database, using given email
track = 'Deep Learning'               #Input from webpage

# Three other files must be in the directory:
# 1 - the image of the certificate template, 'mentor_template.png'
# 2 - Font 1 file NotoSans-CondensedSemiBold.ttf
# 3 - Font 2 file NotoSans-Italic.ttf

def generate_cert(name, track):

    #Dealing with 3 names, lengths
    if len(name) > 16:
        name = name.split(' ')
        if len(name) > 2:
            if len(name[0]+name[1]) < len(name[1]+name[2]):
                name = [name[0]+' '+name[1]] + name[2:]
            else:
                name = name[0:1] + [name[1]+' '+name[2]]

    #lines for the cert
    line_1 = 'for outstanding contributions as the ' + '\'' + track + '\'' + ' mentor'
    line_2 = 'in the MDX Computing Society Study Groups. Your dedication, expertise,'
    line_3 = 'and unwavering support have significantly impacted the success'
    line_4 = 'of the participants. We express our heartfelt gratitude for your efforts.'

    #now the image
    template = cv2.imread('mentor_template.png')           #Loading the img
    template = cv2.cvtColor(template,cv2.COLOR_BGR2RGB)  #OpenCV uses BGR so converting to RGB
    template = Image.fromarray(template)                 #Sending to PIL
    draw = ImageDraw.Draw(template)

    #Loading fonts
    font1 = ImageFont.truetype('NotoSans-CondensedSemiBold.ttf', 250)  
    font2 = ImageFont.truetype('NotoSans-Italic.ttf', 100)  

    #Putting text into img
    h = 500
    w = 1275
    if type(name) == list:
        draw.text((h, w), name[0].upper(), font=font1, fill='#000000')  
        draw.text((h, w+325), name[1].upper(), font=font1, fill='#000000')  
    else:
        draw.text((h, w+200), name.upper(), font=font1, fill='#000000') 
    draw.text((h, w+300+500), line_1, font=font2, fill='#000000')  
    draw.text((h, w+300+500+175), line_2, font=font2, fill='#000000') 
    draw.text((h, w+300+500+175+175), line_3, font=font2, fill='#000000')  
    draw.text((h, w+300+500+175+175+175), line_4, font=font2, fill='#000000')  

    return cv2.cvtColor(np.array(template), cv2.COLOR_RGB2BGR)   #Converting back to RGB

#Calling & saving
template = generate_cert(name, track)
cv2.imwrite('new/cert_m.png', template)