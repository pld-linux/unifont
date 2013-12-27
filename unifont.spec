Summary:	GNU Unifont - Unicode bitmap font
Summary(pl.UTF-8):	GNU Unifont - font bitmapowy Unicode
Name:		unifont
Version:	6.3.20131221
Release:	1
License:	GPL v2+ with GNU font embedding exception
Group:		Fonts
Source0:	http://ftp.gnu.org/gnu/unifont/%{name}-%{version}/%{name}-%{version}.tar.gz
# Source0-md5:	56296ae1eca1b3753933358472166777
URL:		http://czyborra.com/unifont/
BuildRequires:	fontforge
BuildRequires:	xorg-app-bdftopcf
Requires(post,postun):	fontpostinst
Requires:	%{_fontsdir}/misc
BuildRoot:	%{tmpdir}/%{name}-%{version}-root-%(id -u -n)

%description
GNU Unifont is an official GNU package. It is a dual-width
(8x16/16x16) bitmap font, designed to provide coverage for all of
Unicode Plane 0, the Basic Multilingual Plane (BMP). This version has
a glyph for each visible code point in the Unicode 6.3 Basic
Multilingual Plane (Plane 0).

%description -l pl.UTF-8
GNU Unifont to oficjalny pakiet GNU. Jest to font bitmapowy podwójnej
szerokości (8x16/16x16), zaprojektowany z myślą o pokryciu całości
warstwy Unicode Plane 0 (Basic Multilingual Plane - BMP). Ta wersja
zawiera glify dla wszystkich widocznych znaków Unicode 6.3 Basic
Multilingual Plane (Plane 0).

%package -n fonts-misc-unifont
Summary:	GNU Unifont - Unicode font in PCF format
Summary(pl.UTF-8):	GNU Unifont - font Unicode w formacie PCF
Group:		Fonts
Requires(post,postun):	fontpostinst
Requires:	%{_fontsdir}/misc
Obsoletes:	unifont
%if "%{_rpmversion}" >= "5"
BuildArch:	noarch
%endif

%description -n fonts-misc-unifont
GNU Unifont is an official GNU package. It is a dual-width
(8x16/16x16) bitmap font, designed to provide coverage for all of
Unicode Plane 0, the Basic Multilingual Plane (BMP). This version has
a glyph for each visible code point in the Unicode 6.3 Basic
Multilingual Plane (Plane 0).

This package contains the font in PCF format.

%description -n fonts-misc-unifont -l pl.UTF-8
GNU Unifont to oficjalny pakiet GNU. Jest to font bitmapowy podwójnej
szerokości (8x16/16x16), zaprojektowany z myślą o pokryciu całości
warstwy Unicode Plane 0 (Basic Multilingual Plane - BMP). Ta wersja
zawiera glify dla wszystkich widocznych znaków Unicode 6.3 Basic
Multilingual Plane (Plane 0).

Ten pakiet zawiera font w formacie PCF.

%package -n fonts-TTF-unifont
Summary:	GNU Unifont - Unicode font in PCF format
Summary(pl.UTF-8):	GNU Unifont - font Unicode w formacie PCF
Group:		Fonts
Requires(post,postun):	fontpostinst
Requires:	%{_fontsdir}/TTF
%if "%{_rpmversion}" >= "5"
BuildArch:	noarch
%endif

%description -n fonts-TTF-unifont
GNU Unifont is an official GNU package. It is a dual-width
(8x16/16x16) bitmap font, designed to provide coverage for all of
Unicode Plane 0, the Basic Multilingual Plane (BMP). This version has
a glyph for each visible code point in the Unicode 6.3 Basic
Multilingual Plane (Plane 0).

This package contains the font in TTF format.

%description -n fonts-TTF-unifont -l pl.UTF-8
GNU Unifont to oficjalny pakiet GNU. Jest to font bitmapowy podwójnej
szerokości (8x16/16x16), zaprojektowany z myślą o pokryciu całości
warstwy Unicode Plane 0 (Basic Multilingual Plane - BMP). Ta wersja
zawiera glify dla wszystkich widocznych znaków Unicode 6.3 Basic
Multilingual Plane (Plane 0).

Ten pakiet zawiera font w formacie TTF.

%package tools
Summary:	GNU Unifont utility programs
Summary(pl.UTF-8):	Programy narzędziowe dołączone do pakietu GNU Unifont
Group:		Development/Tools

%description tools
GNU Unifont utility programs.

%description tools -l pl.UTF-8
Programy narzędziowe dołączone do pakietu GNU Unifont.

%prep
%setup -q

%build
%{__make} -j1 \
	CC="%{__cc}" \
	CFLAGS="%{rpmcflags} %{rpmcppflags} -Wall" \
	LDFLAGS="%{rpmldflags}"

%install
rm -rf $RPM_BUILD_ROOT

%{__make} install \
	DESTDIR=$RPM_BUILD_ROOT \
	USRDIR=usr \
	PCFDEST=$RPM_BUILD_ROOT%{_fontsdir}/misc \
	TTFDEST=$RPM_BUILD_ROOT%{_fontsdir}/TTF

# source data not needed, docs packaged as %doc
%{__rm} -r $RPM_BUILD_ROOT%{_datadir}/unifont
# sample covering plane 0
%{__rm} $RPM_BUILD_ROOT%{_fontsdir}/{misc/unifont_sample.pcf.gz,TTF/unifont_sample.ttf}

%clean
rm -rf $RPM_BUILD_ROOT

%post	-n fonts-misc-unifont
fontpostinst misc

%postun	-n fonts-misc-unifont
fontpostinst misc

%post	-n fonts-TTF-unifont
fontpostinst TTF

%postun	-n fonts-TTF-unifont
fontpostinst TTF

%files -n fonts-misc-unifont
%defattr(644,root,root,755)
%doc README
%{_fontsdir}/misc/unifont.pcf.gz
%{_mandir}/man5/unifont.5*

%files -n fonts-TTF-unifont
%defattr(644,root,root,755)
%{_fontsdir}/TTF/unifont.ttf

%files tools
%defattr(644,root,root,755)
%attr(755,root,root) %{_bindir}/bdfimplode
%attr(755,root,root) %{_bindir}/hex2bdf
%attr(755,root,root) %{_bindir}/hex2sfd
%attr(755,root,root) %{_bindir}/hexbraille
%attr(755,root,root) %{_bindir}/hexdraw
%attr(755,root,root) %{_bindir}/hexmerge
%attr(755,root,root) %{_bindir}/johab2ucs2
%attr(755,root,root) %{_bindir}/unibdf2hex
%attr(755,root,root) %{_bindir}/unibmp2hex
%attr(755,root,root) %{_bindir}/unicoverage
%attr(755,root,root) %{_bindir}/unidup
%attr(755,root,root) %{_bindir}/unifontchojung
%attr(755,root,root) %{_bindir}/unifontksx
%attr(755,root,root) %{_bindir}/unifontpic
%attr(755,root,root) %{_bindir}/unigencircles
%attr(755,root,root) %{_bindir}/unigenwidth
%attr(755,root,root) %{_bindir}/unihex2bmp
%attr(755,root,root) %{_bindir}/unihex2png
%attr(755,root,root) %{_bindir}/unihexgen
%attr(755,root,root) %{_bindir}/unipagecount
%attr(755,root,root) %{_bindir}/unipng2hex
%{_mandir}/man1/bdfimplode.1*
%{_mandir}/man1/hex2bdf.1*
%{_mandir}/man1/hex2sfd.1*
%{_mandir}/man1/hexbraille.1*
%{_mandir}/man1/hexdraw.1*
%{_mandir}/man1/hexmerge.1*
%{_mandir}/man1/johab2ucs2.1*
%{_mandir}/man1/unibdf2hex.1*
%{_mandir}/man1/unibmp2hex.1*
%{_mandir}/man1/unicoverage.1*
%{_mandir}/man1/unidup.1*
%{_mandir}/man1/unifontchojung.1*
%{_mandir}/man1/unifontksx.1*
%{_mandir}/man1/unifontpic.1*
%{_mandir}/man1/unigencircles.1*
%{_mandir}/man1/unigenwidth.1*
%{_mandir}/man1/unihex2bmp.1*
%{_mandir}/man1/unihex2png.1*
%{_mandir}/man1/unihexgen.1*
%{_mandir}/man1/unipagecount.1*
%{_mandir}/man1/unipng2hex.1*
