%define real_name PerlIO-gzip
%define name perl-%real_name
%define version 0.18
%define release %mkrel 1

Summary:	Perl extension to provide a PerlIO layer to gzip/gunzip
Name:		%{name}
Version:	%{version}
Release:	%{release}
License:	GPL or Artistic
Group:		Development/Perl
Source:		http://www.cpan.org/authors/id/N/NW/NWCLARK/%{real_name}-%{version}.tar.bz2
Patch:		%{real_name}-0.14-no_strict_warnings.patch
URL:		http://search.cpan.org/dist/%{real_name}/
BuildRequires:	perl-devel zlib-devel
BuildRoot:	%{_tmppath}/%{name}-buildroot

%description
PerlIO::gzip provides a PerlIO layer that manipulates files in the format used
by the gzip program. Compression and Decompression are implemented, but not
together. If you attempt to open a file for reading and writing the open will
fail.

%prep
%setup -q -n %{real_name}-%{version}
%patch -p1 -b .fpons

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



