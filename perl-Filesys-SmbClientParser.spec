#
# Conditional build:
%bcond_without	tests # don't perform "make test"
#
%include	/usr/lib/rpm/macros.perl
%define	pdir	Filesys
%define	pnam	SmbClientParser
Summary:	Filesys::SmbClientParser Perl module
Summary(cs):	Modul Filesys::SmbClientParser pro Perl
Summary(da):	Perlmodul Filesys::SmbClientParser
Summary(de):	Filesys::SmbClientParser Perl Modul
Summary(es):	Módulo de Perl Filesys::SmbClientParser
Summary(fr):	Module Perl Filesys::SmbClientParser
Summary(it):	Modulo di Perl Filesys::SmbClientParser
Summary(ja):	Filesys::SmbClientParser Perl ¥â¥¸¥å¡¼¥ë
Summary(ko):	Filesys::SmbClientParser ÆÞ ¸ðÁÙ
Summary(nb):	Perlmodul Filesys::SmbClientParser
Summary(pl):	Modu³ Perla Filesys::SmbClientParser
Summary(pt):	Módulo de Perl Filesys::SmbClientParser
Summary(pt_BR):	Módulo Perl Filesys::SmbClientParser
Summary(ru):	íÏÄÕÌØ ÄÌÑ Perl Filesys::SmbClientParser
Summary(sv):	Filesys::SmbClientParser Perlmodul
Summary(uk):	íÏÄÕÌØ ÄÌÑ Perl Filesys::SmbClientParser
Summary(zh_CN):	Filesys::SmbClientParser Perl Ä£¿é
Name:		perl-Filesys-SmbClientParser
Version:	2.6
Release:	1
License:	GPL
Group:		Development/Languages/Perl
Source0:	http://www.cpan.org/modules/by-module/%{pdir}/%{pdir}-%{pnam}-%{version}.tar.gz
# Source0-md5:	d83747e968ba2d91a847f29d8a8dffbe
Patch0:		%{name}-notest.patch
BuildRequires:	rpm-perlprov >= 4.1-13
BuildRequires:	perl-devel >= 5.6
Requires:	samba-client
%if %{with tests}
BuildRequires:	samba-client
%endif
BuildArch:	noarch
BuildRoot:	%{tmpdir}/%{name}-%{version}-root-%(id -u -n)

%description
Filesys::SmbClientParser - use smbclient.

%description -l pl
Filesys::SmbClientParser - u¿ywa smbclient.

%prep
%setup -q -n %{pdir}-%{pnam}-%{version}
%patch0 -p1

%build
%{__perl} Makefile.PL \
	INSTALLDIRS=vendor
%{__make}
%{?with_tests:%{__make} test}

%install
rm -rf $RPM_BUILD_ROOT

%{__make} install \
	DESTDIR=$RPM_BUILD_ROOT

%clean
rm -rf $RPM_BUILD_ROOT

%files
%defattr(644,root,root,755)
%doc README Changes
%{perl_vendorlib}/Filesys/*.pm
%{_mandir}/man3/*
