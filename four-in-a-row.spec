Summary:	"Four in a row" game for GNOME
Summary(pl.UTF-8):	Gra "cztery w rzędzie" dla GNOME
Name:		four-in-a-row
Version:	3.18.2
Release:	1
License:	GPL v2+
Group:		X11/Applications/Games
Source0:	http://ftp.gnome.org/pub/GNOME/sources/four-in-a-row/3.18/%{name}-%{version}.tar.xz
# Source0-md5:	01c9c52553c65d9e953f458bb05c0fb2
URL:		https://wiki.gnome.org/Apps/Four-in-a-row
BuildRequires:	appstream-glib-devel
BuildRequires:	autoconf >= 2.63
BuildRequires:	automake >= 1:1.11
BuildRequires:	gnome-common
BuildRequires:	gtk+3-devel >= 3.13.2
BuildRequires:	intltool >= 0.50
BuildRequires:	libcanberra-gtk3-devel >= 0.26
BuildRequires:	librsvg-devel >= 2.32.0
BuildRequires:	pkgconfig
BuildRequires:	vala >= 2:0.22
BuildRequires:	yelp-tools
Requires(post,postun):	gtk-update-icon-cache
Requires(post,postun):	glib2 >= 1:2.26.0
Requires:	gtk+3 >= 3.13.2
Requires:	hicolor-icon-theme
Requires:	libcanberra-gtk3 >= 0.26
Requires:	librsvg >= 2.32.0
Provides:	gnome-games-gnect = 1:%{version}-%{release}
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
%{__intltoolize}
%{__aclocal}
%{__autoconf}
%{__autoheader}
%{__automake}
%configure \
	--disable-silent-rules

%{__make}

%install
rm -rf $RPM_BUILD_ROOT

%{__make} install \
	DESTDIR=$RPM_BUILD_ROOT

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
%doc NEWS README
%attr(755,root,root) %{_bindir}/four-in-a-row
%{_datadir}/appdata/four-in-a-row.appdata.xml
%{_datadir}/glib-2.0/schemas/org.gnome.four-in-a-row.gschema.xml
%{_datadir}/four-in-a-row
%{_desktopdir}/four-in-a-row.desktop
%{_iconsdir}/hicolor/*x*/apps/four-in-a-row.png
%{_iconsdir}/hicolor/scalable/apps/four-in-a-row.svg
%{_iconsdir}/hicolor/scalable/apps/four-in-a-row-symbolic.svg
%{_mandir}/man6/four-in-a-row.6*
