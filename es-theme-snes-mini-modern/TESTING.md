# Testing & Verification Guide

## Pre-Installation Testing

### 1. Verify Theme Integrity

Run the verification script before installation:

```bash
cd es-theme-snes-mini-modern
bash tools/verify_theme.sh
```

**Expected output:** "Theme verification PASSED"

### 2. Validate XML Syntax

```bash
# Check main files
xmllint --noout theme.xml
xmllint --noout base.xml

# Check all layouts
for xml in layouts/*.xml; do
    xmllint --noout "$xml" && echo "✓ $xml"
done
```

All should pass without errors.

### 3. Check File Sizes

```bash
# Total theme size (should be < 15 MB)
du -sh .

# Check asset sizes
du -sh art/
du -sh fonts/
```

**Expected:**
- Total theme: ~10 MB
- Art directory: ~9 MB
- Fonts: ~150 KB

## Post-Installation Testing

### 1. Check EmulationStation Logs

```bash
# Monitor logs during theme load
tail -f ~/.emulationstation/es_log.txt
```

**Look for:**
```
[ThemeSystem] Theme set to snes-mini-modern
[ThemeSystem] Loading theme 'snes-mini-modern'...
```

**No errors?** ✅ Theme loaded successfully

### 2. System View Testing

1. Start EmulationStation
2. Navigate through systems (D-pad left/right)
3. Check for:
   - ✅ System logos display correctly
   - ✅ Carousel animation is smooth
   - ✅ System info text appears
   - ✅ Help icons at bottom

### 3. Basic View Testing

1. Enter any system
2. Verify:
   - ✅ Game list displays
   - ✅ Selection highlight works
   - ✅ Box art appears (if available)
   - ✅ System logo at top
   - ✅ Help text at bottom

### 4. Detailed View Testing

1. Press **Select** to switch to Detailed view
2. Verify:
   - ✅ Screenshot/marquee displays
   - ✅ Bezel frame around image
   - ✅ Shadow overlay visible
   - ✅ Game name appears
   - ✅ Description text readable
   - ✅ Text scrolls if long

### 5. Video View Testing

1. Press **Select** to switch to Video view
2. Select a game with video preview
3. Verify:
   - ✅ Video starts after 0.75s delay
   - ✅ Bezel frame around video
   - ✅ Light glow effect visible
   - ✅ Video plays smoothly (no stutter)
   - ✅ Falls back to screenshot if no video
   - ✅ Description text below

**Note:** Video testing requires games with video previews configured.

### 6. Grid View Testing

1. Press **Select** to switch to Grid view
2. Verify:
   - ✅ Thumbnails display in 5×3 grid
   - ✅ Selected tile zooms (1.15x)
   - ✅ Navigation smooth (no lag)
   - ✅ Game name at bottom
   - ✅ Description text appears
   - ✅ Glow effect on selection

### 7. Resolution Testing

#### Test 1920×1080

```bash
# Check current resolution
tvservice -s
# Should show: 1920x1080 @ 60Hz

# Verify layout in use
grep -A 1 "1920x1080" ~/.emulationstation/es_log.txt
```

#### Test 1366×768

```bash
# Set to 1366x768 in /boot/config.txt
sudo nano /boot/config.txt

# Add/modify:
hdmi_group=2
hdmi_mode=39

# Reboot
sudo reboot

# Verify
tvservice -s
# Should show: 1366x768 @ 60Hz
```

### 8. Performance Testing

#### Frame Rate Check

Navigate through menus and observe:
- ✅ No stuttering during carousel scroll
- ✅ Smooth view transitions
- ✅ Grid selection animation fluid
- ✅ Video playback doesn't drop frames

#### Memory Check

```bash
# While ES is running
free -h

# Check VRAM usage (should be reasonable)
vcgencmd get_mem gpu
```

#### Load Time Check

```bash
# Time theme load
time systemctl restart emulationstation

# Should be < 5 seconds on Pi 4
```

### 9. Driver Compatibility Testing

#### FKMS Driver

```bash
# Check driver in use
vcgencmd get_config int | grep kms

# fkms active if shows:
dtoverlay=vc4-fkms-v3d
```

Verify all views work correctly.

#### KMS Driver

```bash
# Edit boot config
sudo nano /boot/config.txt

# Change to:
dtoverlay=vc4-kms-v3d

# Reboot and test
sudo reboot
```

Theme should work identically on both drivers.

## Automated Test Scripts

### Quick Verification

```bash
# Run full verification
make test

# Should output:
# ✓ theme.xml: valid
# ✓ base.xml: valid
# ✓ All layouts: valid
```

### Performance Optimization

```bash
# Optimize all assets
make optimize

# Check size reduction
du -sh art/
```

## Manual Test Checklist

Print and check off during testing:

**System View:**
- [ ] Carousel displays correctly
- [ ] System logos load
- [ ] Navigation is smooth
- [ ] Help text visible

**Basic View:**
- [ ] Game list readable
- [ ] Selection highlight works
- [ ] Box art displays
- [ ] Layout proportions correct

**Detailed View:**
- [ ] Screenshot/marquee visible
- [ ] Bezel frame present
- [ ] Shadow overlay visible
- [ ] Game info displays
- [ ] Text alignment correct

**Video View:**
- [ ] Videos play with delay
- [ ] Bezel and glow effects work
- [ ] Fallback to screenshot works
- [ ] Performance is smooth

**Grid View:**
- [ ] 5×3 grid layout correct
- [ ] Selection zoom works
- [ ] Glow effect visible
- [ ] Navigation smooth

**Performance:**
- [ ] No lag or stutter
- [ ] Memory usage reasonable
- [ ] Theme loads quickly
- [ ] All views transition smoothly

**Both Resolutions:**
- [ ] 1920×1080 tested
- [ ] 1366×768 tested
- [ ] Both layouts work correctly

## Common Issues & Solutions

### Issue: Theme Doesn't Load

**Check:**
```bash
ls -la /etc/emulationstation/themes/snes-mini-modern/theme.xml
# File should exist with read permissions

tail -n 50 ~/.emulationstation/es_log.txt | grep -i error
# Look for specific error messages
```

### Issue: Assets Not Displaying

**Check:**
```bash
# Verify all directories present
ls /etc/emulationstation/themes/snes-mini-modern/art/ui/
ls /etc/emulationstation/themes/snes-mini-modern/fonts/

# Fix permissions
sudo chown -R pi:pi /etc/emulationstation/themes/snes-mini-modern
```

### Issue: Video View Stutters

**Solutions:**
- Reduce video resolution (720p max)
- Shorten video duration (< 30 sec)
- Compress videos (< 50 MB)
- Check GPU memory: `sudo raspi-config` → Performance → GPU Memory (set to 256-512)

### Issue: Grid View Slow

**Solutions:**
- Optimize thumbnails (< 200 KB each)
- Run `make optimize`
- Reduce grid size in base.xml (5×3 → 4×3)

### Issue: Wrong Resolution

**Check:**
```bash
tvservice -s
# Verify actual output resolution

# Check theme include
grep include /etc/emulationstation/themes/snes-mini-modern/theme.xml
```

## Regression Testing

When making changes, re-test:

1. ✅ All 4 views still work
2. ✅ Both resolutions render correctly
3. ✅ No new errors in es_log.txt
4. ✅ Performance unchanged
5. ✅ XML validates

## Reporting Issues

When documenting issues, include:

1. **Hardware:** Pi model, RAM
2. **Software:** RetroPie version, ES version
3. **Resolution:** Output resolution
4. **Driver:** fkms or kms
5. **Log output:** Relevant lines from es_log.txt
6. **Screenshot:** If visual issue

## Success Criteria

Theme is ready for use when:

- ✅ Verification script passes
- ✅ All 4 views work on both resolutions
- ✅ No errors in EmulationStation logs
- ✅ Navigation is smooth (60 FPS)
- ✅ Memory usage reasonable (< 512 MB)
- ✅ Assets display correctly
- ✅ Compatible with both fkms and kms

---

**All tests passing?** Your theme is production-ready! 🎉
