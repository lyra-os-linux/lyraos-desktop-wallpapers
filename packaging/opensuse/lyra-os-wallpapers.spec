Name:           lyra-os-wallpapers
Version:        0.0.0
Release:        1%{?dist}
Summary:        Versioned wallpaper collection for Lyra OS
License:        GPL-3.0-or-later
URL:            https://github.com/lyra-os-linux/lyraos-desktop-wallpapers
Source0:        lyra-wallpapers-src-%{version}.tar.gz
BuildArch:      noarch
BuildRequires:  ImageMagick

%description
Official, versioned Lyra OS wallpaper collection. The 2702 series is shipped
as 4K PNG and JPEG XL images and includes GNOME background metadata.

%prep
%setup -q -n lyra-wallpapers-src-%{version}

%build
./scripts/build-wallpaper-variants.sh

%install
install -d %{buildroot}%{_datadir}/backgrounds/lyra
install -m 0644 dist/backgrounds/*.png dist/backgrounds/*.jxl \
  %{buildroot}%{_datadir}/backgrounds/lyra/
install -d %{buildroot}%{_datadir}/gnome-background-properties
install -m 0644 dist/gnome-background-properties/lyra-os.xml \
  %{buildroot}%{_datadir}/gnome-background-properties/

%files
%license LICENSE
%doc README.md
%dir %{_datadir}/backgrounds
%dir %{_datadir}/backgrounds/lyra
%{_datadir}/backgrounds/lyra/2702-*.png
%{_datadir}/backgrounds/lyra/2702-*.jxl
%dir %{_datadir}/gnome-background-properties
%{_datadir}/gnome-background-properties/lyra-os.xml

%changelog
