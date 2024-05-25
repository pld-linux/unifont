#
# Conditional build:
%bcond_without	ttf	# TrueType fonts (3+GB RAM required)
%bcond_without	viewer	# unifont-viewer package (requires perl-Wx)

Summary:	GNU Unifont - Unicode bitmap font
Summary(pl.UTF-8):	GNU Unifont - font bitmapowy Unicode
Name:		unifont
Version:	15.1.05
Release:	1
License:	GPL v2+ (tools), SIL Open Font License v1.1 or GPL v2+ with GNU font embedding exception (fonts)
Group:		Fonts
Source0:	https://ftp.gnu.org/gnu/unifont/%{name}-%{version}/%{name}-%{version}.tar.gz
# Source0-md5:	9cf49d7398fe89f2e8e36ac8887d48d9
Patch0:		%{name}-info.patch
URL:		http://czyborra.com/unifont/
BuildRequires:	fontforge
BuildRequires:	rpm-build >= 4.6
BuildRequires:	rpm-perlprov
BuildRequires:	rpmbuild(macros) >= 1.752
BuildRequires:	sed >= 4.0
BuildRequires:	texinfo
BuildRequires:	xorg-app-bdftopcf
Requires(post,postun):	fontpostinst
Requires:	%{_fontsdir}/misc
BuildRoot:	%{tmpdir}/%{name}-%{version}-root-%(id -u -n)

%description
GNU Unifont is an official GNU package. It is a dual-width
(8x16/16x16) bitmap font, designed to provide coverage for all of
Unicode Plane 0, the Basic Multilingual Plane (BMP). This version has
a glyph for each visible code point in the Unicode 7.0 Basic
Multilingual Plane (Plane 0).

%description -l pl.UTF-8
GNU Unifont to oficjalny pakiet GNU. Jest to font bitmapowy podwójnej
szerokości (8x16/16x16), zaprojektowany z myślą o pokryciu całości
warstwy Unicode Plane 0 (Basic Multilingual Plane - BMP). Ta wersja
zawiera glify dla wszystkich widocznych znaków Unicode 7.0 Basic
Multilingual Plane (Plane 0).

%package -n fonts-misc-unifont
Summary:	GNU Unifont - Unicode font in PCF format
Summary(pl.UTF-8):	GNU Unifont - font Unicode w formacie PCF
License:	SIL Open Font License v1.1 or GPL v2+ with GNU font embedding exception (fonts)
Group:		Fonts
Requires(post,postun):	fontpostinst
Requires:	%{_fontsdir}/misc
Obsoletes:	unifont < 6
BuildArch:	noarch

%description -n fonts-misc-unifont
GNU Unifont is an official GNU package. It is a dual-width
(8x16/16x16) bitmap font, designed to provide coverage for all of
Unicode Plane 0, the Basic Multilingual Plane (BMP). This version has
a glyph for each visible code point in the Unicode 7.0 Basic
Multilingual Plane (Plane 0).

This package contains the font in PCF format.

%description -n fonts-misc-unifont -l pl.UTF-8
GNU Unifont to oficjalny pakiet GNU. Jest to font bitmapowy podwójnej
szerokości (8x16/16x16), zaprojektowany z myślą o pokryciu całości
warstwy Unicode Plane 0 (Basic Multilingual Plane - BMP). Ta wersja
zawiera glify dla wszystkich widocznych znaków Unicode 7.0 Basic
Multilingual Plane (Plane 0).

Ten pakiet zawiera font w formacie PCF.

%package -n fonts-OTF-unifont
Summary:	GNU Unifont - Unicode font in OpenType format
Summary(pl.UTF-8):	GNU Unifont - font Unicode w formacie OpenType
License:	SIL Open Font License v1.1 or GPL v2+ with GNU font embedding exception (fonts)
Group:		Fonts
Requires(post,postun):	fontpostinst
Requires:	%{_fontsdir}/OTF
BuildArch:	noarch

%description -n fonts-OTF-unifont
GNU Unifont is an official GNU package. It is a dual-width
(8x16/16x16) bitmap font, designed to provide coverage for all of
Unicode Plane 0, the Basic Multilingual Plane (BMP). This version has
a glyph for each visible code point in the Unicode 7.0 Basic
Multilingual Plane (Plane 0).

This package contains the font in OpenType format.

%description -n fonts-OTF-unifont -l pl.UTF-8
GNU Unifont to oficjalny pakiet GNU. Jest to font bitmapowy podwójnej
szerokości (8x16/16x16), zaprojektowany z myślą o pokryciu całości
warstwy Unicode Plane 0 (Basic Multilingual Plane - BMP). Ta wersja
zawiera glify dla wszystkich widocznych znaków Unicode 7.0 Basic
Multilingual Plane (Plane 0).

Ten pakiet zawiera font w formacie OpenType.

%package -n fonts-TTF-unifont
Summary:	GNU Unifont - Unicode font in TrueType format
Summary(pl.UTF-8):	GNU Unifont - font Unicode w formacie TrueType
License:	SIL Open Font License v1.1 or GPL v2+ with GNU font embedding exception (fonts)
Group:		Fonts
Requires(post,postun):	fontpostinst
Requires:	%{_fontsdir}/TTF
BuildArch:	noarch

%description -n fonts-TTF-unifont
GNU Unifont is an official GNU package. It is a dual-width
(8x16/16x16) bitmap font, designed to provide coverage for all of
Unicode Plane 0, the Basic Multilingual Plane (BMP). This version has
a glyph for each visible code point in the Unicode 7.0 Basic
Multilingual Plane (Plane 0).

This package contains the font in TrueType format.

%description -n fonts-TTF-unifont -l pl.UTF-8
GNU Unifont to oficjalny pakiet GNU. Jest to font bitmapowy podwójnej
szerokości (8x16/16x16), zaprojektowany z myślą o pokryciu całości
warstwy Unicode Plane 0 (Basic Multilingual Plane - BMP). Ta wersja
zawiera glify dla wszystkich widocznych znaków Unicode 7.0 Basic
Multilingual Plane (Plane 0).

Ten pakiet zawiera font w formacie TrueType.

%package console
Summary:	GNU Unifont - Unicode font in PSF format
Summary(pl.UTF-8):	GNU Unifont - font Unicode w formacie PSF
License:	SIL Open Font License v1.1 or GPL v2+ with GNU font embedding exception (fonts)
Group:		Fonts
Requires:	kbd
BuildArch:	noarch

%description console
GNU Unifont is an official GNU package. It is a dual-width
(8x16/16x16) bitmap font, designed to provide coverage for all of
Unicode Plane 0, the Basic Multilingual Plane (BMP). This version has
a glyph for each visible code point in the Unicode 7.0 Basic
Multilingual Plane (Plane 0).

This package contains 512 glyph subset in PSF format for use with
Linux console.

%description console -l pl.UTF-8
GNU Unifont to oficjalny pakiet GNU. Jest to font bitmapowy podwójnej
szerokości (8x16/16x16), zaprojektowany z myślą o pokryciu całości
warstwy Unicode Plane 0 (Basic Multilingual Plane - BMP). Ta wersja
zawiera glify dla wszystkich widocznych znaków Unicode 7.0 Basic
Multilingual Plane (Plane 0).

Ten pakiet zawiera 512-znakowy podzbiór w formacie PSF, przeznaczony
do używania na linuksowej konsoli.

%package source
Summary:	GNU Unifont source data
Summary(pl.UTF-8):	Dane źródłowe pakietu GNU Unifont
License:	GPL v2+ (tools), SIL Open Font License v1.1 or GPL v2+ with GNU font embedding exception (fonts)
Group:		Development/Tools
BuildArch:	noarch

%description source
GNU Unifont source data, which could be used to generate or embed
fonts in other formats.

%description source -l pl.UTF-8
Dane źródłowe pakietu GNU Unifont, które można wykorzystać do
generowania lub osadzania fontów w innych formatach.

%package tools
Summary:	GNU Unifont utility programs
Summary(pl.UTF-8):	Programy narzędziowe dołączone do pakietu GNU Unifont
License:	GPL v2+
Group:		Development/Tools

%description tools
GNU Unifont utility programs.

%description tools -l pl.UTF-8
Programy narzędziowe dołączone do pakietu GNU Unifont.

%package viewer
Summary:	GNU Unifont viewer
Summary(pl.UTF-8):	Przeglądarka GNU Unifont
License:	GPL v2+
Group:		X11/Applications

%description viewer
GNU Unifont viewer based on wxWidgets Perl interface.

%description viewer -l pl.UTF-8
Przeglądarka GNU Unifont oparta na interfejsie Perla do wxWidgets.

%prep
%setup -q
%patch0 -p1

%{__sed} -i -e '1s,/usr/bin/env perl,%{__perl},' src/{hexdraw,johab2ucs2}

# no need to regenerate with info patch (omit BR: texi2pdf)
touch doc/unifont.pdf

%build
%{__make} -C doc doc

%{__make} -j1 \
	CC="%{__cc}" \
	CFLAGS="%{rpmcflags} %{rpmcppflags} -Wall" \
	LDFLAGS="%{rpmldflags}"

%if %{with ttf}
%{__make} -C font -j1 truetype
# no need to rebuild other formats
cp -p font/precompiled/*.{bmp,hex,otf,pcf.gz,psf.gz} font/compiled
%endif

%install
rm -rf $RPM_BUILD_ROOT
install -d $RPM_BUILD_ROOT%{_fontsdir}/OTF

%{__make} install \
	DESTDIR=$RPM_BUILD_ROOT \
	USRDIR=usr \
	CONSOLEDEST=$RPM_BUILD_ROOT/lib/kbd/consolefonts \
	OTFDEST=$RPM_BUILD_ROOT%{_fontsdir}/OTF \
	PCFDEST=$RPM_BUILD_ROOT%{_fontsdir}/misc \
	TTFDEST=$RPM_BUILD_ROOT%{_fontsdir}/TTF

%if %{with ttf}
install -d $RPM_BUILD_ROOT%{_fontsdir}/TTF
for f in unifont unifont_csur unifont_jp unifont_upper ; do
	cp -p font/compiled/${f}-%{version}.ttf $RPM_BUILD_ROOT%{_fontsdir}/TTF/${f}.ttf
done
%endif

# sample covering plane 0
%{__rm} $RPM_BUILD_ROOT%{_fontsdir}/{misc/unifont_sample.pcf.gz,OTF/unifont*_sample.otf}

# doxygen documentation for unpackaged code
%{__rm} -r $RPM_BUILD_ROOT%{_datadir}/unifont/html
%{__rm} $RPM_BUILD_ROOT%{_datadir}/unifont/unifont-doxy.pdf

# generated from texi
%{__rm} $RPM_BUILD_ROOT%{_datadir}/unifont/unifont.{pdf,txt.gz}
# move to standard place
install -d $RPM_BUILD_ROOT%{_infodir}
%{__mv} $RPM_BUILD_ROOT%{_datadir}/unifont/unifont.info* $RPM_BUILD_ROOT%{_infodir}

%clean
rm -rf $RPM_BUILD_ROOT

%post	-n fonts-misc-unifont
fontpostinst misc

%postun	-n fonts-misc-unifont
fontpostinst misc

%post	-n fonts-OTF-unifont
fontpostinst OTF

%postun	-n fonts-OTF-unifont
fontpostinst OTF

%post	-n fonts-TTF-unifont
fontpostinst TTF

%postun	-n fonts-TTF-unifont
fontpostinst TTF

%post	tools -p /sbin/postshell
-/usr/sbin/fix-info-dir -c %{_infodir}

%postun	tools -p /sbin/postshell
-/usr/sbin/fix-info-dir -c %{_infodir}

%files -n fonts-misc-unifont
%defattr(644,root,root,755)
%doc COPYING ChangeLog NEWS README
%{_fontsdir}/misc/unifont.pcf.gz
%{_fontsdir}/misc/unifont_csur.pcf.gz
%{_mandir}/man5/unifont.5*

%files -n fonts-OTF-unifont
%defattr(644,root,root,755)
%doc COPYING ChangeLog NEWS README
%{_fontsdir}/OTF/unifont.otf
%{_fontsdir}/OTF/unifont_csur.otf
%{_fontsdir}/OTF/unifont_jp.otf
%{_fontsdir}/OTF/unifont_upper.otf

%if %{with ttf}
%files -n fonts-TTF-unifont
%defattr(644,root,root,755)
%doc COPYING ChangeLog NEWS README
%{_fontsdir}/TTF/unifont.ttf
%{_fontsdir}/TTF/unifont_csur.ttf
%{_fontsdir}/TTF/unifont_jp.ttf
%{_fontsdir}/TTF/unifont_upper.ttf
%endif

%files console
%defattr(644,root,root,755)
/lib/kbd/consolefonts/Unifont-APL8x16.psf.gz

%files source
%defattr(644,root,root,755)
%doc COPYING ChangeLog NEWS README
%dir %{_datadir}/unifont
%{_datadir}/unifont/plane00-combining.txt
%{_datadir}/unifont/unifont.bmp.gz
%{_datadir}/unifont/unifont.hex
%{_datadir}/unifont/unifont_all.hex
%{_datadir}/unifont/unifont_jp.hex
%{_datadir}/unifont/wchardata.c

%files tools
%defattr(644,root,root,755)
%attr(755,root,root) %{_bindir}/bdfimplode
%attr(755,root,root) %{_bindir}/hex2bdf
%attr(755,root,root) %{_bindir}/hex2otf
%attr(755,root,root) %{_bindir}/hex2sfd
%attr(755,root,root) %{_bindir}/hexbraille
%attr(755,root,root) %{_bindir}/hexdraw
%attr(755,root,root) %{_bindir}/hexkinya
%attr(755,root,root) %{_bindir}/hexmerge
%attr(755,root,root) %{_bindir}/johab2syllables
%attr(755,root,root) %{_bindir}/johab2ucs2
%attr(755,root,root) %{_bindir}/unibdf2hex
%attr(755,root,root) %{_bindir}/unibmp2hex
%attr(755,root,root) %{_bindir}/unibmpbump
%attr(755,root,root) %{_bindir}/unicoverage
%attr(755,root,root) %{_bindir}/unidup
%attr(755,root,root) %{_bindir}/unifont1per
%attr(755,root,root) %{_bindir}/unifontchojung
%attr(755,root,root) %{_bindir}/unifontksx
%attr(755,root,root) %{_bindir}/unifontpic
%attr(755,root,root) %{_bindir}/unigen-hangul
%attr(755,root,root) %{_bindir}/unigencircles
%attr(755,root,root) %{_bindir}/unigenwidth
%attr(755,root,root) %{_bindir}/unihex2bmp
%attr(755,root,root) %{_bindir}/unihex2png
%attr(755,root,root) %{_bindir}/unihexfill
%attr(755,root,root) %{_bindir}/unihexgen
%attr(755,root,root) %{_bindir}/unihexpose
%attr(755,root,root) %{_bindir}/unihexrotate
%attr(755,root,root) %{_bindir}/unijohab2html
%attr(755,root,root) %{_bindir}/unipagecount
%attr(755,root,root) %{_bindir}/unipng2hex
%{_mandir}/man1/bdfimplode.1*
%{_mandir}/man1/hex2bdf.1*
%{_mandir}/man1/hex2otf.1*
%{_mandir}/man1/hex2sfd.1*
%{_mandir}/man1/hexbraille.1*
%{_mandir}/man1/hexdraw.1*
%{_mandir}/man1/hexkinya.1*
%{_mandir}/man1/hexmerge.1*
%{_mandir}/man1/johab2syllables.1*
%{_mandir}/man1/johab2ucs2.1*
%{_mandir}/man1/unibdf2hex.1*
%{_mandir}/man1/unibmp2hex.1*
%{_mandir}/man1/unibmpbump.1*
%{_mandir}/man1/unicoverage.1*
%{_mandir}/man1/unidup.1*
%{_mandir}/man1/unifont1per.1*
%{_mandir}/man1/unifontchojung.1*
%{_mandir}/man1/unifontksx.1*
%{_mandir}/man1/unifontpic.1*
%{_mandir}/man1/unigen-hangul.1*
%{_mandir}/man1/unigencircles.1*
%{_mandir}/man1/unigenwidth.1*
%{_mandir}/man1/unihex2bmp.1*
%{_mandir}/man1/unihex2png.1*
%{_mandir}/man1/unihexfill.1*
%{_mandir}/man1/unihexgen.1*
%{_mandir}/man1/unihexpose.1*
%{_mandir}/man1/unihexrotate.1*
%{_mandir}/man1/unijohab2html.1*
%{_mandir}/man1/unipagecount.1*
%{_mandir}/man1/unipng2hex.1*
%{_mandir}/man5/unifont-johab631.5*
%{_infodir}/unifont.info*

%if %{with viewer}
%files viewer
%defattr(644,root,root,755)
%attr(755,root,root) %{_bindir}/unifont-viewer
%{_mandir}/man1/unifont-viewer.1*
%endif
