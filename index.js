var express     =   require("express");
var app         =   express();
var bodyParser  =   require("body-parser");
var router      =   express.Router();
var mongoOp = require("./models/mongo");

app.use(bodyParser.json());
app.use(bodyParser.urlencoded({"extended" : false}));

router.get("/",function(req,res){
    res.json({"error" : false,"message" : "Hello World"});
});

router.route("/dogs")
    .get(function(req,res){
        var response = {};
        mongoOp.find({}).sort({rating: -1}).limit(10).exec(function(err,data){
        // Mongo command to fetch all data from collection.
            if(err) {
                response = {"error" : true,"message" : "Error fetching data"};
            } else {
                response = {"error" : false,"dogs" : data};
            }
            res.json(response);
        });
    })
		.post(function(req,res){
        var db = new mongoOp();
        var response = {};
        // fetch email and password from REST request.
        // Add strict validation when you use this in Production.
        db.src = req.body.src; 
        db.rating = 1200; 
        db.wins = 0; 
        db.losses = 0; 
        db.reportCount = 0; 

        db.save(function(err){
        // save() will run insert() command of MongoDB.
        // it will add new data in collection.
            if(err) {
                response = {"error" : true,"message" : err.message};
            } else {
                response = {"error" : false,"dog" : db};
            }
            res.json(response);
				});
		});

router.route("/dogs/:id")
 		.put(function(req,res){
        var response = {};
        // first find out record exists or not
        // if it does then update the record
        mongoOp.findById(req.params.id,function(err,data){
            if(err) {
                response = {"error" : true,"message" : err.message};
            } else {
            // we got data from Mongo.
            // change it accordingly.
                if(req.body.reportCount !== undefined) {
                    // case where email needs to be updated.
                    data.reportCount = req.body.reportCount;
                }
                if(req.body.rating !== undefined) {
                    // case where email needs to be updated.
                    data.rating = req.body.rating;
                }
                if(req.body.wins !== undefined) {
                    // case where email needs to be updated.
                    data.wins = req.body.wins;
                }
                if(req.body.losses !== undefined) {
                    // case where password needs to be updated
                    data.losses = req.body.losses;
                }

                // save the data
                data.save(function(err){
                    if(err) {
                        response = {"error" : true,"message" : err.message};
                    } else {
                        response = {"error" : false,"dog" : data};
                    }
                    res.json(response);
                })
            }
        });
    });

router.route("/dogs/rivals")
  .get(function(req, res){
    var response = null;
    while(!response) {
      console.log(response);
//      mongoOp.findRandom().limit(2).exec(function(err, data) {
//        console.log(data[0]["_id"]);
//        console.log(data[1]["_id"]);
//        console.log("help");
//        if(err) {
//          response = {"error": true, "message": err.message};
//        } else if(data.length < 2) {
//          response = {"error": true, "message": "Who let the dogs out"};
//        } else if(data[0]["_id"] != data[1]["_id"]) {
//          response = {"error": false, "dogs": data};
//        }
//      });
    }
    res.json(response);
  });
    
app.use('/',router);

app.listen(3000);
console.log("Listening to PORT 3000");

