%define		_class		Math
%define		_subclass	Stats
%define		upstream_name	%{_class}_%{_subclass}
%define		pre	beta3

Name:		php-pear-%{upstream_name}
Version:	0.9.0
Release:	17
Summary:	Classes to calculate statistical parameters
License:	PHP License
Group:		Development/PHP
URL:		https://pear.php.net/package/Math_Stats/
Source0:	http://download.pear.php.net/package/%{upstream_name}-%{version}beta3.tar.bz2
Requires(post): php-pear
Requires(preun): php-pear
Requires:	php-pear
BuildArch:	noarch
BuildRequires:	php-pear

%description
Classes to calculate statistical parameters of numerical arrays of
data. The data can be in a simple numerical array, or in a cummulative
numerical array. A cummulative array, has the value as the index and
the number of repeats as the value for the array item, e.g. $data =
array(3=>4, 2.3=>5, 1.25=>6, 0.5=>3). Nulls can be rejected, ignored
or handled as zero values.

%prep
%setup -q -c
mv package.xml %{upstream_name}-%{version}%{pre}/%{upstream_name}.xml

%install

cd %{upstream_name}-%{version}%{pre}
pear install --nodeps --packagingroot %{buildroot} %{upstream_name}.xml
rm -rf %{buildroot}%{_datadir}/pear/.??*

rm -rf %{buildroot}%{_datadir}/pear/docs
rm -rf %{buildroot}%{_datadir}/pear/tests
rm -rf %{buildroot}%{_datadir}/pear/%{_class}/examples
rm -rf %{buildroot}%{_datadir}/pear/%{_class}/test

install -d %{buildroot}%{_datadir}/pear/packages
install -m 644 %{upstream_name}.xml %{buildroot}%{_datadir}/pear/packages

%clean



%files
%defattr(-,root,root)
%doc %{upstream_name}-%{version}beta3/README*
%doc %{upstream_name}-%{version}beta3/examples
%{_datadir}/pear/%{_class}
%{_datadir}/pear/packages/%{upstream_name}.xml


%changelog
* Fri Dec 16 2011 Oden Eriksson <oeriksson@mandriva.com> 0.9.0-15mdv2012.0
+ Revision: 742119
- fix major breakage by careless packager

* Fri May 27 2011 Oden Eriksson <oeriksson@mandriva.com> 0.9.0-14
+ Revision: 679403
- mass rebuild

* Tue Dec 07 2010 Oden Eriksson <oeriksson@mandriva.com> 0.9.0-13mdv2011.0
+ Revision: 613717
- the mass rebuild of 2010.1 packages

* Sat Dec 12 2009 Guillaume Rousse <guillomovitch@mandriva.org> 0.9.0-12mdv2010.1
+ Revision: 477968
- don't ship tests and examples in pear tree

* Wed Nov 25 2009 Guillaume Rousse <guillomovitch@mandriva.org> 0.9.0-11mdv2010.1
+ Revision: 470161
- spec cleanup
- use pear installer
- don't ship tests, even in documentation
- own all directories
- use rpm filetriggers starting from mandriva 2010.1

* Tue Sep 15 2009 Thierry Vignaud <tv@mandriva.org> 0.9.0-10mdv2010.0
+ Revision: 441347
- rebuild

* Thu Jan 01 2009 Oden Eriksson <oeriksson@mandriva.com> 0.9.0-9mdv2009.1
+ Revision: 322368
- rebuild

* Thu Jul 17 2008 Oden Eriksson <oeriksson@mandriva.com> 0.9.0-8mdv2009.0
+ Revision: 236970
- rebuild

  + Olivier Blin <blino@mandriva.org>
    - restore BuildRoot

  + Thierry Vignaud <tv@mandriva.org>
    - kill re-definition of %%buildroot on Pixel's request


* Sat Nov 11 2006 Oden Eriksson <oeriksson@mandriva.com> 0.9.0-7mdv2007.0
+ Revision: 82201
- Import php-pear-Math_Stats

* Fri Feb 10 2006 Oden Eriksson <oeriksson@mandriva.com> 0.9.0-7mdk
- new group (Development/PHP)

* Fri Aug 26 2005 Oden Eriksson <oeriksson@mandriva.com> 0.9.0-6mdk
- rebuilt to fix auto deps

* Wed Aug 10 2005 Oden Eriksson <oeriksson@mandriva.com> 0.9.0-5mdk
- rebuilt to use new pear auto deps/reqs from pld

* Sun Jul 31 2005 Oden Eriksson <oeriksson@mandriva.com> 0.9.0-4mdk
- fix deps

* Thu Jul 21 2005 Oden Eriksson <oeriksson@mandriva.com> 0.9.0-3mdk
- reworked the %%post and %%preun stuff, like in conectiva
- fix deps

* Wed Jul 20 2005 Oden Eriksson <oeriksson@mandriva.com> 0.9.0-2mdk
- fix deps

* Tue Jul 19 2005 Oden Eriksson <oeriksson@mandriva.com> 0.9.0-1mdk
- initial Mandriva package (PLD import)

