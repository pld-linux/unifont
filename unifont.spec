Summary:	Unicode font by Roman Czyborra
Summary(pl):	Font unicode Romana Czyborry
Name:		unifont
Version:	1.0
Release:	1
License:	GPL
Group:		X11/Fonts
Source0:	http://czyborra.com/unifont/%{name}.hex.gz
# Source0-md5:	4a1df5242ba65b968bcf7be87f70f1b2
Source1:	hex2bdf
BuildRequires:	XFree86-devel
Prereq:		/usr/X11R6/bin/mkfontdir
BuildArch:	noarch
BuildRoot:	%{tmpdir}/%{name}-%{version}-root-%(id -u -n)


%description
Unicode font by Roman Czyborra.

%description -l pl
Font unicode Romana Czyborry.

%prep
%setup -q -T -c

%build
gzip -dc %{SOURCE0} | %{SOURCE1} | bdftopcf | gzip -c - > unifont.pcf.gz

%install
rm -rf $RPM_BUILD_ROOT
install -d $RPM_BUILD_ROOT%{_datadir}/fonts/misc

install unifont.pcf.gz $RPM_BUILD_ROOT%{_datadir}/fonts/misc

%clean
rm -rf $RPM_BUILD_ROOT

%post
cd %{_datadir}/fonts/misc
umask 022
mkfontdir

%postun
cd %{_datadir}/fonts/misc
umask 022
mkfontdir

%files
%defattr(644,root,root,755)
%{_datadir}/fonts/misc/*
