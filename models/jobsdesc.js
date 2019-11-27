let mongoose = require('mongoose');

let jobSchema = new mongoose.Schema({
  TITLE : {type: String, required :false},
  COMPANY : {type: String, required:false},
  LOCATION : {type: String, required:false},
  SALARY : {type: Number, required: false},
  DESCRIPTION : {type: String, required:false},
  LINK : {type: String, required:false},
  cluster : {type : Number, required: false},
});

let jobs = module.exports = mongoose.model('samples',jobSchema,'samples');
