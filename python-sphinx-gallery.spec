%global srcname sphinx-gallery

Name:           python-%{srcname}
Version:        0.1.5
Release:        5%{?dist}
Summary:        Sphinx extension to automatically generate an examples gallery

License:        BSD
URL:            http://sphinx-gallery.readthedocs.io/en/latest/
Source0:        https://github.com/sphinx-gallery/sphinx-gallery/archive/v%{version}/%{srcname}-%{version}.tar.gz
# Fix UnicodeDecodeError with py35
# https://github.com/sphinx-gallery/sphinx-gallery/issues/170
Patch0:         https://github.com/sphinx-gallery/sphinx-gallery/commit/fa2ea5f35051846e43837c6eb87496435a6064c0.patch

BuildArch:      noarch

%description
A Sphinx extension that builds an HTML version of any Python script and puts
it into an examples gallery.


%package -n python2-%{srcname}
Summary:        %{summary}
BuildRequires:  python2-devel
BuildRequires:  python-setuptools
# For tests
BuildRequires:  python-coverage
BuildRequires:  python-nose
BuildRequires:  python-matplotlib
BuildRequires:  python-pillow
BuildRequires:  python-sphinx
Requires:       python-matplotlib
Requires:       python-pillow
Requires:       python-sphinx
%{?python_provide:%python_provide python2-%{srcname}}

%description -n python2-%{srcname}
A Sphinx extension that builds an HTML version of any Python script and puts
it into an examples gallery.


%package -n     python%{python3_pkgversion}-%{srcname}
Summary:        %{summary}
BuildRequires:  python%{python3_pkgversion}-devel
BuildRequires:  python%{python3_pkgversion}-setuptools
# For tests
BuildRequires:  python%{python3_pkgversion}-coverage
BuildRequires:  python%{python3_pkgversion}-nose
BuildRequires:  python%{python3_pkgversion}-matplotlib
BuildRequires:  python%{python3_pkgversion}-pillow
BuildRequires:  python%{python3_pkgversion}-sphinx
Requires:       python%{python3_pkgversion}-matplotlib
Requires:       python%{python3_pkgversion}-pillow
Requires:       python%{python3_pkgversion}-sphinx
%{?python_provide:%python_provide python%{python3_pkgversion}-%{srcname}}

%description -n python%{python3_pkgversion}-%{srcname}
A Sphinx extension that builds an HTML version of any Python script and puts
it into an examples gallery.


%prep
%setup -qn %{srcname}-%{version}
%patch0 -p1 -b .utf8

# Remove bundled eggs
rm -rf %{srcname}.egg-info


%build
%py2_build
%py3_build


%install
%py2_install
%py3_install
# No need for copy_sphinxgallery.sh
rm -r %{buildroot}%{_bindir}


%check
#export LANG=en_US.UTF-8
nosetests-%{python2_version}
rm -f .coverage
nosetests-%{python3_version}


%files -n python2-%{srcname}
%license LICENSE
%doc CHANGES.rst README.rst
%{python2_sitelib}/sphinx_gallery-%{version}-py%{python2_version}.egg-info/
%{python2_sitelib}/sphinx_gallery/

%files -n python%{python3_pkgversion}-%{srcname}
%license LICENSE
%doc README.rst
%{python3_sitelib}/sphinx_gallery-%{version}-py%{python3_version}.egg-info/
%{python3_sitelib}/sphinx_gallery/


%changelog
* Sat Feb 11 2017 Fedora Release Engineering <releng@fedoraproject.org> - 0.1.5-5
- Rebuilt for https://fedoraproject.org/wiki/Fedora_26_Mass_Rebuild

* Mon Dec 19 2016 Miro Hrončok <mhroncok@redhat.com> - 0.1.5-4
- Rebuild for Python 3.6

* Mon Nov 21 2016 Orion Poplawski <orion@cora.nwra.com> - 0.1.5-3
- Add upstream patch to fix UnicodeDecodeError

* Sat Nov 19 2016 Orion Poplawski <orion@cora.nwra.com> - 0.1.5-2
- Use github source, ship LICENSE
- Update URL
- Add needed requires

* Tue Nov 15 2016 Orion Poplawski <orion@cora.nwra.com> - 0.1.5-1
- Initial Fedora package
