#
# Conditional build:
%bcond_without	tests	# don't perform "make test"
#
%include	/usr/lib/rpm/macros.perl
%define		pdir	Filesys
%define		pnam	SmbClientParser
Summary:	Filesys::SmbClientParser - Perl client to reach Samba ressources with smbclient
Summary(pl):	Filesys::SmbClientParser - klient perlowy zasobów Samby korzystaj±cy z smbclienta
Name:		perl-Filesys-SmbClientParser
Version:	2.7
Release:	2
License:	unknown
Group:		Development/Languages/Perl
Source0:	http://www.cpan.org/modules/by-module/%{pdir}/%{pdir}-%{pnam}-%{version}.tar.gz
# Source0-md5:	16f73fb28db6e2d7f97690f01f6c1bd0
Patch0:		%{name}-notest.patch
BuildRequires:	rpm-perlprov >= 4.1-13
BuildRequires:	perl-devel >= 1:5.8.0
Requires:	samba-client
%if %{with tests}
BuildRequires:	samba-client
%endif
BuildArch:	noarch
BuildRoot:	%{tmpdir}/%{name}-%{version}-root-%(id -u -n)

%description
Filesys::SmbClientParser module is a Perl client to reach Samba
ressources.  SmbClientParser works with output of bin smbclient, so
it doesn't work on Win* platforms (but query of Win* platform works
of course).

%description -l pl
Modu³ Filesys::SmbClientParser jest perlowym klientem zasobów Samby.
SmbClientParser dzia³a na wyj¶ciu programu smbclient, wiêc nie bêdzie
dzia³aæ na platformach Win* (jednak¿e ³±czenie sie z serwerem Win*
oczywi¶cie dzia³a).

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
