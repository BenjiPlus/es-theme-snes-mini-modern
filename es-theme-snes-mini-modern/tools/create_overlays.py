#!/usr/bin/env python3
"""
Create visual overlay assets for SNES Mini Modern theme
Generates: shadow_overlay.png, light_glow.png, bezel_frame.png
"""

from PIL import Image, ImageDraw, ImageFilter
import os

OUTPUT_DIR = '../art/ui/'

def create_shadow_overlay(size=(1000, 1000)):
    """Create radial shadow overlay."""
    img = Image.new('RGBA', size, (0, 0, 0, 0))
    draw = ImageDraw.Draw(img)
    
    center_x, center_y = size[0] // 2, size[1] // 2
    max_radius = min(size) // 2
    
    # Draw concentric circles with decreasing opacity (radial gradient)
    steps = 50
    for i in range(steps):
        radius = int(max_radius * (steps - i) / steps)
        alpha = int(100 * i / steps)  # Fade from center to edges
        draw.ellipse(
            [(center_x - radius, center_y - radius),
             (center_x + radius, center_y + radius)],
            fill=(0, 0, 0, alpha)
        )
    
    # Blur for smooth gradient
    img = img.filter(ImageFilter.GaussianBlur(radius=30))
    
    return img


def create_light_glow(size=(1000, 1000)):
    """Create light glow effect for selection highlight."""
    img = Image.new('RGBA', size, (0, 0, 0, 0))
    draw = ImageDraw.Draw(img)
    
    center_x, center_y = size[0] // 2, size[1] // 2
    max_radius = min(size) // 2
    
    # Draw white radial glow
    steps = 40
    for i in range(steps):
        radius = int(max_radius * (steps - i) / steps)
        alpha = int(150 * (steps - i) / steps)  # Bright center, fade out
        draw.ellipse(
            [(center_x - radius, center_y - radius),
             (center_x + radius, center_y + radius)],
            fill=(255, 255, 255, alpha)
        )
    
    # Blur for soft glow
    img = img.filter(ImageFilter.GaussianBlur(radius=50))
    
    return img


def create_bezel_frame(size=(800, 600), border_width=20):
    """Create decorative bezel frame for video/image preview."""
    img = Image.new('RGBA', size, (0, 0, 0, 0))
    draw = ImageDraw.Draw(img)
    
    # Outer border (dark gray with slight transparency)
    outer_color = (40, 40, 50, 200)
    draw.rectangle([(0, 0), (size[0]-1, size[1]-1)], 
                   outline=outer_color, width=border_width)
    
    # Inner highlight (lighter gray)
    inner_offset = border_width - 4
    inner_color = (120, 120, 140, 180)
    draw.rectangle([(inner_offset, inner_offset), 
                   (size[0]-inner_offset-1, size[1]-inner_offset-1)],
                   outline=inner_color, width=4)
    
    # Corner accents (SNES-style red accent)
    accent_color = (227, 30, 36, 220)  # SNES red
    corner_size = 15
    
    # Top-left corner
    draw.line([(0, 0), (corner_size, 0)], fill=accent_color, width=3)
    draw.line([(0, 0), (0, corner_size)], fill=accent_color, width=3)
    
    # Top-right corner
    draw.line([(size[0]-corner_size-1, 0), (size[0]-1, 0)], fill=accent_color, width=3)
    draw.line([(size[0]-1, 0), (size[0]-1, corner_size)], fill=accent_color, width=3)
    
    # Bottom-left corner
    draw.line([(0, size[1]-1), (corner_size, size[1]-1)], fill=accent_color, width=3)
    draw.line([(0, size[1]-corner_size-1), (0, size[1]-1)], fill=accent_color, width=3)
    
    # Bottom-right corner
    draw.line([(size[0]-corner_size-1, size[1]-1), (size[0]-1, size[1]-1)], fill=accent_color, width=3)
    draw.line([(size[0]-1, size[1]-corner_size-1), (size[0]-1, size[1]-1)], fill=accent_color, width=3)
    
    return img


def main():
    """Generate all overlay assets."""
    output_path = os.path.join(os.path.dirname(__file__), OUTPUT_DIR)
    os.makedirs(output_path, exist_ok=True)
    
    print("Creating shadow overlay...")
    shadow = create_shadow_overlay((1200, 1200))
    shadow.save(os.path.join(output_path, 'shadow_overlay.png'), 'PNG')
    
    print("Creating light glow...")
    glow = create_light_glow((1200, 1200))
    glow.save(os.path.join(output_path, 'light_glow.png'), 'PNG')
    
    print("Creating bezel frame...")
    bezel = create_bezel_frame((1000, 800), border_width=25)
    bezel.save(os.path.join(output_path, 'bezel_frame.png'), 'PNG')
    
    print(f"✓ All overlays created in {output_path}")
    print("  - shadow_overlay.png")
    print("  - light_glow.png")
    print("  - bezel_frame.png")


if __name__ == '__main__':
    main()
