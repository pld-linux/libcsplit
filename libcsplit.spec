# m4/libcerror.m4
%define		libcerror_ver	20120425
Summary:	Library to support cross-platform C split string functions
Summary(pl.UTF-8):	Biblioteka wspierająca wieloplatformowe funkcje dzielenia łańcuchów w C
Name:		libcsplit
Version:	20190102
Release:	1
License:	LGPL v3+
Group:		Libraries
#Source0Download: https://github.com/libyal/libcsplit/releases
Source0:	https://github.com/libyal/libcsplit/releases/download/%{version}/%{name}-beta-%{version}.tar.gz
# Source0-md5:	099c4df3d879f4e72afdc93259d52ac7
URL:		https://github.com/libyal/libcsplit/
BuildRequires:	autoconf >= 2.59
BuildRequires:	automake >= 1.6
BuildRequires:	gettext-tools >= 0.18.1
BuildRequires:	libcerror-devel >= %{libcerror_ver}
BuildRequires:	libtool
BuildRequires:	pkgconfig
Requires:	libcerror >= %{libcerror_ver}
BuildRoot:	%{tmpdir}/%{name}-%{version}-root-%(id -u -n)

%description
libcsplit is a library to support cross-platform C split string
functions.

%description -l pl.UTF-8
libcsplit to biblioteka wspierająca wieloplatformowe funkcje dzielenia
łańcuchów w C.

%package devel
Summary:	Header files for libcsplit library
Summary(pl.UTF-8):	Pliki nagłówkowe biblioteki libcsplit
Group:		Development/Libraries
Requires:	%{name} = %{version}-%{release}
Requires:	libcerror-devel >= %{libcerror_ver}

%description devel
Header files for libcsplit library.

%description devel -l pl.UTF-8
Pliki nagłówkowe biblioteki libcsplit.

%package static
Summary:	Static libcsplit library
Summary(pl.UTF-8):	Statyczna biblioteka libcsplit
Group:		Development/Libraries
Requires:	%{name}-devel = %{version}-%{release}

%description static
Static libcsplit library.

%description static -l pl.UTF-8
Statyczna biblioteka libcsplit.

%prep
%setup -q

%build
%{__gettextize}
%{__libtoolize}
%{__aclocal} -I m4
%{__autoconf}
%{__autoheader}
%{__automake}
%configure
%{__make}

%install
rm -rf $RPM_BUILD_ROOT

%{__make} install \
	DESTDIR=$RPM_BUILD_ROOT

# obsoleted by pkg-config
%{__rm} $RPM_BUILD_ROOT%{_libdir}/libcsplit.la

%clean
rm -rf $RPM_BUILD_ROOT

%post	-p /sbin/ldconfig
%postun	-p /sbin/ldconfig

%files
%defattr(644,root,root,755)
%doc AUTHORS ChangeLog README
%attr(755,root,root) %{_libdir}/libcsplit.so.*.*.*
%attr(755,root,root) %ghost %{_libdir}/libcsplit.so.1

%files devel
%defattr(644,root,root,755)
%attr(755,root,root) %{_libdir}/libcsplit.so
%{_includedir}/libcsplit
%{_includedir}/libcsplit.h
%{_pkgconfigdir}/libcsplit.pc
%{_mandir}/man3/libcsplit.3*

%files static
%defattr(644,root,root,755)
%{_libdir}/libcsplit.a
