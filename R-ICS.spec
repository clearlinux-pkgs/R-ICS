#
# This file is auto-generated. DO NOT EDIT
# Generated by: autospec.py
#
Name     : R-ICS
Version  : 1.3.1
Release  : 1
URL      : https://cran.r-project.org/src/contrib/ICS_1.3-1.tar.gz
Source0  : https://cran.r-project.org/src/contrib/ICS_1.3-1.tar.gz
Summary  : Tools for Exploring Multivariate Data via ICS/ICA
Group    : Development/Tools
License  : GPL-2.0+
Requires: R-mvtnorm
Requires: R-robustbase
Requires: R-survey
BuildRequires : R-mvtnorm
BuildRequires : R-robustbase
BuildRequires : R-survey
BuildRequires : clr-R-helpers

%description
No detailed description available

%prep
%setup -q -c -n ICS

%build
export http_proxy=http://127.0.0.1:9/
export https_proxy=http://127.0.0.1:9/
export no_proxy=localhost,127.0.0.1,0.0.0.0
export LANG=C
export SOURCE_DATE_EPOCH=1521206809

%install
rm -rf %{buildroot}
export SOURCE_DATE_EPOCH=1521206809
export LANG=C
export CFLAGS="$CFLAGS -O3 -flto -fno-semantic-interposition "
export FCFLAGS="$CFLAGS -O3 -flto -fno-semantic-interposition "
export FFLAGS="$CFLAGS -O3 -flto -fno-semantic-interposition "
export CXXFLAGS="$CXXFLAGS -O3 -flto -fno-semantic-interposition "
export AR=gcc-ar
export RANLIB=gcc-ranlib
export LDFLAGS="$LDFLAGS  -Wl,-z -Wl,relro"
mkdir -p %{buildroot}/usr/lib64/R/library

mkdir -p ~/.R
mkdir -p ~/.stash
echo "CFLAGS = $CFLAGS -march=haswell -ftree-vectorize " > ~/.R/Makevars
echo "FFLAGS = $FFLAGS -march=haswell -ftree-vectorize " >> ~/.R/Makevars
echo "CXXFLAGS = $CXXFLAGS -march=haswell -ftree-vectorize " >> ~/.R/Makevars
R CMD INSTALL --install-tests --built-timestamp=${SOURCE_DATE_EPOCH} --build  -l %{buildroot}/usr/lib64/R/library ICS
for i in `find %{buildroot}/usr/lib64/R/ -name "*.so"`; do mv $i $i.avx2 ; mv $i.avx2 ~/.stash/; done
echo "CFLAGS = $CFLAGS -march=skylake-avx512 -ftree-vectorize " > ~/.R/Makevars
echo "FFLAGS = $FFLAGS -march=skylake-avx512 -ftree-vectorize " >> ~/.R/Makevars
echo "CXXFLAGS = $CXXFLAGS -march=skylake-avx512 -ftree-vectorize " >> ~/.R/Makevars
R CMD INSTALL --preclean --install-tests --no-test-load --built-timestamp=${SOURCE_DATE_EPOCH} --build  -l %{buildroot}/usr/lib64/R/library ICS
for i in `find %{buildroot}/usr/lib64/R/ -name "*.so"`; do mv $i $i.avx512 ; mv $i.avx512 ~/.stash/; done
echo "CFLAGS = $CFLAGS -ftree-vectorize " > ~/.R/Makevars
echo "FFLAGS = $FFLAGS -ftree-vectorize " >> ~/.R/Makevars
echo "CXXFLAGS = $CXXFLAGS -ftree-vectorize " >> ~/.R/Makevars
R CMD INSTALL --preclean --install-tests --built-timestamp=${SOURCE_DATE_EPOCH} --build  -l %{buildroot}/usr/lib64/R/library ICS
cp ~/.stash/* %{buildroot}/usr/lib64/R/library/*/libs/ || :
%{__rm} -rf %{buildroot}%{_datadir}/R/library/R.css
%check
export LANG=C
export http_proxy=http://127.0.0.1:9/
export https_proxy=http://127.0.0.1:9/
export no_proxy=localhost,127.0.0.1,0.0.0.0
export _R_CHECK_FORCE_SUGGESTS_=false
R CMD check --no-manual --no-examples --no-codoc -l %{buildroot}/usr/lib64/R/library ICS|| : 
cp ~/.stash/* %{buildroot}/usr/lib64/R/library/*/libs/ || :


%files
%defattr(-,root,root,-)
/usr/lib64/R/library/ICS/CHANGES
/usr/lib64/R/library/ICS/CITATION
/usr/lib64/R/library/ICS/DESCRIPTION
/usr/lib64/R/library/ICS/INDEX
/usr/lib64/R/library/ICS/Meta/Rd.rds
/usr/lib64/R/library/ICS/Meta/features.rds
/usr/lib64/R/library/ICS/Meta/hsearch.rds
/usr/lib64/R/library/ICS/Meta/links.rds
/usr/lib64/R/library/ICS/Meta/nsInfo.rds
/usr/lib64/R/library/ICS/Meta/package.rds
/usr/lib64/R/library/ICS/Meta/vignette.rds
/usr/lib64/R/library/ICS/NAMESPACE
/usr/lib64/R/library/ICS/R/ICS
/usr/lib64/R/library/ICS/R/ICS.rdb
/usr/lib64/R/library/ICS/R/ICS.rdx
/usr/lib64/R/library/ICS/doc/ICS.R
/usr/lib64/R/library/ICS/doc/ICS.Rnw
/usr/lib64/R/library/ICS/doc/ICS.pdf
/usr/lib64/R/library/ICS/doc/index.html
/usr/lib64/R/library/ICS/help/AnIndex
/usr/lib64/R/library/ICS/help/ICS.rdb
/usr/lib64/R/library/ICS/help/ICS.rdx
/usr/lib64/R/library/ICS/help/aliases.rds
/usr/lib64/R/library/ICS/help/paths.rds
/usr/lib64/R/library/ICS/html/00Index.html
/usr/lib64/R/library/ICS/html/R.css
/usr/lib64/R/library/ICS/pictures/cat.pgm
/usr/lib64/R/library/ICS/pictures/road.pgm
/usr/lib64/R/library/ICS/pictures/sheep.pgm