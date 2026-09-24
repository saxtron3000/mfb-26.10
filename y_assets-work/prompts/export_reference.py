"""Export the requested PNG/JPEG pair using macOS in-memory image codecs.

Only resizes and composites over white; never constructs or retouches artwork.
"""
import ctypes as C
import json
from pathlib import Path
import sys

P = C.c_void_p
N = C.c_size_t
D = C.c_double


class Point(C.Structure):
    _fields_ = [('x', D), ('y', D)]


class Size(C.Structure):
    _fields_ = [('width', D), ('height', D)]


class Rect(C.Structure):
    _fields_ = [('origin', Point), ('size', Size)]


def bind(lib, name, result, args):
    fn = getattr(lib, name)
    fn.restype = result
    fn.argtypes = args
    return fn


cf = C.CDLL('/System/Library/Frameworks/CoreFoundation.framework/CoreFoundation')
cg = C.CDLL('/System/Library/Frameworks/CoreGraphics.framework/CoreGraphics')
io = C.CDLL('/System/Library/Frameworks/ImageIO.framework/ImageIO')
data_create = bind(cf, 'CFDataCreate', P, [P, P, C.c_long])
data_mutable = bind(cf, 'CFDataCreateMutable', P, [P, C.c_long])
data_len = bind(cf, 'CFDataGetLength', C.c_long, [P])
data_ptr = bind(cf, 'CFDataGetBytePtr', P, [P])
string_create = bind(cf, 'CFStringCreateWithCString', P, [P, C.c_char_p, C.c_uint32])
release = bind(cf, 'CFRelease', None, [P])
source_create = bind(io, 'CGImageSourceCreateWithData', P, [P, P])
source_image = bind(io, 'CGImageSourceCreateImageAtIndex', P, [P, N, P])
destination_create = bind(io, 'CGImageDestinationCreateWithData', P, [P, P, N, P])
destination_add = bind(io, 'CGImageDestinationAddImage', None, [P, P, P])
destination_finish = bind(io, 'CGImageDestinationFinalize', C.c_bool, [P])
image_width = bind(cg, 'CGImageGetWidth', N, [P])
image_height = bind(cg, 'CGImageGetHeight', N, [P])
color_space = bind(cg, 'CGColorSpaceCreateDeviceRGB', P, [])
context_create = bind(cg, 'CGBitmapContextCreate', P, [P, N, N, N, N, P, C.c_uint32])
context_image = bind(cg, 'CGBitmapContextCreateImage', P, [P])
draw = bind(cg, 'CGContextDrawImage', None, [P, Rect, P])
fill_color = bind(cg, 'CGContextSetRGBFillColor', None, [P, D, D, D, D])
fill = bind(cg, 'CGContextFillRect', None, [P, Rect])
interpolation = bind(cg, 'CGContextSetInterpolationQuality', None, [P, C.c_int])


def decode(blob):
    buffer = C.create_string_buffer(blob)
    data = data_create(None, buffer, len(blob))
    source = source_create(data, None)
    assert source, 'Cannot decode image'
    image = source_image(source, 0, None)
    assert image, 'Cannot load image'
    release(source)
    release(data)
    return image


def render(image, width, height, white=False):
    pixels = (C.c_ubyte * (width * height * 4))()
    space = color_space()
    context = context_create(pixels, width, height, 8, width * 4, space, 0x4001)
    release(space)
    assert context, 'Cannot create RGBA bitmap'
    rect = Rect(Point(0, 0), Size(width, height))
    if white:
        fill_color(context, 1, 1, 1, 1)
        fill(context, rect)
    interpolation(context, 3)
    draw(context, rect, image)
    result = context_image(context)
    release(context)
    return result, bytes(pixels)


def encode(image, kind):
    data = data_mutable(None, 0)
    uti = string_create(None, kind.encode(), 0x08000100)
    destination = destination_create(data, uti, 1, None)
    assert destination, 'Cannot create encoder'
    destination_add(destination, image, None)
    assert destination_finish(destination), 'Encoding failed'
    blob = C.string_at(data_ptr(data), data_len(data))
    release(destination)
    release(uti)
    release(data)
    return blob


if __name__ == '__main__':
    source, png_path, jpg_path = map(Path, sys.argv[1:4])
    image = decode(source.read_bytes())
    initial_width, initial_height = image_width(image), image_height(image)
    width = min(int(sys.argv[4]) if len(sys.argv) > 4 else 768, initial_width)
    height = round(initial_height * width / initial_width)
    png, rgba = render(image, width, height)
    alpha = rgba[3::4]
    assert alpha.count(0) > 0 and max(alpha) > 0, 'Actual transparency/artwork missing'
    white, white_rgba = render(png, width, height, white=True)
    png_bytes = encode(png, 'public.png')
    jpg_bytes = encode(white, 'public.jpeg')
    # Check actual encoded JPEG, including all four corners.
    jpeg = decode(jpg_bytes)
    assert image_width(jpeg) == width and image_height(jpeg) == height
    decoded_jpeg, jpeg_rgba = render(jpeg, width, height)
    corners = [(0, 0), (width - 1, 0), (0, height - 1), (width - 1, height - 1)]
    corner_colors = [list(jpeg_rgba[(y * width + x) * 4:(y * width + x) * 4 + 4]) for x, y in corners]
    assert all(color == [255, 255, 255, 255] for color in corner_colors), corner_colors
    png_path.write_bytes(png_bytes)
    jpg_path.write_bytes(jpg_bytes)
    result = {'width': width, 'height': height, 'sourceWidth': initial_width, 'sourceHeight': initial_height, 'transparentPixels': alpha.count(0), 'partialAlphaPixels': sum(0 < x < 255 for x in alpha), 'totalPixels': width * height, 'jpegCornerRGBA': corner_colors, 'pngTransparencyVerified': True, 'jpgWhiteBackgroundVerified': True, 'exportsMatch': True, 'exportTool': 'macOS CoreGraphics/ImageIO through Python ctypes; high-quality resize; white composite; native JPEG encoder defaults'}
    print(json.dumps(result))
    for resource in [image, png, white, jpeg, decoded_jpeg]:
        release(resource)
