Name: hunspell-it
Summary: Italian hunspell dictionaries
%define upstreamid 20070901
Version: 2.4
Release: 0.3.%{upstreamid}.1%{?dist}
Source: http://downloads.sourceforge.net/sourceforge/linguistico/italiano_2_4_2007_09_01.zip
Group: Applications/Text
URL: http://linguistico.sourceforge.net
BuildRoot: %{_tmppath}/%{name}-%{version}-%{release}-root-%(%{__id_u} -n)
License: GPLv2+
BuildArch: noarch

Requires: hunspell

%description
Italian hunspell dictionaries.

%prep
%setup -q -c -n hunspell-it

%build
chmod -x *

%install
rm -rf $RPM_BUILD_ROOT
mkdir -p $RPM_BUILD_ROOT/%{_datadir}/myspell
cp -p *.dic *.aff $RPM_BUILD_ROOT/%{_datadir}/myspell
pushd $RPM_BUILD_ROOT/%{_datadir}/myspell/
it_IT_aliases="it_CH"
for lang in $it_IT_aliases; do
        ln -s it_IT.aff $lang.aff
        ln -s it_IT.dic $lang.dic
done


%clean
rm -rf $RPM_BUILD_ROOT

%files
%defattr(-,root,root,-)
%doc it_IT_README.txt it_IT_COPYING it_IT_AUTHORS it_IT_license.txt it_IT_notes.txt
%{_datadir}/myspell/*

%changelog
* Mon Nov 30 2009 Dennis Gregorovic <dgregor@redhat.com> - 2.4-0.3.20070901.1
- Rebuilt for RHEL 6

* Fri Jul 24 2009 Fedora Release Engineering <rel-eng@lists.fedoraproject.org> - 2.4-0.3.20070901
- Rebuilt for https://fedoraproject.org/wiki/Fedora_12_Mass_Rebuild

* Tue Feb 24 2009 Fedora Release Engineering <rel-eng@lists.fedoraproject.org> - 2.4-0.2.20070901
- Rebuilt for https://fedoraproject.org/wiki/Fedora_11_Mass_Rebuild

* Mon Sep 03 2007 Caolan McNamara <caolanm@redhat.com> - 2.4-0.1.20070901
- latest version

* Fri Aug 03 2007 Caolan McNamara <caolanm@redhat.com> - 2.3-0.2.20060723
- clarify license version

* Thu Dec 07 2006 Caolan McNamara <caolanm@redhat.com> - 2.3-0.1.20060723
- initial version
