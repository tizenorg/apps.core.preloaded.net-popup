%define _usrdir /usr
%define _appdir %{_usrdir}/apps

Name:       org.tizen.net-popup
Summary:    Network Notification Popup application
Version:    0.2.01_2
Release:    1
Group:      App/Network
License:    Flora License
Source0:    %{name}-%{version}.tar.gz
BuildRequires: cmake
BuildRequires: pkgconfig(appcore-efl)
BuildRequires: pkgconfig(bundle)
BuildRequires: pkgconfig(dlog)
BuildRequires: pkgconfig(ecore)
BuildRequires: pkgconfig(edje)
BuildRequires: pkgconfig(elementary)
BuildRequires: pkgconfig(evas)
BuildRequires: pkgconfig(syspopup)
BuildRequires: pkgconfig(syspopup-caller)
BuildRequires: pkgconfig(glib-2.0)
BuildRequires: pkgconfig(status)
BuildRequires:	pkgconfig(notification)
BuildRequires:	pkgconfig(appsvc)
BuildRequires: gettext

%description
Network Notification Popup application

%prep
%setup -q


%build
cmake . -DCMAKE_INSTALL_PREFIX=%{_appdir}/org.tizen.net-popup

make %{?jobs:-j%jobs}


%install
%make_install

#License
mkdir -p %{buildroot}%{_datadir}/license
cp LICENSE.Flora %{buildroot}%{_datadir}/license/org.tizen.net-popup


%files
%manifest org.tizen.net-popup.manifest
%defattr(-,root,root,-)
%{_usrdir}/share/packages/org.tizen.net-popup.xml
%{_appdir}/org.tizen.net-popup/bin/net-popup
%{_datadir}/license/org.tizen.net-popup
%{_appdir}/org.tizen.net-popup/res/locale/*/LC_MESSAGES/*.mo