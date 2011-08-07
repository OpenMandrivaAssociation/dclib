%define name		dclib
%define	version		0.3.23
%define	release		%mkrel 1
%define	major		5
%define	libname		%mklibname dc %{major}
%define	develname	%mklibname -d dc
%define staticname	%mklibname -d -s dc


Name:		%{name}
Version:	%{version}
Release:	%{release}
Summary:	Direct Connect file sharing library
Group:		System/Libraries
License:	GPLv2+
URL:		http://sourceforge.net/projects/wxdcgui/
Source0:	http://dl.sourceforge.net/wxdcgui/%{name}-%{version}.tar.bz2
Patch1:		dclib-0.3.23-openssl.patch
BuildRequires:	libxml2-devel >= 2.0.0
BuildRequires:	openssl-devel
BuildRequires:	bzip2-devel
BuildRequires:	zlib-devel
BuildRequires:	autoconf
BuildRequires:	automake
BuildRoot:	%{_tmppath}/%{name}-%{version}


%description
This library implements the Direct Connect file sharing protocol.


%package -n %{libname}
Summary:	Direct Connect shared library
Group:		System/Libraries
#Requires:	%{name} = %{version}
Provides:	%{name} = %{version}-%{release}
#Provides:	%{libname} = %{version}-%{release}
#Obsoletes:	libdc  < 0.3.22
Obsoletes:	%{libname} < 0.3.22


%description -n %{libname}
The package contains the shared library required for running programs
based on dclib.


%package -n %{develname}
Summary:	Direct Connect developer files
Group:		Development/C++
BuildRequires:	pkgconfig >= 0.9.0
BuildRequires:	openssl-devel
Requires:	%{libname} = %{version}
Requires:	%{name} = %{version}
Requires:	libxml2-devel >= 2.0.0
Provides:	dc-devel = %{version}-%{release}
Provides:	%{name}-devel = %{version}-%{release}
#Provides:	%{develname} = %{version}-%{release}
Obsoletes:	dc-devel < 0.3.22
Obsoletes:	%{name}-devel < 0.3.22
#Obsoletes:	libdc-devel < 0.3.22
Obsoletes:	%{develname} < 0.3.22

%description -n %{develname}
The package contains the C++ headers and the libraries required to compile
programs based on dclib.


%package -n %{staticname}
Summary:	Static libraries for programs using the Direct Connect protocol
Group:		Development/C++
Requires:	%{develname} = %{version}
Requires:	%{name} = %{version}
Requires:	libxml2-devel >= 2.0.0
Provides:	dc-static-devel = %{version}-%{release}
Provides:	%{name}-static-devel = %{version}-%{release}
#Provides:	%{staticname} = %{version}-%{release}
#Obsoletes:	dc-devel < 0.3.22
#Obsoletes:	{name}-devel < 0.3.22
#Obsoletes:	libdc-devel < 0.3.22

%description -n %{staticname}
The package contains the libraries required to run programs statically
linked with dclib.


%prep
%setup -q -n %{name}-%{version}
%patch1 -p1 -b .openssl


%build
%configure2_5x --enable-static
%make
#configure --disable-static
#make {?_smp_mflags}


%install
rm -rf %{buildroot}
%makeinstall_std
#make install DESTDIR=%{buildroot}

# Remove an useless directory level (dclib-0.3) in the include path
mv %{buildroot}%{_includedir}/dclib-0.3/dclib %{buildroot}%{_includedir}
rmdir %{buildroot}%{_includedir}/dclib-0.3

# Not needed for Mdv >= 2009
#post -n {libname} -p /sbin/ldconfig
#postun -n {libname} -p /sbin/ldconfig


%clean
rm -rf %{buildroot}


%files -n %{libname}
%defattr(-,root,root)
%doc AUTHORS ChangeLog COPYING COPYING.OpenSSL INSTALL
# Neeeded?
#doc  dclib.lsm
# FC: {_libdir}/*.so.*
%{_libdir}/libdc.so.%{major}*

%files -n %{develname}
%defattr(-,root,root)
%doc HACKING NEWS README TODO
%dir %{_includedir}/%{name}
%{_includedir}/%{name}/*
%{_libdir}/libdc.so
%{_libdir}/pkgconfig/%{name}.pc

%files -n %{staticname}
%defattr(-,root,root)
%{_libdir}/libdc.a
%{_libdir}/libdc.la


