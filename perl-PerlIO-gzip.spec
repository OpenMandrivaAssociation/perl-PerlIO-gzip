%define upstream_name    PerlIO-gzip
%define upstream_version 0.18

Name:       perl-%{upstream_name}
Version:    %perl_convert_version %{upstream_version}
Release:    %mkrel 7

Summary:	Perl extension to provide a PerlIO layer to gzip/gunzip
License:	GPL+ or Artistic
Group:		Development/Perl
Url:		http://search.cpan.org/dist/%{upstream_name}/
Source0:	http://www.cpan.org/authors/id/N/NW/NWCLARK/%{upstream_name}-%{upstream_version}.tar.bz2
Patch0:		%{upstream_name}-0.14-no_strict_warnings.patch

BuildRequires:	perl-devel
BuildRequires:  zlib-devel
BuildRoot:	%{_tmppath}/%{name}-%{version}-%{release}

%description
PerlIO::gzip provides a PerlIO layer that manipulates files in the format used
by the gzip program. Compression and Decompression are implemented, but not
together. If you attempt to open a file for reading and writing the open will
fail.

%prep
%setup -q -n %{upstream_name}-%{upstream_version}
%patch0 -p1 -b .fpons

%build
%{__perl} Makefile.PL INSTALLDIRS=vendor
%make

%check
%make test

%install
rm -rf %{buildroot}
%makeinstall_std

%clean
rm -rf %{buildroot}

%files
%defattr(-,root,root)
%doc README Changes
%{_mandir}/*/*
%{perl_vendorarch}/PerlIO
%{perl_vendorarch}/auto/PerlIO


%changelog
* Sun Jan 22 2012 Oden Eriksson <oeriksson@mandriva.com> 0.180.0-6mdv2012.0
+ Revision: 765592
- rebuilt for perl-5.14.2

* Sat Jan 21 2012 Oden Eriksson <oeriksson@mandriva.com> 0.180.0-5
+ Revision: 764105
- rebuilt for perl-5.14.x

* Wed May 04 2011 Oden Eriksson <oeriksson@mandriva.com> 0.180.0-4
+ Revision: 667291
- mass rebuild

* Sun Aug 01 2010 Funda Wang <fwang@mandriva.org> 0.180.0-3mdv2011.0
+ Revision: 564574
- rebuild for perl 5.12.1

* Tue Jul 20 2010 Jérôme Quelin <jquelin@mandriva.org> 0.180.0-2mdv2011.0
+ Revision: 556072
- rebuild for perl 5.12

* Mon Aug 03 2009 Jérôme Quelin <jquelin@mandriva.org> 0.180.0-1mdv2010.1
+ Revision: 407959
- rebuild using %%perl_convert_version

* Wed Jun 18 2008 Thierry Vignaud <tv@mandriva.org> 0.18-3mdv2009.0
+ Revision: 223954
- rebuild

* Tue Jan 15 2008 Thierry Vignaud <tv@mandriva.org> 0.18-2mdv2008.1
+ Revision: 152232
- rebuild
- kill re-definition of %%buildroot on Pixel's request

  + Olivier Blin <blino@mandriva.org>
    - restore BuildRoot


* Sat Dec 09 2006 Olivier Thauvin <nanardon@mandriva.org> 0.18-1mdv2007.0
+ Revision: 93976
- 0.18

* Tue Aug 08 2006 Olivier Thauvin <nanardon@mandriva.org> 0.17-4mdv2007.0
+ Revision: 53862
- rebuild
- Import perl-PerlIO-gzip

* Fri Feb 03 2006 Rafael Garcia-Suarez <rgarciasuarez@mandriva.com> 0.17-3mdk
- Rebuild, spec cleanup

* Mon Nov 15 2004 Rafael Garcia-Suarez <rgarciasuarez@mandrakesoft.com> 0.17-2mdk
- Rebuild for new perl

* Thu Jul 01 2004 Rafael Garcia-Suarez <rgarciasuarez@mandrakesoft.com> 0.17-1mdk
- 0.17.

* Wed Apr 14 2004 Rafael Garcia-Suarez <rgarciasuarez@mandrakesoft.com> 0.15-3mdk
- rebuild for new perl

