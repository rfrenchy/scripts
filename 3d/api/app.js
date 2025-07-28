
var express = require('express');
var mysql = require('mysql');

var connection = mysql.createConnection({
    host: 'localhost',
    user:  'debian-sys-maint',
    password: 'QCRt3iJIpawP714C',
    database: '3d'
});

var app = express();

app.get('/data', function (req, res) {
    console.log("Received a request for /data");
    res.send("test\n");

    /**
    const x = connection.query('SELECT * FROM Person WHERE id = 2');

    const names = []
    let count = 0;
    
    x.on('result', function (row) { 
        
        if (row.Firstname != null) {
            names.push(row.Firstname);
            res.send(names[count] + "\n");
            count++;
        }
    })
        //});
    */
})

app.get('/reverse/:word', function(req, res) {
    res.send(req.params.word.split("").reverse().join("") + "\n");
})


app.get('/person/:id', function(req, res) {
   const person = connection.query(`SELECT * FROM Person WHERE id = "${req.params.id}";`);
   person.on('result', function(row) {
        res.send(row.id + " " + row.Firstname + " " + row.Lastname + " " + row.Age + " " + row.Occupation + "\n");
   }) 
})

app.get('/person/name/:firstname', function(req, res) {
   const person = connection.query(`SELECT * FROM Person WHERE BINARY Firstname = "${req.params.firstname}";`);

   person.on('result', function(row) {
        res.send(row.Firstname + " " + row.Lastname + "\n");
   }) 
})

// var app = express();

app.listen(3000, function () {
  console.log('listening on port 3000');
});