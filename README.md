# SNES Mini Modern Theme

**A modernized EmulationStation theme for RetroPie 4.8 / Raspberry Pi 4**

![Version](https://img.shields.io/badge/version-1.0.0-blue)
![ES Version](https://img.shields.io/badge/EmulationStation-v2.10.2-green)
![License](https://img.shields.io/badge/license-Private%20Use-red)

## 📋 Overview

This is a **private, modernized version** of the classic SNES Mini theme, upgraded for EmulationStation v2.10.2 on RetroPie 4.8 (Raspberry Pi 4). It retains the authentic SNES Mini visual aesthetic while adding modern features and optimizations.

**Key Features:**
- ✅ EmulationStation v2.10.2 (formatVersion 4) compatibility
- ✅ Support for 1920×1080 and 1366×768 resolutions
- ✅ All four view types: Basic, Detailed, Video, and Grid
- ✅ Enhanced visuals: shadows, glows, and bezels
- ✅ Video preview with 0.75s delay
- ✅ Optimized for Raspberry Pi 4 performance
- ✅ Both fkms and kms GPU driver compatible

## 🎮 Supported Systems

Core systems included:
- NES, SNES, Super Famicom
- Nintendo 64, GameBoy, GameBoy Color, GameBoy Advance
- PlayStation, PSP
- Sega Genesis/Megadrive, Master System, Dreamcast, Saturn
- Arcade, MAME, Final Burn Alpha
- ScummVM
- And 50+ more systems

## 📐 Resolutions

Three layout options:

1. **1920×1080** - Full HD base layout
2. **1366×768 (Scaled)** - Proportionally scaled, maintains aspect ratio
3. **1366×768 (Stretched)** - Full screen fill

EmulationStation will automatically select the appropriate layout based on your display configuration.

## 🚀 Installation

### Method 1: System-wide Installation (Recommended)

```bash
# Clone or copy the theme to EmulationStation themes directory
sudo mkdir -p /etc/emulationstation/themes/snes-mini-modern
sudo rsync -a --delete /path/to/es-theme-snes-mini-modern/ /etc/emulationstation/themes/snes-mini-modern/

# Restart EmulationStation
sudo systemctl restart emulationstation 2>/dev/null || pkill -TERM emulationstation
```

### Method 2: User Installation

```bash
# Install to user directory
mkdir -p ~/.emulationstation/themes/snes-mini-modern
rsync -a --delete /path/to/es-theme-snes-mini-modern/ ~/.emulationstation/themes/snes-mini-modern/

# Restart EmulationStation
pkill -TERM emulationstation
```

### Selecting the Theme

1. Start EmulationStation
2. Press **Start** button
3. Navigate to **UI Settings**
4. Select **Theme Set**
5. Choose **snes-mini-modern**
6. Restart EmulationStation

## 🎨 Views

### Basic View
Clean game list with box art preview and system logo.

### Detailed View
Game list + large screenshot/marquee + game description with shadow overlay and bezel frame.

### Video View
Game list + video preview (0.75s delay) with decorative bezel, lighting glow, and description.

### Grid View
5×3 thumbnail grid with SNES-inspired highlight glow, system logo, and metadata footer.

## 🛠️ Tools

### Layout Scaling Tool

Generate custom resolution layouts:

```bash
# Scale proportionally (maintains aspect ratio)
python3 tools/scale_layout.py layouts/1920x1080.xml 1600 900 > layouts/1600x900.xml

# Dry run to preview changes
python3 tools/scale_layout.py layouts/1920x1080.xml 1280 720 --dry-run
```

### Layout Stretching Tool

Fill screen regardless of aspect ratio:

```bash
# Stretch to fill screen
python3 tools/stretch_layout.py layouts/1920x1080.xml 1440 1080 > layouts/1440x1080.xml

# With safe area (2% border)
python3 tools/stretch_layout.py layouts/1920x1080.xml 1366 768 --safe-area 2 > layouts/custom.xml
```

### Create Visual Overlays

Regenerate shadow, glow, and bezel assets:

```bash
python3 tools/create_overlays.py
```

### Optimize PNGs

Reduce file sizes for better performance:

```bash
python3 tools/optimize_pngs.py
```

## 📊 Performance

**Target specs for Raspberry Pi 4:**
- VRAM usage: < 10 MB per screen
- No frame drops during navigation
- Smooth video preview transitions
- Compatible with both fkms and kms drivers

**Optimization tips:**
- Video previews should be < 30 seconds, 720p max
- Keep screenshot/box art < 500 KB each
- System logos optimized to < 50 KB

## 🐛 Troubleshooting

### Theme doesn't appear in Theme Set list
- Ensure the theme folder name matches exactly: `snes-mini-modern`
- Check that `theme.xml` exists in the root of the theme folder
- Verify file permissions: `sudo chown -R pi:pi /etc/emulationstation/themes/snes-mini-modern`

### Warnings in es_log.txt
Check EmulationStation logs:
```bash
tail -n 200 ~/.emulationstation/es_log.txt
```

Common issues:
- Missing font files → ensure fonts/ directory is copied
- Missing system logo → check art/systems/ folder
- XML syntax errors → validate with: `xmllint --noout theme.xml`

### Video view not working
- Ensure video previews are in correct format (MP4, H.264)
- Check video path in gamelist.xml
- Verify video file size (< 50 MB recommended)

### Grid view layout issues
- Grid may need adjustment for different metadata configurations
- Edit `base.xml` grid `<autoLayout>` to customize (e.g., `4 3` for 4×3 grid)

## 🔧 Customization

### Change Background Colors

Edit `base.xml` and modify the background color in each view:

```xml
<image name="background" extra="true">
    <color>000000FF</color>  <!-- Change this hex color -->
</image>
```

### Adjust Grid Layout

In `base.xml`, modify grid settings:

```xml
<imagegrid name="gamegrid">
    <autoLayout>5 3</autoLayout>  <!-- Change to 4 3, 6 3, etc. -->
    <autoLayoutSelectedZoom>1.15</autoLayoutSelectedZoom>  <!-- Zoom level -->
</imagegrid>
```

### Disable Visual Effects

To disable shadows/glows for better performance, comment out in `base.xml`:

```xml
<!-- 
<image name="shadow_overlay" extra="true">
    ...
</image>
-->
```

## 📄 License

**Private Use Only - Not for Public Distribution**

This theme is for personal, private use only. It incorporates assets from the original SNES Mini theme by ruckage and is not licensed for public distribution or commercial use.

**Original theme:** es-theme-snes-mini by ruckage  
**Modernization:** ES v2.10.2 / RetroPie 4.8 compatibility

## 🙏 Credits

- **Original SNES Mini Theme:** ruckage
- **Modernization & FormatVersion 4 Upgrade:** 2025
- **Target Platform:** RetroPie 4.8 / EmulationStation v2.10.2
- **Hardware:** Raspberry Pi 4

## 📞 Support

For issues specific to RetroPie or EmulationStation:
- [RetroPie Forums](https://retropie.org.uk/forum/)
- [EmulationStation Documentation](https://github.com/RetroPie/EmulationStation)

---

**Version:** 1.0.0  
**Last Updated:** 2025  
**Tested On:** Raspberry Pi 4 (4GB) / RetroPie 4.8 / EmulationStation v2.10.2
