Name: snmp
Version: 1.0.0
Release: 1
Summary: SaltStack SNMP formula
License: Commercial
Group: Applications/System
Vendor: White Socks Software, Inc.
BuildArch: noarch
%description
SaltStack SNMP formula
%package formula
BuildArch: noarch
Summary: SNMP SaltStack formula
%description formula
SaltStack SNMP formula

%build
git clone "https://github.com/saltstack-formulas/snmp-formula.git"
(cd snmp-formula && find -maxdepth 1 -mindepth 1 ! -name snmp | xargs rm -rf)

%install
set -ex

echo $PWD

mkdir -p "${RPM_BUILD_ROOT}/srv/formulas/snmp-formula/snmp"
cp -r "${RPM_BUILD_DIR}/snmp-formula/snmp" "${RPM_BUILD_ROOT}/srv/formulas/snmp-formula/"

(cd ${RPM_BUILD_ROOT}; find srv/formulas/snmp-formula -type f -print) | awk '{print "/"$0}' > snmp-formula-files.txt
%files formula -f snmp-formula-files.txt
