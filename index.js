const express = require('express');
const path= require('path');
const bodyParser = require('body-parser');
var app = express();

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
  var jobs =  [
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
  res.render('results',{job_desc : jobs});
});

//Start Server
const PORT= 3000;

app.listen(PORT, () => console.log(`Server started on ${PORT}`));
