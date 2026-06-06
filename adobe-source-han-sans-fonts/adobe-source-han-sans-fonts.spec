Name: adobe-source-han-sans
Summary: Source Han Sans
Version: 2.005
Release: 1%{?dist}
License: OFL-1.1-RFN

BuildArch: noarch
BuildRequires: unzip

Source0: https://github.com/adobe-fonts/source-han-sans/releases/download/%{version}R/01_SourceHanSans.ttc.zip
Source1: https://github.com/adobe-fonts/source-han-sans/releases/download/%{version}R/02_SourceHanSans-VF.zip
Source10: https://raw.githubusercontent.com/adobe-fonts/source-han-sans/refs/tags/%{version}/LICENSE.txt

%description
Source Han Sans

%package fonts
Summary: Source Han Sans
%description fonts
Source Han Sans

%package vf-fonts
Summary: Source Han Sans - Variable
%description vf-fonts
Source Han Sans - Variable

%prep
%setup -q -c -T
cp %{SOURCE10} LICENSE.txt
unzip -q "%{SOURCE0}" -d fonts
unzip -q "%{SOURCE1}" -d vf-fonts

%install
install -Dm 0644 ./fonts/*.ttc -t %{buildroot}/%{_datadir}/fonts/%{name}-fonts
install -Dm 0644 ./vf-fonts/Variable/OTC/*.ttc -t %{buildroot}/%{_datadir}/fonts/%{name}-vf-fonts

%files fonts
%license LICENSE.txt
%{_datadir}/fonts/%{name}-fonts

%files vf-fonts
%license LICENSE.txt
%{_datadir}/fonts/%{name}-vf-fonts
