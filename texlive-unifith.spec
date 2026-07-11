%global tl_name unifith
%global tl_revision 60698

Name:		texlive-%{tl_name}
Epoch:		1
Version:	1.6
Release:	%{tl_revision}.1
Summary:	Typeset theses for University of Florence (Italy)
Group:		Publishing
URL:		https://www.ctan.org/tex-archive/macros/latex/contrib/unifith
License:	lppl1.3c
Source0:	https://mirrors.ctan.org/systems/texlive/tlnet/archive/unifith.r%{tl_revision}.tar.xz
Source1:	https://mirrors.ctan.org/systems/texlive/tlnet/archive/unifith.doc.r%{tl_revision}.tar.xz
BuildArch:	noarch
BuildSystem:	texlive
Provides:	texlive(%{tl_name}) = %{tl_revision}

%description
The package provides a class to typeset Ph.D., Master, and Bachelor
theses that adhere to the publishing guidelines of the University of
Florence (Italy).

