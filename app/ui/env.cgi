#!/bin/sh

# 添加 HTTP 响应头
echo "Content-Type: application/javascript; charset=utf-8"
echo ""

cat <<EOF
  const host = window.location.hostname;     
  const isInternalIp = /^(?:10|127|172\.(?:1[6-9]|2\d|3[01])|192\.168|169\.254|100\.64)\./.test(host) || host === 'localhost';

  const protocol= window.location.protocol;
  const hostname=isInternalIp ? host : ('vs-code.'+ host);
  const port = isInternalIp ? '5333' : window.location.port;
  const airPort=port?(':'+port):'';

  // 构建目标URL
  const targetURL =protocol + "//" + hostname + airPort;

  // 尝试获取当前父级 iframe 元素
  let iframe = window.frameElement;
  if(iframe){
      iframe.frameBorder = "0";
      iframe.setAttribute("webkitallowfullscreen", "true");
      iframe.setAttribute("mozallowfullscreen", "true");
      iframe.setAttribute('allow', 'clipboard-read; clipboard-write');

      //沙盒属性
      iframe.sandbox="allow-same-origin allow-scripts allow-forms allow-modals allow-popups allow-popups-to-escape-sandbox allow-downloads"
      iframe.src =targetURL;

      console.log('✅ 修改iframe成功！');
  }else{
      //飞牛APP因跨源（cross-origin)获取不了，则直接跳转
      //window.location.href = targetURL;
      window.open(targetURL, '_top');
      window.alert(5 + 6);
  }

  console.log("CGI加载的JS文件成功！");
EOF

