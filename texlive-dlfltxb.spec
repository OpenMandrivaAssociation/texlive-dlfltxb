# revision 17337
# category Package
# catalog-ctan /macros/latex/contrib/dlfltxb
# catalog-date 2010-03-04 23:40:34 +0100
# catalog-license lppl
# catalog-version undef
Name:		texlive-dlfltxb
Version:	20100304
Release:	9
Summary:	Macros related to "Introdktion til LaTeX"
Group:		Publishing
URL:		http://www.ctan.org/tex-archive/macros/latex/contrib/dlfltxb
License:	LPPL
Source0:	http://mirrors.ctan.org/systems/texlive/tlnet/archive/dlfltxb.tar.xz
Source1:	http://mirrors.ctan.org/systems/texlive/tlnet/archive/dlfltxb.doc.tar.xz
BuildArch:	noarch
BuildRequires:	texlive-tlpkg
Requires(pre):	texlive-tlpkg
Requires(post):	texlive-kpathsea

%description
The bundle contains various macros either used for creating the
author's book "Introduktion til LaTeX" (in Danish), or
presented in the book as code tips. The bundle comprises: -
dlfltxbcodetips: various macros helpful in typesetting
mathematics; - dlfltxbmarkup: provides a macros used throughout
the book, for registering macro names, packages etc. in the
text, in the margin and in the index, all by using categorised
keys (note, a configuration file may be used; a sample is
included in the distribution); - dlfltxbtocconfig: macros for
the two tables of contents that the book has; - dlfltxbmisc:
various macros for typesetting LaTeX arguments, and the macro
used in the bibliography that can wrap a URL up into a bibtex
entry. Interested parties may review the book itself on the web
at the author's institution (it is written in Danish).

%post
    %{_sbindir}/texlive.post

%postun
    if [ $1 -eq 0 ]; then
	%{_sbindir}/texlive.post
    fi

#-----------------------------------------------------------------------
%files
%{_texmfdistdir}/bibtex/bst/dlfltxb/dlfltxbbibtex.bst
%{_texmfdistdir}/tex/latex/dlfltxb/dlfltxbcodetips.sty
%{_texmfdistdir}/tex/latex/dlfltxb/dlfltxbmarkup.sty
%{_texmfdistdir}/tex/latex/dlfltxb/dlfltxbmarkupbookkeys.sty
%{_texmfdistdir}/tex/latex/dlfltxb/dlfltxbmisc.sty
%{_texmfdistdir}/tex/latex/dlfltxb/dlfltxbtocconfig.sty
%doc %{_texmfdistdir}/doc/latex/dlfltxb/README
%doc %{_texmfdistdir}/doc/latex/dlfltxb/dlfltxbbibtex.dbj
%doc %{_texmfdistdir}/doc/latex/dlfltxb/dlfltxbcodetips.pdf
%doc %{_texmfdistdir}/doc/latex/dlfltxb/dlfltxbcodetips.tex
%doc %{_texmfdistdir}/doc/latex/dlfltxb/dlfltxbmarkup-showkeys.pdf
%doc %{_texmfdistdir}/doc/latex/dlfltxb/dlfltxbmarkup-showkeys.tex
%doc %{_texmfdistdir}/doc/latex/dlfltxb/dlfltxbmarkup.pdf
%doc %{_texmfdistdir}/doc/latex/dlfltxb/dlfltxbmarkup.tex
%doc %{_texmfdistdir}/doc/latex/dlfltxb/dlfltxbmisc.pdf
%doc %{_texmfdistdir}/doc/latex/dlfltxb/dlfltxbmisc.tex
%doc %{_texmfdistdir}/doc/latex/dlfltxb/dlfltxbtocconfig.pdf
%doc %{_texmfdistdir}/doc/latex/dlfltxb/dlfltxbtocconfig.tex
%doc %{_texmfdistdir}/doc/latex/dlfltxb/package_doc.bib

#-----------------------------------------------------------------------
%prep
%setup -c -a0 -a1

%build

%install
mkdir -p %{buildroot}%{_texmfdistdir}
cp -fpar bibtex tex doc %{buildroot}%{_texmfdistdir}


%changelog
* Wed Jan 04 2012 Paulo Andrade <pcpa@mandriva.com.br> 20100304-2
+ Revision: 751003
- Rebuild to reduce used resources

* Sat Nov 05 2011 Paulo Andrade <pcpa@mandriva.com.br> 20100304-1
+ Revision: 718240
- texlive-dlfltxb
- texlive-dlfltxb
- texlive-dlfltxb
- texlive-dlfltxb

