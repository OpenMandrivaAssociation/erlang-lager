%global realname lager
%global upstream basho
# Technically, we're noarch; but erlang whose directories we install into is not.
%global debug_package %{nil}


Name:       erlang-%{realname}
Version:    3.2.1
Release:    %mkrel 1
Group:      Development/Java

Summary:    A logging framework for Erlang/OTP
Group:      Development/Erlang
License:    ASL 2.0
URL:        https://github.com/%{upstream}/%{realname}
Source0:    https://github.com/%{upstream}/%{realname}/archive/%{version}/%{realname}-%{version}.tar.gz
BuildRequires:  erlang-goldrush >= 0.1.8
BuildRequires:  erlang-rebar


%description
Lager (as in the beer) is a logging framework for Erlang. Its purpose is to
provide a more traditional way to perform logging in an erlang application that
plays nicely with traditional UNIX logging tools like logrotate and syslog.


%prep
%autosetup -n %{realname}-%{version}


%build
%{erlang_compile}


%install
%{erlang_install}


%files
%license LICENSE
%doc README.md
%{erlang_appdir}/



%changelog
* Thu Nov 17 2016 neoclust <neoclust> 3.2.1-1.mga6
+ Revision: 1068022
- New version 3.2.1

* Fri May 06 2016 neoclust <neoclust> 3.2.0-1.mga6
+ Revision: 1009845
- imported package erlang-lager

