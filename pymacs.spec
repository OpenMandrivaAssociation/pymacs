%define tarname Pymacs
%define name pymacs
%define version 0.24
%define rel	beta2
%define release 0.%rel

Summary: Bidirectional communication between Emacs Lisp and Python
Name:	 %{name}
Version: %{version}
Release: %{release}
Source0: %{tarname}-%{version}-%{rel}.tar.gz
License: GPLv2+
Group:	 Development/Python
Url:	 http://pymacs.progiciels-bpi.ca
BuildRoot: %{_tmppath}/%{name}-%{version}-%{release}-buildroot
BuildArch: noarch
BuildRequires:	emacs, python-devel, python-docutils

%description
Pymacs is a powerful tool for bidirectional communication between
Emacs Lisp and Python. Pymacs aims to provide Python as an extension
language for Emacs; using Pymacs, one may load and use Python modules
within Emacs Lisp code. Python functions may also use Emacs services
and handle objects in the Emacs Lisp space.

%package -n python-%{name}
Summary: Bidirectional communication between Emacs Lisp and Python
Group:	 Development/Python

%description -n python-%{name}
Pymacs is a powerful tool for bidirectional communication between
Emacs Lisp and Python. Pymacs aims to provide Python as an extension
language for Emacs; using Pymacs, one may load and use Python modules
within Emacs Lisp code. Python functions may also use Emacs services
and handle objects in the Emacs Lisp space.

This package contains the Python portion of Pymacs.

%package -n emacs-%{name}
Summary: Bidirectional communication between Emacs Lisp and Python
Group:	 Editors
Requires: emacs

%description -n emacs-%{name}
Pymacs is a powerful tool for bidirectional communication between
Emacs Lisp and Python. Pymacs aims to provide Python as an extension
language for Emacs; using Pymacs, one may load and use Python modules
within Emacs Lisp code. Python functions may also use Emacs services
and handle objects in the Emacs Lisp space.

This package contains the Emacs portion of Pymacs.

%prep
%setup -q -n %{tarname}-%{version}-%{rel}

%build
%__make all

%install
%__rm -rf %{buildroot}
PYTHONDONTWRITEBYTECODE= %__python setup.py install --root=%{buildroot}
rst2html --input-encoding=UTF-8 pymacs.rst pymacs.html
%__install -d -m 755 %{buildroot}%{_datadir}/emacs/site-lisp/
emacs -batch --eval '(byte-compile-file "pymacs.el" t)'
%__install -m 644 pymacs.el pymacs.elc %{buildroot}%{_datadir}/emacs/site-lisp/
%__install -d -m 755 %{buildroot}%{_sysconfdir}/emacs/site-start.d
echo "(require 'pymacs)" >> %{buildroot}%{_sysconfdir}/emacs/site-start.d/pymacs.el

%clean
%__rm -rf %{buildroot}

%files -n python-%{name} 
%defattr(-,root,root)
%py_sitedir/Pymacs*

%files -n emacs-%{name}
%defattr(-,root,root)
%doc COPYING README THANKS TODO pymacs.html
%_sysconfdir/emacs/site-start.d/pymacs.el
%_datadir/emacs/site-lisp/pymacs.*
