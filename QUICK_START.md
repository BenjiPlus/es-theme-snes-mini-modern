# Quick Start Guide

**Get your SNES Mini Modern theme running in 5 minutes!**

## 📦 What You Have

A complete, modernized EmulationStation theme with:
- ✅ 1920×1080 and 1366×768 support
- ✅ All 4 views (Basic, Detailed, Video, Grid)
- ✅ 50+ system logos
- ✅ Modern visual effects
- ✅ Automated installation tools

## 🚀 Installation (3 Steps)

### 1. Copy Theme to Pi

**Via SSH:**
```bash
# From your computer, copy to Pi:
scp -r es-theme-snes-mini-modern/ pi@retropie.local:/tmp/

# Then SSH into Pi:
ssh pi@retropie.local
```

**Via USB:**
- Copy folder to USB drive
- Insert USB into Pi
- SSH or use terminal

### 2. Install Theme

```bash
cd /tmp/es-theme-snes-mini-modern  # or wherever you copied it

# Install (choose one method):

# System-wide (recommended):
make install

# Or user-only:
make install-user
```

### 3. Select Theme

```bash
# Restart EmulationStation
make restart
```

Then in EmulationStation:
1. Press **Start** button
2. Go to **UI Settings**
3. Choose **Theme Set** → **snes-mini-modern**
4. Press **B** to exit
5. Start → Quit → Restart EmulationStation

**Done!** 🎉

## 🎮 Testing

1. Navigate to any system with games
2. Press **Select** to cycle views:
   - Basic → Detailed → Video → Grid
3. All views should render perfectly

## 🔧 Troubleshooting

### Theme not in list?
```bash
ls /etc/emulationstation/themes/snes-mini-modern/
# Should show all files

# Fix permissions:
sudo chown -R pi:pi /etc/emulationstation/themes/snes-mini-modern
```

### Check for errors:
```bash
tail -n 50 ~/.emulationstation/es_log.txt
```

### Verify theme integrity:
```bash
cd /etc/emulationstation/themes/snes-mini-modern
bash tools/verify_theme.sh
```

## 📝 Common Tasks

**Optimize performance:**
```bash
cd /etc/emulationstation/themes/snes-mini-modern
make optimize
```

**Create custom resolution:**
```bash
make custom WIDTH=1600 HEIGHT=900
# Then edit theme.xml to include it
```

**Uninstall:**
```bash
make uninstall
```

## 📚 More Info

- Full documentation: `README.md`
- Installation guide: `INSTALL.md`
- Changes from original: `CHANGELOG.md`
- Licensing: `LICENSE`

## 💡 Tips

1. **For best video performance:**
   - Keep videos < 30 seconds
   - Use 720p or lower
   - H.264 MP4 format

2. **For faster loading:**
   - Run `make optimize` after installation
   - Keep box art < 500 KB

3. **Customize per system:**
   - Edit files in `systems/` folder
   - See `systems/snes.xml` for example

## ⚙️ System Requirements

- RetroPie 4.8+
- EmulationStation v2.10.2+
- Raspberry Pi 4 (2GB+ RAM)
- Works with fkms or kms drivers

## 🎨 Resolutions

Theme auto-detects your resolution:
- **1920×1080** → Uses 1080p layout
- **1366×768** → Uses scaled 768p layout
- **Other** → Falls back to closest match

Want different scaling? Edit `theme.xml` includes.

---

**Everything working?** Enjoy your modernized SNES Mini theme! 🎮

**Having issues?** Check `INSTALL.md` for detailed troubleshooting.
