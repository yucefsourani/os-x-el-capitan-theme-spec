%global debug_package %{nil}
Name:           os-x-el-capitan-theme
Version:        0.9
Release:        1%{?dist}
Summary:        OS X Theme for Cinnamon and GTK 3.0 Desktops. If unsatisfied with GTK 3 theming
Group:		User Interface/Desktops
License:        GPLv3
URL:            https://www.gnome-look.org/p/1013490/
Source0:        https://dl.opendesktop.org/api/files/download/id/1474234465/OS.X.El.Capitan.v%{version}.tar.gz
BuildArch:	noarch
Requires:	filesystem
Requires:       gtk-murrine-engine

%description
OS X Theme for Cinnamon and GTK 3.0 Desktops. If unsatisfied with GTK 3 theming


%prep
%setup -n "OS X El Capitan"
%{__rm} Wallpaper.jpg

%build



%install
rm -rf $RPM_BUILD_ROOT
%{__mkdir} -p %{buildroot}%{_datadir}/themes/%{name}
%{__cp} -rf * %{buildroot}%{_datadir}/themes/%{name}



%files
%doc CREDITS
%doc README.md
%{_datadir}/themes/%{name}



%changelog
* Mon Sep 19 2016 yucef
- 
