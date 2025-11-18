from pathlib import Path
import uuid
from PIL import Image
import dspy
from models import ImageInput
from urllib.request import urlopen
from io import BytesIO

OUTPUT_DIR = Path("tmp_crops")
OUTPUT_DIR.mkdir(exist_ok=True)

def crop_and_zoom(
    image_path: str,
    x: int,
    y: int,
    width: int,
    height: int,
    zoom: float = 1.5,
) -> ImageInput:
    """Crop a rectangle from an image and optionally zoom it.
    Args:
        image_path: The path to the image to crop (can be a file path or URL).
        x: The x coordinate of the top-left corner of the rectangle.
        y: The y coordinate of the top-left corner of the rectangle.
        width: The width of the rectangle.
        height: The height of the rectangle.
        zoom: The zoom factor.

    Returns:
        The cropped image.
    """
    img = _get_Image(image_path)
    box = (x, y, x + width, y + height)
    cropped = img.crop(box)

    if zoom != 1.0:
        new_size = (int(cropped.width * zoom), int(cropped.height * zoom))
        cropped = cropped.resize(new_size, Image.LANCZOS)

    out_path = OUTPUT_DIR / f"{uuid.uuid4().hex}.png"
    cropped.save(out_path)
    return get_ImageInput(out_path)

def _get_Image(image_path: str) -> Image:
    """ Get a PIL image from a path.
    Args:
        image_path: The path to the image (can be a file path or URL).

    Returns:
        The PIL image.
    """
    path_str = str(image_path)
    if path_str.startswith(('http://', 'https://')):
        with urlopen(path_str) as response:
            img = Image.open(BytesIO(response.read()))
    else:
        img = Image.open(path_str)
    return img

def get_ImageInput(image_path: str) -> ImageInput:
    """ Get an ImageInput object from a path.
    Args:
        image_path: The path to the image (can be a file path or URL).

    Returns:
        The ImageInput object.
    """
    img = _get_Image(str(image_path))
    width, height = img.size
    return ImageInput(image=dspy.Image(img), image_path=str(image_path), width=width, height=height)
