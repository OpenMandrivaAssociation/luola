%define name	luola
%define version	1.3.2
%define release	%mkrel 2
%define Summary	Fly a small V shaped ship in a 2D arcade game

Summary:	%{Summary}
Name:		%{name}
Version:	%{version}
Release:	%{release}
Source0:	http://www.luolamies.org/software/luola/%{name}-%{version}.tar.bz2
Source1:	%{name}.stdlevels.tar.bz2
Source2:	%{name}.demolevel.tar.bz2
License:	GPLv2+
Group:		Games/Arcade
URL:		http://www.luolamies.org/software/luola/
BuildRoot:	%{_tmppath}/%{name}-%{version}-%{release}-buildroot
BuildRequires:	ImageMagick SDL-devel SDL_image-devel SDL_mixer-devel

%description
Luola is a 2D arcade game where you fly a small V shaped ship in different
kinds of levels. It's genre "Luolalentely" (Cave-flying) is (or was) very
popular in Finland. Though cavern-flying games are not originally
Finnish, nowdays most of them are.

%prep
%setup -q
tar -jxf %{SOURCE1} -C data/levels
tar -jxf %{SOURCE2} -C data/levels
mv data/levels/LEVELPACK data/levels/LEVELS

%build
%configure2_5x	--bindir=%{_gamesbindir} --enable-sdl-gfx --datadir=%{_gamesdatadir} --enable-sound
%make

%install
rm -rf $RPM_BUILD_ROOT
%{makeinstall_std} datadir=%{_gamesdatadir}
install -m644 data/levels/*.png %{buildroot}%_gamesdatadir/%name/levels/
%find_lang %{name}

#Menu items
mkdir -p $RPM_BUILD_ROOT%{_datadir}/applications/
cat << EOF > %buildroot%{_datadir}/applications/mandriva-%{name}.desktop
[Desktop Entry]
Type=Application
Exec=%{_gamesbindir}/%{name}
Icon=%{name}
Categories=Game;ArcadeGame;
Name=Luola
Comment=%{Summary}
EOF
#Icons
install -d $RPM_BUILD_ROOT{%{_iconsdir},%{_miconsdir},%{_liconsdir}}
convert -size 32x32 %{name}.png $RPM_BUILD_ROOT%{_iconsdir}/%{name}.png
convert -size 48x48 %{name}.png $RPM_BUILD_ROOT%{_liconsdir}/%{name}.png
convert -size 16x16 %{name}.png $RPM_BUILD_ROOT%{_miconsdir}/%{name}.png

%post
%update_menus

%postun
%clean_menus

%clean
rm -rf $RPM_BUILD_ROOT

%files -f %{name}.lang
%defattr(-, root, root)
%doc README AUTHORS
%{_gamesbindir}/*
%{_gamesdatadir}/%{name}
%{_datadir}/applications/mandriva-%{name}.desktop
%{_miconsdir}/%{name}.png
%{_iconsdir}/%{name}.png
%{_liconsdir}/%{name}.png

