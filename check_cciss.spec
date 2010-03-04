Name: check_cciss
Version: 1.1
Release: 1.era

Summary: check_cciss
License: GPL
Group: System/Monitoring
Url: http://github.com/erasme/check_ccissc/

Source: http://github.com/downloads/erasme/check_cciss/%name-%version.tar.gz

BuildRoot:      %{_tmppath}/%{name}-%{version}-%{release}-root-%(%{__id_u} -n)
BuildArch: noarch

Requires: hpacucli

%description
%name is a HP array check utility. It will compare
current array status with a reference status saved in
/etc/cciss/normal_state. It requires hpacucli.

%prep
%setup -q -n %name-%version

%build

%install
rm -rf $RPM_BUILD_ROOT

mkdir -p $RPM_BUILD_ROOT/%{_sbindir}
install check_cciss $RPM_BUILD_ROOT%{_sbindir}/

%post
if [ ! -L /etc/cron.hourly/check_cciss ]; then ln -s %{_sbindir}/check_cciss /etc/cron.hourly/check_cciss; fi
%{_sbindir}/check_cciss -i

%postun
rm /etc/cron.hourly/check_cciss

%files
%_sbindir/*
%doc README

%changelog		   
* Thu Feb 04 2010 Michel Blanc <mblanc@erasme.org> 1.0-1.era
- First packaged for CentOS

