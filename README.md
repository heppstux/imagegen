# Django Web Image Placeholder (WIP)

Inspired by [placehold.it](http://placehold.it/) WIP (pronounced "work in progress") is a simple Django app delivering placeholder images for Web designers and developers.

This application has been developed in a "30 Minutes Situation", where placehold.it went down and all our design-prototypes stopped working properly. By "30 Minutes" I literally mean "1800s" so please DO NOT EXPECT ANYTHING from this tool. It works for our purpose but certainly contains bugs, security issues and performance is laughable. **Thus, feel free to fork, fix and commit back – I love PRs!**

---

## Installation

Please refer to the official Django documentation on how to deploy Django applications.

Note that WIP requires a font named "Courier New.ttf" and "FontAwesome.otf" in an accessible path.

You should succeed with a little background knowledge by following these steps:

Install Django on the Development System.

1. create a Virtual Environment ```virtual-env YOURENVNAME``` and...
2. ...activate it ```source YOURENVNAME/bin/active```.
3. install required packages into the new venv (pip recommended) ```pip install Django Pillow```
4. create a Django Project ```django-admin startproject YOURNAME```
5. clone the repository into the new Django project ```git clone URL-TO-THIS-REPO```
6. modify _settings.py_ by add ```imagegen``` to your ```INSTALLED_APPS```
7. add ```url(r'^', include('imagegen.urls')),``` to your _urls.py_
8. start the development-server ```./manage.py runserver``` _(There are no models for this app, thus no migrations needed)_


Done: App can be reached at [localhost:8000](http://localhost:8000).

If you want to run this on a public server READ DJANGO'S DOCUMENTATION! Also, I highly recommend any sort of caching mechanism if you're going to run this and expect some load. But anyways READ THE DJANGO-DOCS ;-)

---

## Usage

### Image Size

http://example.com/WIDTH

http://example.com/WIDTHxHEIGHT

Note: `HEIGHT` is always optional and defaults to `WIDTH`, both are limited to 4096px.

#### Example
_http://example.com/300_ will give you a 300x300px sized PNG

_http://example.com/800x600_ will give you a 800x600px sized PNG

---

### Colors

#### Text Color:
http://example.com/WIDTHxHEIGHT/HEXCOL

`HEXCOL` can be any 3- or 6-digit hex color number formatted in RGB or RRGGBB.

#### Background Color:
http://example.com/WIDTHxHEIGHT/CCC/HEXCOL

`HEXCOL` can be any 3- or 6-digit hex color number formatted in RGB or RRGGBB.

---

### HighRes Images aka. Retina Support

Append `@2x` or `@3x` to the previous mentioned URLS. This will double or tripple the size of the returned image. 

#### Examples

_http://example.com/800@2x_

_http://example.com/400x300@3x_

_http://example.com/200x100/EEE/000000@2x_

---

### File Format

Append `.png`, `.jpg` or `.jpeg` to the previous mentioned URLS. Defaults to `.png`.

#### Example

_http://example.com/800x600.jpeg_

_http://example.com/800x600/FF00FF.jpeg_

_http://example.com/800x600/FF00FF@2x.jpg_

---

### Customize Text

http://example.com/WIDTHxHEIGHT?text=Plus+will+be+interpreted+as+white+space

Make sure `?text` is attached behind any File Format specifying URL extension e.g. _http://example.com/800x600/FF00FF.jpeg?text=this+is+correct_

---

### Icons

http://example.com/WIDTHxHEIGHT?icon=anyFontAwesomeIconName

Most icons from Font Awesome 4.3 are included, see the full [list of supported icons](https://github.com/heppstux/imagegen/blob/master/fontawesome2.py#L22-L612).

Attention: If `icon` is present no text will be rendered.

---

### URL Scheme Overview

    ^(((?P<width>\d+)(x(?P<height>\d+))?(/(?P<color>[0-9A-Fa-f]{6}|[0-9A-Fa-f]{3}))?)(/(?P<background>[0-9A-Fa-f]{6}|[0-9A-Fa-f]{3}))?)(@(?P<retinaSupport>[1-3])x)?(?P<fileFormat>(\.png|\.jpg|\.jpeg)?)$

![Regular expression visualization](https://www.debuggex.com/i/0dxmMKY2KsKC9FCb.png)

[URL Scheme (thanks to debuggex.com)](https://www.debuggex.com/r/0dxmMKY2KsKC9FCb.png)

---

# License

	(C) 2015 by Stephan S. Hepper
	
	WIP is free software: you can redistribute it and/or modify
	it under the terms of the GNU General Public License as published by
	the Free Software Foundation, either version 3 of the License, or
	(at your option) any later version.
	 
	WIP is distributed in the hope that it will be useful,
	but WITHOUT ANY WARRANTY; without even the implied warranty of
	MERCHANTABILITY or FITNESS FOR A PARTICULAR PURPOSE.  See the
	GNU General Public License for more details.
	 
	You should have received a copy of the GNU General Public License
	along with WIP. If not, see <http://www.gnu.org/licenses/>.
