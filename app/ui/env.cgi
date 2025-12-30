#!/bin/sh

# 获取当前 IP
REQUEST_IP=$(hostname -I | awk '{print $1}')

# 添加 HTTP 响应头
echo "Content-Type: application/javascript; charset=utf-8"
echo ""


cat <<EOF


window.FNOS_APP = {
  name: "FUCKYOU",
  version: "${REQUEST_IP}",
  port: "${REQUEST_URI}"
};
// 检查是否是内网IP
function isInternalIp(url) {
  const privateIpv4 = /^(?:10|127|172\.(?:1[6-9]|2\d|3[01])|192\.168|169\.254|100\.64)\./;
  return privateIpv4.test(url) || url === 'localhost';
}


console.log("CGI加载的JS文件成功！");
EOF



