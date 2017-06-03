var express = require('express');
var io = require('socket.io');

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