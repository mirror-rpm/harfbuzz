Name:           harfbuzz
Version:        0.9.11
Release:        1%{?dist}
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
make install DESTDIR=$RPM_BUILD_ROOT INSTALL="install -p"
rm -f $RPM_BUILD_ROOT%{_libdir}/*.la


%post -p /sbin/ldconfig

%postun -p /sbin/ldconfig


%files
%doc NEWS ChangeLog AUTHORS COPYING README
%{_libdir}/*.so.*

%files devel
%{_bindir}/hb-view
%{_bindir}/hb-ot-shape-closure
%{_bindir}/hb-shape
%{_includedir}/harfbuzz/
%{_libdir}/*.so
%{_libdir}/pkgconfig/harfbuzz.pc


%changelog
* Fri Jan 11 2013 Parag Nemade <pnemade AT pnemade DOT com> - 0.9.11-1
- Update to 0.9.11 upstream release

* Thu Jan 03 2013 Parag Nemade <pnemade AT pnemade DOT com> - 0.9.10-1
- Update to 0.9.10 upstream release

* Thu Dec 06 2012 Parag Nemade <paragn AT fedoraproject DOT org> - 0.9.9-1
- Update to 0.9.9 upstream release

* Wed Dec 05 2012 Parag Nemade <paragn AT fedoraproject DOT org> - 0.9.8-1
- Update to 0.9.8 upstream release

* Wed Nov 21 2012 Parag Nemade <paragn AT fedoraproject DOT org> - 0.9.7-1
- Update to 0.9.7 upstream release

* Wed Nov 14 2012 Parag Nemade <paragn AT fedoraproject DOT org> - 0.9.6-1
- Update to 0.9.6 upstream release

* Mon Oct 15 2012 Parag Nemade <paragn AT fedoraproject DOT org> - 0.9.5-1
- Update to 0.9.5 upstream release

* Mon Sep 10 2012 Parag Nemade <paragn AT fedoraproject DOT org> - 0.9.4-1
- Update to 0.9.4 upstream release

* Sun Aug 19 2012 Parag Nemade <paragn AT fedoraproject DOT org> - 0.9.3-1
- Update to 0.9.3 upstream release

* Mon Aug 13 2012 Parag Nemade <paragn AT fedoraproject DOT org> - 0.9.2-1
- Update to 0.9.2 upstream release

* Thu Jul 19 2012 Fedora Release Engineering <rel-eng@lists.fedoraproject.org> - 0.6.0-7
- Rebuilt for https://fedoraproject.org/wiki/Fedora_18_Mass_Rebuild

* Mon Apr 23 2012 Kalev Lember <kalevlember@gmail.com> - 0.6.0-6
- Rebuilt for libicu 49

* Fri Jan 13 2012 Fedora Release Engineering <rel-eng@lists.fedoraproject.org> - 0.6.0-5
- Rebuilt for https://fedoraproject.org/wiki/Fedora_17_Mass_Rebuild

* Tue Dec 06 2011 Adam Jackson <ajax@redhat.com> - 0.6.0-4
- Rebuild for new libpng

* Sat Sep 10 2011 Kalev Lember <kalevlember@gmail.com> - 0.6.0-3
- Rebuilt for libicu 4.8

* Thu Jun 16 2011 Kalev Lember <kalev@smartlink.ee> - 0.6.0-2
- Moved hb-view to -devel subpackage (#713126)

* Tue Jun 14 2011 Kalev Lember <kalev@smartlink.ee> - 0.6.0-1
- Initial RPM release
