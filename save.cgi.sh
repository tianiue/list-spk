#!/bin/sh
echo "Content-type: application/json"
echo ""

read -n $CONTENT_LENGTH POST_DATA

echo "$POST_DATA" | grep -o 'mount_point=[^&]*' | cut -d= -f2 > /var/packages/OpenListMount/etc/mount_point
echo "$POST_DATA" | grep -o 'auth_mode=[^&]*' | cut -d= -f2 > /var/packages/OpenListMount/etc/auth_mode

if grep -q 'auth_mode=api' <<< "$POST_DATA"; then
  echo "$POST_DATA" | grep -o 'api_token=[^&]*' | cut -d= -f2 > /var/packages/OpenListMount/etc/api_token
else
  echo "$POST_DATA" | grep -o 'username=[^&]*' | cut -d= -f2 > /var/packages/OpenListMount/etc/username
  echo "$POST_DATA" | grep -o 'password=[^&]*' | cut -d= -f2 > /var/packages/OpenListMount/etc/password
fi

/var/packages/OpenListMount/scripts/start-stop-status restart
echo '{"status":"success"}'