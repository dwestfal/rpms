# $Id$
# Authority: dag
# Upstream: Don Owens <dowens$cpan,org>

%define perl_vendorlib %(eval "`%{__perl} -V:installvendorlib`"; echo $installvendorlib)
%define perl_vendorarch %(eval "`%{__perl} -V:installvendorarch`"; echo $installvendorarch)

%define real_name JSON-DWIW

Summary: Perl module that implements a JSON converter that Does What I Want
Name: perl-JSON-DWIW
Version: 0.13
Release: 1
License: Artistic/GPL
Group: Applications/CPAN
URL: http://search.cpan.org/dist/JSON-DWIW/

Source: http://www.cpan.org/authors/id/D/DO/DOWENS/JSON-DWIW-%{version}.tar.gz
BuildRoot: %{_tmppath}/%{name}-%{version}-%{release}-root

BuildRequires: perl

%description
perl-JSON-DWIW is a Perl module that implements a JSON converter that
Does What I Want.

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
%doc INSTALL META.yml README
%doc %{_mandir}/man3/JSON::DWIW.3pm*
%doc %{_mandir}/man3/JSON::DWIW::Boolean.3pm*
#%doc %{_mandir}/man3/*.3pm*
%dir %{perl_vendorarch}/JSON/
%{perl_vendorarch}/JSON/DWIW/
%{perl_vendorarch}/JSON/DWIW.pm
%dir %{perl_vendorarch}/auto/JSON/
%{perl_vendorarch}/auto/JSON/DWIW/

%changelog
* Sun Aug 05 2007 Dag Wieers <dag@wieers.com> - 0.13-1
- Initial package. (using DAR)