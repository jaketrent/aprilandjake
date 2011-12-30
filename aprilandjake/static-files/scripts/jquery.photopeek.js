/**
 * 1. select all piles
 * 2.
 */

(function ($) {

  $.fn.photopeek = function (settings) {

    var opts = {
      transforms: [
        [
          { top: 20, left: 30, rotate: '-3deg' }, // top right
          { top: -20, left: 20, rotate: '8deg' }, // bottom right
          { top: 40, left: -30, rotate: '-10deg' }, // bottom left
          { top: -20, left: -30, rotate: '-5deg' }, // top left
          { top: 0, left: 0 } // center
        ]
      ],
      use_random_transforms: false,
      min_x_offset: 0,
      max_x_offset: 40,
      min_y_offset: 0,
      max_y_offset: 40,
      min_rotate: -10,
      max_rotate: 10
    };

    $.extend(opts, settings);

    var preset_transforms = function ($imgs) {
      var x_sign = -1;
      var y_sign = -1;
      var presets = [];
      $imgs.each(function (index) {
        x_sign = x_sign * -1;
        y_sign = index % 2 ? y_sign * -1 : y_sign;
        if (index < $imgs.length - 1) {
          presets.push({
            top: x_sign * randomXToY(opts.min_y_offset, opts.max_y_offset),
            left: y_sign * randomXToY(opts.min_x_offset, opts.max_x_offset),
            rotate: randomXToY(opts.min_rotate, opts.max_rotate) + 'deg'
          });
        } else {
          presets.push({
            top: 0,
            left: 0,
            rotate: "0deg"
          });
        }
      });
      opts.transforms.push(presets);
    };

    var randomXToY = function (minVal, maxVal, floatDigits) {
      var randVal = minVal + (Math.random() * (maxVal - minVal));
      return typeof floatDigits == 'undefined' ? Math.round(randVal) : randVal.toFixed(floatDigits);
    };

    if (opts.use_random_transforms) {
      opts.transforms = [];
    }

    this.each(function (index) {

      var $album = $(this);
      var $imgs = $album.children("img");

      var trans = null;
      if (opts.use_random_transforms) {
        preset_transforms($imgs);
        trans = opts.transforms[index];
      } else {
        trans = opts.transforms[0];
      }
      $album.bind("mouseenter", function () {
        $album.children("img").each(function (img_index) {
          var imgs_trans = trans[img_index];
          $(this).attr('style', '-moz-transform: rotate(' + imgs_trans.rotate + ') translate(' + imgs_trans.left + 'px, ' + imgs_trans.top + 'px); ' +
                             '-webkit-transform: rotate(' + imgs_trans.rotate + ') translate(' + imgs_trans.left + 'px, ' + imgs_trans.top + 'px); ' +
                                  '-o-transform: rotate(' + imgs_trans.rotate + ') translate(' + imgs_trans.left + 'px, ' + imgs_trans.top + 'px); ' +
                                 '-ms-transform: rotate(' + imgs_trans.rotate + ') translate(' + imgs_trans.left + 'px, ' + imgs_trans.top + 'px); ' +
                                     'transform: rotate(' + imgs_trans.rotate + ') translate(' + imgs_trans.left + 'px, ' + imgs_trans.top + 'px);');
        });
      });

      $album.bind("mouseleave", function() {
        $album.children("img").each(function (img_index) {
          $(this).attr('style', '');
        });
      });

    });

  };

  return this;

})(jQuery);
