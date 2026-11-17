#!/usr/bin/env bash
set -euo pipefail

# Builds the Lyra OS wallpaper collection. Source images use version-prefixed
# package names and keep their native resolution: upscaling to 4K only
# interpolates pixels and triples the package size, while GNOME already
# scales the picture to the screen (zoom). Artifacts are PNG and JPEG XL.
root=$(cd "$(dirname "${BASH_SOURCE[0]}")/.." && pwd)
dist="$root/dist"
tmp=$(mktemp -d "$root/.build-tmp.XXXXXX")
trap 'rm -rf "$tmp"' EXIT
export MAGICK_TEMPORARY_PATH="$tmp"

command -v magick >/dev/null 2>&1 || { echo 'error: ImageMagick is required' >&2; exit 1; }
mkdir -p "$dist/backgrounds" "$dist/gnome-background-properties"

sources=(
  "$root/wallpapers/2702-dawn.png"
  "$root/wallpapers/2702-voyage.png"
  "$root/wallpapers/2702-aurora.png"
  "$root/wallpapers/2702-twilight.png"
  "$root/wallpapers/2702-anchorage.png"
  "$root/wallpapers/2702-sunrise.png"
  "$root/wallpapers/2702-serene.png"
  "$root/wallpapers/2702-haze.png"
  "$root/wallpapers/2702-cloudsea.png"
  "$root/wallpapers/2702-lagoon.png"
  "$root/wallpapers/2702-bloom.png"
  "$root/wallpapers/2702-lotus.png"
  "$root/wallpapers/2702-silk.png"
  "$root/wallpapers/2702-strata.png"
  "$root/wallpapers/2702-ascent.png"
  "$root/wallpapers/2702-mosaic.png"
  "$root/wallpapers/2702-dusk.png"
  "$root/wallpapers/2702-nocturne.png"
  "$root/wallpapers/2702-dunes.png"
  "$root/wallpapers/2702-orbit.png"
  "$root/wallpapers/2702-eclipse.png"
  "$root/wallpapers/2702-halo.png"
)
for source in "${sources[@]}"; do
  [[ -f $source ]] || { echo "error: required wallpaper missing: $source" >&2; exit 1; }
done
rm -f "$dist"/backgrounds/*.{png,jxl,svg}
install -m 0644 "$root/src/wallpaper/lyra-os.xml" \
  "$dist/gnome-background-properties/lyra-os.xml"

for source in "${sources[@]}"; do
  stem=$(basename "$source" .png)
  magick "$source" -strip "$dist/backgrounds/$stem.png"
  magick "$dist/backgrounds/$stem.png" -quality 92 \
    "$dist/backgrounds/$stem.jxl"
  printf 'Rendered %s\n' "$stem"
done

printf 'Built %d wallpapers in %s/backgrounds\n' "${#sources[@]}" "$dist"
