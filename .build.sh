#!/bin/bash

set -e

# Create package structure
mkdir -p package/conf
mkdir -p package/scripts
mkdir -p package/webapi

# Copy source files
cp -r src/* package/

# Generate INFO file
cat <<EOF > package/INFO
package="OpenListMount"
version="$(date +%Y%m%d)"
arch="x86_64 aarch64"
firmware="7.2-69057"
maintainer="OpenListTeam"
displayname="OpenList Mount"
description="Mount OpenList WebDAV with dual auth support"
install_dep_packages="WebDAVServer:service"
startable="yes"
support_conf_folder="yes"
dsmappname="SYNO.SDS.AdminCenter.Application"
dsmapppage="content"
adminport="8182"
EOF

# Set permissions
chmod 755 package/scripts/*

# Package SPK
cd package
tar -czvf ../OpenListMount.spk *

echo "SPK package built: OpenListMount.spk"
