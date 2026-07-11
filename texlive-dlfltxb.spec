%global tl_name dlfltxb
%global tl_revision 79618

Name:		texlive-%{tl_name}
Version:	%{tl_revision}
Release:	1
Summary:	Macros related to Introdktion til LaTeX
Group:		Publishing
URL:		https://www.ctan.org/tex-archive/macros/latex/contrib/dlfltxb
License:	lppl1.3
Source0:	https://mirrors.ctan.org/systems/texlive/tlnet/archive/dlfltxb.r%{tl_revision}.tar.xz
Source1:	https://mirrors.ctan.org/systems/texlive/tlnet/archive/dlfltxb.doc.r%{tl_revision}.tar.xz
BuildArch:	noarch
BuildSystem:	texlive
Provides:	texlive(%{tl_name}) = %{tl_revision}

%description
The bundle contains various macros either used for creating the author's
book "Introduktion til LaTeX" (in Danish), or presented in the book as
code tips. The bundle comprises: dlfltxbcodetips: various macros helpful
in typesetting mathematics; dlfltxbmarkup: provides macros used
throughout, for registering macro names, packages etc. in the text, in
the margin and in the index, all by using categorised keys (note, a
configuration file may be used; a sample is included in the
distribution); dlfltxbtocconfig: macros for the two tables of contents
that the book has; dlfltxbmisc: various macros for typesetting LaTeX
arguments, and the macro used in the bibliography that can wrap a URL up
into a BibTeX entry. Interested parties may review the book itself on
the web at the author's institution (it is written in Danish).

