Summary:	Constraint-based lexical selection module
Summary(pl.UTF-8):	Moduł selekcji leksykalnej opartej na ograniczeniach
Name:		apertium-lex-tools
Version:	0.1.0
%define	snap	20130521
Release:	0.%{snap}.1
License:	GPL v2+
Group:		Applications/Text
# svn co http://apertium.svn.sourceforge.net/svnroot/apertium/trunk/apertium-lex-tools
Source0:	%{name}-r44914.tar.xz
# Source0-md5:	fb312984f9af2bf4c70db947a9bb0cc6
URL:		http://apertium.sourceforge.net/
BuildRequires:	apertium-devel >= 3.2.0
BuildRequires:	autoconf >= 2.61
BuildRequires:	automake
BuildRequires:	libstdc++-devel
BuildRequires:	libxml2-devel >= 1:2.6.17
BuildRequires:	lttoolbox-devel >= 3.2.0-2.svn20130412
BuildRequires:	pkgconfig
Requires:	apertium >= 3.2.0
Requires:	libxml2 >= 1:2.6.17
Requires:	lttoolbox >= 3.2.0-2.svn20130412
BuildRoot:	%{tmpdir}/%{name}-%{version}-root-%(id -u -n)

%description
Constraint-based lexical selection module.

%description -l pl.UTF-8
Moduł selekcji leksykalnej opartej na ograniczeniach.

%prep
%setup -q -n %{name}

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
