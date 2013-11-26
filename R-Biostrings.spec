%define		packname	Biostrings

Summary:	String objects representing biological sequences
Name:		R-%{packname}
Version:	2.30.1
Release:	2
License:	Artistic 2.0
Group:		Applications/Engineering
Source0:	http://bioconductor.org/packages/release/bioc/src/contrib/%{packname}_%{version}.tar.gz
# Source0-md5:	acf4d4047855f20096e751cf5fadbf5e
URL:		http://bioconductor.org/packages/release/bioc/html/Biostrings.html
BuildRequires:	R
BuildRequires:	R-Biobase
BuildRequires:	R-IRanges-devel >= 1.6.6
BuildRequires:	R-XVector-devel
BuildRequires:	texlive-latex
Requires:	R
Requires:	R-Biobase
Requires:	R-IRanges >= 1.6.6
Requires:	R-XVector
BuildRoot:	%{tmpdir}/%{name}-%{version}-root-%(id -u -n)

%description
Memory efficient string containers, string matching algorithms, and
other utilities, for fast manipulation of large biological sequences
or set of sequences.

%package        devel
Summary:	Development files for %{name}
Group:		Development/Libraries
Requires:	%{name} = %{version}-%{release}

%description    devel
The %{name}-devel package contains libraries and header files for
developing applications that use %{name}.

%prep
%setup -q -c -n %{packname}

%build

%install
rm -rf $RPM_BUILD_ROOT
install -d $RPM_BUILD_ROOT%{_libdir}/R/library

R CMD INSTALL %{packname} -l $RPM_BUILD_ROOT%{_libdir}/R/library

%clean
rm -rf $RPM_BUILD_ROOT

%files
%defattr(644,root,root,755)
%dir %{_libdir}/R/library/%{packname}/
%doc %{_libdir}/R/library/%{packname}/doc
%doc %{_libdir}/R/library/%{packname}/DESCRIPTION
%doc %{_libdir}/R/library/%{packname}/html
%doc %{_libdir}/R/library/%{packname}/NEWS
%{_libdir}/R/library/%{packname}/help
%{_libdir}/R/library/%{packname}/R
%{_libdir}/R/library/%{packname}/extdata
%{_libdir}/R/library/%{packname}/data
%{_libdir}/R/library/%{packname}/libs
%{_libdir}/R/library/%{packname}/Meta
%{_libdir}/R/library/%{packname}/UnitTests
%{_libdir}/R/library/%{packname}/INDEX
%{_libdir}/R/library/%{packname}/NAMESPACE

%files devel
%{_libdir}/R/library/%{packname}/include
