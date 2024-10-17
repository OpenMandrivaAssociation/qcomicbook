Name:		qcomicbook
Version:	0.9.0
Release:	2
Summary:	Comic book archive viewer
Group:		File tools
License:	GPLv2+
URL:		https://qcomicbook.linux-projects.net
Source0:	http://qcomicbook.linux-projects.net/releases/%{name}-%{version}.tar.gz
BuildRequires:	cmake
BuildRequires:	pkgconfig(poppler-qt4)
BuildRequires:	pkgconfig(imlib2)
Requires:	unzip
Suggests:	unrar
Suggests:	p7zip

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
%cmake_qt4
%make

%install
%makeinstall_std -C build

%files
%doc AUTHORS README ChangeLog COPYING THANKS TODO
%{_bindir}/%{name}
%{_datadir}/applications/%{name}.desktop
%{_mandir}/man1/%{name}.1.*
%{_datadir}/pixmaps/%{name}.png
%{_datadir}/%{name}

