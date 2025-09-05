#!/bin/sh
MOUNT_POINT=$(cat /var/packages/OpenListMount/etc/mount_point || echo "/volume1/OpenList")

case $1 in
    start)
        if [ -f /var/packages/OpenListMount/etc/api_token ]; then
            rclone mount openlist:/ "$MOUNT_POINT" \
              --webdav-header "Authorization: Bearer $(cat /var/packages/OpenListMount/etc/api_token)" \
              --vfs-cache-mode writes \
              --allow-other \
              --umask 000 &
        else
            rclone mount openlist:/ "$MOUNT_POINT" \
              --webdav-user $(cat /var/packages/OpenListMount/etc/username) \
              --webdav-pass $(cat /var/packages/OpenListMount/etc/password) \
              --vfs-cache-mode writes \
              --allow-other \
              --umask 000 &
        fi
        ;;
    stop)
        fusermount -u "$MOUNT_POINT"
        ;;
    status)
        mountpoint -q "$MOUNT_POINT" && echo "Running" || echo "Stopped"
        ;;
esac
