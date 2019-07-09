var tls = require('tls');
var fs = require('fs');
var host = 'localhost';
var port = 4001;

var serverOptions = {
    key: fs.readFileSync('./my_key.pem'),
    cert: fs.readFileSync('./my_cert.pem')
};


var client = tls.connect(port, host, serverOptions, function() {
    console.log('connected');
    console.log('authorized: ' + client.authorized);
    if (!client.authorized) {
        console.log('client denied access:', client.authorizationError);
    } else {}
});