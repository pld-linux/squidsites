Summary:	squidsites - Squid reporting tool
Summary(pl):	squidsites - narzêdzie tworz±ce raporty Squida
Name:		squidsites
Version:	1.01
Release:	1
License:	GPL
Group:		Networking/Utilities
Source0:	http://www.stefanopassiglia.com/downloads/%{name}-%{version}.tgz
# Source0-md5:	6fd20bc753614b020f58a26569d86086
URL:		http://www.stefanopassiglia.com
BuildRoot:	%{tmpdir}/%{name}-%{version}-root-%(id -u -n)

%description
squidsites is a tool that parses Squid access log file and generates a
report ofthe most visited sites.

%description -l pl
squidsites jest narzêdziem analizuj±cym logi Squida oraz tworz±cym
raport z najczêsciej odwiedzanych stron.

%prep
%setup -q -c

%build
cd src/
%{__make}

%install
rm -rf $RPM_BUILD_ROOT
install -d $RPM_BUILD_ROOT%{_bindir}

install src/squidsites $RPM_BUILD_ROOT%{_bindir}

%clean
rm -rf $RPM_BUILD_ROOT

%files
%defattr(644,root,root,755)
%doc Authors Bugs ChangeLog README
%attr(755,root,root) %{_bindir}/*
