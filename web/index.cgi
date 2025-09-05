#!/bin/sh
echo "Content-type: text/html"
echo ""

AUTH_MODE=$(cat /var/packages/OpenListMount/etc/auth_mode || echo "api")
MOUNT_POINT=$(cat /var/packages/OpenListMount/etc/mount_point || echo "/volume1/OpenList")

cat <<EOF
<html>
<script>
function saveConfig() {
  fetch('/webman/modules/OpenListMount/save.cgi', {
    method: 'POST',
    body: new FormData(document.getElementById('configForm'))
  }).then(() => alert('Settings saved'));
}
</script>
<div class="content-container">
  <form id="configForm">
    <div class="form-group">
      <label>Mount Path:</label>
      <input type="text" name="mount_point" value="$MOUNT_POINT" required>
    </div>
    <div class="form-group">
      <label>Auth Mode:</label>
      <select name="auth_mode" onchange="document.getElementById('apiFields').style.display=this.value==='api'?'block':'none';document.getElementById('passwordFields').style.display=this.value==='password'?'block':'none'">
        <option value="api" ${AUTH_MODE == "api" ? "selected" : ""}>API Token</option>
        <option value="password" ${AUTH_MODE == "password" ? "selected" : ""}>Password</option>
      </select>
    </div>
    <div id="apiFields" style="display:${AUTH_MODE == "api" ? "block" : "none"}">
      <div class="form-group">
        <label>API Token:</label>
        <input type="password" name="api_token">
      </div>
    </div>
    <div id="passwordFields" style="display:${AUTH_MODE == "password" ? "block" : "none"}">
      <div class="form-group">
        <label>Username:</label>
        <input type="text" name="username">
      </div>
      <div class="form-group">
        <label>Password:</label>
        <input type="password" name="password">
      </div>
    </div>
    <button type="button" onclick="saveConfig()">Save</button>
  </form>
</div>
</html>
EOF
