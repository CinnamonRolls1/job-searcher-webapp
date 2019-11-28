const express = require('express');
const path= require('path');
const bodyParser = require('body-parser');
const mongoose = require('mongoose')


//connecting to database
mongoose.connect('mongodb://localhost/jobData');
let conn = mongoose.connection;
//conn.db.listCollections().toArray(function(err,names){console.log(names);})

//check db connection
conn.once('open',function(){console.log('Connected to mongoDB');});

//check db error
conn.on('error',function(err){console.log(err);})

//console.log(conn.readyState );

//Init app
var app = express();

//Bring model
let Job = require('./models/jobsdesc');
//console.log(Job.db.name);
//conn.db.listCollections().toArray(function(err,names){console.log(names);})

//Load view engine
app.set('views',path.join(__dirname, 'views'));
app.set('view engine','pug');

//Body-Parser middleware
app.use(bodyParser.urlencoded({extended:false}));
app.use(bodyParser.json());

//GET for Home route
app.get('/', function(req,res){
  res.render('home');
});


app.post('/', function(req, res){
  //get form data
  var role = req.body.role;
  var location = req.body.location;
  var salary = req.body.salary;
  console.log(role,location);


  //writing query to json

  // var obj = {
    //   role: role,
    //   location: location,
    //   salary: salary
    // };
  var fs = require('fs');

  let rawdata = fs.readFileSync('query.json');
  let obj = JSON.parse(rawdata);
  obj.role=role;
  obj.location=location;
  obj.salary=salary;
  var json = JSON.stringify(obj);
  fs.writeFileSync('query.json', json);
  var util = require("util");
  console.log("jnnnfjf ");

  var spawn = require("child_process").spawn;
  var process = spawn('python3',["match_query.py"]);

  res.redirect('/results');

})


/*app.get('/results', function(req,res) {
  var jobs = [
    { title : 'Software engineer', desc : 'random', salary : 10000},
       { title : 'Back end', desc : 'random', salary : 10000},
       { title : 'Cloud Reliabilty', desc : 'random', salary : 10000},
       { title : 'Compiler Research', desc : 'random', salary : 10000},
       { title : 'Full Stack', desc : 'random', salary : 10000},
       { title : 'Content Creator', desc : 'random', salary : 10000},
       { title : 'Server Technology', desc : 'random', salary : 10000},
       { title : 'Manager', desc : 'random', salary : 10000},
       { title : 'Project Head', desc : 'random', salary : 10000}
  ]
  res.render('results', {job_desc: jobs});
});*/

app.get('/sponsered', function(req,res) {
  res.render('sponsered');
});
app.get('/about', function(req, res) {
  res.render('about');
});
app.get('/team', function(req, res) {
  res.render('team');
});



app.get('/results', function(req,res) {
  // var jobs =  [
  //   { title : 'Software engineer', desc : 'random', salary : 10000},
  //   { title : 'Back end', desc : 'random', salary : 10000},
  //   { title : 'Cloud Reliabilty', desc : 'random', salary : 10000},
  //   { title : 'Compiler Research', desc : 'random', salary : 10000},
  //   { title : 'Full Stack', desc : 'random', salary : 10000},
  //   { title : 'Content Creator', desc : 'random', salary : 10000},
  //   { title : 'Server Technology', desc : 'random', salary : 10000},
  //   { title : 'Manager', desc : 'random', salary : 10000},
  //   { title : 'Project Head', desc : 'random', salary : 10000}
  // ]


  // Job.find({},function(err,docs){
    // console.log(docs.slice(1,3));
  var fs = require('fs');
  let data = fs.readFileSync("result.json");
  let obj = JSON.parse(data);
  console.log(obj.jobs);
  res.render('results',{job_desc : obj});
  // });


});

//Start Server
const PORT= 8000;

app.listen(PORT, () => console.log(`Server started on ${PORT}`));
