var http = require('http');

var options = {
    host: 'www.google.com',
    port: 80,
    path: "/index.html",
    method: "GET"
};
// write chuck to text file
var fs = require('fs');



var webfile = fs.createWriteStream("web.txt");

var request = http.request(options, function(res) {

    console.log('Got response:' + res.statusCode);
    console.log('HEADERS:' + res.headers);
    console.log('HEADERS:' + res.url);
    res.setEncoding('utf8');
    res.on('data', function(chunk) {
        console.log('BODY:' + chunk);

    });

    res.pipe(webfile);
}).end()