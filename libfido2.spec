%define major 1
%define libname %mklibname fido2
%define devname %mklibname fido2 -d

Summary:		FIDO2 library
Name:		libfido2
Version:		1.16.0
Release:		2
License:		BSD-2-Clause-Patent
Group:	Security
Url:		https://github.com/Yubico/%{name}
Source0:	https://developers.yubico.com/%{name}/Releases/%{name}-%{version}.tar.gz

BuildSystem:	cmake

BuildRequires:  gnupg2
BuildRequires:  cmake
BuildRequires:  make
BuildRequires:  pkgconfig(libcbor)
# Experimental
#BuildRequires:  pkgconfig(libpcsclite)
BuildRequires:  pkgconfig(libudev)
BuildRequires:  pkgconfig(openssl)
BuildRequires:  pkgconfig(zlib)

%description
%{name} is an open source library to support the FIDO2 protocol.  FIDO2 is
an open authentication standard that consists of the W3C Web Authentication
specification (WebAuthn API), and the Client to Authentication Protocol
(CTAP).  CTAP is an application layer protocol used for communication
between a client (browser) or a platform (operating system) with an external
authentication device (for example the Yubico Security Key).

#-----------------------------------------------------------------------------

%package -n %{libname}
Summary:	FIDO2 protocol support library
Group:		System/Libraries

%description -n %{libname}
This is an open source library to support the FIDO2 protocol.

%files -n %{libname}
%doc NEWS README.adoc
%license LICENSE
%{_libdir}/%{name}.so.%{major}*

#-----------------------------------------------------------------------------

%package -n %{devname}
Summary:	Development files for %{name}
Group:		Development/C
Requires:	%{libname} = %{EVRD}
Provides:	fido2-devel = %{EVRD}
Provides:	%{_lib}fido2-devel = %{EVRD}

%description -n %{devname}
Development files (Headers etc.) for %{name}.

%files -n %{devname}
%{_includedir}/fido/*.h
%{_includedir}/fido.h
%{_libdir}/%{name}.so
%{_libdir}/pkgconfig/%{name}.pc
%{_mandir}/man3/fido_*.3{,.*}
%{_mandir}/man3/eddsa_pk_*.3{,.*}
%{_mandir}/man3/es256_pk_*.3{,.*}
%{_mandir}/man3/es384_pk_*.3{,.*}
%{_mandir}/man3/rs256_pk_*.3{,.*}

#-----------------------------------------------------------------------------

%package -n fido2-tools
Summary:        FIDO2 tools
Group:	Security
Requires:	%{libname} = %{EVRD}

%description -n fido2-tools
FIDO2 command line tools to access and configure a FIDO2 compliant
authentication device.

%files -n fido2-tools
%{_bindir}/fido2-assert
%{_bindir}/fido2-cred
%{_bindir}/fido2-token
%{_mandir}/man1/fido2-assert.1{,.*}
%{_mandir}/man1/fido2-cred.1{,.*}
%{_mandir}/man1/fido2-token.1{,.*}

#-----------------------------------------------------------------------------

%prep
%autosetup -p1
