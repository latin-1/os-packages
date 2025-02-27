Name: adobe-source-han-sans-fonts
Version: 2.004
Release: 1%{?dist}
Summary: Source Han Sans
License: OFL

BuildArch: noarch
Source: https://raw.githubusercontent.com/adobe-fonts/source-han-sans/release/OTC/SourceHanSans-Bold.ttc
Source: https://raw.githubusercontent.com/adobe-fonts/source-han-sans/release/OTC/SourceHanSans-ExtraLight.ttc
Source: https://raw.githubusercontent.com/adobe-fonts/source-han-sans/release/OTC/SourceHanSans-Heavy.ttc
Source: https://raw.githubusercontent.com/adobe-fonts/source-han-sans/release/OTC/SourceHanSans-Light.ttc
Source: https://raw.githubusercontent.com/adobe-fonts/source-han-sans/release/OTC/SourceHanSans-Medium.ttc
Source: https://raw.githubusercontent.com/adobe-fonts/source-han-sans/release/OTC/SourceHanSans-Normal.ttc
Source: https://raw.githubusercontent.com/adobe-fonts/source-han-sans/release/OTC/SourceHanSans-Regular.ttc
Source: https://raw.githubusercontent.com/adobe-fonts/source-han-sans/release/Variable/OTC/SourceHanSans-VF.otf.ttc

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
