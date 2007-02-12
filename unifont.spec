Summary:	Unicode font by Roman Czyborra
Summary(pl.UTF-8):	Font unicode Romana Czyborry
Name:		unifont
Version:	1.0
Release:	2
License:	GPL
Group:		Fonts
Source0:	http://czyborra.com/unifont/%{name}.hex.gz
# Source0-md5:	4a1df5242ba65b968bcf7be87f70f1b2
Source1:	hex2bdf
BuildRequires:	xorg-app-bdftopcf
Requires(post,postun):	fontpostinst
Requires:	%{_fontsdir}/misc
BuildArch:	noarch
BuildRoot:	%{tmpdir}/%{name}-%{version}-root-%(id -u -n)

%description
Unicode font by Roman Czyborra.

%description -l pl.UTF-8
Font unicode Romana Czyborry.

%prep
%setup -q -T -c

%build
gzip -dc %{SOURCE0} | %{SOURCE1} | bdftopcf | gzip -c - > unifont.pcf.gz

%install
rm -rf $RPM_BUILD_ROOT
install -d $RPM_BUILD_ROOT%{_fontsdir}/misc

install unifont.pcf.gz $RPM_BUILD_ROOT%{_fontsdir}/misc

%clean
rm -rf $RPM_BUILD_ROOT

%post
fontpostinst misc

%postun
fontpostinst misc

%files
%defattr(644,root,root,755)
%{_fontsdir}/misc/*
