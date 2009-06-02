Summary:	An astronomy application
Summary(pl.UTF-8):	Aplikacja astronomiczna
Name:		nightfall
Version:	1.70
Release:	1
License:	GPL v2+
Group:		X11/Applications
Source0:	http://www.la-samhna.de/nightfall/%{name}-%{version}.tar.gz
# Source0-md5:	e2e3ded15f8b69a620585b035071a1ea
Patch0:		%{name}-desktop.patch
Patch1:		%{name}-ac.patch
URL:		http://www.hs.uni-hamburg.de/DE/Ins/Per/Wichmann/Nightfall.html
BuildRequires:	OpenGL-GLU-devel
BuildRequires:	OpenGL-glut-devel
BuildRequires:	autoconf
BuildRequires:	automake
BuildRequires:	gettext-devel
BuildRequires:	gtk+2-devel >= 2:2.6
BuildRequires:	gtkglarea-devel >= 1.99
BuildRequires:	intltool
BuildRequires:	libgnomeui-devel >= 2.0
BuildRequires:	libjpeg-devel
BuildRequires:	pkgconfig
BuildRequires:	rpmbuild(macros) >= 1.198
BuildRequires:	scrollkeeper
Requires(post,postun):	scrollkeeper
Requires:	gnuplot
BuildRoot:	%{tmpdir}/%{name}-%{version}-root-%(id -u -n)

%description
Nightfall is an astronomy application for fun, education, and science.
It can produce animated views of eclipsing binary stars, calculate
synthetic lightcurves and radial velocity curves, and eventually
determine the best-fit model for a given set of observational data.

%description -l pl.UTF-8
Nightfall jest aplikacją astronomiczną do zabawy, edukacji oraz
nauki. Potrafi tworzyć animowane obrazy zaćmionych podwójnych
gwiazd, wyliczać syntetyczne krzywe światła, krzywe prędkości
gwiezdnych i ewentualnie określa najlepiej pasujący model dla danego
zestawu danych obserwacyjnych.

%prep
%setup -q
%patch0 -p1
%patch1 -p1

%build
%{__gettextize}
%{__intltoolize}
%{__aclocal}
%{__autoconf}
%configure \
	--with-gnuplot
%{__make}

%install
rm -rf $RPM_BUILD_ROOT
install -d $RPM_BUILD_ROOT{%{_desktopdir},%{_pixmapsdir}}

%{__make} install \
	DESTDIR=$RPM_BUILD_ROOT

install %{name}.desktop $RPM_BUILD_ROOT%{_desktopdir}
install %{name}.xpm $RPM_BUILD_ROOT%{_pixmapsdir}

%find_lang %{name} --all-name

%clean
rm -rf $RPM_BUILD_ROOT

%post
%scrollkeeper_update_post

%postun
%scrollkeeper_update_postun

%files -f %{name}.lang
%defattr(644,root,root,755)
%doc AUTHORS README doc/*
%attr(755,root,root) %{_bindir}/*
%{_datadir}/%{name}
%{_omf_dest_dir}/%{name}
%{_desktopdir}/%{name}.desktop
%{_mandir}/man1/%{name}.1*
%{_pixmapsdir}/%{name}.xpm
