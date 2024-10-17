#
# this file based on spec file for package myrulib (Version 0.27)
#
# Copyright (c) 2009-2011 Denis Kandrashin, Kyrill Detinov
# This file and all modifications and additions to the pristine
# package are under the same license as the package itself.
#

Name:           myrulib
Version:        0.29.16
Release:        2
License:        GPLv3
Summary:        E-Book Library Manager
URL:            https://myrulib.lintest.ru
Group:          Office
Source0:        http://www.lintest.ru/pub/%{name}-%{version}.tar.bz2
BuildRequires:  pkgconfig(icu-i18n)
BuildRequires:  pkgconfig(libxml-2.0)
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
