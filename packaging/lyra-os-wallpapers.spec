Name:           lyra-os-wallpapers
Version:        1.9.1
Release:        1%{?dist}
Summary:        Versioned wallpaper collection for Lyra OS
License:        GPL-3.0-or-later
URL:            https://github.com/lyra-os-linux/lyraos-desktop-wallpapers
Source0:        %{name}-%{version}.tar.xz
BuildArch:      noarch
BuildRequires:  ImageMagick

%description
Dawn and Voyage wallpapers for Lyra OS, shipped as 4K PNG and JPEG XL
images with GNOME background metadata.

%prep
%autosetup

%build
./scripts/build-wallpaper-variants.sh

%install
install -d %{buildroot}%{_datadir}/backgrounds/lyra
install -m 0644 dist/backgrounds/2702-dawn.png dist/backgrounds/2702-dawn.jxl \
  dist/backgrounds/2702-voyage.png dist/backgrounds/2702-voyage.jxl \
  %{buildroot}%{_datadir}/backgrounds/lyra/
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
%dir %{_datadir}/gnome-background-properties
%{_datadir}/gnome-background-properties/lyra-os.xml

%changelog
