import argparse
import os
from PIL import Image, ImageDraw

def main():
    parser = argparse.ArgumentParser(description="Generate dot grid paper.")
    parser.add_argument("--width", type=float, default=8.5, help="Width of the paper in inches")
    parser.add_argument("--height", type=float, default=11, help="Height of the paper in inches")
    parser.add_argument("--spacing", type=float, default=1/8, help="Spacing between dots in inches")
    parser.add_argument("--dpi", type=int, default=300, help="Dots per inch (DPI)")
    parser.add_argument("--output", type=str, default="dot_paper.pdf", help="Output file name")

    args = parser.parse_args()

    # Ensure the output directory exists
    output_dir = "./dot_paper/output"
    os.makedirs(output_dir, exist_ok=True)
    output_path = os.path.join(output_dir, args.output)

    # Constants for the image size and dot spacing
    INCH_TO_PIXELS = args.dpi
    WIDTH_INCHES = args.width
    HEIGHT_INCHES = args.height
    DOT_SPACING_INCHES = args.spacing

    # Calculate dimensions in pixels
    width_pixels = int(WIDTH_INCHES * INCH_TO_PIXELS)
    height_pixels = int(HEIGHT_INCHES * INCH_TO_PIXELS)
    dot_spacing_pixels = int(DOT_SPACING_INCHES * INCH_TO_PIXELS)

    # Create a new white image
    image = Image.new("RGB", (width_pixels, height_pixels), "white")
    draw = ImageDraw.Draw(image)

    # Draw dots
    for x in range(0, width_pixels, dot_spacing_pixels):
        for y in range(0, height_pixels, dot_spacing_pixels):
            draw.ellipse((x-1, y-1, x+1, y+1), fill="black")

    # Save the image as a PDF
    image.save(output_path, "PDF")

if __name__ == "__main__":
    main()
