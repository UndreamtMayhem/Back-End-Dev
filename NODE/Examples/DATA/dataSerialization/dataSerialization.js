// TODO use dirname instead


// convert2JSON DEPENDENCIES
var csv2json = require('csv2json');
var fs = require('fs');

// convert2CSV DEPENDENCIES

const Json2csvTransform = require('json2csv').Transform;
// XML dependencies
var xml2js = require('xml2js');

// dataSerialization

module.exports = {
    csv2JSON: function(options) {
        fs.createReadStream(options.inputPath)
            .pipe(csv2json({
                // Defaults to comma.
                separator: options.separator
            }))
            .pipe(fs.createWriteStream(options.outputPath));
    },
    Json2CSV: function(options) {
        const opts = { fields: options.requiredFields };
        const transformOpts = { highWaterMark: 16384, encoding: 'utf-8' };

        try {
            const input = fs.createReadStream(options.json2convert, { encoding: 'utf8' });

            const output = fs.createWriteStream(options.outputPath, { encoding: 'utf8' });

            const json2csv = new Json2csvTransform(opts, transformOpts);

            const processor = input.pipe(json2csv).pipe(output);

        } catch (err) {
            console.error(err);
        }
    },
    Json2XML: function(options) {
        var profiles = require(options.json2convert);
        var builder = new xml2js.Builder({ rootName: options.rootName });
        profiles = builder.buildObject(profiles);

        console.log(profiles); // <-- show me the XML 
        try {
            fs.writeFile(options.outputPath, profiles, function(err) {
                if (err) {
                    return console.log(err);
                }

                console.log("The file was saved!");
            });
        } catch (err) {
            console.error(err);
        }
    },

    xml2JSON: function(options) {

        var parser = new xml2js.Parser();
        fs.readFile(__dirname + options.xml2convert, function(err, data) {
            parser.parseString(data, function(err, result) {
                var json = JSON.stringify(result);
                console.log(json)
                fs.writeFile(options.outputPath, json, function(err) {
                    if (err) {
                        return console.log(err);
                    }
                    console.log("The file was saved!");
                });
            });
        });
    }
}