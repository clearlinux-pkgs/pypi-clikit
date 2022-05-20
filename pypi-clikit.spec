#
# This file is auto-generated. DO NOT EDIT
# Generated by: autospec.py
#
Name     : pypi-clikit
Version  : 0.6.2
Release  : 5
URL      : https://files.pythonhosted.org/packages/0b/07/27d700f8447c0ca81454a4acdb7eb200229a6d06fe0b1439acc3da49a53f/clikit-0.6.2.tar.gz
Source0  : https://files.pythonhosted.org/packages/0b/07/27d700f8447c0ca81454a4acdb7eb200229a6d06fe0b1439acc3da49a53f/clikit-0.6.2.tar.gz
Summary  : CliKit is a group of utilities to build beautiful and testable command line interfaces.
Group    : Development/Tools
License  : MIT
Requires: pypi-clikit-license = %{version}-%{release}
Requires: pypi-clikit-python = %{version}-%{release}
Requires: pypi-clikit-python3 = %{version}-%{release}
BuildRequires : buildreq-distutils3
BuildRequires : pypi(poetry_core)

%description
# CliKit
CliKit is a group of utilities to build beautiful and testable command line interfaces.

%package license
Summary: license components for the pypi-clikit package.
Group: Default

%description license
license components for the pypi-clikit package.


%package python
Summary: python components for the pypi-clikit package.
Group: Default
Requires: pypi-clikit-python3 = %{version}-%{release}

%description python
python components for the pypi-clikit package.


%package python3
Summary: python3 components for the pypi-clikit package.
Group: Default
Requires: python3-core
Provides: pypi(clikit)
Requires: pypi(crashtest)
Requires: pypi(pastel)
Requires: pypi(pylev)

%description python3
python3 components for the pypi-clikit package.


%prep
%setup -q -n clikit-0.6.2
cd %{_builddir}/clikit-0.6.2
pushd ..
cp -a clikit-0.6.2 buildavx2
popd

%build
export http_proxy=http://127.0.0.1:9/
export https_proxy=http://127.0.0.1:9/
export no_proxy=localhost,127.0.0.1,0.0.0.0
export LANG=C.UTF-8
export SOURCE_DATE_EPOCH=1653009554
export GCC_IGNORE_WERROR=1
export AR=gcc-ar
export RANLIB=gcc-ranlib
export NM=gcc-nm
export CFLAGS="$CFLAGS -O3 -ffat-lto-objects -flto=auto "
export FCFLAGS="$FFLAGS -O3 -ffat-lto-objects -flto=auto "
export FFLAGS="$FFLAGS -O3 -ffat-lto-objects -flto=auto "
export CXXFLAGS="$CXXFLAGS -O3 -ffat-lto-objects -flto=auto "
export MAKEFLAGS=%{?_smp_mflags}
python3 -m build --wheel --skip-dependency-check --no-isolation
pushd ../buildavx2/
export CFLAGS="$CFLAGS -m64 -march=x86-64-v3 -Wl,-z,x86-64-v3 "
export CXXFLAGS="$CXXFLAGS -m64 -march=x86-64-v3 -Wl,-z,x86-64-v3 "
export FFLAGS="$FFLAGS -m64 -march=x86-64-v3 -Wl,-z,x86-64-v3 "
export FCFLAGS="$FCFLAGS -m64 -march=x86-64-v3 "
export LDFLAGS="$LDFLAGS -m64 -march=x86-64-v3 "
python3 -m build --wheel --skip-dependency-check --no-isolation

popd

%install
export MAKEFLAGS=%{?_smp_mflags}
rm -rf %{buildroot}
mkdir -p %{buildroot}/usr/share/package-licenses/pypi-clikit
cp %{_builddir}/clikit-0.6.2/LICENSE %{buildroot}/usr/share/package-licenses/pypi-clikit/84661790a5df00ab944c2d37978d6ce5ac88e554
pip install --root=%{buildroot} --no-deps --ignore-installed dist/*.whl
echo ----[ mark ]----
cat %{buildroot}/usr/lib/python3*/site-packages/*/requires.txt || :
echo ----[ mark ]----
pushd ../buildavx2/
export CFLAGS="$CFLAGS -m64 -march=x86-64-v3 -Wl,-z,x86-64-v3 "
export CXXFLAGS="$CXXFLAGS -m64 -march=x86-64-v3 -Wl,-z,x86-64-v3 "
export FFLAGS="$FFLAGS -m64 -march=x86-64-v3 -Wl,-z,x86-64-v3 "
export FCFLAGS="$FCFLAGS -m64 -march=x86-64-v3 "
export LDFLAGS="$LDFLAGS -m64 -march=x86-64-v3 "
pip install --root=%{buildroot}-v3 --no-deps --ignore-installed dist/*.whl
popd
/usr/bin/elf-move.py avx2 %{buildroot}-v3 %{buildroot}/usr/share/clear/optimized-elf/ %{buildroot}/usr/share/clear/filemap/filemap-%{name}

%files
%defattr(-,root,root,-)

%files license
%defattr(0644,root,root,0755)
/usr/share/package-licenses/pypi-clikit/84661790a5df00ab944c2d37978d6ce5ac88e554

%files python
%defattr(-,root,root,-)

%files python3
%defattr(-,root,root,-)
/usr/lib/python3*/*
