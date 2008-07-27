#
# Conditional build:
%bcond_without	tests	# do perform "make test"
#
%include	/usr/lib/rpm/macros.perl
%define		pdir	Devel
%define		pnam	Caller-Perl
Summary:	Devel::Caller::Perl - allow method to get arguments passed to higher subroutines
Summary(pl.UTF-8):	Devel::Caller::Perl - umożliwienie metodzie pobranie argumentów z wyższych funkcji
Name:		perl-Devel-Caller-Perl
Version:	1.4
Release:	2
# same as perl
License:	GPL v1+ or Artistic
Group:		Development/Languages/Perl
Source0:	http://www.cpan.org/modules/by-module/%{pdir}/%{pdir}-%{pnam}-%{version}.tar.gz
# Source0-md5:	ef4407ab5c506e4daa63ee1496b5872f
BuildRequires:	perl-Module-Build >= 0.21-2
BuildRequires:	perl-devel >= 1:5.8.0
BuildRequires:	rpm-perlprov >= 4.1-13
%if %{with tests}
BuildRequires:	perl-Test-Simple
%endif
BuildArch:	noarch
BuildRoot:	%{tmpdir}/%{name}-%{version}-root-%(id -u -n)

%description
Devel::Caller::Perl Perl module allows a method to get arguments
passed to subroutines higher up in the call stack.

%description -l pl.UTF-8
Moduł Perla Devel::Caller::Perl pozwala metodzie odczytać argumenty
przekazane do funkcji wyżej w stosie wywołań.

%prep
%setup -q -n %{pdir}-%{pnam}-%{version}

%build
%{__perl} Build.PL \
	installdirs=vendor \
	destdir=$RPM_BUILD_ROOT
./Build

%{?with_tests:./Build test}

%install
rm -rf $RPM_BUILD_ROOT

./Build install

%clean
rm -rf $RPM_BUILD_ROOT

%files
%defattr(644,root,root,755)
%dir %{perl_vendorlib}/Devel/Caller
%{perl_vendorlib}/Devel/Caller/Perl.pm
%{_mandir}/man3/*
