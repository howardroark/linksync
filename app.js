var socketIO = require('socket.io');
var express require('express');
var path = require('path');

var server = express()
    .use(function (req, res) {
        res.sendFile(path.join(__dirname, 'public/index.html'));
    })
    .listen(process.env.PORT);

var io = socketIO(server);

io.sockets.on('connection', function (socket) {
    socket.on('join', function (channel) {
        console.log('join', channel);
        socket.join(channel);
    });
    socket.on('broadcast', function (data) {
        console.log('broadcast', data);
        socket.broadcast.to(data.channel).emit('update', {
            message: data.message
        });
    });
});
