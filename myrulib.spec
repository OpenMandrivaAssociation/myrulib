#
# this file based on spec file for package myrulib (Version 0.27)
#
# Copyright (c) 2009-2011 Denis Kandrashin, Kyrill Detinov
# This file and all modifications and additions to the pristine
# package are under the same license as the package itself.
#

Name:           myrulib
Version:        0.29.8
Release:        1
License:        GPLv3
Summary:        E-Book Library Manager
URL:            http://myrulib.lintest.ru
Group:          Office
Source0:        http://www.lintest.ru/pub/%{name}-%{version}.tar.bz2
BuildRequires:  libicu-devel
BuildRequires:  libxml2-devel
BuildRequires:  wxgtku2.8-devel >= 2.8.10
BuildRequires:  bzip2-devel

%description
MyRuLib is an application for organizing your own collection of e-books.

Authors:
--------
    Denis Kandrashin <mail@lintest.ru>

%prep
%setup -q
[ ! -x configure ] && %{__chmod} +x configure
chmod -R a+r .

%build
%configure \
    --with-icu \
    --without-strip
%make

%install
%makeinstall_std
%find_lang %{name}

%files -f %{name}.lang
%{_bindir}/%{name}
%{_datadir}/applications/%{name}.desktop
%{_datadir}/icons/hicolor/*/*/%{name}.png
%{_datadir}/pixmaps/%{name}.png
%doc AUTHORS README


%changelog
* Sun Jun 10 2012 Dmitry Mikhirev <dmikhirev@mandriva.org> 0.29.8-1
+ Revision: 804325
- update to 0.29.8

* Thu Jan 19 2012 Dmitry Mikhirev <dmikhirev@mandriva.org> 0.28.13-1
+ Revision: 762401
- imported package myrulib

