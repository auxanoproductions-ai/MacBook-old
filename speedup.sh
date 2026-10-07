#!/bin/bash
# Safe speed-up script for macOS Big Sur.
# Usage: bash speedup.sh   (asks for your password once)
set -u
echo "== Mac Speed-Up (Big Sur) =="
sudo -v || exit 1

echo; echo "== 1. System info =="
sw_vers; sysctl -n machdep.cpu.brand_string
echo "RAM: $(( $(sysctl -n hw.memsize) / 1073741824 )) GB"
df -h / | tail -1

echo; echo "== 2. Top CPU and memory apps =="
ps -Ao pid,%cpu,%mem,comm -r | head -8

echo; echo "== 3. Clearing caches and logs =="
rm -rf ~/Library/Caches/* 2>/dev/null
sudo rm -rf /Library/Caches/* 2>/dev/null
rm -rf ~/Library/Logs/* 2>/dev/null
sudo rm -rf /private/var/log/asl/*.asl 2>/dev/null
rm -rf ~/Library/Developer/Xcode/DerivedData/* 2>/dev/null
echo "Done."

echo; echo "== 4. Emptying Trash =="
rm -rf ~/.Trash/* 2>/dev/null; echo "Done."

echo; echo "== 5. Reducing visual effects =="
defaults write com.apple.universalaccess reduceMotion -bool true
defaults write com.apple.universalaccess reduceTransparency -bool true
defaults write com.apple.dock launchanim -bool false
defaults write com.apple.dock expose-animation-duration -float 0.1
defaults write com.apple.dock autohide-time-modifier -float 0.2
defaults write NSGlobalDomain NSAutomaticWindowAnimationsEnabled -bool false
defaults write com.apple.finder DisableAllAnimations -bool true
killall Dock Finder 2>/dev/null; echo "Done."

echo; echo "== 6. Maintenance tasks =="
sudo periodic daily weekly monthly
sudo dscacheutil -flushcache; sudo killall -HUP mDNSResponder
sudo purge
echo "Done."

echo; echo "== 7. Login items (remove extras manually) =="
osascript -e 'tell application "System Events" to get the name of every login item' 2>/dev/null
ls /Library/LaunchAgents ~/Library/LaunchAgents /Library/LaunchDaemons 2>/dev/null

echo; echo "== 8. Big folders in your home =="
du -sh ~/* 2>/dev/null | sort -hr | head -10

echo; echo "== Finished. Restart your Mac now. =="
df -h / | tail -1
