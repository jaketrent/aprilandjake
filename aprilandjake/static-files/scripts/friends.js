var friend = {
  app_prefix: "ajf-",
  fav_cache: new Array(),
  toggle_fav: function () {
    $(this).toggleClass("faved");
    var id = $(this).attr('id');
    var parts = id.split("|")
    var url = parts[2];
    if (friend.fav_exists(url)) {
      friend.unfav(url);
    } else {
      var data = friend.create_storage_data(parts);
      friend.fav(url, data);
    }
    friend.render_favs();
  },
  fav_exists: function (url) {
    var item = localStorage.getItem(friend.get_storage_key(url));
    return item != null;
  },
  fav: function (url, data) {
    localStorage.setItem(friend.get_storage_key(url), data);
    friend.add_to_cache(url, data, true);
  },
  unfav: function (url) {
    localStorage.removeItem(friend.get_storage_key(url));
    friend.rm_from_cache(url);
  },
  get_storage_key: function (url) {
    return friend.app_prefix + url;
  },
  create_storage_data: function (parts) {
    return parts[0] + "'s " + parts[1];
  },
  is_friend_data: function (index) {
    return localStorage.key(index).match(friend.app_prefix);
  },
  add_to_cache: function (url, name, sort) {
    friend.fav_cache.push({
        url: url,
        name: name
    });
    if (sort != undefined && sort) {
      friend.sort_cache();
    }
  },
  rm_from_cache: function (url) {
    var index = friend.get_index_in_cache(url);
    friend.fav_cache.splice(index, 1);
  },
  clear_cache: function () {
    friend.fav_cache = new Array();
  },
  cache_favs: function () {
    friend.clear_cache();
    var i = 0;
    for (i; i < localStorage.length; ++i) {
      if (friend.is_friend_data(i)) {
        var key = localStorage.key(i);
        friend.add_to_cache(key.substring(4), localStorage.getItem(key));
      }
    }
    friend.sort_cache();
  },
  sort_cache: function () {
    friend.fav_cache.sort(function (a, b) {
      if (a.name < b.name)
        return -1;
      if (a.name > b.name)
        return 1;
      return 0;
    });
  },
  fav_in_cache: function (url) {
    return friend.get_index_in_cache(url) != -1;
  },
  get_index_in_cache: function (url) {
    var index = -1;
    var i = 0;
    for (i; i < friend.fav_cache.length; ++i) {
      if (friend.fav_cache[i].url === url) {
        index = i;
        break;
      }
    }
    return index;
  },
  init_fav_stars: function () {
    if (friend.fav_cache.length <= 0) {
      friend.cache_favs();
    }
    $(".friend-list .fav").each(function () {
      var url = $(this).next(".proj").attr("href");
      if (friend.fav_in_cache(url)) {
        $(this).addClass("faved");
      }
    });
  },
  render_favs: function () {
    var i = 0;
    var num_favs = friend.fav_cache.length;
    var html = "";
    if (num_favs > 0) {
      html += "View your favorites on:<br /><a href='/friends/favs/'><img src='/static/images/runner-logo.png' /></a>";
    }
    $(".runner").html(html);
  },

  runner_index: -1,
  init_runner: function () {
    friend.runner_index = 0;
    if (friend.fav_cache.length <= 0) {
      friend.cache_favs();
    }
    friend.run();
    $(".prev").click(friend.prev);
    $(".next").click(friend.next);
    $(".runner-site em").click(friend.close_runner);
  },
  next: function () {
    if (++friend.runner_index == friend.fav_cache.length) {
      friend.runner_index = 0;
    };
    friend.run();
  },
  prev: function () {
    if (--friend.runner_index < 0) {
      friend.runner_index = friend.fav_cache.length - 1;
    }
    friend.run();
  },
  close_runner: function () {
    window.location = $("#runner-frame").attr("src");
  },
  run: function () {
    var fav = friend.fav_cache[friend.runner_index];
    $(".runner-site em").html(fav.name);
    $("#runner-frame").attr('src', fav.url);
  }
};