module.exports = function dogsController(
  mongo
) {
  return {
    getDogs,
    postDogs,
    putDogs,
    getRivals
  }

  function getDogs(req, res) {
    var response = {};
    mongo.dog.find({}).sort({rating: -1}).limit(10).exec(function(err, dogs){
      // Mongo command to fetch all dogs from collection.
      if(err) {
        response = {"error" : true,"message" : "Error fetching dogs"};
      } else {
        response = {"error" : false,"dogs" : dogs};
      }
      res.json(response);
    });
  }

  function postDogs(req, res) {
    var dog = new mongo.dog();
    var response = {};
    // fetch email and password from REST request.
    // Add strict validation when you use this in Production.
    dog.src = req.body.src; 
    dog.rating = 1200; 
    dog.wins = 0; 
    dog.losses = 0; 
    dog.reportCount = 0; 

    dog.save(function(err){
      // save() will run insert() command of MongoDB.
      // it will add new dog in collection.
      if(err) {
        response = {"error" : true,"message" : err.message};
      } else {
        response = {"error" : false,"dog" : dog};
      }
      res.json(response);
    });
  }

  function putDogs(req,res) {
    var response = {};
    // first find out record exists or not
    // if it does then update the record
    mongo.dog.findById(req.params.id,function(err, dog){
      if(err) {
        response = {"error" : true,"message" : err.message};
      } else {
        // we got dog from Mongo.
        // change it accordingly.
        if(req.body.reportCount !== undefined) {
          // case where email needs to be updated.
          dog.reportCount = req.body.reportCount;
        }
        if(req.body.rating !== undefined) {
          // case where email needs to be updated.
          dog.rating = req.body.rating;
        }
        if(req.body.wins !== undefined) {
          // case where email needs to be updated.
          dog.wins = req.body.wins;
        }
        if(req.body.losses !== undefined) {
          // case where password needs to be updated
          dog.losses = req.body.losses;
        }

        // save the dog
        dog.save(function(err){
          if(err) {
            response = {"error" : true,"message" : err.message};
          } else {
            response = {"error" : false,"dog" : dog};
          }
          res.json(response);
        })
      }
    });
  }

  function getRivals(req, res) {
    var response = {};
    res.json(response);
  } 
}
