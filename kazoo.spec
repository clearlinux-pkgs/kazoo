#
# This file is auto-generated. DO NOT EDIT
# Generated by: autospec.py
#
Name     : kazoo
Version  : 2.8.0
Release  : 36
URL      : https://files.pythonhosted.org/packages/49/fb/4f1d6890e2b1aa9fe7a7d9c42b5ef32732bc7b02e6bacc556ab1cc41aba3/kazoo-2.8.0.tar.gz
Source0  : https://files.pythonhosted.org/packages/49/fb/4f1d6890e2b1aa9fe7a7d9c42b5ef32732bc7b02e6bacc556ab1cc41aba3/kazoo-2.8.0.tar.gz
Summary  : Higher Level Zookeeper Client
Group    : Development/Tools
License  : Apache-2.0
Requires: kazoo-license = %{version}-%{release}
Requires: kazoo-python = %{version}-%{release}
Requires: kazoo-python3 = %{version}-%{release}
Requires: eventlet
Requires: gevent
Requires: pure-sasl
Requires: six
BuildRequires : buildreq-distutils3
BuildRequires : eventlet
BuildRequires : gevent
BuildRequires : pure-sasl
BuildRequires : six

%description
=====

%package license
Summary: license components for the kazoo package.
Group: Default

%description license
license components for the kazoo package.


%package python
Summary: python components for the kazoo package.
Group: Default
Requires: kazoo-python3 = %{version}-%{release}

%description python
python components for the kazoo package.


%package python3
Summary: python3 components for the kazoo package.
Group: Default
Requires: python3-core
Provides: pypi(kazoo)
Requires: pypi(six)

%description python3
python3 components for the kazoo package.


%prep
%setup -q -n kazoo-2.8.0
cd %{_builddir}/kazoo-2.8.0

%build
export http_proxy=http://127.0.0.1:9/
export https_proxy=http://127.0.0.1:9/
export no_proxy=localhost,127.0.0.1,0.0.0.0
export LANG=C.UTF-8
export SOURCE_DATE_EPOCH=1594611063
export GCC_IGNORE_WERROR=1
export CFLAGS="$CFLAGS -fno-lto "
export FCFLAGS="$FFLAGS -fno-lto "
export FFLAGS="$FFLAGS -fno-lto "
export CXXFLAGS="$CXXFLAGS -fno-lto "
export MAKEFLAGS=%{?_smp_mflags}
python3 setup.py build

%install
export MAKEFLAGS=%{?_smp_mflags}
rm -rf %{buildroot}
mkdir -p %{buildroot}/usr/share/package-licenses/kazoo
cp %{_builddir}/kazoo-2.8.0/LICENSE %{buildroot}/usr/share/package-licenses/kazoo/294b43b2cec9919063be1a3b49e8722648424779
python3 -tt setup.py build  install --root=%{buildroot}
echo ----[ mark ]----
cat %{buildroot}/usr/lib/python3*/site-packages/*/requires.txt || :
echo ----[ mark ]----

%files
%defattr(-,root,root,-)

%files license
%defattr(0644,root,root,0755)
/usr/share/package-licenses/kazoo/294b43b2cec9919063be1a3b49e8722648424779

%files python
%defattr(-,root,root,-)

%files python3
%defattr(-,root,root,-)
/usr/lib/python3*/*
