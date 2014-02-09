Summary: A python client for etcd
Name: python-etcd
Version: 0.3.0
Release: 3%{?dist}
License: MIT
Group: System Environment/Libraries
URL: http://github.com/jplana/python-etcd

Source: python-etcd-%{version}.tar.gz
BuildArch: noarch
BuildRoot: %{_tmppath}/%{name}-%{version}-%{release}-root

BuildRequires: python-devel
BuildRequires: python-setuptools
Requires: python-urllib3

%description
A python client for Etcd.

%prep
%setup -n python-etcd-%{version}

%build
%{__python} setup.py build

%install
%{__rm} -rf %{buildroot}
%{__python} setup.py install --skip-build --root="%{buildroot}" --prefix="%{_prefix}" \
    --single-version-externally-managed

%clean
%{__rm} -rf %{buildroot}

%files
%defattr(-, root, root, 0755)
%doc NEWS.txt README.rst
%{python_sitelib}/python_etcd-%{version}-py*.egg-info
%{python_sitelib}/etcd/

%changelog
* Sun Feb 09 2014 Nacho Barrientos <nacho.barrientos@cern.ch> - 0.3.0-3
- Urllib 1.6 compat -- Catch socket errors
- Py2.6 compat -- Use indexes in .format calls
