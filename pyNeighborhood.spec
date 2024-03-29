Summary:	A GTK+2 GUI for samba tools
Summary(pl.UTF-8):	Graficzny interfejs GTK+ dla narzędzi samby
Name:		pyNeighborhood
Version:	0.4
Release:	0.9
License:	GPL v2
Group:		X11/Applications/Networking
Source0:	http://dl.sourceforge.net/pyneighborhood/%{name}-%{version}.tar.gz
# Source0-md5:	1cecae28bb5753f39fb0b6a9a0f5364e
URL:		http://pyneighborhood.sourceforge.net/
BuildRequires:	python >= 1:2.3
BuildRequires:	which
Requires:	python >= 1:2.3
Requires:	python-pygtk-gtk >= 1:2.6.0
Requires:	samba-client >= 3.0.0
BuildRoot:	%{tmpdir}/%{name}-%{version}-root-%(id -u -n)

%description
pyNeighborhood is GTK+ 2 rewrite of a well-known GTK+ 1 tool
LinNeighborhood (using pyGTK), so it is the GUI frontend for samba
tools, such as smbclient, smbmount etc. It's written in Python and
uses the GTK+ 2 toolkit with pyGTK implementation.

%description -l pl.UTF-8
pyNeighborhood to przepisane do GTK+ 2 szeroko znane narzędzie
LinNeighborhood (używając pyGTK), czyli interfejs graficzny dla
narzędzi samby, takich jak smbclient, smbmount itp. Jest napisane w
Pythonie i używa GTK+ 2 wraz z implementacją pyGTK.

%prep
%setup -q

%build
./configure \
	--prefix=%{_prefix}
%{__make}

%install
rm -rf $RPM_BUILD_ROOT

%{__make} install \
	DESTDIR=$RPM_BUILD_ROOT

%clean
rm -rf $RPM_BUILD_ROOT

%files
%defattr(644,root,root,755)
%doc APPINFO Changelog README TODO
%attr(755,root,root) %{_bindir}/*
%{_desktopdir}/pyNeighborhood.desktop
%dir %{_datadir}/pyNeighborhood
%{_datadir}/pyNeighborhood/icons
%dir %{_datadir}/pyNeighborhood/src
%{_datadir}/pyNeighborhood/src/*.pyc
