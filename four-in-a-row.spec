Summary:	"Four in a row" game for GNOME
Summary(pl.UTF-8):	Gra "cztery w rzędzie" dla GNOME
Name:		four-in-a-row
Version:	3.36.4
Release:	1
License:	GPL v2+
Group:		X11/Applications/Games
Source0:	http://ftp.gnome.org/pub/GNOME/sources/four-in-a-row/3.36/%{name}-%{version}.tar.xz
# Source0-md5:	d93f264b9444264cb7b676b1db50071d
URL:		https://wiki.gnome.org/Apps/Four-in-a-row
BuildRequires:	appstream-glib
BuildRequires:	glib2-devel >= 1:2.40.0
BuildRequires:	gsound-devel >= 1.0.2
BuildRequires:	gtk+3-devel >= 3.22.23
BuildRequires:	libcanberra-gtk3-devel >= 0.26
BuildRequires:	librsvg-devel >= 1:2.32.0
BuildRequires:	meson
BuildRequires:	ninja >= 1.5
BuildRequires:	pkgconfig
BuildRequires:	rpmbuild(macros) >= 1.736
BuildRequires:	tar >= 1:1.22
BuildRequires:	vala >= 2:0.22
BuildRequires:	vala-librsvg >= 1:2.32.0
BuildRequires:	xz
BuildRequires:	yelp-tools
Requires(post,postun):	gtk-update-icon-cache
Requires(post,postun):	glib2 >= 1:2.40.0
Requires:	glib2 >= 1:2.40.0
Requires:	gsound >= 1.0.2
Requires:	gtk+3 >= 3.22.23
Requires:	hicolor-icon-theme
Requires:	libcanberra-gtk3 >= 0.26
Requires:	librsvg >= 1:2.32.0
Provides:	gnome-games-gnect = 1:%{version}-%{release}
Obsoletes:	gnect
Obsoletes:	gnome-games-gnect < 1:3.8.0
BuildRoot:	%{tmpdir}/%{name}-%{version}-root-%(id -u -n)

%description
Four-in-a-row is a GNOME game which objective is to build a line of
four of your marbles while trying to stop your opponent (human or
computer) from building a line of his or her own.

%description -l pl.UTF-8
Four-in-a-row to gra dla GNOME, której celem jest zbudowanie rzędu
czterech kafelków, a jednocześnie powstrzymanie przeciwnika (człowieka
lub komputera) od zbudowania własnego rzędu.

%prep
%setup -q

%build
%meson build

%ninja_build -C build

%install
rm -rf $RPM_BUILD_ROOT

%ninja_install -C build

%find_lang %{name} --with-gnome

%clean
rm -rf $RPM_BUILD_ROOT

%post
%glib_compile_schemas
%update_icon_cache hicolor

%postun
%glib_compile_schemas
%update_icon_cache hicolor

%files -f %{name}.lang
%defattr(644,root,root,755)
%doc COPYING.themes NEWS README.md
%attr(755,root,root) %{_bindir}/four-in-a-row
%{_datadir}/dbus-1/services/org.gnome.Four-in-a-row.service
%{_datadir}/glib-2.0/schemas/org.gnome.Four-in-a-row.gschema.xml
%{_datadir}/four-in-a-row
%{_datadir}/metainfo/org.gnome.Four-in-a-row.appdata.xml
%{_desktopdir}/org.gnome.Four-in-a-row.desktop
%{_iconsdir}/hicolor/*x*/apps/org.gnome.Four-in-a-row.png
%{_iconsdir}/hicolor/symbolic/apps/org.gnome.Four-in-a-row-symbolic.svg
%{_mandir}/man6/four-in-a-row.6*
