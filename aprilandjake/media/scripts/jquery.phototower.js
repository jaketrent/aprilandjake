(function ($) {

  $.fn.phototower = function (settings) {

    var defaults = {
      url: "http://picasaweb.google.com/data/feed/base/user/trent.jake?alt=json&kind=photo&hl=en_US&access=public",
      top_offset: 85,
      img_height: 216,
      img_width: 288,
      addt_height: 40
    };

    var opts = $.extend({}, defaults, settings);

    var photo = {
      rendered_index: 0,
      cache: [],
      get_data: function ($this) {
        $.ajax({
          url: opts.url,
          type: "GET",
          dataType: "jsonp",
          success: function (data) {
            photo.init($this, data);
          },
          error: function () {
            // fail - minor feature - photos towering like jenga
          }
        });
      },
      init: function ($this, data) {
        photo.persist_cache(data);
        $(window).scroll(function () {
          photo.render_more($this);
        });
      },
      persist_cache: function (data) {
        for (e in data.feed.entry) {
          var entry = data.feed.entry[e];
          var img = photo.convert_entry(entry);
          if (photo.filter_cache(img)) {
            photo.cache.push(img);
          }
        }
      },
      filter_cache: function (img) {
        return img.thumbnail.height === opts.img_height;
      },
      convert_entry: function (entry) {
        return {
          thumbnail: entry.media$group.media$thumbnail[2]
        }
      },
      render_more: function ($this) {
        var bottomScrollY = $(window).scrollTop() + $(window).height();
        var towerHeight = photo.rendered_index * (opts.img_height + opts.addt_height) + opts.top_offset;
        if (towerHeight + (opts.img_height + opts.addt_height) < bottomScrollY) {
          var thumbnail = photo.cache[photo.rendered_index++].thumbnail;
          var $img = $($("#img-tmpl").tmpl(thumbnail));
          $img.css({
            'top': towerHeight,
            'left': 680
          });

          $this.queue("tower", function() {
            $this.append($img);
            setTimeout(function() {
              $this.dequeue("tower");
              $img.css({
                opacity: 1
              });
            }, 1500);
          });
          $this.dequeue("tower");
        }
      }
    };

    this.each(function () {
      photo.get_data($(this));
    });

    return this;

  };

})(jQuery);