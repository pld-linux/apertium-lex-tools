#
# TODO: deval and static subpackages?
#
Summary:	Constraint-based lexical selection module
Summary(pl.UTF-8):	Moduł selekcji leksykalnej opartej na ograniczeniach
Name:		apertium-lex-tools
Version:	0.5.0
Release:	2
License:	GPL v2+
Group:		Applications/Text
Source0:	https://github.com/apertium/apertium-lex-tools/archive/v%{version}/%{name}-%{version}.tar.gz
# Source0-md5:	c37d536c2ac823b50f660b83382625d1
URL:		http://apertium.sourceforge.net/
BuildRequires:	apertium-devel >= 3.3.0
BuildRequires:	autoconf >= 2.61
BuildRequires:	automake
BuildRequires:	libstdc++-devel
BuildRequires:	libxml2-devel >= 1:2.6.17
BuildRequires:	lttoolbox-devel >= 3.3.0
BuildRequires:	pkgconfig
Requires:	apertium >= 3.3.0
Requires:	libxml2 >= 1:2.6.17
Requires:	lttoolbox >= 3.3.0
BuildRoot:	%{tmpdir}/%{name}-%{version}-root-%(id -u -n)

%description
Constraint-based lexical selection module.

%description -l pl.UTF-8
Moduł selekcji leksykalnej opartej na ograniczeniach.

%prep
%setup -q

%{__sed} -E -i -e '1s,#!\s*/usr/bin/env\s+bash(\s|$),#!/bin/bash\1,' \
      src/validate-lrx.sh

%build
%{__libtoolize}
%{__aclocal}
%{__autoconf}
%{__automake}
%configure
%{__make}

%install
rm -rf $RPM_BUILD_ROOT

%{__make} install \
	DESTDIR=$RPM_BUILD_ROOT

%{__rm} $RPM_BUILD_ROOT%{_libdir}/libapertium-lex-tools.la

%clean
rm -rf $RPM_BUILD_ROOT

%files
%defattr(644,root,root,755)
%doc AUTHORS README TODO
%attr(755,root,root) %{_bindir}/lrx-comp
%attr(755,root,root) %{_bindir}/lrx-proc
%attr(755,root,root) %{_bindir}/multitrans
%attr(755,root,root) %{_bindir}/apertium-validate-lrx
%attr(755,root,root) %{_bindir}/process-tagger-output
%ghost %{_libdir}/libapertium-lex-tools.so.1
%{_libdir}/libapertium-lex-tools.so.*.*.*
%dir %{_datadir}/apertium-lex-tools
%{_datadir}/apertium-lex-tools/*.py
%{_datadir}/apertium-lex-tools/lrx.dtd

#%{_libdir}/libapertium-lex-tools.so
#%{_includedir}/apertium-lex-tools
#%{_pkgconfigdir}/apertium-lex-tools.pc
#%{_libdir}/libapertium-lex-tools.a
