# Installation Guide

## Prerequisites

- RetroPie 4.8 installed
- EmulationStation v2.10.2 or later
- Raspberry Pi 4 (2GB+ RAM recommended)
- SSH access or keyboard connected

## Step-by-Step Installation

### 1. Access Your Raspberry Pi

**Via SSH:**
```bash
ssh pi@retropie.local
# Default password: raspberry
```

**Or use a keyboard** directly connected to your Pi.

### 2. Download/Transfer Theme

If you have the theme on a USB drive:

```bash
# Mount USB drive (usually auto-mounted at /media/usb0)
cd /media/usb0

# Or if not mounted:
sudo mount /dev/sda1 /media/usb0
```

If downloading from a source:

```bash
cd /tmp
# [Your download method here]
```

### 3. Install Theme

**Option A: System-wide (All Users)**

```bash
# Create themes directory if it doesn't exist
sudo mkdir -p /etc/emulationstation/themes

# Copy theme
sudo rsync -av --delete es-theme-snes-mini-modern/ /etc/emulationstation/themes/snes-mini-modern/

# Fix permissions
sudo chown -R pi:pi /etc/emulationstation/themes/snes-mini-modern
```

**Option B: User-specific**

```bash
# Create themes directory
mkdir -p ~/.emulationstation/themes

# Copy theme
rsync -av --delete es-theme-snes-mini-modern/ ~/.emulationstation/themes/snes-mini-modern/
```

### 4. Verify Installation

Check that files are in place:

```bash
ls /etc/emulationstation/themes/snes-mini-modern/
# Should show: art/ fonts/ layouts/ systems/ theme.xml base.xml etc.
```

### 5. Restart EmulationStation

**From SSH:**
```bash
sudo systemctl restart emulationstation
```

**Or:**
```bash
pkill -TERM emulationstation
```

**From EmulationStation menu:**
- Press Start → Quit → Restart EmulationStation

### 6. Select Theme

1. Press **Start** button
2. Select **UI Settings**
3. Scroll to **Theme Set**
4. Choose **snes-mini-modern**
5. Press **B** to go back
6. Restart EmulationStation (Start → Quit → Restart EmulationStation)

## Resolution Configuration

### For 1366×768 Displays

The theme will auto-detect your resolution. If you want to force a specific layout:

1. Edit `theme.xml`:
```bash
nano /etc/emulationstation/themes/snes-mini-modern/theme.xml
```

2. Change the default include:
```xml
<!-- Use scaled version -->
<include>./layouts/1366x768_scale.xml</include>

<!-- OR use stretched version -->
<include>./layouts/1366x768_stretch.xml</include>
```

3. Save and restart EmulationStation

### For 1920×1080 Displays

Default configuration works out of the box. No changes needed.

### For Custom Resolutions

Use the scaling tool to generate a custom layout:

```bash
cd /etc/emulationstation/themes/snes-mini-modern

# Generate custom resolution
python3 tools/scale_layout.py layouts/1920x1080.xml YOUR_WIDTH YOUR_HEIGHT > layouts/custom.xml

# Update theme.xml to use it
nano theme.xml
# Add: <include>./layouts/custom.xml</include>
```

## Verification

### Check Logs for Errors

```bash
tail -n 100 ~/.emulationstation/es_log.txt
```

Look for lines like:
```
[ThemeSystem] Theme set to snes-mini-modern
```

**No errors?** You're good to go! ✅

**Seeing errors?** Check the Troubleshooting section below.

### Test All Views

1. Navigate to a system with games
2. Press **Select** to cycle through views:
   - Basic View
   - Detailed View
   - Video View (if you have video previews)
   - Grid View

All views should load without errors.

## Troubleshooting

### Theme Doesn't Appear in List

**Problem:** snes-mini-modern not in Theme Set menu

**Solutions:**
```bash
# Check theme directory exists
ls /etc/emulationstation/themes/snes-mini-modern/theme.xml

# Verify permissions
sudo chown -R pi:pi /etc/emulationstation/themes/snes-mini-modern

# Check for XML syntax errors
xmllint --noout /etc/emulationstation/themes/snes-mini-modern/theme.xml
```

### Missing Fonts or Assets

**Problem:** White boxes, missing text, or broken layouts

**Solutions:**
```bash
# Verify all directories copied
ls /etc/emulationstation/themes/snes-mini-modern/
# Should include: art/ fonts/ layouts/ systems/ tools/

# Re-copy if needed
sudo rsync -av --delete es-theme-snes-mini-modern/ /etc/emulationstation/themes/snes-mini-modern/
```

### Video View Not Working

**Problem:** Videos don't play or show black screen

**Solutions:**
- Ensure video files are H.264 MP4 format
- Check video paths in your gamelist.xml files
- Verify videos are < 50 MB and < 720p resolution
- Some systems may need OMX player enabled

### Grid View Layout Issues

**Problem:** Grid tiles overlapping or misaligned

**Solutions:**
```bash
# Edit grid settings
nano /etc/emulationstation/themes/snes-mini-modern/base.xml

# Find <imagegrid> section and adjust:
<autoLayout>5 3</autoLayout>  # Change to 4 3 or 6 3
<margin>0.012 0.015</margin>   # Increase for more spacing
```

### Performance Issues

**Problem:** Slow navigation, stuttering, or lag

**Solutions:**
1. Optimize PNG assets:
```bash
cd /etc/emulationstation/themes/snes-mini-modern
python3 tools/optimize_pngs.py
```

2. Disable visual effects:
```bash
nano base.xml
# Comment out shadow_overlay and light_glow sections
```

3. Reduce video preview quality (< 720p, < 30 sec)

### Wrong Resolution Detected

**Problem:** Theme looks stretched or too small

**Solutions:**
1. Check your actual display resolution:
```bash
tvservice -s
```

2. Force specific layout in theme.xml:
```bash
nano /etc/emulationstation/themes/snes-mini-modern/theme.xml
# Change include line to desired resolution
```

## Advanced Configuration

### Enable KMS Driver (Recommended for Pi 4)

Edit boot config:
```bash
sudo nano /boot/config.txt
```

Change:
```
#dtoverlay=vc4-kms-v3d
```
To:
```
dtoverlay=vc4-kms-v3d
```

Reboot:
```bash
sudo reboot
```

### Custom Backgrounds Per System

1. Navigate to system directory:
```bash
cd /etc/emulationstation/themes/snes-mini-modern/systems
```

2. Create system-specific XML (e.g., `snes.xml`):
```xml
<theme>
    <view name="basic, detailed, video">
        <image name="background" extra="true">
            <path>./art/backgrounds/custom_snes_bg.png</path>
        </image>
    </view>
</theme>
```

3. Place custom background in `/art/backgrounds/`

## Uninstallation

To remove the theme:

```bash
# System-wide removal
sudo rm -rf /etc/emulationstation/themes/snes-mini-modern

# User removal
rm -rf ~/.emulationstation/themes/snes-mini-modern
```

Then select a different theme in EmulationStation UI Settings.

## Getting Help

If you encounter issues:

1. Check EmulationStation logs: `~/.emulationstation/es_log.txt`
2. Verify theme integrity: `xmllint --noout theme.xml`
3. Test with default theme to isolate issue
4. Consult [RetroPie Forums](https://retropie.org.uk/forum/)

---

**Need to regenerate layouts?** See `tools/scale_layout.py` documentation in README.md

**Performance tuning?** See `tools/optimize_pngs.py`
