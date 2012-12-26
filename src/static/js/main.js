
angular.module('aj', [], function ($interpolateProvider) {
  $interpolateProvider.startSymbol('[[');
  $interpolateProvider.endSymbol(']]');
});

function MainCtrl($scope, $http) {
  $http.jsonp('http://gdata.youtube.com/feeds/api/playlists/PLbWbiOD0YMByR_l4GCzD7V3_d54HF9fZ9?v=2&alt=jsonc&callback=JSON_CALLBACK')
    .success(function(data, status, headers, config) {
      $scope.videos = data.data.items;
      console.log(data);
    }).error(function(data, status, headers, config) {
      console.log('ERROR');
      console.log(data);
    });

  $scope.callPlayer = function (frame_id, func, args) {

    console.log('calling player');
    console.log('args:');
    console.log(args);
    console.log('done');

    if (window.jQuery && frame_id instanceof jQuery) frame_id = frame_id.get(0).id;
    var iframe = document.getElementById(frame_id);
    if (iframe && iframe.tagName.toUpperCase() != 'IFRAME') {
      iframe = iframe.getElementsByTagName('iframe')[0];
    }

    // When the player is not ready yet, add the event to a queue
    // Each frame_id is associated with an own queue.
    // Each queue has three possible states:
    //  undefined = uninitialised / array = queue / 0 = ready
    if (!$scope.callPlayer.queue) $scope.callPlayer.queue = {};
    var queue = $scope.callPlayer.queue[frame_id],
      domReady = document.readyState == 'complete';

    if (domReady && !iframe) {
      // DOM is ready and iframe does not exist. Log a message
      window.console && console.log('$scope.callPlayer: Frame not found; id=' + frame_id);
      if (queue) clearInterval(queue.poller);
    } else if (func === 'listening') {
      // Sending the "listener" message to the frame, to request status updates
      if (iframe && iframe.contentWindow) {
        func = '{"event":"listening","id":' + JSON.stringify(''+frame_id) + '}';
        iframe.contentWindow.postMessage(func, '*');
      }
    } else if (!domReady || iframe && (!iframe.contentWindow || queue && !queue.ready)) {
      if (!queue) queue = $scope.callPlayer.queue[frame_id] = [];
      queue.push([func, args]);
      if (!('poller' in queue)) {
        // keep polling until the document and frame is ready
        queue.poller = setInterval(function() {
          $scope.callPlayer(frame_id, 'listening');
        }, 250);
        // Add a global "message" event listener, to catch status updates:
        messageEvent(1, function runOnceReady(e) {
          var tmp = JSON.parse(e.data);
          if (tmp && tmp.id == frame_id && tmp.event == 'onReady') {
            // YT Player says that they're ready, so mark the player as ready
            clearInterval(queue.poller);
            queue.ready = true;
            messageEvent(0, runOnceReady);
            // .. and release the queue:
            while (tmp = queue.shift()) {
              $scope.callPlayer(frame_id, tmp[0], tmp[1]);
            }
          }
        }, false);
      }
    } else if (iframe && iframe.contentWindow) {
      // When a function is supplied, just call it (like "onYouTubePlayerReady")
      if (func.call) return func();
      // Frame exists, send message
      iframe.contentWindow.postMessage(JSON.stringify({
        "event": "command",
        "func": func,
        "args": args || [],
        "id": frame_id
      }), "*");
    }
    /* IE8 does not support addEventListener... */
    function messageEvent(add, listener) {
      var w3 = add ? window.addEventListener : window.removeEventListener;
      w3 ?
        w3('message', listener, !1)
        :
        (add ? window.attachEvent : window.detachEvent)('onmessage', listener);
    }
  }

}