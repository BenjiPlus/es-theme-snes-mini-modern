#!/bin/bash
# Theme Verification Script
# Checks that all required files and directories are present

THEME_ROOT="$(cd "$(dirname "$0")/.." && pwd)"
cd "$THEME_ROOT"

echo "SNES Mini Modern Theme - Verification Check"
echo "=============================================="
echo ""

# Color codes
RED='\033[0;31m'
GREEN='\033[0;32m'
YELLOW='\033[1;33m'
NC='\033[0m' # No Color

errors=0
warnings=0

# Check required files
echo "Checking required files..."

required_files=(
    "theme.xml"
    "base.xml"
    "layouts/1920x1080.xml"
    "layouts/1366x768_scale.xml"
    "layouts/1366x768_stretch.xml"
    "README.md"
    "INSTALL.md"
    "CHANGELOG.md"
    "LICENSE"
)

for file in "${required_files[@]}"; do
    if [ -f "$file" ]; then
        echo -e "${GREEN}✓${NC} $file"
    else
        echo -e "${RED}✗${NC} $file (MISSING)"
        ((errors++))
    fi
done

echo ""

# Check required directories
echo "Checking required directories..."

required_dirs=(
    "art/ui"
    "art/systems"
    "fonts"
    "layouts"
    "tools"
    "systems"
)

for dir in "${required_dirs[@]}"; do
    if [ -d "$dir" ]; then
        count=$(find "$dir" -type f | wc -l)
        echo -e "${GREEN}✓${NC} $dir ($count files)"
    else
        echo -e "${RED}✗${NC} $dir (MISSING)"
        ((errors++))
    fi
done

echo ""

# Check for specific assets
echo "Checking critical assets..."

critical_assets=(
    "art/ui/shadow_overlay.png"
    "art/ui/light_glow.png"
    "art/ui/bezel_frame.png"
    "art/ui/gamelist_background.png"
    "art/ui/border_top.png"
    "art/ui/border_bottom.png"
)

for asset in "${critical_assets[@]}"; do
    if [ -f "$asset" ]; then
        size=$(du -h "$asset" | cut -f1)
        echo -e "${GREEN}✓${NC} $asset ($size)"
    else
        echo -e "${YELLOW}⚠${NC} $asset (MISSING - may affect visuals)"
        ((warnings++))
    fi
done

echo ""

# Check fonts
echo "Checking fonts..."

font_count=$(find fonts/ -name "*.ttf" -o -name "*.otf" 2>/dev/null | wc -l)
if [ "$font_count" -gt 0 ]; then
    echo -e "${GREEN}✓${NC} Found $font_count font files"
    find fonts/ -type f \( -name "*.ttf" -o -name "*.otf" \) -exec echo "  → {}" \;
else
    echo -e "${RED}✗${NC} No fonts found"
    ((errors++))
fi

echo ""

# Check system logos
echo "Checking system logos..."

logo_count=$(find art/systems/ -name "*.png" 2>/dev/null | wc -l)
if [ "$logo_count" -gt 0 ]; then
    echo -e "${GREEN}✓${NC} Found $logo_count system logos"
else
    echo -e "${YELLOW}⚠${NC} No system logos found"
    ((warnings++))
fi

echo ""

# Validate XML syntax (if xmllint is available)
if command -v xmllint &> /dev/null; then
    echo "Validating XML syntax..."
    
    for xml in theme.xml base.xml layouts/*.xml; do
        if [ -f "$xml" ]; then
            if xmllint --noout "$xml" 2>/dev/null; then
                echo -e "${GREEN}✓${NC} $(basename $xml)"
            else
                echo -e "${RED}✗${NC} $(basename $xml) (INVALID XML)"
                ((errors++))
            fi
        fi
    done
else
    echo -e "${YELLOW}⚠${NC} xmllint not found - skipping XML validation"
    echo "  Install: sudo apt-get install libxml2-utils"
    ((warnings++))
fi

echo ""

# Check Python tools
echo "Checking Python tools..."

python_tools=(
    "tools/scale_layout.py"
    "tools/stretch_layout.py"
    "tools/create_overlays.py"
    "tools/optimize_pngs.py"
)

for tool in "${python_tools[@]}"; do
    if [ -f "$tool" ] && [ -x "$tool" ]; then
        echo -e "${GREEN}✓${NC} $tool (executable)"
    elif [ -f "$tool" ]; then
        echo -e "${YELLOW}⚠${NC} $tool (not executable)"
        chmod +x "$tool" 2>/dev/null && echo "  → Made executable"
    else
        echo -e "${RED}✗${NC} $tool (MISSING)"
        ((errors++))
    fi
done

echo ""

# Summary
echo "=============================================="
if [ $errors -eq 0 ] && [ $warnings -eq 0 ]; then
    echo -e "${GREEN}✓ Theme verification PASSED${NC}"
    echo "  All required files and directories are present."
    echo "  Theme is ready for installation."
elif [ $errors -eq 0 ]; then
    echo -e "${YELLOW}⚠ Theme verification PASSED with warnings${NC}"
    echo "  Errors: $errors"
    echo "  Warnings: $warnings"
    echo "  Theme should work but may have minor issues."
else
    echo -e "${RED}✗ Theme verification FAILED${NC}"
    echo "  Errors: $errors"
    echo "  Warnings: $warnings"
    echo "  Please fix errors before installation."
fi

echo ""

exit $errors
