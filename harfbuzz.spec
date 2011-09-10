Name:           harfbuzz
Version:        0.6.0
Release:        3%{?dist}
Summary:        Text shaping library

License:        MIT
URL:            http://freedesktop.org/wiki/Software/HarfBuzz
Source0:        http://www.freedesktop.org/software/harfbuzz/release/harfbuzz-%{version}.tar.bz2

BuildRequires:  cairo-devel
BuildRequires:  freetype-devel
BuildRequires:  glib2-devel
BuildRequires:  libicu-devel

%description
HarfBuzz is an implementation of the OpenType Layout engine.


%package        devel
Summary:        Development files for %{name}
Requires:       %{name} = %{version}-%{release}

%description    devel
The %{name}-devel package contains libraries and header files for
developing applications that use %{name}.


%prep
%setup -q


%build
%configure --disable-static

# Remove lib64 rpath
sed -i 's|^hardcode_libdir_flag_spec=.*|hardcode_libdir_flag_spec=""|g' libtool
sed -i 's|^runpath_var=LD_RUN_PATH|runpath_var=DIE_RPATH_DIE|g' libtool

make %{?_smp_mflags} V=1


%install
make install DESTDIR=$RPM_BUILD_ROOT
rm -f $RPM_BUILD_ROOT%{_libdir}/*.la


%post -p /sbin/ldconfig

%postun -p /sbin/ldconfig


%files
%doc COPYING README
%{_libdir}/*.so.*

%files devel
%{_bindir}/hb-view
%{_includedir}/harfbuzz/
%{_libdir}/*.so
%{_libdir}/pkgconfig/harfbuzz.pc


%changelog
* Sat Sep 10 2011 Kalev Lember <kalevlember@gmail.com> - 0.6.0-3
- Rebuilt for libicu 4.8

* Thu Jun 16 2011 Kalev Lember <kalev@smartlink.ee> - 0.6.0-2
- Moved hb-view to -devel subpackage (#713126)

* Tue Jun 14 2011 Kalev Lember <kalev@smartlink.ee> - 0.6.0-1
- Initial RPM release
