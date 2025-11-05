from PIL import Image
import sys

def add_pixels_to_image(image_path, pixels_txt, output_path):
    # Open the base image
    img = Image.open(image_path).convert("RGBA")
    pixels = img.load()

    # Read pixel instructions
    with open(pixels_txt, "r", encoding="utf-8") as f:
        for line in f:
            if line.strip() == "" or line.startswith("#"):
                continue
            try:
                x, y, r, g, b, a = map(int, line.strip().split(","))
                if 0 <= x < img.width and 0 <= y < img.height:
                    pixels[x, y] = (r, g, b, a)
            except ValueError:
                print(f"Skipping invalid line: {line.strip()}")

    # Save the new image
    img.save(output_path, "PNG")
    print(f"Saved edited image as {output_path}")

if __name__ == "__main__":
    if len(sys.argv) != 4:
        print("Usage: python add_pixels.py <image.png> <pixels.txt> <output.png>")
    else:
        add_pixels_to_image(sys.argv[1], sys.argv[2], sys.argv[3])
