# $Id$
# Authority: dag
# Upstream: Zack Smith <fbui$comcast,net>

Summary: Artificial benchmark for measuring memory bandwidth
Name: bandwidth
Version: 0.12
Release: 1
License: GPL
Group: Applications/Internet
URL: http://home.comcast.net/~fbui/bandwidth.html

Source: http://home.comcast.net/~fbui/bandwidth-%{version}.tar.gz
BuildRoot: %{_tmppath}/%{name}-%{version}-%{release}-root

%description
bandwidth is an artificial benchmark for measuring memory bandwidth,
useful for identifying a computer's weak areas.

%prep
%setup

%build
%{__make} %{?_smp_mflags} CFLAGS="%{optflags}"

%install
%{__rm} -rf %{buildroot}
#%{__make} install DESTDIR="%{buildroot}"
%{__install} -Dp -m0755 bandwidth %{buildroot}%{_bindir}/bandwidth

%clean
%{__rm} -rf %{buildroot}

%files
%defattr(-, root, root, 0755)
%doc COPYING README
%{_bindir}/bandwidth

%changelog
* Sat Jul 28 2007 Dag Wieers <dag@wieers.com> - 0.12-1
- Initial package. (using DAR)