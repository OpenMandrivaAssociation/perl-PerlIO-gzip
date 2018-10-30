%define modname	PerlIO-gzip
%define modver	0.18

Summary:	Perl extension to provide a PerlIO layer to gzip/gunzip
Name:		perl-%{modname}
Version:	%perl_convert_version %{modver}
Release:	18
License:	GPLv2+ or Artistic
Group:		Development/Perl
Url:		http://search.cpan.org/dist/%{modname}/
Source0:	http://www.cpan.org/authors/id/N/NW/NWCLARK/%{modname}-%{modver}.tar.bz2
Patch0:		%{modname}-0.14-no_strict_warnings.patch
Patch1:		PerlIO-gzip-0.18-RT92412.patch
BuildRequires:	perl(Test::More)
BuildRequires:	perl-devel
BuildRequires:	pkgconfig(zlib)

%description
PerlIO::gzip provides a PerlIO layer that manipulates files in the format used
by the gzip program. Compression and Decompression are implemented, but not
together. If you attempt to open a file for reading and writing the open will
fail.

%prep
%setup -qn %{modname}-%{modver}
%apply_patches

%build
%__perl Makefile.PL INSTALLDIRS=vendor
%make

%check
%make test

%install
%makeinstall_std

%files
%doc README Changes
%{perl_vendorarch}/PerlIO
%{perl_vendorarch}/auto/PerlIO
%{_mandir}/man3/*

