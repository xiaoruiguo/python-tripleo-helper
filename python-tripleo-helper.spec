%if 0%{?fedora}
%global with_python3 1
%endif

Name:           python-tripleo-helper
Version:        0.0.VERS
Release:        1%{?dist}

Summary:        A Python library to drive a TripleO based installer
License:        ASL 2.0
URL:            http://softwarefactory-project.io/r/python-tripleo-helper

Source0:        tripleo-helper-%{version}.tar.gz

BuildArch:      noarch

%description
A Python library to drive a TripleO based installer

%package -n python2-tripleo-helper
Summary:        A Python library to drive a TripleO based installer
%{?python_provide:%python_provide python2-tripleo-helper}

BuildRequires:  PyYAML
BuildRequires:  libffi-devel
BuildRequires:  openssl-devel
BuildRequires:  python-click
BuildRequires:  python-futures
BuildRequires:  python-jinja2
BuildRequires:  python-neutronclient
BuildRequires:  python-novaclient
BuildRequires:  python-paramiko
BuildRequires:  python-setuptools
BuildRequires:  python-tox
BuildRequires:  python2-devel
Requires:       PyYAML
Requires:       python-click
Requires:       python-futures
Requires:       python-jinja2
Requires:       python-neutronclient
Requires:       python-novaclient
Requires:       python-paramiko >= 1.16

%description -n python2-tripleo-helper
A Python library to drive a TripleO based installer

%if 0%{?with_python3}
%package -n python3-tripleo-helper
Summary:        A Python library to drive a TripleO based installer
%{?python_provide:%python_provide python3-tripleo-helper}

BuildRequires:  libffi-devel
BuildRequires:  openssl-devel
BuildRequires:  python-tox
BuildRequires:  python3-click
BuildRequires:  python3-devel
BuildRequires:  python3-jinja2
BuildRequires:  python3-neutronclient
BuildRequires:  python3-novaclient
BuildRequires:  python3-paramiko
BuildRequires:  python3-setuptools
Requires:       python3-PyYAML
Requires:       python3-click
Requires:       python3-jinja2
Requires:       python3-neutronclient
Requires:       python3-novaclient
Requires:       python3-paramiko >= 1.16

%description -n python3-tripleo-helper
A Python library to drive a TripleO based installer
%endif


%prep
%autosetup -n tripleo-helper-%{version}


%build
%py2_build
%if 0%{?with_python3}
%py3_build
%endif


%install
install -d %{buildroot}%{_bindir}
%py2_install
%if 0%{?with_python3}
%py3_install
%endif


%check
%{__python2} setup.py test
%if 0%{?with_python3}
%{__python3} setup.py test
%endif

%files -n python2-tripleo-helper
%doc
%{python2_sitelib}/tripleohelper
%{python2_sitelib}/*.egg-info
%{_bindir}/chainsaw-ovb
%{_bindir}/chainsaw-libvirt

%if 0%{?with_python3}
%files -n python3-tripleo-helper
%doc
%{python3_sitelib}/tripleohelper
%{python3_sitelib}/*.egg-info
%{_bindir}/chainsaw-ovb
%{_bindir}/chainsaw-libvirt
%endif

%changelog
* Tue Aug 23 2016 Yanis Guenane <yguenane@redhat.com> 0.1-1
- Initial commit
