
var request = require('request');
var cheerio = require('cheerio');

exports.list = function (req, res) {
  request('http://pinterest.com/jaketrent/pins/', function(err, resp, body){
    var $ = cheerio.load(body);
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
    /*$pins.each(function(i, pin){
      $pin = $(pin);
      pins.push({
        img: $pin.find('.PinImageImg').attr('src'),
        url: 'http://pinterest.com' + $pin.find('.ImgLink').attr('href'),
        desc: $pin.find('.description').text()
      });
    });*/
    res.send(pins);
  });
};