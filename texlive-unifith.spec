Name:		texlive-unifith
Version:	60698
Release:	2
Summary:	Typeset theses for University of Florence (Italy)
Group:		Publishing
URL:		http://www.ctan.org/tex-archive/macros/latex/contrib/unifith
License:	lppl1.3c
Source0:	http://mirrors.ctan.org/systems/texlive/tlnet/archive/unifith.r%{version}.tar.xz
Source1:	http://mirrors.ctan.org/systems/texlive/tlnet/archive/unifith.doc.r%{version}.tar.xz
BuildArch:	noarch
BuildRequires:	texlive-tlpkg
Requires(pre):	texlive-tlpkg
Requires(post):	texlive-kpathsea

%description
The package provides a class to typeset Ph.D., Master, and
Bachelor theses that adhere to the publishing guidelines of the
University of Florence (Italy).

%prep
%autosetup -p1 -c -a1

%build

%install
rm -rf tlpkg
mkdir -p %{buildroot}%{_texmfdistdir}
cp -a * %{buildroot}%{_texmfdistdir}

%files
%{_texmfdistdir}/tex/latex/unifith
%{_texmfdistdir}/bibtex/bst/unifith
%doc %{_texmfdistdir}/doc/latex/unifith

%post -p %{_sbindir}/texlive.post

%postun
[ "$1" -eq 0 ] && %{_sbindir}/texlive.post
