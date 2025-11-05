## Pixel Rose Overlay

This project lets you add pixel overlays to a sprite by applying coordinates stored in a text file. The helper script `add_pixels.py` reads those instructions and writes a new image with the modified pixels.

### Requirements
- Python 3.8 or newer
- [Pillow](https://pillow.readthedocs.io/) (`pip install pillow`)

### Usage
```bash
python add_pixels.py <base_image> <pixels.txt> <output_image>
```
Provide your own base image and pixel instruction file. The script loads the base sprite, applies every pixel described in the text file, and saves the result as the output image you specify.

### Pixel Instruction Format
Each non-empty, non-comment line in `rose_pixels.txt` must follow:

```
x,y,R,G,B,A
```

- `x`, `y`: zero-based coordinates inside the base image.
- `R`, `G`, `B`, `A`: integer channel values from 0 to 255.

Lines starting with `#` or blank lines are ignored. The file is UTF-8 encoded so comment text can include non-ASCII characters.

### Provided Files
- `add_pixels.py`: Python helper that applies the overlay.
