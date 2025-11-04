#!/usr/bin/env python3
"""
EmulationStation Theme Layout Stretcher
Stretches layout XML to fill target resolution (non-proportional scaling)

Usage:
    python3 stretch_layout.py <input_xml> <target_width> <target_height> [options]
    
Example:
    python3 stretch_layout.py layouts/1920x1080.xml 1366 768 > layouts/1366x768_stretch.xml
    
Options:
    --dry-run              Show changes without generating output
    --source-width WIDTH   Source width (default: 1920)
    --source-height HEIGHT Source height (default: 1080)
    --safe-area PERCENT    Safe area percentage (default: 0, range: 0-10)
"""

import sys
from scale_layout import scale_layout, DEFAULT_SOURCE_WIDTH, DEFAULT_SOURCE_HEIGHT


def stretch_layout(input_file: str, target_width: int, target_height: int,
                   source_width: int = DEFAULT_SOURCE_WIDTH,
                   source_height: int = DEFAULT_SOURCE_HEIGHT,
                   safe_area: float = 0.0,
                   dry_run: bool = False) -> str:
    """
    Stretch layout to fill screen independently in X and Y.
    
    Args:
        input_file: Path to source XML
        target_width: Target resolution width
        target_height: Target resolution height
        source_width: Source resolution width
        source_height: Source resolution height
        safe_area: Percentage to shrink for safe area (0-10)
        dry_run: Show changes without output
    
    Returns:
        Stretched XML as string
    """
    # Apply safe area adjustment
    if safe_area > 0:
        safe_factor = 1.0 - (safe_area / 100.0)
        adjusted_width = int(target_width * safe_factor)
        adjusted_height = int(target_height * safe_factor)
        
        if dry_run:
            print(f"Safe area: {safe_area}%", file=sys.stderr)
            print(f"Adjusted to: {adjusted_width}x{adjusted_height}", file=sys.stderr)
    else:
        adjusted_width = target_width
        adjusted_height = target_height
    
    # Use scale_layout with independent X/Y scaling
    return scale_layout(
        input_file, adjusted_width, adjusted_height,
        source_width, source_height,
        dry_run=dry_run
    )


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
    safe_area = 0.0
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
        elif arg == '--safe-area' and i + 1 < len(sys.argv):
            safe_area = float(sys.argv[i + 1])
            i += 2
        else:
            print(f"Unknown option: {arg}", file=sys.stderr)
            i += 1
    
    try:
        result = stretch_layout(
            input_file, target_width, target_height,
            source_width, source_height,
            safe_area, dry_run
        )
        
        if not dry_run:
            print(result)
        else:
            print("\nDry run complete. Use without --dry-run to generate output.",
                  file=sys.stderr)
    
    except Exception as e:
        print(f"Error: {e}", file=sys.stderr)
        sys.exit(1)


if __name__ == '__main__':
    main()
