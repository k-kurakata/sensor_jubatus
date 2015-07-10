//サーバ作成
var io = require('socket.io')(8080);

//クライアント接続があると、以下の処理をさせる。
io.on('connection', function (socket) {

  //接続通知をクライアントに送信
  io.emit("sendMessageToClient", {value:"1人入室しました。"});

  //クライアントからの受信イベントを設定
  socket.on("sendMessageToServer", function (data) {
      io.emit("sendMessageToClient", {value:data.value});
  });     

  //接続切れイベントを設定
  socket.on("disconnect", function () {
      io.emit("sendMessageToClient", {value:"1人退室しました。"});
  });
});
