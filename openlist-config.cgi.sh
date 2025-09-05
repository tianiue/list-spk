#!/bin/sh
echo "Content-type: text/html"
echo ""

WEBDAV_URL=$(cat /var/packages/OpenListMount/etc/webdav_url)
MOUNT_POINT=$(cat /var/packages/OpenListMount/etc/mount_point)
AUTH_MODE=$(cat /var/packages/OpenListMount/etc/auth_mode || echo "api")

cat <<EOF
<html>
<script>
function saveConfig() {
  const form = document.getElementById('configForm');
  fetch('/webman/modules/OpenListMount/save.cgi', {
    method: 'POST',
    body: new FormData(form)
  }).then(() => DSM.notify(DSM.msg.SettingsSaved));
}
</script>
<div class="content-container">
  <form id="configForm">
    <div class="form-group">
      <label>Mount Path:</label>
      <input type="text" name="mount_point" value="$MOUNT_POINT" class="form-control">
    </div>
    <div class="form-group">
      <label>Auth Mode:</label>
      <select name="auth_mode" class="form-control" onchange="toggleAuthFields()">
        <option value="api" ${AUTH_MODE == "api" ? "selected" : ""}>API Token</option>
        <option value="password" ${AUTH_MODE == "password" ? "selected" : ""}>Password</option>
      </select>
    </div>
    <div id="apiFields" style="display:${AUTH_MODE == "api" ? "block" : "none"}">
      <div class="form-group">
        <label>API Token:</label>
        <input type="password" name="api_token" class="form-control">
      </div>
    </div>
    <div id="passwordFields" style="display:${AUTH_MODE == "password" ? "block" : "none"}">
      <div class="form-group">
        <label>Username:</label>
        <input type="text" name="username" class="form-control">
      </div>
      <div class="form-group">
        <label>Password:</label>
        <input type="password" name="password" class="form-control">
      </div>
    </div>
    <button type="button" onclick="saveConfig()" class="btn btn-primary">Save</button>
  </form>
</div>
<script>
function toggleAuthFields() {
  const mode = document.querySelector('[name="auth_mode"]').value;
  document.getElementById('apiFields').style.display = mode === 'api' ? 'block' : 'none';
  document.getElementById('passwordFields').style.display = mode === 'password' ? 'block' : 'none';
}
</script>
</html>
EOF