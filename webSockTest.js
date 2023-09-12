// Create a WebSocket instance and specify the server URL
//const socket = new WebSocket('ws://localhost:7001');
var header = {
  "Cookie": "FROM_TYPE=weixin; v=5.5; wechatSESS_ID=ddcc58baf2f4ddbeef1d7cd38818663df30cba2bd5ed45e3; Authorization=eyJ0eXAiOiJKV1QiLCJhbGciOiJSUzI1NiJ9.eyJ1c2VySWQiOjI0OTc1MjUyLCJzY2hJZCI6MjAwNTgsImV4cGlyZUF0IjoxNjkxOTQzNTQ4fQ.x1b5PgjwKq1WH_8PDDfGH9Ie3oM9uSzHDIwouB4bF-FxSgs6gO0lydw30yuhQsM1-UPrijA5yxg9U1EuUvRo_s9ZuziypiqJql2Y-sFpvS1ZYXD6lmQQhwdOnZzn0wr0rwGudAczQdXExBpTjX7YX8rwQs8Wr5mLsR08pXrFV-Ma0MAvxVzvG44F6c95ecx1oXa4VY1j0eRsp23T3NQZ8mMHOysaU2EZtHm_JMI7VAq1RN4EjFlkgt0I3UG1EctmH1LQH5RrEPgEXhHFbKLtAQbeJPcFCiHWNYh568KGnj7W6ETaXPdGsU_5vRW-OPIfVj3GJBUCI4Cpz8jDg22KZw; Hm_lvt_7ecd21a13263a714793f376c18038a87=1691766975,1691851495,1691895854,1691936349; Hm_lpvt_7ecd21a13263a714793f376c18038a87=1691938077; SERVERID=82967fec9605fac9a28c437e2a3ef1a4|1691938078|1691936345"
};
//document.cookie="FROM_TYPE=weixin; v=5.5; wechatSESS_ID=ddcc58baf2f4ddbeef1d7cd38818663df30cba2bd5ed45e3; Authorization=eyJ0eXAiOiJKV1QiLCJhbGciOiJSUzI1NiJ9.eyJ1c2VySWQiOjI0OTc1MjUyLCJzY2hJZCI6MjAwNTgsImV4cGlyZUF0IjoxNjkxOTQzNTQ4fQ.x1b5PgjwKq1WH_8PDDfGH9Ie3oM9uSzHDIwouB4bF-FxSgs6gO0lydw30yuhQsM1-UPrijA5yxg9U1EuUvRo_s9ZuziypiqJql2Y-sFpvS1ZYXD6lmQQhwdOnZzn0wr0rwGudAczQdXExBpTjX7YX8rwQs8Wr5mLsR08pXrFV-Ma0MAvxVzvG44F6c95ecx1oXa4VY1j0eRsp23T3NQZ8mMHOysaU2EZtHm_JMI7VAq1RN4EjFlkgt0I3UG1EctmH1LQH5RrEPgEXhHFbKLtAQbeJPcFCiHWNYh568KGnj7W6ETaXPdGsU_5vRW-OPIfVj3GJBUCI4Cpz8jDg22KZw; Hm_lvt_7ecd21a13263a714793f376c18038a87=1691766975,1691851495,1691895854,1691936349; Hm_lpvt_7ecd21a13263a714793f376c18038a87=1691938077; SERVERID=82967fec9605fac9a28c437e2a3ef1a4|1691938078|1691936345"
const socket = new WebSocket('wss://wechat.v2.traceint.com/ws?ns=prereserve/queue',[],{headers:header});
// Event listener for when the connection is opened
socket.addEventListener('open', event => {
    console.log('WebSocket connection opened');
    socket.send("GET https://wechat.v2.traceint.com/ws?ns=prereserve/queue HTTP/1.1\n" +
        "Host: wechat.v2.traceint.com\n" +
        "Connection: Upgrade\n" +
        "Pragma: no-cache\n" +
        "Cache-Control: no-cache\n" +
        "User-Agent: Mozilla/5.0 (Windows NT 10.0; Win64; x64) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/107.0.0.0 Safari/537.36 NetType/WIFI MicroMessenger/7.0.20.1781(0x6700143B) WindowsWechat(0x63090621) XWEB/8351 Flue\n" +
        "Upgrade: websocket\n" +
        "Origin: https://web.traceint.com\n" +
        "Sec-WebSocket-Version: 13\n" +
        "Accept-Encoding: gzip, deflate, br\n" +
        "Accept-Language: zh-CN,zh\n" +
        "Cookie: FROM_TYPE=weixin; v=5.5; wechatSESS_ID=ddcc58baf2f4ddbeef1d7cd38818663df30cba2bd5ed45e3; Authorization=eyJ0eXAiOiJKV1QiLCJhbGciOiJSUzI1NiJ9.eyJ1c2VySWQiOjI0OTc1MjUyLCJzY2hJZCI6MjAwNTgsImV4cGlyZUF0IjoxNjkxOTQzNTQ4fQ.x1b5PgjwKq1WH_8PDDfGH9Ie3oM9uSzHDIwouB4bF-FxSgs6gO0lydw30yuhQsM1-UPrijA5yxg9U1EuUvRo_s9ZuziypiqJql2Y-sFpvS1ZYXD6lmQQhwdOnZzn0wr0rwGudAczQdXExBpTjX7YX8rwQs8Wr5mLsR08pXrFV-Ma0MAvxVzvG44F6c95ecx1oXa4VY1j0eRsp23T3NQZ8mMHOysaU2EZtHm_JMI7VAq1RN4EjFlkgt0I3UG1EctmH1LQH5RrEPgEXhHFbKLtAQbeJPcFCiHWNYh568KGnj7W6ETaXPdGsU_5vRW-OPIfVj3GJBUCI4Cpz8jDg22KZw; Hm_lvt_7ecd21a13263a714793f376c18038a87=1691766975,1691851495,1691895854,1691936349; Hm_lpvt_7ecd21a13263a714793f376c18038a87=1691937307; SERVERID=82967fec9605fac9a28c437e2a3ef1a4|1691937308|1691936345\n" +
        "Sec-WebSocket-Key: 5PmYDn6nGnLjp164iVSAbQ==\n" +
        "Sec-WebSocket-Extensions: permessage-deflate; client_max_window_bits")
    // Send a message to the server
    socket.send('{"ns":"prereserve/queue","msg":""}');
});
socket.onopen = function(event) {
  console.log("WebSocket connection opened");

  // 构造WebSocket握手请求
  var headers = {
    "Cookie": "FROM_TYPE=weixin; v=5.5; wechatSESS_ID=ddcc58baf2f4ddbeef1d7cd38818663df30cba2bd5ed45e3; Authorization=eyJ0eXAiOiJKV1QiLCJhbGciOiJSUzI1NiJ9.eyJ1c2VySWQiOjI0OTc1MjUyLCJzY2hJZCI6MjAwNTgsImV4cGlyZUF0IjoxNjkxOTQzNTQ4fQ.x1b5PgjwKq1WH_8PDDfGH9Ie3oM9uSzHDIwouB4bF-FxSgs6gO0lydw30yuhQsM1-UPrijA5yxg9U1EuUvRo_s9ZuziypiqJql2Y-sFpvS1ZYXD6lmQQhwdOnZzn0wr0rwGudAczQdXExBpTjX7YX8rwQs8Wr5mLsR08pXrFV-Ma0MAvxVzvG44F6c95ecx1oXa4VY1j0eRsp23T3NQZ8mMHOysaU2EZtHm_JMI7VAq1RN4EjFlkgt0I3UG1EctmH1LQH5RrEPgEXhHFbKLtAQbeJPcFCiHWNYh568KGnj7W6ETaXPdGsU_5vRW-OPIfVj3GJBUCI4Cpz8jDg22KZw; Hm_lvt_7ecd21a13263a714793f376c18038a87=1691766975,1691851495,1691895854,1691936349; Hm_lpvt_7ecd21a13263a714793f376c18038a87=1691938077; SERVERID=82967fec9605fac9a28c437e2a3ef1a4|1691938078|1691936345"
  };
  var handshakeRequest = [
    "GET / HTTP/1.1",
    "Host: wechat.v2.traceint.com",
    "Upgrade: websocket",
    "Connection: Upgrade",
    "Sec-WebSocket-Key: some_key",
    "Sec-WebSocket-Version: 13",
    "Cookie: " + headers.Cookie,
    "\r\n"
  ].join("\r\n");

  // 发送握手请求
  socket.send(handshakeRequest);

  // 在握手成功后，你可以在此发送和接收数据
};
// Event listener for receiving messages from the server
socket.addEventListener('message', event => {
    console.log('Received message:', event.data);
});

// Event listener for when the connection is closed
socket.addEventListener('close', event => {
    console.log('WebSocket connection closed:', event.code, event.reason);
});
for (let i = 0; i < 10; i++) {
    socket.send("hello")
}