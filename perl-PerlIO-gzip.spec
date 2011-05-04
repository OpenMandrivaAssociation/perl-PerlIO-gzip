%define upstream_name    PerlIO-gzip
%define upstream_version 0.18

Name:       perl-%{upstream_name}
Version:    %perl_convert_version %{upstream_version}
Release:    %mkrel 4

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
rm -rf $RPM_BUILD_ROOT
%makeinstall_std

%clean
rm -rf $RPM_BUILD_ROOT

%files
%defattr(-,root,root)
%doc README Changes
%{_mandir}/*/*
%{perl_vendorarch}/PerlIO
%{perl_vendorarch}/auto/PerlIO
