# Picslate - 

Picslate is a picture translator based on tesseract and return a PIL image with the newly translated text



## Installation

Using [pip](https://pip.pypa.io/en/stable/).

```bash
pip install picslate
```
or
```bash
git clone ...
pip install picslate/
```
Addionally, you should install a translator and tesseract

## Usage


```python
from picslate import convert

img=convert(image,from_lang,to_lang)
img.show()


```

```bash
picslate image from_lang to_lang
```

## Documentation / Explanation

You can check more information about my projects on my [website](https://thomasportier.com/)

You can check the documentation on [doc](https://doc.thomasportier.com/picslate/)

## License
[MIT](https://github.com/ts0mas/wordbay/blob/master/LICENSE.md)
