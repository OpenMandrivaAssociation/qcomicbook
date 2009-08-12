Name:           qcomicbook
Version:        0.4.1
Release:        %mkrel 1
Summary:        Comic book archive viewer
Source0:        http://linux.bydg.org/~yogin/%{name}/%{name}-%{version}.tar.gz
URL:            http://linux.bydg.org/~yogin/
Group:          File tools
License:        GPLv2+
Requires:       unzip
Requires(post): desktop-file-utils
Requires(postun): desktop-file-utils
BuildRequires:  desktop-file-utils
BuildRequires:  imagemagick
BuildRequires:  imlib2-devel
BuildRequires:  qt4-devel
BuildRoot:      %{_tmppath}/%{name}-%{version}-%{release}-root

%description
QComicBook is a viewer for comic book archives containing jpeg/png 
images, which aims at convenience and simplicity. Features include:

    * automatic handling of archives
    * full-screen mode
    * two-pages mode and japanese mode
    * thumbnails view
    * page scaling (fit to window witdth/height, whole page)
    * mouse or keyboard navigation, whatever you prefer
    * bookmarks
    * and more... 

%prep
%setup -q
%{__perl} -pi -e 's|moc-qt4|%{qt4dir}/bin/moc|g' src/Makefile.{am,in}
%{__perl} -pi -e 's|with_Qt_dir/lib|with_Qt_dir/%{_lib}|' acinclude.m4
%{_bindir}/autoreconf --verbose --force --install

%{_bindir}/convert fedora/qcomicbook.png -resize 64x64 qcomicbook-64.png
%{_bindir}/convert fedora/qcomicbook.png -resize 16x16 qcomicbook-16.png

%{__cat} << EOF > %{name}.desktop
[Desktop Entry]
Name=QComicBook
Comment=Comic book archive viewer
Exec=%{_bindir}/%{name}
Icon=qcomicbook
Terminal=false
Type=Application
Categories=Graphics;Viewer;
EOF

%build
%{configure2_5x} \
  --with-Qt-dir=%{qt4dir} \
  --with-Qt-bin-dir=%{qt4dir}/bin \
  --with-Qt-lib-dir=%{qt4lib}
%{make}

%install
%{__rm} -rf %{buildroot}
%{makeinstall_std}

%{__mkdir_p} %{buildroot}%{_datadir}/pixmaps
%{__mkdir_p} %{buildroot}%{_datadir}/icons/hicolor/16x16/apps
%{__mkdir_p} %{buildroot}%{_datadir}/icons/hicolor/32x32/apps
%{__mkdir_p} %{buildroot}%{_datadir}/icons/hicolor/64x64/apps
%{__install} -m 644 fedora/qcomicbook.png %{buildroot}%{_datadir}/pixmaps/qcomicbook.png
%{__install} -m 644 qcomicbook-16.png %{buildroot}%{_datadir}/icons/hicolor/16x16/apps/qcomicbook.png
%{__install} -m 644 fedora/qcomicbook.png  %{buildroot}%{_datadir}/icons/hicolor/32x32/apps/qcomicbook.png
%{__install} -m 644 qcomicbook-64.png %{buildroot}%{_datadir}/icons/hicolor/64x64/apps/qcomicbook.png

%{__mkdir_p} %{buildroot}%{_datadir}/applications
%{_bindir}/desktop-file-install --vendor mandriva       \
        --dir %{buildroot}%{_datadir}/applications      \
        %{name}.desktop

%clean 
%{__rm} -rf %{buildroot} 

%post
%{update_desktop_database}
%update_icon_cache hicolor

%postun
%{clean_desktop_database}
%clean_icon_cache hicolor

%files 
%defattr(-,root,root)
%doc AUTHORS README ChangeLog THANKS TODO
%{_bindir}/*
%{_datadir}/pixmaps/qcomicbook.png
%{_datadir}/icons/hicolor/16x16/apps/qcomicbook.png
%{_datadir}/icons/hicolor/32x32/apps/qcomicbook.png
%{_datadir}/icons/hicolor/64x64/apps/qcomicbook.png
%{_datadir}/%{name}/*
%{_datadir}/applications/mandriva-%{name}.desktop
%{_mandir}/man?/*
