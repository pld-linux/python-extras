#
# Conditional build:
%bcond_without	tests	# do not perform "make test" (use for extras/testtools pair bootstrap)
%bcond_without	python2 # CPython 2.x module
%bcond_without	python3 # CPython 3.x module

Summary:	Useful extra bits for Python - things that should be in the standard library
Summary(pl.UTF-8):	Przydatne dodatki do Pythona, które powinny być w bibliotece standardowej
Name:		python-extras
Version:	1.0.0
Release:	4
License:	MIT
Group:		Libraries/Python
#Source0Download: https://pypi.org/simple/extras/
Source0:	https://files.pythonhosted.org/packages/source/e/extras/extras-%{version}.tar.gz
# Source0-md5:	3a63ad60cf8f0186c9e3a02f55ec5b14
URL:		https://github.com/testing-cabal/extras
BuildRequires:	rpm-pythonprov
BuildRequires:	rpmbuild(macros) >= 1.714
%if %{with python2}
BuildRequires:	python-modules >= 1:2.6
BuildRequires:	python-setuptools
%if %{with tests}
BuildRequires:	python-testtools
%endif
%endif
%if %{with python3}
BuildRequires:	python3-modules >= 1:3.2
BuildRequires:	python3-setuptools
%if %{with tests}
BuildRequires:	python3-testtools
%endif
%endif
Requires:	python-modules >= 1:2.6
BuildArch:	noarch
BuildRoot:	%{tmpdir}/%{name}-%{version}-root-%(id -u -n)

%description
extras is a set of extensions to the Python standard library,
originally written to make the code within testtools cleaner, but now
split out for general use outside of a testing context.

%description -l pl.UTF-8
extras to zbiór rozszerzeń biblioteki standardowej Pythona, pierwotnie
napisany, aby uczynić kod biblioteki testtools czytelniejszym, ale
później wydzielony do ogólnego użytku, nie tylko w kontekście testów.

%package -n python3-extras
Summary:	Useful extra bits for Python - things that should be in the standard library
Summary(pl.UTF-8):	Przydatne dodatki do Pythona, które powinny być w bibliotece standardowej
Group:		Libraries/Python
Requires:	python3-modules >= 1:3.2

%description -n python3-extras
extras is a set of extensions to the Python standard library,
originally written to make the code within testtools cleaner, but now
split out for general use outside of a testing context.

%description -n python3-extras -l pl.UTF-8
extras to zbiór rozszerzeń biblioteki standardowej Pythona, pierwotnie
napisany, aby uczynić kod biblioteki testtools czytelniejszym, ale
później wydzielony do ogólnego użytku, nie tylko w kontekście testów.

%prep
%setup -q -n extras-%{version}

%build
%if %{with python2}
%py_build

%if %{with tests}
%{__python} -m unittest discover -s extras.tests
%endif
%endif

%if %{with python3}
%py3_build

%if %{with tests}
%{__python3} -m unittest discover -s extras.tests
%endif
%endif

%install
rm -rf $RPM_BUILD_ROOT

%if %{with python2}
%py_install

%py_postclean
%{__rm} -r $RPM_BUILD_ROOT%{py_sitescriptdir}/extras/tests
%endif

%if %{with python3}
%py3_install

%{__rm} -r $RPM_BUILD_ROOT%{py3_sitescriptdir}/extras/tests
%endif

%clean
rm -rf $RPM_BUILD_ROOT

%if %{with python2}
%files
%defattr(644,root,root,755)
%doc LICENSE NEWS README.rst
%{py_sitescriptdir}/extras
%{py_sitescriptdir}/extras-%{version}-py*.egg-info
%endif

%if %{with python3}
%files -n python3-extras
%defattr(644,root,root,755)
%doc LICENSE NEWS README.rst
%{py3_sitescriptdir}/extras
%{py3_sitescriptdir}/extras-%{version}-py*.egg-info
%endif
