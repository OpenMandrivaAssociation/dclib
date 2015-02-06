%define name		dclib
%define	version		0.3.23
%define release		3
%define	major		5
%define	libname		%mklibname dc %{major}
%define	develname	%mklibname -d dc
%define staticname	%mklibname -d -s dc


Name:		%{name}
Version:		%{version}
Release:		%{release}
Summary:		Direct Connect file sharing library
Group:		System/Libraries
License:		GPLv2+
URL:		http://sourceforge.net/projects/wxdcgui/
Source0	:	http://dl.sourceforge.net/wxdcgui/%{name}-%{version}.tar.bz2
Patch1:		dclib-0.3.23-openssl.patch
Patch2:		dclib-0.3.23-glib.patch
BuildRequires:	pkgconfig(libxml-2.0)
BuildRequires:	pkgconfig(openssl)
BuildRequires:	bzip2-devel
BuildRequires:	pkgconfig(zlib)
BuildRequires:	autoconf
BuildRequires:	automake



%description
This library implements the Direct Connect file sharing protocol.


%package -n %{libname}
Summary:	Direct Connect shared library
Group:		System/Libraries
Provides:	%{name} = %{version}-%{release}
Obsoletes:	%{libname} < 0.3.22


%description -n %{libname}
The package contains the shared library required for running programs
based on dclib.


%package -n %{develname}
Summary:	Direct Connect developer files
Group:		Development/C++
BuildRequires:	pkgconfig >= 0.9.0
BuildRequires:	pkgconfig(openssl)
Requires:	%{libname} = %{version}
Requires:	%{name} = %{version}
Requires:	pkgconfig(libxml-2.0)
Provides:	dc-devel = %{version}-%{release}
Provides:	%{name}-devel = %{version}-%{release}
Obsoletes:	dc-devel < 0.3.22
Obsoletes:	%{name}-devel < 0.3.22
Obsoletes:	%{develname} < 0.3.22

%description -n %{develname}
The package contains the C++ headers and the libraries required to compile
programs based on dclib.


%package -n %{staticname}
Summary:	Static libraries for programs using the Direct Connect protocol
Group:		Development/C++
Requires:	%{develname} = %{version}
Requires:	%{name} = %{version}
Requires:	pkgconfig(libxml-2.0)
Provides:	dc-static-devel = %{version}-%{release}
Provides:	%{name}-static-devel = %{version}-%{release}


%description -n %{staticname}
The package contains the libraries required to run programs statically
linked with dclib.


%prep
%setup -q -n %{name}-%{version}
%patch1 -p1 -b .openssl
%patch2 -p0 -b .glib

%build
%configure2_5x --enable-static
%make



%install
%makeinstall_std
# Remove an useless directory level (dclib-0.3) in the include path
mv %{buildroot}%{_includedir}/dclib-0.3/dclib %{buildroot}%{_includedir}
rmdir %{buildroot}%{_includedir}/dclib-0.3

%files -n %{libname}
%doc AUTHORS ChangeLog COPYING COPYING.OpenSSL INSTALL
# Neeeded?
#doc  dclib.lsm
# FC: {_libdir}/*.so.*
%{_libdir}/libdc.so.%{major}*

%files -n %{develname}
%doc HACKING NEWS README TODO
%dir %{_includedir}/%{name}
%{_includedir}/%{name}/*
%{_libdir}/libdc.so
%{_libdir}/pkgconfig/%{name}.pc

%files -n %{staticname}
%{_libdir}/libdc.a





%changelog
* Sun Aug 07 2011 Andrey Bondrov <abondrov@mandriva.org> 0.3.23-1mdv2012.0
+ Revision: 693569
- imported package dclib


* Tue Dec 28 2010 Giovanni Mariani <mc2374@mclink.it> 0.3.23-69.1mib2010.2
- Ported to 2010.2 for MIB, from an old FC10 package
- Made sure to build static libraries
- Splitted the original devel package in devel and static-devel packages (see Wiki specs)
- Bump the major to match the library SONAME
- Made the libraries buildable and installable on both 32/64 archs
- Added BR for zlib (see README file in the sources)
- Added some version info for BR (see configure output)
- Made the BuildRoot tag Wiki spec compliant
- Made use of proper macros instead of the deprecated "$RPM_BUILD_ROOT" one
- Silenced some rpmlint warnings

* Tue Aug 25 2009 Tomas Mraz <tmraz@redhat.com> - 0.3.23-4
- rebuilt with new openssl

* Fri Jul 24 2009 Fedora Release Engineering <rel-eng@lists.fedoraproject.org> - 0.3.23-3
- Rebuilt for https://fedoraproject.org/wiki/Fedora_12_Mass_Rebuild

* Tue Feb 24 2009 Fedora Release Engineering <rel-eng@lists.fedoraproject.org> - 0.3.23-2
- Rebuilt for https://fedoraproject.org/wiki/Fedora_11_Mass_Rebuild

* Mon Feb 16 2009 Milos Jakubicek <xjakub@fi.muni.cz> - 0.3.23-1
- Update to 0.3.23
- Fixed license tag

* Wed Jan 28 2009 Milos Jakubicek <xjakub@fi.muni.cz> - 0.3.22-1
- Update to 0.3.22
- Many bugfixes, code cleanup etc.
- Upload slot changes
- Major feature changes (together with valknut) mentioned in NEWS from 0.3.11 to 0.3.21:
  0.3.20: Segment size adjustable, Download folders from search, Warnings about settings,
  0.3.19: More search results returned, Switching active/passive mode, StrongDC compatible encryption,
  Partial list uploads, Search window improvements, User list icon changes
  0.3.14: Nick tab completion improvements, Chat command improvements, Filelist storage changes, 
  Public hubs display improved, /rebuild command fixed and improved, Folder search results

* Thu Jan 15 2009 Tomas Mraz <tmraz@redhat.com> - 0.3.11-5
- rebuild with new openssl

* Fri Feb  8 2008 Luke Macken <lmacken@redhat.com> - 0.3.11-4
- Rebuild for gcc 4.3

* Wed Dec 05 2007 Release Engineering <rel-eng at fedoraproject dot org> - 0.3.11-3
- Rebuild for deps

* Wed Dec  5 2007 Luke Macken <lmacken@redhat.com> 0.3.11-2
- Rebuild

* Sun Oct 14 2007 Luke Macken <lmacken@redhat.com> 0.3.11-1
- 0.3.11
- Remove patches:
    01-dclib-0.3.10-remove-cmd4.patch
    02-dclib-0.3.10-use-gnulib-md5.patch
    03-dclib-0.3.10-use-new-md5-api.patch
    04-dclib-0.3.10-gnulib-md5-configure-test.patch

* Tue Sep 18 2007 Luke Macken <lmacken@redhat.com> 0.3.10-2
- Remove RSA MD5 implementation in favor of the gnulib implementation.  Patches
  taken from upstream ticket:
  https://sourceforge.net/tracker/?func=detail&atid=897767&aid=1796674&group_id=181579

* Tue Aug 27 2007 Luke Macken <lmacken@redhat.com> 0.3.10-1
- 0.3.10
- Update License to GPLv2
- Remove dclib-0.3.8-cconfig-use-cfile.patch

* Tue Apr 17 2007 Luke Macken <lmacken@redhat.com> 0.3.8-2
- Add dclib-0.3.8-cconfig-use-cfile.patch from Edward Sheldrake to fix
  rawhide build errors

* Mon Jan  3 2007 Luke Macken <lmacken@redhat.com> 0.3.8-1
- 0.3.8 from new upstream
- Remove patches:
    dclib-0.3.7-permissions.patch
    dclib-0.3.7-keylock.patch
    dclib-0.3.7-hashfix.patch

* Sun Sep  3 2006 Luke Macken <lmacken@redhat.com> 0.3.7-8
- Rebuild for FC6

* Sun Apr 20 2006 Luke Macken <lmacken@redhat.com> 0.3.7-7
- dclib-0.3.7-permissions.patch
  make valknut use the umask instead of hardcoded permissions
- dclib-0.3.7-keylock.patch
  fixes $Lock-parsing problem
- dclib-0.3.7-hashfix.patch
  fixes production of wrong hashes

* Mon Feb 13 2006 Luke Macken <lmacken@redhat.com> 0.3.7-6
- Rebuild for FE5

* Tue Dec 27 2005 Luke Macken <lmacken@redhat.com> 0.3.7-5
- Rebuild

* Thu Nov 10 2005 Luke Macken <lmacken@redhat.com> 0.3.7-4
- Rebuild for new openssl

* Mon Oct 03 2005 Luke Macken <lmacken@redhat.com> 0.3.7-3
- Add libxml2-devel to Requires

* Sun Oct 02 2005 Luke Macken <lmacken@redhat.com> 0.3.7-2
- Add documentation and license to package
- Set defattr and fix Requires in the devel package

* Thu Sep 29 2005 Luke Macken <lmacken@redhat.com> 0.3.7-1
- Packaged for Fedora Extras
