Summary: OCS-Store
Name: ocsstore
Version: 2.1.1
Release: 1%{?dist}
License: GPLv3+
Group: Applications/Internet
URL: https://github.com/opendesktop/ocsstore

#Source0: https://github.com/opendesktop/ocsstore/archive/release-%{version}.tar.gz
Source0: %{name}.tar.gz

Requires: libQt5Gui5 >= 5.3.0, libQt5WebSockets5 >= 5.3.0, libQt5DBus5 >= 5.3.0
BuildRequires: make, automake, gcc, gcc-c++, libtool, libqt5-qtbase-devel >= 5.3.0, libQt5Gui-devel >= 5.3.0, libqt5-qtwebsockets-devel >= 5.3.0, libQt5DBus-devel >= 5.3.0, git, nodejs, npm, rpm-build

%description
OCS-compatible Electron-based frontend.

%prep
#%%autosetup -n %{name}-release-%{version}
%autosetup -n %{name}

%build
%define debug_package %{nil}
make

%install
make DESTDIR="%{buildroot}" prefix="/usr" install

%files
%defattr(-,root,root)
%{_bindir}/%{name}
/usr/lib/%{name}-*/*
%{_datadir}/applications/%{name}.desktop
%{_datadir}/icons/hicolor/scalable/apps/%{name}.svg

%clean
rm -rf %{buildroot}

%changelog
* Wed Jul 19 2017 Akira Ohgaki <akiraohgaki@gmail.com> - 2.1.1-1
- Fix for file installation

* Sun Jul 09 2017 Akira Ohgaki <akiraohgaki@gmail.com> - 2.1.0-1
- Rebrand
