# Makefile for SNES Mini Modern Theme
# Quick installation and maintenance commands

THEME_NAME = snes-mini-modern
SYSTEM_THEME_DIR = /etc/emulationstation/themes/$(THEME_NAME)
USER_THEME_DIR = $(HOME)/.emulationstation/themes/$(THEME_NAME)

.PHONY: help install install-user uninstall restart optimize test clean

# Default target
help:
	@echo "SNES Mini Modern Theme - Installation Commands"
	@echo ""
	@echo "Available targets:"
	@echo "  make install        - Install theme system-wide (requires sudo)"
	@echo "  make install-user   - Install theme for current user only"
	@echo "  make uninstall      - Remove system-wide installation"
	@echo "  make restart        - Restart EmulationStation"
	@echo "  make optimize       - Optimize PNG files for better performance"
	@echo "  make test           - Validate XML syntax"
	@echo "  make clean          - Remove generated files"
	@echo ""

# Install system-wide (all users)
install:
	@echo "Installing SNES Mini Modern theme system-wide..."
	sudo mkdir -p $(SYSTEM_THEME_DIR)
	sudo rsync -av --delete --exclude='.git' --exclude='*.pyc' --exclude='__pycache__' ./ $(SYSTEM_THEME_DIR)/
	sudo chown -R pi:pi $(SYSTEM_THEME_DIR)
	@echo "✓ Theme installed to $(SYSTEM_THEME_DIR)"
	@echo "→ Select theme in EmulationStation: UI Settings → Theme Set → $(THEME_NAME)"

# Install for current user only
install-user:
	@echo "Installing SNES Mini Modern theme for current user..."
	mkdir -p $(USER_THEME_DIR)
	rsync -av --delete --exclude='.git' --exclude='*.pyc' --exclude='__pycache__' ./ $(USER_THEME_DIR)/
	@echo "✓ Theme installed to $(USER_THEME_DIR)"
	@echo "→ Select theme in EmulationStation: UI Settings → Theme Set → $(THEME_NAME)"

# Uninstall system-wide
uninstall:
	@echo "Removing SNES Mini Modern theme..."
	sudo rm -rf $(SYSTEM_THEME_DIR)
	@echo "✓ Theme uninstalled"
	@echo "→ Select a different theme in EmulationStation UI Settings"

# Restart EmulationStation
restart:
	@echo "Restarting EmulationStation..."
	@sudo systemctl restart emulationstation 2>/dev/null || pkill -TERM emulationstation || true
	@echo "✓ EmulationStation restarted"

# Optimize PNG files
optimize:
	@echo "Optimizing PNG files..."
	@python3 tools/optimize_pngs.py
	@echo "✓ PNG optimization complete"

# Validate XML files
test:
	@echo "Validating theme XML files..."
	@xmllint --noout theme.xml && echo "✓ theme.xml: valid" || echo "✗ theme.xml: invalid"
	@xmllint --noout base.xml && echo "✓ base.xml: valid" || echo "✗ base.xml: invalid"
	@xmllint --noout layouts/1920x1080.xml && echo "✓ 1920x1080.xml: valid" || echo "✗ 1920x1080.xml: invalid"
	@xmllint --noout layouts/1366x768_scale.xml && echo "✓ 1366x768_scale.xml: valid" || echo "✗ 1366x768_scale.xml: invalid"
	@xmllint --noout layouts/1366x768_stretch.xml && echo "✓ 1366x768_stretch.xml: valid" || echo "✗ 1366x768_stretch.xml: invalid"
	@echo "✓ XML validation complete"

# Clean generated files
clean:
	@echo "Cleaning generated files..."
	@find . -type f -name "*.pyc" -delete
	@find . -type d -name "__pycache__" -exec rm -rf {} + 2>/dev/null || true
	@echo "✓ Cleanup complete"

# Quick install and restart (convenience)
quick: install restart
	@echo "✓ Quick install complete - theme should now be available"

# Generate custom resolution layout
# Usage: make custom WIDTH=1600 HEIGHT=900
custom:
	@if [ -z "$(WIDTH)" ] || [ -z "$(HEIGHT)" ]; then \
		echo "Error: WIDTH and HEIGHT required"; \
		echo "Usage: make custom WIDTH=1600 HEIGHT=900"; \
		exit 1; \
	fi
	@echo "Generating $(WIDTH)x$(HEIGHT) layout..."
	@python3 tools/scale_layout.py layouts/1920x1080.xml $(WIDTH) $(HEIGHT) > layouts/$(WIDTH)x$(HEIGHT).xml
	@echo "✓ Created layouts/$(WIDTH)x$(HEIGHT).xml"
	@echo "→ Edit theme.xml to include this layout"
