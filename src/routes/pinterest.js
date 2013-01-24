
var request = require('superagent');
var cheerio = require('cheerio');

exports.list = function (req, res) {
  var username = req.param('username');
  request
    .get('http://pinterest.com/' + username + '/pins/')
    .end(function(response){

      console.log('pinterest ws status: ' + response.statusCode);
      console.log(response.text);

      var $ = cheerio.load(response.text);
      var pins = [];
      var $pin;
      var $pins = $('.pin');

      var i = 0;
      for (i; i < 10; ++i) {
        $pin = $pins.eq(i);
        pins.push({
          img: $pin.find('.PinImageImg').attr('src'),
          url: 'http://pinterest.com' + $pin.find('.ImgLink').attr('href'),
          desc: $pin.find('.description').text()
        });
      }
      res.send(pins);
    });
};