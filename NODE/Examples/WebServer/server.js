var http = require('http');
var path = require('path');
var fs = require('fs');
var mimeTypes = {
    '.js': 'text/javascript',
    '.html': 'text/html',
    '.css': 'text/css'
};
var pages = [{
    id: '1',
    route: '',
    output: 'Woohoo!'
}, {
    id: '2',
    route: 'about',
    output: 'A simple routing with Node example'
}, {
    id: '3',
    route: '/about/this',
    output: 'Multilevel routing with Node'
}, {
    id: '4',
    route: '/about/node',
    output: 'Evented I/O for V8 JavaScript.'
}, {
    id: '5',
    route: 'another page',
    output: function() {
        return 'Here\'s      ' + this.route;
    }
}, ];


var cache = {};

function cacheAndDeliver(f, cb) {


    fs.stat(f, function(err, stats) {
        if (err) {
            return console.log('Oh no!, Eror', err);
        }
        var lastChanged = Date.parse(stats.ctime),
            isUpdated = (cache[f]) && lastChanged > cache[f].timestamp;
        if (!cache[f] || isUpdated) {
            fs.readFile(f, function(err, data) {
                console.log('loading ' + f + ' from file');
                if (!cache[f]) {
                    fs.readFile(f, function(err, data) {
                        if (!err) {
                            cache[f] = {
                                content: data,
                                timestamp: Date.now() //store a Unix    time stamp };

                            }
                            cb(err, data);

                            return;
                        }
                        console.log('loading ' + f + ' from cache');
                        cb(null, cache[f].content);
                    });
                }
            })
        }
    });
}
http.createServer(function(request, response) {
    /*
    var id = url.parse(decodeURI(request.url), true).query.id;
    //var lookup=path.basename(decodeURI(request.url));
    if (id) {
        pages.forEach(function(page) {
            if (page.id === id) {
                response.writeHead(200, {
                    'Content-Type': 'text/html'
                });
                response.end(typeof page.output === 'function' ? page.output() : page.output);
            }
        });
    }
    if (!response.finished) {
        response.writeHead(404);
        response.end('Page Not Found');
    }
    */
    var lookup = path.basename(decodeURI(request.url)) || 'index.html';
    var f = 'content/' + lookup;
    fs.exists(f, function(exists) {
        if (exists) {
            cacheAndDeliver(f, function(err, data) {
                if (err) {
                    response.writeHead(500);
                    response.end('Server Error!');
                    return;
                }
                var headers = {
                    'Content-type': mimeTypes[path.extname(f)]
                };
                response.writeHead(200, headers);
                response.end(data);
            });
            return;
        }
        response.writeHead(404); //no such file found!   
        response.end();
    });
}).listen(8080);