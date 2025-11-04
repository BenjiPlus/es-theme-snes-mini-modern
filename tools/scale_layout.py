#!/usr/bin/env python3
"""
EmulationStation Theme Layout Scaler
Proportionally scales layout XML from one resolution to another

Usage:
    python3 scale_layout.py <input_xml> <target_width> <target_height> [options]
    
Example:
    python3 scale_layout.py layouts/1920x1080.xml 1366 768 > layouts/1366x768_scale.xml
    python3 scale_layout.py layouts/1920x1080.xml 1600 900 --dry-run
    
Options:
    --dry-run              Show changes without generating output
    --source-width WIDTH   Source width (default: 1920)
    --source-height HEIGHT Source height (default: 1080)
    --tags TAG1,TAG2       Additional tags to scale (comma-separated)
    --precision DIGITS     Decimal precision (default: 6)
"""

import sys
import re
import xml.etree.ElementTree as ET
from typing import List, Tuple

# Default source resolution
DEFAULT_SOURCE_WIDTH = 1920
DEFAULT_SOURCE_HEIGHT = 1080

# Tags that contain scalable numeric values
SCALABLE_TAGS = {
    'pos', 'size', 'fontSize', 'maxSize', 'minSize', 
    'padding', 'margin', 'logoSize', 'selectorHeight',
    'selectorOffsetY', 'horizontalMargin', 'lineSpacing',
    'maxLogoCount', 'cornerSize'
}


def parse_numeric_value(value: str) -> Tuple[List[float], str]:
    """
    Extract numeric values from a string.
    Returns tuple of (numbers, separator)
    """
    # Match floating point or integer numbers
    numbers = re.findall(r'-?\d+\.?\d*', value)
    # Detect separator (space is most common)
    separator = ' ' if ' ' in value else ''
    return [float(n) for n in numbers], separator


def scale_value(value: str, sx: float, sy: float, tag_name: str) -> str:
    """
    Scale a numeric value based on tag type.
    Some tags scale X only, some Y only, some both.
    """
    numbers, separator = parse_numeric_value(value)
    
    if not numbers:
        return value
    
    # Single value tags that scale with Y (height-based)
    if tag_name in ['fontSize', 'selectorHeight', 'selectorOffsetY', 
                     'horizontalMargin', 'lineSpacing']:
        if len(numbers) == 1:
            scaled = [numbers[0] * sy]
        else:
            scaled = numbers  # Don't scale if unexpected format
    
    # Tags with X Y pairs
    elif tag_name in ['pos', 'size', 'maxSize', 'minSize', 'logoSize', 
                       'padding', 'margin', 'cornerSize']:
        if len(numbers) == 2:
            scaled = [numbers[0] * sx, numbers[1] * sy]
        elif len(numbers) == 1:
            # Single value - scale both
            scaled = [numbers[0] * sx]
        else:
            scaled = numbers
    
    # Count-based tags (don't scale)
    elif tag_name in ['maxLogoCount']:
        return value
    
    else:
        # Default: scale pairs of X Y
        scaled = []
        for i, num in enumerate(numbers):
            if i % 2 == 0:
                scaled.append(num * sx)
            else:
                scaled.append(num * sy)
    
    # Format with appropriate precision
    return separator.join([f"{n:.6f}".rstrip('0').rstrip('.') for n in scaled])


def scale_xml_element(element: ET.Element, sx: float, sy: float, 
                      additional_tags: set, precision: int) -> None:
    """
    Recursively scale all numeric values in XML element and children.
    """
    # Scale text content if this is a scalable tag
    if element.tag in SCALABLE_TAGS or element.tag in additional_tags:
        if element.text and element.text.strip():
            original = element.text.strip()
            scaled = scale_value(original, sx, sy, element.tag)
            if scaled != original:
                element.text = scaled
    
    # Scale attributes if any contain numeric values
    for attr_name, attr_value in element.attrib.items():
        if any(char.isdigit() for char in attr_value):
            scaled = scale_value(attr_value, sx, sy, attr_name)
            if scaled != attr_value:
                element.attrib[attr_name] = scaled
    
    # Recurse into children
    for child in element:
        scale_xml_element(child, sx, sy, additional_tags, precision)


def scale_layout(input_file: str, target_width: int, target_height: int,
                 source_width: int = DEFAULT_SOURCE_WIDTH,
                 source_height: int = DEFAULT_SOURCE_HEIGHT,
                 additional_tags: set = None,
                 precision: int = 6,
                 dry_run: bool = False) -> str:
    """
    Scale an EmulationStation layout XML file.
    
    Args:
        input_file: Path to source XML
        target_width: Target resolution width
        target_height: Target resolution height
        source_width: Source resolution width (default 1920)
        source_height: Source resolution height (default 1080)
        additional_tags: Extra tags to scale
        precision: Decimal precision for output
        dry_run: If True, only show what would change
    
    Returns:
        Scaled XML as string
    """
    # Calculate scaling factors
    sx = target_width / source_width
    sy = target_height / source_height
    
    if dry_run:
        print(f"Scaling factors: X={sx:.6f}, Y={sy:.6f}", file=sys.stderr)
        print(f"Source: {source_width}x{source_height}", file=sys.stderr)
        print(f"Target: {target_width}x{target_height}", file=sys.stderr)
    
    # Parse XML
    tree = ET.parse(input_file)
    root = tree.getroot()
    
    # Add custom tags if provided
    tags_to_scale = SCALABLE_TAGS | (additional_tags or set())
    
    # Scale all elements
    scale_xml_element(root, sx, sy, tags_to_scale, precision)
    
    # Add comment header
    comment = ET.Comment(f'\nLayout: {target_width}x{target_height}\n'
                        f'Generated by scale_layout.py from {source_width}x{source_height}\n'
                        f'Scale factors: X={sx:.6f}, Y={sy:.6f}\n')
    root.insert(0, comment)
    
    # Convert to string with proper formatting
    xml_str = ET.tostring(root, encoding='unicode', method='xml')
    
    # Pretty print (basic)
    xml_str = xml_str.replace('><', '>\n<')
    
    return xml_str


def main():
    """Main entry point."""
    if len(sys.argv) < 4:
        print(__doc__)
        sys.exit(1)
    
    input_file = sys.argv[1]
    target_width = int(sys.argv[2])
    target_height = int(sys.argv[3])
    
    # Parse options
    source_width = DEFAULT_SOURCE_WIDTH
    source_height = DEFAULT_SOURCE_HEIGHT
    additional_tags = set()
    precision = 6
    dry_run = False
    
    i = 4
    while i < len(sys.argv):
        arg = sys.argv[i]
        
        if arg == '--dry-run':
            dry_run = True
            i += 1
        elif arg == '--source-width' and i + 1 < len(sys.argv):
            source_width = int(sys.argv[i + 1])
            i += 2
        elif arg == '--source-height' and i + 1 < len(sys.argv):
            source_height = int(sys.argv[i + 1])
            i += 2
        elif arg == '--tags' and i + 1 < len(sys.argv):
            additional_tags = set(sys.argv[i + 1].split(','))
            i += 2
        elif arg == '--precision' and i + 1 < len(sys.argv):
            precision = int(sys.argv[i + 1])
            i += 2
        else:
            print(f"Unknown option: {arg}", file=sys.stderr)
            i += 1
    
    try:
        result = scale_layout(
            input_file, target_width, target_height,
            source_width, source_height,
            additional_tags, precision, dry_run
        )
        
        if not dry_run:
            print(result)
        else:
            print("\nDry run complete. Use without --dry-run to generate output.",
                  file=sys.stderr)
    
    except FileNotFoundError:
        print(f"Error: File not found: {input_file}", file=sys.stderr)
        sys.exit(1)
    except Exception as e:
        print(f"Error: {e}", file=sys.stderr)
        sys.exit(1)


if __name__ == '__main__':
    main()
