Summary:	An astronomy application
Summary(pl.UTF-8):	Aplikacja astronomiczna
Name:		nightfall
Version:	1.62
Release:	1
License:	GPL v2+
Group:		X11/Applications
Source0:	http://www.la-samhna.de/nightfall/%{name}-%{version}.tar.gz
# Source0-md5:	318314e97b83fdb74860aba6adef219b
Patch0:		%{name}-desktop.patch
URL:		http://www.hs.uni-hamburg.de/DE/Ins/Per/Wichmann/Nightfall.html
#BuildRequires:	gnuplot
BuildRequires:	gtk+-devel
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

%build
%configure \
	--with-gnuplot
%{__make}

%install
rm -rf $RPM_BUILD_ROOT
install -d $RPM_BUILD_ROOT{%{_desktopdir},%{_pixmapsdir}}

%{__make} install \
	DESTDIR=$RPM_BUILD_ROOT

install %{name}.desktop $RPM_BUILD_ROOT%{_desktopdir}/
install %{name}.xpm $RPM_BUILD_ROOT%{_pixmapsdir}/

%find_lang %{name} --all-name

%clean
rm -rf $RPM_BUILD_ROOT

%files -f %{name}.lang
%defattr(644,root,root,755)
%doc AUTHORS README doc/*
%attr(755,root,root) %{_bindir}/*
%{_datadir}/%{name}
%{_desktopdir}/%{name}.desktop
%{_mandir}/man1/%{name}.1*
%{_pixmapsdir}/%{name}.xpm
