
const express = require('express');
const mysql = require('mysql');

const connection = mysql.createConnection({
    host: 'localhost',
    user:  'debian-sys-maint',
    password: 'QCRt3iJIpawP714C',
    database: '3d'
});

const app = express();

app.get('/data', function (req, res) {
    console.log("Received a request for /data");
    res.send("test\n");
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

app.get('/lettercount/:word', function(req, res) {
    const chars = req.params.word.split("")
    const keys = {};
    chars.forEach(c => {
        const k = keys[c];
        if (!k) keys[c] = 1;
        else keys[c] = keys[c] + 1
    })
    
    res.send(JSON.stringify(keys) + "\n")
})

app.listen(3000, function () {
  console.log('listening on port 3000');
});