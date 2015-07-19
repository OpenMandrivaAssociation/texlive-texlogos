# revision 19083
# category Package
# catalog-ctan /macros/latex/contrib/texlogos/texlogos.sty
# catalog-date 2007-01-16 09:34:54 +0100
# catalog-license lppl
# catalog-version 1.3.1
Name:		texlive-texlogos
Version:	1.3.1
Release:	10
Summary:	Ready-to-use LaTeX logos
Group:		Publishing
URL:		http://www.ctan.org/tex-archive/macros/latex/contrib/texlogos/texlogos.sty
License:	LPPL
Source0:	http://mirrors.ctan.org/systems/texlive/tlnet/archive/texlogos.tar.xz
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
%setup -c -a0

%build

%install
mkdir -p %{buildroot}%{_texmfdistdir}
cp -fpar tex %{buildroot}%{_texmfdistdir}


%changelog
* Wed Jan 04 2012 Paulo Andrade <pcpa@mandriva.com.br> 1.3.1-2
+ Revision: 756741
- Rebuild to reduce used resources

* Sat Nov 05 2011 Paulo Andrade <pcpa@mandriva.com.br> 1.3.1-1
+ Revision: 719706
- texlive-texlogos
- texlive-texlogos
- texlive-texlogos

