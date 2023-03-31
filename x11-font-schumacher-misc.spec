Name: x11-font-schumacher-misc
Version: 1.1.3
Release: 2
Summary: Xorg X11 font schumacher-misc
Group: Development/X11
URL: https://xorg.freedesktop.org
Source0: https://xorg.freedesktop.org/releases/individual/font/font-schumacher-misc-%{version}.tar.xz
License: MIT-like
BuildArch: noarch
BuildRequires: fontconfig
BuildRequires: pkgconfig(fontutil) >= 1.0.1
BuildRequires: pkgconfig(xorg-macros) >= 1.1.5
Requires(post,postun): mkfontscale

%description
Xorg X11 font schumacher-misc.

%prep
%autosetup -p1 -n font-schumacher-misc-%{version}

%build
%configure --with-fontdir=%{_datadir}/fonts/misc

%make_build

%install
%make_install
rm -f %{buildroot}%{_datadir}/fonts/misc/fonts.dir
rm -f %{buildroot}%{_datadir}/fonts/misc/fonts.scale

%post
mkfontscale %{_datadir}/fonts/misc
mkfontdir %{_datadir}/fonts/misc

%postun
mkfontscale %{_datadir}/fonts/misc
mkfontdir %{_datadir}/fonts/misc

%files
%doc COPYING
%{_datadir}/fonts/misc/cl*.pcf.gz
