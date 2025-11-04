#!/usr/bin/env python3
"""
Simple PNG optimizer using PIL
Reduces file size by optimizing compression
"""

import os
import sys
from PIL import Image

def optimize_png(filepath):
    """Optimize a single PNG file."""
    try:
        with Image.open(filepath) as img:
            original_size = os.path.getsize(filepath)
            
            # Re-save with optimization
            img.save(filepath, 'PNG', optimize=True, compress_level=9)
            
            new_size = os.path.getsize(filepath)
            savings = original_size - new_size
            savings_pct = (savings / original_size * 100) if original_size > 0 else 0
            
            print(f"✓ {os.path.basename(filepath)}: "
                  f"{original_size//1024}KB → {new_size//1024}KB "
                  f"({savings_pct:.1f}% reduction)")
    except Exception as e:
        print(f"✗ {filepath}: {e}")

def main():
    """Optimize all PNGs in art directory."""
    art_dir = os.path.join(os.path.dirname(__file__), '../art')
    
    png_files = []
    for root, dirs, files in os.walk(art_dir):
        for file in files:
            if file.endswith('.png'):
                png_files.append(os.path.join(root, file))
    
    print(f"Found {len(png_files)} PNG files to optimize...\n")
    
    for png_file in png_files:
        optimize_png(png_file)
    
    print(f"\n✓ Optimization complete!")

if __name__ == '__main__':
    main()
