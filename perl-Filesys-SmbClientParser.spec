%include	/usr/lib/rpm/macros.perl
%define	pdir	Filesys
%define	pnam	SmbClientParser
Summary:	Filesys-SmbClientParser perl module
Summary(pl):	Modu³ perla Filesys-SmbClientParser
Name:		perl-Filesys-SmbClientParser
Version:	2.1
Release:	1
License:	GPL
Group:		Development/Languages/Perl
Source0:	ftp://ftp.cpan.org/pub/CPAN/modules/by-module/%{pdir}/%{pdir}-%{pnam}-%{version}.tar.gz
Patch0:		%{name}-notest.patch
BuildRequires:	rpm-perlprov >= 3.0.3-16
BuildRequires:	perl >= 5.6
Requires:	samba-client
BuildArch:	noarch
BuildRoot:	%{tmpdir}/%{name}-%{version}-root-%(id -u -n)

%description
Filesys-SmbClientParser - use smbclient.

%description -l pl
Filesys-SmbClientParser - u¿ywa smbclient.

%prep
%setup -q -n %{pdir}-%{pnam}-%{version}
%patch0 -p1

%build
perl Makefile.PL
%{__make}

%install
rm -rf $RPM_BUILD_ROOT

%{__make} install DESTDIR=$RPM_BUILD_ROOT

%clean
rm -rf $RPM_BUILD_ROOT

%files
%defattr(644,root,root,755)
%doc README Changes
%{perl_sitelib}/Filesys/*.pm
%{_mandir}/man3/*
