%define	name	qcomicbook
%define	version	0.4.0
%define	release	%mkrel 1
%define summary Comic book archive viewer
%define group	File tools

Name:		%{name} 
Summary:	%{summary}
Version:	%{version} 
Release:	%{release} 
Source0:	%{name}-%{version}.tar.bz2
URL:		http://linux.bydg.org/~yogin/
Group:		%{group}
BuildRoot:	%{_tmppath}/%{name}-%{version}-%{release}-buildroot
License:	GPLv2+
Requires:	unzip
BuildRequires:	qt4-devel >= 4.2.0
BuildRequires:  imageMmgick
BuildRequires:	imlib2-devel

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

%build
%{__perl} -pi -e 's|with_Qt_dir/lib|with_Qt_dir/%{_lib}|' acinclude.m4
autoreconf --verbose --force --install
%configure \
  --with-Qt-dir=%{qt3dir} \
  --with-Qt-bin-dir=%{qt3dir}/bin \
  --with-Qt-lib-dir=%{qt3lib}
%make

%install
rm -rf $RPM_BUILD_ROOT

%makeinstall

install -m644 ./fedora/qcomicbook.png -D $RPM_BUILD_ROOT%{_iconsdir}/qcomicbook.png
# Create other icons
convert ./fedora/qcomicbook.png -resize 48x48 ./qcomicbook-48.png
convert ./fedora/qcomicbook.png -resize 16x16 ./qcomicbook-16.png
install -m644 ./qcomicbook-48.png -D $RPM_BUILD_ROOT%{_liconsdir}/qcomicbook.png
install -m644 ./qcomicbook-16.png -D $RPM_BUILD_ROOT%{_miconsdir}/qcomicbook.png

mkdir -p $RPM_BUILD_ROOT%{_datadir}/applications
cat << EOF >$RPM_BUILD_ROOT%{_datadir}/applications/mandriva-%{name}.desktop
[Desktop Entry]
Name=QComicBook
Comment=Comic book archive viewer
Exec=%{_bindir}/%{name}
Icon=qcomicbook
Terminal=false
Type=Application
Categories=Graphics;Viewer;
EOF

%post
%{update_menus}

%postun
%{clean_menus}

%clean 
rm -rf $RPM_BUILD_ROOT 

%files 
%defattr(-,root,root)
%doc AUTHORS README ChangeLog THANKS TODO
%{_iconsdir}/*
%{_bindir}/*
%{_mandir}/man?/*
%{_datadir}/%{name}/*
%{_datadir}/applications/mandriva-%{name}.desktop
