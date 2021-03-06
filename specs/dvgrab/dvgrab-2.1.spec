# $Id: dvgrab.spec 4303 2006-04-18 22:05:03Z dries $
# Authority: dag
# Upstream: Dan Dennedy <ddennedy$users,sourceforge,net>

### EL5 ships with dvgrab dvgrab-2.0-1.2.2
# ExclusiveDist: el2 rh7 el3 el4

Summary: DV grabber through the FireWire interface
Name: dvgrab
Version: 2.1
Release: 1
License: GPL
Group: Applications/Multimedia
URL: http://kino.schirmacher.de/

Source: http://dl.sf.net/sourceforge/kino/dvgrab-%{version}.tar.gz
BuildRoot: %{_tmppath}/%{name}-%{version}-%{release}-root

BuildRequires: libraw1394-devel >= 1.1.0, libavc1394-devel, libdv-devel
BuildRequires: libquicktime-devel, libjpeg-devel, libpng-devel
BuildRequires: libogg-devel, libvorbis-devel, a52dec-devel, libmpeg3-devel
BuildRequires: gcc-c++
Requires: kernel >= 2.4.0

%description
Dvgrab is a command line driven soft that grab AVI-2 films from a DV camera
using the IEEE-1394 bus (aka FireWire).
DV stand for Digital Video and is the name of the new numeric camera
generation.

%prep
%setup

%build
%configure
%{__make} %{?_smp_mflags}

%install
%{__rm} -rf %{buildroot}
%{__make} install DESTDIR="%{buildroot}"

%clean
%{__rm} -rf %{buildroot}

%files
%defattr(-, root, root, 0755)
%doc AUTHORS ChangeLog COPYING README TODO
%doc %{_mandir}/man1/dvgrab.1*
%{_bindir}/dvgrab

%changelog
* Mon Jan 15 2006 Dag Wieers <dag@wieers.com> - 2.1-1
- Updated to release 2.1.

* Tue Jul 27 2004 Matthias Saou <http://freshrpms.net> 1.6-1
- Update to 1.6.

* Tue Jun 22 2004 Matthias Saou <http://freshrpms.net> 1.5-3
- Added missing build requirements to obtain a full-featured package.

* Sun Apr 11 2004 Dag Wieers <dag@wieers.com> - 1.5-2
- Rebuild against libdv 0.102.

* Tue Mar 23 2004 Dag Wieers <dag@wieers.com> - 1.5-1
- Updated to release 1.5.

* Wed Dec 17 2003 Dag Wieers <dag@wieers.com> - 1.4-0
- Initial package. (using DAR)

