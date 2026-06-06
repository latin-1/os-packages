Name: adobe-source-han-serif
Summary: Source Han Serif
Version: 2.003
Release: 1%{?dist}
License: OFL-1.1-RFN

BuildArch: noarch
BuildRequires: unzip

Source0: https://github.com/adobe-fonts/source-han-serif/releases/download/%{version}R/01_SourceHanSerif.ttc.zip
Source1: https://github.com/adobe-fonts/source-han-serif/releases/download/%{version}R/02_SourceHanSerif-VF.zip
Source10: https://raw.githubusercontent.com/adobe-fonts/source-han-serif/refs/tags/%{version}/LICENSE.txt

%package fonts
Summary: Source Han Serif

%package vf-fonts
Summary: Source Han Serif - Variable

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
