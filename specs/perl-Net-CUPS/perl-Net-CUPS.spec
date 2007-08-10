# $Id$
# Authority: dag
# Upstream: D. Hageman <dhageman$dracken,com>

%define perl_vendorlib %(eval "`%{__perl} -V:installvendorlib`"; echo $installvendorlib)
%define perl_vendorarch %(eval "`%{__perl} -V:installvendorarch`"; echo $installvendorarch)

%define real_name Net-CUPS

Summary: Perl module that implements a Common Unix Printing System Interface
Name: perl-Net-CUPS
Version: 0.51
Release: 1
License: Artistic/GPL
Group: Applications/CPAN
URL: http://search.cpan.org/dist/Net-CUPS/

Source: http://www.cpan.org/modules/by-module/Net/Net-CUPS-%{version}.tar.gz
BuildRoot: %{_tmppath}/%{name}-%{version}-%{release}-root

BuildRequires: perl

%description
perl-Net-CUPS is a Perl module that implements a Perl module implements
a Common Unix Printing System Interface.

%prep
%setup -n %{real_name}-%{version}

%build
CFLAGS="%{optflags}" %{__perl} Makefile.PL INSTALLDIRS="vendor" PREFIX="%{buildroot}%{_prefix}"
%{__make} %{?_smp_mflags} OPTIMIZE="%{optflags}"

%install
%{__rm} -rf %{buildroot}
%{__make} pure_install

### Clean up buildroot
find %{buildroot} -name .packlist -exec %{__rm} {} \;

%clean
%{__rm} -rf %{buildroot}

%files
%defattr(-, root, root, 0755)
%doc Changes MANIFEST README TODO
%doc %{_mandir}/man3/*.3pm*
%dir %{perl_vendorarch}/Net/
%{perl_vendorarch}/Net/CUPS/
%{perl_vendorarch}/Net/CUPS.pm
%dir %{perl_vendorarch}/auto/Net/
%{perl_vendorarch}/auto/Net/CUPS/

%changelog
* Sat Aug 04 2007 Dag Wieers <dag@wieers.com> - 0.51-1
- Initial package. (using DAR)