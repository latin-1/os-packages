Name: adobe-source-han-serif-fonts
Version: 2.004
Release: 1%{?dist}
Summary: Source Han Serif
License: OFL

BuildArch: noarch
Source: https://raw.githubusercontent.com/adobe-fonts/source-han-serif/release/OTC/SourceHanSerif-Bold.ttc
Source: https://raw.githubusercontent.com/adobe-fonts/source-han-serif/release/OTC/SourceHanSerif-ExtraLight.ttc
Source: https://raw.githubusercontent.com/adobe-fonts/source-han-serif/release/OTC/SourceHanSerif-Heavy.ttc
Source: https://raw.githubusercontent.com/adobe-fonts/source-han-serif/release/OTC/SourceHanSerif-Light.ttc
Source: https://raw.githubusercontent.com/adobe-fonts/source-han-serif/release/OTC/SourceHanSerif-Medium.ttc
Source: https://raw.githubusercontent.com/adobe-fonts/source-han-serif/release/OTC/SourceHanSerif-Regular.ttc
Source: https://raw.githubusercontent.com/adobe-fonts/source-han-serif/release/OTC/SourceHanSerif-SemiBold.ttc
Source: https://raw.githubusercontent.com/adobe-fonts/source-han-serif/release/Variable/OTC/SourceHanSerif-VF.otf.ttc

%description

%prep

%build

%install
files=("%{SOURCE0}" "%{SOURCE1}" "%{SOURCE2}" "%{SOURCE3}" "%{SOURCE4}" "%{SOURCE5}" "%{SOURCE6}" "%{SOURCE7}")
for file in "${files[@]}"; do
  install -Dm 644 "$file" "%{buildroot}%{_datadir}/fonts/%{name}/$(basename "$file")"
done

%files
%{_datadir}/fonts/%{name}/*
