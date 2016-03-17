var express     =   require("express");
var bodyParser  =   require("body-parser");
var mongoose    =   require("mongoose");
mongoose.connect('mongodb://localhost:27017/dogshow');

module.exports = function $app(
    dogsController
) {
  var app = express();
  var router = express.Router();
  // Pre-Middleware
  app.use(bodyParser.json());
  app.use(bodyParser.urlencoded({"extended" : false}));

  router.route("/dogs")
      .get(dogsController.getDogs)
      .post(dogsController.postDogs);

  router.route("/dogs/:id")
      .put(dogsController.putDogs);

  router.route("/dogs/rivals")
    .get(dogsController.getRivals);

  // Post-Middleware
      
  app.use('/',router);

  return app;
}
