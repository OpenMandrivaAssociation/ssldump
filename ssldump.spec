%define name	ssldump
%define version 0.9
%define realversion 0.9b3
%define release %mkrel 0.beta3.10


Name:		%{name}
Summary:	SSLv3/TLS network protocol analyzer
Version:	%{version}
Release:	%{release}
URL:		http://www.rtfm.com/ssldump/
Source0:	%{name}-%{realversion}.tar.bz2
Patch0:		ssldump_wrong_includes.patch.bz2
Patch1:		ssldump-openssl.patch.bz2

License:	BSD style
Group:		Monitoring

Requires:	openssl

BuildRequires:	openssl-devel, libpcap-devel
BuildRoot:	%{_tmppath}/%{name}-%{version}-%{release}-buildroot


%description
Ssldump is a SSLv3/TLS network protocol analyzer. It identifies TCP
connections on the chosen network interface and attempts to interpret
them as SSLv3/TLS traffic, it decodes the records and displays them in
a textual form to stdout. If provided with the appropriate keying
material, it will also decrypt the connections and display the
application data traffic.

This product includes software developed by Eric Rescorla for RTFM,
Inc.


%prep
rm -Rf $RPM_BUILD_ROOT

%setup -n %name-%realversion

%patch0 -p1
%patch1 -p0

%build
%configure --with-pcap-lib=%{_libdir} --with-openssl-lib=%{_libdir}
%make


%install
mkdir -p $RPM_BUILD_ROOT%{_sbindir}
install ssldump $RPM_BUILD_ROOT%{_sbindir}/ssldump
mkdir -p $RPM_BUILD_ROOT%{_mandir}/man1
install --mode=0644 ssldump.1 $RPM_BUILD_ROOT%{_mandir}/man1/ssldump.1


%clean
rm -rf $RPM_BUILD_ROOT


%files
%defattr(-, root, root, 0755)
%doc ChangeLog COPYRIGHT CREDITS README
%{_mandir}/man1/ssldump.1*
%{_sbindir}/ssldump


