#
# (C) 2015 by Stephan S. Hepper
#
# WIP is free software: you can redistribute it and/or modify
# it under the terms of the GNU General Public License as published by
# the Free Software Foundation, either version 3 of the License, or
# (at your option) any later version.
#
# WIP is distributed in the hope that it will be useful,
# but WITHOUT ANY WARRANTY; without even the implied warranty of
# MERCHANTABILITY or FITNESS FOR A PARTICULAR PURPOSE.  See the
# GNU General Public License for more details.
#
# You should have received a copy of the GNU General Public License
# along with WIP. If not, see <http://www.gnu.org/licenses/>.
#


from django.http import HttpResponse
from PIL import Image, ImageDraw, ImageFont

# Create your views here.
def draw_text_center(im, draw, text, font, **kwargs):
    text_size = draw.textsize(text, font)

    return draw.text(
        ((im.size[0] - text_size[0]) / 2, (im.size[1] - text_size[1]) / 2.3),
        text, font=font, **kwargs)



def pngImage(request, width, height, fileFormat, retinaSupport, color, background):

    retinaFaktor = int(retinaSupport or 1)
    height = height or width
    width = min(int(width) * retinaFaktor, 4096)
    height = min(int(height) * retinaFaktor, 4096)

    fileFormat = fileFormat or '.png'
    color = color or '979797'
    background = background or "CCC"

    fileFormat = fileFormat[1:]
    if fileFormat == "jpg":
        fileFormat = "jpeg"


    img = Image.new("RGB", (width, height), '#'+str(background))
    draw = ImageDraw.Draw(img)


    if request.GET.get('icon'):
        iconCode = request.GET.get('icon')
        from fontawesome2 import faIcons
        try:
            faIcon = faIcons.get(iconCode)
            faFont = ImageFont.truetype("FontAwesome.otf", int(min(height, width)/1.5))
            draw_text_center(img, draw, faIcon, font=faFont, fill='#'+str(color))
        except:
            pass

    elif width > 28:
        fontName = "Courier New.ttf"
        fontSize = 50 * retinaFaktor
        fontImageRatio = 0.8

        text = request.GET.get('text') or "%dx%d%s"%(width/retinaFaktor, height/retinaFaktor,
                                                    ("@%dx"%(retinaFaktor) if retinaFaktor > 1 else ""))

        font = ImageFont.truetype(fontName, fontSize)

        # find best fitting fontsize
        while (fontSize > 1) and (draw.textsize(text, font)[0] > (fontImageRatio * img.size[0])):
            fontSize -= 1
            font = ImageFont.truetype(fontName, fontSize)

        draw_text_center(img, draw, text, font=font, fill='#'+str(color))


    response = HttpResponse(content_type="image/%s"%(fileFormat))

    img.save(response, fileFormat)

    return response