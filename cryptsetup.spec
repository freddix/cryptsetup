Summary:	LUKS for dm-crypt implemented in cryptsetup
Name:		cryptsetup
Version:	1.6.3
Release:	2
License:	GPL
Group:		Base
Source0:	http://cryptsetup.googlecode.com/files/%{name}-%{version}.tar.bz2
# Source0-md5:	a7aeb549a543eeac433eadfb6bc67837
URL:		http://code.google.com/p/cryptsetup/
BuildRequires:	autoconf
BuildRequires:	automake
BuildRequires:	device-mapper-devel
BuildRequires:	gettext-devel
BuildRequires:	libgcrypt-devel
BuildRequires:	libuuid-devel
BuildRequires:	popt-devel
BuildRequires:	libtool
Requires:	%{name}-libs = %{version}-%{release}
BuildRoot:	%{tmpdir}/%{name}-%{version}-root-%(id -u -n)

%description
LUKS is the upcoming standard for Linux hard disk encryption. By
providing a standard on-disk-format, it does not only facilitate
compatibility among distributions, but also provide secure management
of multiple user passwords. In contrast to existing solution, LUKS
stores all setup necessary setup information in the partition header,
enabling the user to transport or migrate his data seamlessly.

This package contains implementation of LUKS for dm-crypt implemented
in cryptsetup.

%package libs
Summary:	Cryptsetup library
Group:		Libraries

%description libs
Cryptsetup library.

%package devel
Summary:	Header files for cryptsetup library
Group:		Development/Libraries
Requires:	%{name}-libs = %{version}-%{release}
Requires:	libgcrypt-devel
Requires:	libgpg-error-devel
Requires:	pkgconfig(uuid)

%description devel
Header files for cryptsetup library.

%prep
%setup -q

%build
%{__gettextize}
%{__libtoolize}
%{__autoheader}
%{__aclocal} -I m4
%{__autoconf}
%{__automake}
%configure
%{__make}

%install
rm -rf $RPM_BUILD_ROOT

%{__make} install \
	DESTDIR=$RPM_BUILD_ROOT

%find_lang %{name}

%clean
rm -rf $RPM_BUILD_ROOT

%post	-p /usr/sbin/ldconfig
%postun	-p /usr/sbin/ldconfig

%files -f %{name}.lang
%defattr(644,root,root,755)
%doc ChangeLog
%attr(755,root,root) %{_sbindir}/cryptsetup
%attr(755,root,root) %{_sbindir}/veritysetup
%{_mandir}/man8/*

%files libs
%defattr(644,root,root,755)
%attr(755,root,root) %ghost %{_libdir}/libcryptsetup.so.?
%attr(755,root,root) %{_libdir}/libcryptsetup.so.*.*.*

%files devel
%defattr(644,root,root,755)
%attr(755,root,root) %{_libdir}/libcryptsetup.so
%{_includedir}/*.h
%{_pkgconfigdir}/*.pc

