Name:		texlive-texlogos
Version:	19083
Release:	2
Summary:	Ready-to-use LaTeX logos
Group:		Publishing
URL:		http://www.ctan.org/tex-archive/macros/latex/contrib/texlogos/texlogos.sty
License:	LPPL
Source0:	http://mirrors.ctan.org/systems/texlive/tlnet/archive/texlogos.r%{version}.tar.xz
BuildArch:	noarch
BuildRequires:	texlive-tlpkg
Requires(pre):	texlive-tlpkg
Requires(post):	texlive-kpathsea

%description
TeXlogos defines an assortment of frequently used logos not
contained in base LaTeX itself. The MetaFont, MetaPost, AMS,
BibTeX and SliTeX logos are defined, as long as you have the
appropriate CM/Logo/AMS fonts. Currency symbols Euro, Cent,
Yen, Won and Naira are defined so as not to need TS1-encoded
fonts. Also defined are the C++ logo, with the '+' signs
properly positioned, and the logo of the Vienna University
Business Administration Center (BWZ).

%post
%{_sbindir}/texlive.post

%postun
if [ $1 -eq 0 ]; then
	%{_sbindir}/texlive.post
fi

#-----------------------------------------------------------------------
%files
%{_texmfdistdir}/tex/latex/texlogos/texlogos.sty

#-----------------------------------------------------------------------
%prep
%autosetup -p1 -c

%build

%install
mkdir -p %{buildroot}%{_texmfdistdir}
cp -fpar tex %{buildroot}%{_texmfdistdir}
