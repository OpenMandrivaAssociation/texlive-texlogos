%global tl_name texlogos
%global tl_revision 19083

Name:		texlive-%{tl_name}
Epoch:		1
Version:	1.3.1
Release:	%{tl_revision}.1
Summary:	Ready-to-use LaTeX logos
Group:		Publishing
URL:		https://www.ctan.org/tex-archive/macros/latex/contrib/texlogos/texlogos.sty
License:	lppl
Source0:	https://mirrors.ctan.org/systems/texlive/tlnet/archive/texlogos.r%{tl_revision}.tar.xz
BuildArch:	noarch
BuildSystem:	texlive
Provides:	texlive(%{tl_name}) = %{tl_revision}

%description
TeXlogos defines an assortment of frequently used logos not contained in
base LaTeX itself. The Metafont, MetapostAMS, BibTeX and SliTeX logos
are defined, as long as you have the appropriate CM/Logo/AMS fonts.
Currency symbols Euro, Cent, Yen, Won and Naira are defined so as not to
need TS1-encoded fonts. Also defined are the C++ logo, with the '+'
signs properly positioned, and the logo of the Vienna University
Business Administration Center (BWZ).

