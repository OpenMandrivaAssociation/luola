%define name	luola
%define version	1.3.2
%define release	%mkrel 5
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

%description
Luola is a 2D arcade game where you fly a small V shaped ship in different
kinds of levels. It's genre "Luolalentely" (Cave-flying) is (or was) very
popular in Finland. Though cavern-flying games are not originally
Finnish, nowdays most of them are.

%prep
%setup -q
tar -xf %{SOURCE1} -C data/levels

%build
%configure2_5x	--bindir=%{_gamesbindir} --enable-sdl-gfx --datadir=%{_gamesdatadir} --enable-sound
%make

%install
rm -rf $RPM_BUILD_ROOT
%{makeinstall_std} datadir=%{_gamesdatadir}
install -m644 data/levels/*.{png,lev} %{buildroot}%_gamesdatadir/%name/levels/
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

%if %mdkversion < 200900
%post
%update_menus
%endif

%if %mdkversion < 200900
%postun
%clean_menus
%endif

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

