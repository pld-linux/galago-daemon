Summary:	Galago daemon
Summary(pl.UTF-8):	Demon Galago
Name:		galago-daemon
Version:	0.5.1
Release:	1
License:	GPL v2+
Group:		Applications/System
Source0:	http://www.galago-project.org/files/releases/source/galago-daemon/%{name}-%{version}.tar.gz
# Source0-md5:	fdb81f938f86f380b127158ebb542279
URL:		http://www.galago-project.org/
BuildRequires:	glib2-devel >= 1:2.12.1
BuildRequires:	libgalago-devel >= 0.5.1
BuildRequires:	pkgconfig
Requires:	dbus >= 0.91
BuildRoot:	%{tmpdir}/%{name}-%{version}-root-%(id -u -n)

%description
Galago "presence" daemon is the center of all presence transactions
for Galago. This service is automatically launched by D-BUS when
needed.
    
%description -l pl.UTF-8
Demon stanu obecności Galago jest centrum wszystkich transakcji Galago.
Usługa ta jest w razie potrzeby automatycznie uruchamiana przez D-BUS.

%prep
%setup -q

%build
cp -f /usr/share/automake/config.sub .
%configure
%{__make}

%install
rm -rf $RPM_BUILD_ROOT

%{__make} install \
	DESTDIR=$RPM_BUILD_ROOT

%clean
rm -rf $RPM_BUILD_ROOT

%files
%defattr(644,root,root,755)
%doc AUTHORS ChangeLog NEWS README
%attr(755,root,root) %{_libexecdir}/galago-daemon
%{_datadir}/dbus-1/services/*.service
%{_sysconfdir}/dbus-1/system.d/*
%config(noreplace) %verify(not md5 mtime size) %{_sysconfdir}/dbus-1/system.d/galago-daemon.conf
