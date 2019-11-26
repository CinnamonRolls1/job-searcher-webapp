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
  console.log(role,location);
  res.redirect('/results');

})



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


  Job.find({},function(err,docs){
    res.render('results',{job_desc : docs});
  })


});

//Start Server
const PORT= 3000;

app.listen(PORT, () => console.log(`Server started on ${PORT}`));
