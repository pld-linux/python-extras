#
# Conditional build:
%bcond_without	tests	# do not perform "make test" (use for extras/testtools pair bootstrap)
%bcond_without	python2 # CPython 2.x module
%bcond_without	python3 # CPython 3.x module

Summary:	Useful extra bits for Python - things that should be in the standard library
Summary(pl.UTF-8):	Przydatne dodatki do Pythona, które powinny być w bibliotece standardowej
Name:		python-extras
Version:	0.0.3
Release:	6
License:	MIT
Group:		Libraries/Python
Source0:	https://pypi.python.org/packages/source/e/extras/extras-%{version}.tar.gz
# Source0-md5:	62d8ba049e3386a6df69b413ea81517b
URL:		https://github.com/testing-cabal/extras
BuildRequires:	python-distribute
BuildRequires:	rpm-pythonprov
BuildRequires:	rpmbuild(macros) >= 1.710
%if %{with python3}
BuildRequires:	python3-distribute
%endif
%if %{with tests}
%if %{with python2}
BuildRequires:	python-testtools
%endif
%if %{with python3}
BuildRequires:	python3-testtools
%endif
%endif
Requires:	python-modules
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
Requires:	python3-modules

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
%{__python} setup.py \
	build --build-base build-2 \
	%{?with_tests:test}
%endif

%if %{with python3}
%{__python3} setup.py \
	build --build-base build-3 \
	%{?with_tests:test}
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
