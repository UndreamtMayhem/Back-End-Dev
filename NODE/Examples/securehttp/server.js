var fs = require('fs');
var https = require('https');
var options = {
    key: fs.readFileSync('server_key.pem'),
    cert: fs.readFileSync('server_cert.pem')
};
var server = https.createServer(options, function(req, res) {
    res.writeHead(200, {
        'Content-Type': 'text/plain'
    });
    res.end('Hello World!');
});