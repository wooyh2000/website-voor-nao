var mysql = require('mysql');

var con = mysql.createConnection({
    host="oege.ie.hva.nl",
    user="wooyh",
    passwd="vyrdBMHRSmNtJx$",
    database="zwooyh"

});

con.connect(function(err) {
  if (err) throw err;
  console.log("Connected!");
});
