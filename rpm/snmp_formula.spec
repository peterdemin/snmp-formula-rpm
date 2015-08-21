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
git clone "https://github.com/peterdemin/snmp-formula.git" --branch specific --depth 1
(cd snmp-formula && find -maxdepth 1 -mindepth 1 ! -name snmp | xargs rm -rf)

%install
set -ex

echo $PWD

REL_DIR="srv/salt/snmp"
TARGET_DIR="${RPM_BUILD_ROOT}/${REL_DIR}"
mkdir -p "${TARGET_DIR}"
cp -r "${RPM_BUILD_DIR}/snmp-formula/snmp" "${TARGET_DIR}/.."

(cd ${RPM_BUILD_ROOT}; find ${REL_DIR} -type f -print) | awk '{print "/"$0}' > snmp-formula-files.txt
%files formula -f snmp-formula-files.txt
