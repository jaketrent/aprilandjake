

function MainCtrl($http) {

  $http.jsonp('http://gdata.youtube.com/feeds/api/playlists/PLbWbiOD0YMByR_l4GCzD7V3_d54HF9fZ9?v=2&alt=jsonc&callback=JSON_CALLBACK')
    .success(function(data, status, headers, config) {
      console.log(data);
    }).error(function(data, status, headers, config) {
      console.log('ERROR');
      console.log(data);
    });

}