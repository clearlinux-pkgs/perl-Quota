#
# This file is auto-generated. DO NOT EDIT
# Generated by: autospec.py
# Using build pattern: cpan
#
Name     : perl-Quota
Version  : 1.8.2
Release  : 30
URL      : https://cpan.metacpan.org/authors/id/T/TO/TOMZO/Quota-1.8.2.tar.gz
Source0  : https://cpan.metacpan.org/authors/id/T/TO/TOMZO/Quota-1.8.2.tar.gz
Source1  : http://http.debian.net/debian/pool/main/libq/libquota-perl/libquota-perl_1.7.2+dfsg-1.debian.tar.xz
Summary  : Quota - Perl interface to file system quotas
Group    : Development/Tools
License  : Artistic-1.0-Perl GPL-2.0
Requires: perl-Quota-license = %{version}-%{release}
Requires: perl-Quota-perl = %{version}-%{release}
BuildRequires : buildreq-cpan
BuildRequires : libtirpc-dev
# Suppress stripping binaries
%define __strip /bin/true
%define debug_package %{nil}

%description
Quota extension module for Perl
-------------------------------
Author:    T. Zoerner (tomzo AT users.sourceforge.net)

%package dev
Summary: dev components for the perl-Quota package.
Group: Development
Provides: perl-Quota-devel = %{version}-%{release}
Requires: perl-Quota = %{version}-%{release}

%description dev
dev components for the perl-Quota package.


%package license
Summary: license components for the perl-Quota package.
Group: Default

%description license
license components for the perl-Quota package.


%package perl
Summary: perl components for the perl-Quota package.
Group: Default
Requires: perl-Quota = %{version}-%{release}

%description perl
perl components for the perl-Quota package.


%prep
%setup -q -n Quota-1.8.2
cd %{_builddir}
tar xf %{_sourcedir}/libquota-perl_1.7.2+dfsg-1.debian.tar.xz
cd %{_builddir}/Quota-1.8.2
mkdir -p deblicense/
cp -r %{_builddir}/debian/* %{_builddir}/Quota-1.8.2/deblicense/

%build
export http_proxy=http://127.0.0.1:9/
export https_proxy=http://127.0.0.1:9/
export no_proxy=localhost,127.0.0.1,0.0.0.0
export LANG=C.UTF-8
if test -f Makefile.PL; then
%{__perl} -I. Makefile.PL
make  %{?_smp_mflags}
else
%{__perl} Build.PL
./Build
fi

%check
export LANG=C.UTF-8
export http_proxy=http://127.0.0.1:9/
export https_proxy=http://127.0.0.1:9/
export no_proxy=localhost,127.0.0.1,0.0.0.0
make TEST_VERBOSE=1 test

%install
rm -rf %{buildroot}
mkdir -p %{buildroot}/usr/share/package-licenses/perl-Quota
cp %{_builddir}/debian/copyright %{buildroot}/usr/share/package-licenses/perl-Quota/d2d1cc40adf3aefa74839be703dd77c631f1f1fd || :
if test -f Makefile.PL; then
make pure_install PERL_INSTALL_ROOT=%{buildroot} INSTALLDIRS=vendor
else
./Build install --installdirs=vendor --destdir=%{buildroot}
fi
find %{buildroot} -type f -name .packlist -exec rm -f {} ';'
find %{buildroot} -depth -type d -exec rmdir {} 2>/dev/null ';'
find %{buildroot} -type f -name '*.bs' -empty -exec rm -f {} ';'
%{_fixperms} %{buildroot}/*

%files
%defattr(-,root,root,-)

%files dev
%defattr(-,root,root,-)
/usr/share/man/man3/Quota.3

%files license
%defattr(0644,root,root,0755)
/usr/share/package-licenses/perl-Quota/d2d1cc40adf3aefa74839be703dd77c631f1f1fd

%files perl
%defattr(-,root,root,-)
/usr/lib/perl5/*
