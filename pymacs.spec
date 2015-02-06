%define tarname Pymacs
%define name pymacs
%define version 0.25
%define rel	%{nil}
%define release 2

Summary: Bidirectional communication between Emacs Lisp and Python
Name:	 %{name}
Version: %{version}
Release: %{release}
Source0: %{tarname}-%{version}.tar.gz
License: GPLv2+
Group:	 Development/Python
Url:	 http://pymacs.progiciels-bpi.ca
BuildArch: noarch
BuildRequires:	emacs
BuildRequires:	python2-devel
BuildRequires:	python-docutils

%description
Pymacs is a powerful tool for bidirectional communication between
Emacs Lisp and Python. Pymacs aims to provide Python as an extension
language for Emacs; using Pymacs, one may load and use Python modules
within Emacs Lisp code. Python functions may also use Emacs services
and handle objects in the Emacs Lisp space.

%package -n python2-%{name}
Summary: Bidirectional communication between Emacs Lisp and Python
Group:	 Development/Python
%rename python-%{name}

%description -n python2-%{name}
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
%setup -q -n %{tarname}-%{version}

%build

%__make all PYTHON=%__python2

%install
%__rm -rf %{buildroot}
PYTHONDONTWRITEBYTECODE= %__python2 setup.py install --root=%{buildroot}
rst2html --input-encoding=UTF-8 pymacs.rst pymacs.html
%__install -d -m 755 %{buildroot}%{_datadir}/emacs/site-lisp/
emacs -batch --eval '(byte-compile-file "pymacs.el" t)'
%__install -m 644 pymacs.el pymacs.elc %{buildroot}%{_datadir}/emacs/site-lisp/
%__install -d -m 755 %{buildroot}%{_sysconfdir}/emacs/site-start.d
echo "(require 'pymacs)" >> %{buildroot}%{_sysconfdir}/emacs/site-start.d/pymacs.el

%clean
%__rm -rf %{buildroot}

%files -n python2-%{name} 
%py2_puresitedir/Pymacs*

%files -n emacs-%{name}
%doc COPYING README THANKS TODO pymacs.html
%_sysconfdir/emacs/site-start.d/pymacs.el
%_datadir/emacs/site-lisp/pymacs.*

