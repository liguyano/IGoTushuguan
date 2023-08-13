// Create a WebSocket instance and specify the server URL
//const socket = new WebSocket('ws://localhost:7001');
const socket = new WebSocket('ws://wechat.v2.traceint.com/ws?ns=prereserve/queue');
document.cookie = "FROM_TYPE=weixin; v=5.5; wechatSESS_ID=84b93ea0fed93750633fd0d4e08897b6c8237396e8f80ecb; Authorization=eyJ0eXAiOiJKV1QiLCJhbGciOiJSUzI1NiJ9.eyJ1c2VySWQiOjI0OTc1MjUyLCJzY2hJZCI6MjAwNTgsImV4cGlyZUF0IjoxNjkxODU4Njk0fQ.p1hxJkwIFX4_ueGriSdUNKvqDs24hHERGj3r07OcSEHPcxJRcP99Yzwqxw_WNuWVMGIcOlXlRRHm_vktdeNFuW_XNGC8GSXpllY2Z0RdvtTTXyrcVO0Few35XG2SduFp-BoFgf67hQ4lQ2hHv-0Afh_Y0E-7QKrejgCvybjPXnYtJ5Ja7odNdHAO4LHPw_FDmTY5yZ72c9OLs3D31gSvpkVBG0iopiiT_pGqpupwYrJpDoyLeyz1c1BteUnjfcjSwMoOK9PuBWANsjEp2zabuApfG0O5FxhKNWUw1m3nGSBovx4ava9IK718s-7bpU2kPrVM5fBsECE8M94zF05Q3w; Hm_lvt_7ecd21a13263a714793f376c18038a87=1691766975,1691851495; Hm_lpvt_7ecd21a13263a714793f376c18038a87=1691851495; SERVERID=d3936289adfff6c3874a2579058ac651|1691851497|1691851490"

// Event listener for when the connection is opened
socket.addEventListener('open', event => {
    console.log('WebSocket connection opened');

    // Send a message to the server
    socket.send('Hello, WebSocket!');
});

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