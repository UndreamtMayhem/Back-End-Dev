const dataSerialization = require('./dataSerialization');

/*
dataSerialization.csv2JSON({
    seperator: ',',
    inputPath: 'out.csv',
    outputPath: 'data.json'
});



dataSerialization.Json2CSV({
    json2convert: './example.json',
    outputPath: "./data.csv",
    requiredFields: ['first_name', 'email', 'last_name']
});


dataSerialization.Json2XML({
    json2convert: './example.json',
    outputPath: "./data.xml",
    rootName: "data"
})
*/
dataSerialization.xml2JSON({
    xml2convert: 'data.xml',
    outputPath: "./x.json",
})