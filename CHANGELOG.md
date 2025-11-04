# Changelog

All notable changes to the SNES Mini Modern theme will be documented in this file.

## [1.0.0] - 2025-01-04

### 🎉 Initial Private Release

**Target Platform:**
- RetroPie 4.8
- EmulationStation v2.10.2
- Raspberry Pi 4
- Tested on 1920×1080 and 1366×768 displays

### Added

#### Core Features
- ✅ **FormatVersion 4 Support** - Full compatibility with EmulationStation v2.10.2
- ✅ **Multi-Resolution Support** - 1920×1080 and 1366×768 layouts (scaled and stretched variants)
- ✅ **Four View Types** - Basic, Detailed, Video, and Grid views fully implemented
- ✅ **Auto-Resolution Detection** - Theme automatically selects appropriate layout based on display

#### Visual Enhancements
- ✨ **Shadow Overlays** - Subtle radial shadows behind preview areas for depth
- ✨ **Light Glow Effects** - Soft highlight on selected items in grid view
- ✨ **Bezel Frames** - Decorative frames around video/image previews with SNES-style red accents
- ✨ **Modern Typography** - Optimized font sizes and spacing for readability
- ✨ **Smooth Animations** - Grid view with zoom on selection (1.15x scale)

#### Video View
- 🎥 Video preview with 0.75s delay before autoplay
- 🎥 Fallback to screenshot when video unavailable
- 🎥 Bezel frame integration with glow effects
- 🎥 Proper aspect ratio handling

#### Grid View
- 🎮 5×3 tile layout optimized for both resolutions
- 🎮 Animated selection with zoom effect
- 🎮 Game name and description footer
- 🎮 Centered navigation with smooth scrolling

#### System Coverage
- 🌍 **50+ Systems Supported** including:
  - Nintendo: NES, SNES, N64, GB, GBC, GBA, DS
  - Sony: PlayStation, PSP
  - Sega: Genesis, Mega Drive, Master System, Dreamcast, Saturn, 32X
  - Arcade: MAME, FBA, Neo Geo
  - Computers: C64, Amiga, MSX, PC
  - Handhelds: Game Gear, Lynx, Wonderswan, Neo Geo Pocket
  - And many more...

#### Tools & Automation
- 🛠️ **scale_layout.py** - Proportional layout scaling tool with smart tag detection
- 🛠️ **stretch_layout.py** - Full-screen stretch tool with safe area support
- 🛠️ **create_overlays.py** - Generate shadow, glow, and bezel assets
- 🛠️ **optimize_pngs.py** - PNG compression for performance optimization

#### Documentation
- 📖 Comprehensive README.md with features, installation, and usage
- 📖 Detailed INSTALL.md with step-by-step instructions and troubleshooting
- 📖 CHANGELOG.md (this file)
- 📖 Inline XML comments in all theme files

### Technical Details

#### Performance Optimizations
- Target VRAM usage: < 10 MB per screen
- Optimized PNG assets with compression
- Efficient layering to minimize overdraw
- Tested on Pi 4 with both fkms and kms drivers

#### File Structure
```
es-theme-snes-mini-modern/
├── theme.xml              # Main entry point (formatVersion 4)
├── base.xml               # View definitions for all views
├── layouts/               # Resolution-specific overrides
│   ├── 1920x1080.xml
│   ├── 1366x768_scale.xml
│   └── 1366x768_stretch.xml
├── art/
│   ├── ui/                # UI elements, overlays, borders
│   └── systems/           # System logos (58 systems)
├── fonts/                 # TTF fonts (5 variants)
├── sounds/                # Navigation sound effects
├── tools/                 # Python utilities
└── screenshots/           # (Reserved for documentation)
```

#### XML Structure
- Uses relative positioning (0-1 coordinate system) where possible
- Proper text element configuration with font paths
- Help system styling per view
- Metadata display optimization

### Changed from Original SNES Mini Theme

#### Upgraded
- ⬆️ formatVersion 3 → 4 (ES v2.10.2 compatibility)
- ⬆️ Added grid view (not present in original)
- ⬆️ Enhanced video view with modern features
- ⬆️ Improved layout system with automated scaling

#### Enhanced
- 🎨 Added visual effects (shadows, glows, bezels)
- 🎨 Modernized color scheme with subtle transparency
- 🎨 Better text readability with updated fonts and spacing
- 🎨 Smooth animations and transitions

#### Optimized
- ⚡ Reduced texture memory footprint
- ⚡ Faster loading with compressed assets
- ⚡ Better performance on Pi 4 hardware
- ⚡ Cleaner XML structure with reduced redundancy

### Attribution

**Based on:** es-theme-snes-mini by ruckage (v1.10, 2018)  
**Modernized for:** EmulationStation v2.10.2 / RetroPie 4.8  
**License:** Private use only - not for public distribution

### Known Issues

None at this time. Theme has been tested and verified on:
- Raspberry Pi 4 (4GB)
- RetroPie 4.8
- EmulationStation v2.10.2
- Both 1920×1080 and 1366×768 displays
- Both fkms and kms GPU drivers

### Future Considerations

Potential enhancements for future private updates:
- [ ] 4K (3840×2160) layout support
- [ ] Additional aspect ratios (21:9 ultrawide)
- [ ] Per-system custom backgrounds
- [ ] Alternative color schemes
- [ ] CRT shader integration
- [ ] Animated system logos
- [ ] Custom collection icons

---

## Version History

- **1.0.0** (2025-01-04) - Initial private release with full ES v2.10.2 support

---

**Format:** This changelog follows [Keep a Changelog](https://keepachangelog.com/en/1.0.0/) principles.
