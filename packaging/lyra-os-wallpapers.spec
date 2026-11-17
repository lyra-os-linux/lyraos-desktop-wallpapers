Name:           lyra-os-wallpapers
Version:        1.10.0
Release:        1%{?dist}
Summary:        Versioned wallpaper collection for Lyra OS
License:        GPL-3.0-or-later
URL:            https://github.com/lyra-os-linux/lyraos-desktop-wallpapers
Source0:        %{name}-%{version}.tar.xz
BuildArch:      noarch
BuildRequires:  ImageMagick

%description
Twenty-two wallpapers for Lyra OS: scenic paintings (Dawn, Voyage and
companions) and abstract compositions, shipped as 4K PNG and JPEG XL
images with GNOME background metadata.

%prep
%autosetup

%build
./scripts/build-wallpaper-variants.sh

%install
install -d %{buildroot}%{_datadir}/backgrounds/lyra
for wallpaper in dawn voyage aurora twilight anchorage sunrise serene haze cloudsea \
    lagoon bloom lotus silk strata ascent mosaic dusk nocturne dunes \
    orbit eclipse halo; do
  install -m 0644 dist/backgrounds/2702-$wallpaper.png \
    dist/backgrounds/2702-$wallpaper.jxl %{buildroot}%{_datadir}/backgrounds/lyra/
done
install -d %{buildroot}%{_datadir}/gnome-background-properties
install -m 0644 dist/gnome-background-properties/lyra-os.xml \
  %{buildroot}%{_datadir}/gnome-background-properties/

%files
%license LICENSE
%doc README.md
%dir %{_datadir}/backgrounds
%dir %{_datadir}/backgrounds/lyra
%{_datadir}/backgrounds/lyra/2702-dawn.png
%{_datadir}/backgrounds/lyra/2702-dawn.jxl
%{_datadir}/backgrounds/lyra/2702-voyage.png
%{_datadir}/backgrounds/lyra/2702-voyage.jxl
%{_datadir}/backgrounds/lyra/2702-aurora.png
%{_datadir}/backgrounds/lyra/2702-aurora.jxl
%{_datadir}/backgrounds/lyra/2702-twilight.png
%{_datadir}/backgrounds/lyra/2702-twilight.jxl
%{_datadir}/backgrounds/lyra/2702-anchorage.png
%{_datadir}/backgrounds/lyra/2702-anchorage.jxl
%{_datadir}/backgrounds/lyra/2702-sunrise.png
%{_datadir}/backgrounds/lyra/2702-sunrise.jxl
%{_datadir}/backgrounds/lyra/2702-serene.png
%{_datadir}/backgrounds/lyra/2702-serene.jxl
%{_datadir}/backgrounds/lyra/2702-haze.png
%{_datadir}/backgrounds/lyra/2702-haze.jxl
%{_datadir}/backgrounds/lyra/2702-cloudsea.png
%{_datadir}/backgrounds/lyra/2702-cloudsea.jxl
%{_datadir}/backgrounds/lyra/2702-lagoon.png
%{_datadir}/backgrounds/lyra/2702-lagoon.jxl
%{_datadir}/backgrounds/lyra/2702-bloom.png
%{_datadir}/backgrounds/lyra/2702-bloom.jxl
%{_datadir}/backgrounds/lyra/2702-lotus.png
%{_datadir}/backgrounds/lyra/2702-lotus.jxl
%{_datadir}/backgrounds/lyra/2702-silk.png
%{_datadir}/backgrounds/lyra/2702-silk.jxl
%{_datadir}/backgrounds/lyra/2702-strata.png
%{_datadir}/backgrounds/lyra/2702-strata.jxl
%{_datadir}/backgrounds/lyra/2702-ascent.png
%{_datadir}/backgrounds/lyra/2702-ascent.jxl
%{_datadir}/backgrounds/lyra/2702-mosaic.png
%{_datadir}/backgrounds/lyra/2702-mosaic.jxl
%{_datadir}/backgrounds/lyra/2702-dusk.png
%{_datadir}/backgrounds/lyra/2702-dusk.jxl
%{_datadir}/backgrounds/lyra/2702-nocturne.png
%{_datadir}/backgrounds/lyra/2702-nocturne.jxl
%{_datadir}/backgrounds/lyra/2702-dunes.png
%{_datadir}/backgrounds/lyra/2702-dunes.jxl
%{_datadir}/backgrounds/lyra/2702-orbit.png
%{_datadir}/backgrounds/lyra/2702-orbit.jxl
%{_datadir}/backgrounds/lyra/2702-eclipse.png
%{_datadir}/backgrounds/lyra/2702-eclipse.jxl
%{_datadir}/backgrounds/lyra/2702-halo.png
%{_datadir}/backgrounds/lyra/2702-halo.jxl
%dir %{_datadir}/gnome-background-properties
%{_datadir}/gnome-background-properties/lyra-os.xml

%changelog
