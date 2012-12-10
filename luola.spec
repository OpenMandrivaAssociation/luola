%define name	luola
%define version	1.3.2
%define release	%mkrel 6
%define Summary	Fly a small V shaped ship in a 2D arcade game

Summary:	%{Summary}
Name:		%{name}
Version:	%{version}
Release:	%{release}
Source0:	http://www.luolamies.org/software/luola/%{name}-%{version}.tar.bz2
Source1:    http://luolamies.org/software/luola/stdlevels-6.0.tar.gz
License:	GPLv2+
Group:		Games/Arcade
URL:		http://www.luolamies.org/software/luola/
BuildRoot:	%{_tmppath}/%{name}-%{version}-%{release}-buildroot
BuildRequires:	imagemagick SDL-devel SDL_image-devel SDL_mixer-devel
BuildRequires:	zlib-devel
%description
Luola is a 2D arcade game where you fly a small V shaped ship in different
kinds of levels. It's genre "Luolalentely" (Cave-flying) is (or was) very
popular in Finland. Though cavern-flying games are not originally
Finnish, nowdays most of them are.

%prep
%setup -q
tar -xf %{SOURCE1} -C data/levels

%build
export LDFLAGS="-lm"
%configure2_5x	--bindir=%{_gamesbindir} --enable-sdl-gfx --datadir=%{_gamesdatadir} --enable-sound
%make

%install
%{makeinstall_std} datadir=%{_gamesdatadir}
install -m644 data/levels/*.{png,lev} %{buildroot}%_gamesdatadir/%name/levels/

#Menu items
mkdir -p %{buildroot}%{_datadir}/applications/
cat << EOF > %{buildroot}%{_datadir}/applications/mandriva-%{name}.desktop
[Desktop Entry]
Type=Application
Exec=%{_gamesbindir}/%{name}
Icon=%{name}
Categories=Game;ArcadeGame;
Name=Luola
Comment=%{Summary}
EOF
#Icons
install -d %{buildroot}{%{_iconsdir},%{_miconsdir},%{_liconsdir}}
convert -size 32x32 %{name}.png %{buildroot}%{_iconsdir}/%{name}.png
convert -size 48x48 %{name}.png %{buildroot}%{_liconsdir}/%{name}.png
convert -size 16x16 %{name}.png %{buildroot}%{_miconsdir}/%{name}.png

%files
%defattr(-, root, root)
%doc README AUTHORS
%{_gamesbindir}/*
%{_gamesdatadir}/%{name}
%{_datadir}/applications/mandriva-%{name}.desktop
%{_miconsdir}/%{name}.png
%{_iconsdir}/%{name}.png
%{_liconsdir}/%{name}.png



%changelog
* Mon Sep 14 2009 Thierry Vignaud <tvignaud@mandriva.com> 1.3.2-6mdv2010.0
+ Revision: 439676
- rebuild

* Sun Mar 29 2009 Michael Scherer <misc@mandriva.org> 1.3.2-5mdv2009.1
+ Revision: 362153
- add missing buildRequires
- add new complete tarball of levels, fix #49276

  + Oden Eriksson <oeriksson@mandriva.com>
    - lowercase ImageMagick

* Mon Jul 28 2008 Thierry Vignaud <tvignaud@mandriva.com> 1.3.2-4mdv2009.0
+ Revision: 251560
- rebuild

  + Pixel <pixel@mandriva.com>
    - rpm filetriggers deprecates update_menus/update_scrollkeeper/update_mime_database/update_icon_cache/update_desktop_database/post_install_gconf_schemas

* Fri Jan 25 2008 Funda Wang <fundawang@mandriva.org> 1.3.2-2mdv2008.1
+ Revision: 157785
- fix desktop entry

  + Olivier Blin <oblin@mandriva.com>
    - restore BuildRoot

* Tue Dec 18 2007 Thierry Vignaud <tvignaud@mandriva.com> 1.3.2-1mdv2008.1
+ Revision: 132318
- auto-convert XDG menu entry
- kill re-definition of %%buildroot on Pixel's request
- import luola


* Mon Feb 06 2006 Lenny Cartier <lenny@mandriva.com> 1.3.2-1mdk
- 1.3.2

* Wed Dec 21 2005 Lenny Cartier <lenny@mandriva.com> 1.3.0-1mdk
- 1.3.0

* Mon Apr 11 2005 Lenny Cartier <lenny@mandrakesoft.com> 1.2.7-1mdk
- 1.2.7

* Mon Jan 17 2005 Lenny Cartier <lenny@mandrakesoft.com> 1.2.6-1mdk
- 1.2.6

* Sun Jan 02 2005 Per Øyvind Karlsen <peroyvind@linux-mandrake.com> 1.2.5-1mdk
- 1.2.5
- drop packager tag
- change icons

* Mon Dec 20 2004 Lenny Cartier <lenny@mandrakesoft.com> 1.2.3-1mdk
- 1.2.3

* Sun Dec 05 2004 Lenny Cartier <lenny@mandrakesoft.com> 1.2.2-1mdk
- 1.2.2

* Sat Dec 20 2003 Lenny Cartier <lenny@mandrakesoft.com> 1.2.1-1mdk
- 1.2.1

* Mon Aug 04 2003 Per Øyvind Karlsen <peroyvind@linux-mandrake.com> 1.2.0-1mdk
- 1.2.0

* Fri Jul 25 2003 Per Øyvind Karlsen <peroyvind@sintrax.net> 1.1.7-2mdk
- rebuild
- use %%{_gamesdatadir}
- change summary macro to avoid possible conflicts if we were to build debug package

* Mon Jun 23 2003 Lenny Cartier <lenny@mandrakesoft.com> 1.1.7-1mdk
- 1.1.7

* Fri Jun 06 2003 Lenny Cartier <lenny@mandrakesoft.com> 1.1.6-1mdk
- 1.1.6

* Tue Jun 03 2003 Per Øyvind Karlsen <peroyvind@sintrax.net> 1.1.5-2mdk
- use %%configure2_5x macro

* Tue Jun 03 2003 Lenny Cartier <lenny@mandrakesoft.com> 1.1.5-1mdk
- 1.1.5

* Fri Apr 04 2003 Lenny Cartier <lenny@mandrakesoft.com> 1.1.0-1mdk
- 1.1.0

* Fri Dec 06 2002 Lenny Cartier <lenny@mandrakesoft.com> 1.0.2-1mdk
- 1.0.2

* Mon Dec 02 2002 Lenny Cartier <lenny@mandrakesoft.com> 1.0.1-1mdk
- 1.0.1

* Mon Nov 11 2002 Per Øyvind Karlsen <peroyvind@delonic.no> 0.9.9-1mdk
- 0.9.9
- Move stuff to correct places
- Add levels(they were split from the sourcecode package in 0.9.9)
- Updated description(we don't live in Finland, now do we?;)
- Add menuitem
- Add icons
- Updated build stage

* Thu Sep 05 2002 Lenny Cartier <lenny@mandrakesoft.com> 0.9.7-4mdk
- rebuild

* Sun Jul 21 2002 Guillaume Cottenceau <gc@mandrakesoft.com> 0.9.7-3mdk
- recompile against new vorbis stuff

* Mon Apr 29 2002 Guillaume Cottenceau <gc@mandrakesoft.com> 0.9.7-2mdk
- rebuild for new alsa

* Thu Mar 14 2002 Guillaume Cottenceau <gc@mandrakesoft.com> 0.9.7-1mdk
- first mdk package
