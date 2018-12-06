#
# This file is auto-generated. DO NOT EDIT
# Generated by: autospec.py
#
Name     : perl-Quota
Version  : 1.7.2
Release  : 8
URL      : https://cpan.metacpan.org/authors/id/T/TO/TOMZO/Quota-1.7.2.tar.gz
Source0  : https://cpan.metacpan.org/authors/id/T/TO/TOMZO/Quota-1.7.2.tar.gz
Source1  : http://http.debian.net/debian/pool/main/libq/libquota-perl/libquota-perl_1.7.2+dfsg-1.debian.tar.xz
Summary  : Quota - Perl interface to file system quotas
Group    : Development/Tools
License  : Artistic-1.0-Perl GPL-2.0
Requires: perl-Quota-lib = %{version}-%{release}
Requires: perl-Quota-license = %{version}-%{release}
BuildRequires : buildreq-cpan

%description
Quota extension module for Perl
-------------------------------
Author:    Tom Zoerner (tomzo AT users.sourceforge.net)

%package dev
Summary: dev components for the perl-Quota package.
Group: Development
Requires: perl-Quota-lib = %{version}-%{release}
Provides: perl-Quota-devel = %{version}-%{release}

%description dev
dev components for the perl-Quota package.


%package lib
Summary: lib components for the perl-Quota package.
Group: Libraries
Requires: perl-Quota-license = %{version}-%{release}

%description lib
lib components for the perl-Quota package.


%package license
Summary: license components for the perl-Quota package.
Group: Default

%description license
license components for the perl-Quota package.


%prep
%setup -q -n Quota-1.7.2
cd ..
%setup -q -T -D -n Quota-1.7.2 -b 1
mkdir -p deblicense/
mv %{_topdir}/BUILD/debian/* %{_topdir}/BUILD/Quota-1.7.2/deblicense/

%build
export http_proxy=http://127.0.0.1:9/
export https_proxy=http://127.0.0.1:9/
export no_proxy=localhost,127.0.0.1,0.0.0.0
export LANG=C
if test -f Makefile.PL; then
%{__perl} Makefile.PL
make  %{?_smp_mflags}
else
%{__perl} Build.PL
./Build
fi

%check
export LANG=C
export http_proxy=http://127.0.0.1:9/
export https_proxy=http://127.0.0.1:9/
export no_proxy=localhost,127.0.0.1,0.0.0.0
make TEST_VERBOSE=1 test

%install
rm -rf %{buildroot}
mkdir -p %{buildroot}/usr/share/package-licenses/perl-Quota
cp deblicense/copyright %{buildroot}/usr/share/package-licenses/perl-Quota/deblicense_copyright
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
/usr/lib/perl5/vendor_perl/5.28.1/x86_64-linux-thread-multi/Quota.pm
/usr/lib/perl5/vendor_perl/5.28.1/x86_64-linux-thread-multi/auto/Quota/autosplit.ix

%files dev
%defattr(-,root,root,-)
/usr/share/man/man3/Quota.3

%files lib
%defattr(-,root,root,-)
/usr/lib/perl5/vendor_perl/5.28.1/x86_64-linux-thread-multi/auto/Quota/Quota.so

%files license
%defattr(0644,root,root,0755)
/usr/share/package-licenses/perl-Quota/deblicense_copyright
