Summary:	Constraint-based lexical selection module
Summary(pl.UTF-8):	Moduł selekcji leksykalnej opartej na ograniczeniach
Name:		apertium-lex-tools
Version:	0.2.1
Release:	1
License:	GPL v2+
Group:		Applications/Text
Source0:	http://downloads.sourceforge.net/apertium/%{name}-%{version}.tar.gz
# Source0-md5:	7b13266bb29fcbc61a73c4e74d047cfa
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

%build
%{__aclocal}
%{__autoconf}
%{__autoheader}
%{__automake}
%configure
%{__make}

%install
rm -rf $RPM_BUILD_ROOT

%{__make} install \
	DESTDIR=$RPM_BUILD_ROOT

%clean
rm -rf $RPM_BUILD_ROOT

%files
%defattr(644,root,root,755)
%doc AUTHORS README README.yasmet TODO
%attr(755,root,root) %{_bindir}/lrx-comp
%attr(755,root,root) %{_bindir}/lrx-proc
%attr(755,root,root) %{_bindir}/multitrans
