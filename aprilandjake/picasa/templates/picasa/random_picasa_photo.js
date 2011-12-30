timeout = 8000;

function getRandomPhoto() {
    /**
     * Do something like this in the template that includes this script:
     * <script type="text/javascript">
     * randomPhotoURL = '{% url picasa-random-photo %}';
     * </script>
     */
    $.ajax({'url': randomPhotoURL,
            'type': 'GET',
            'data': {},
            'dataType': 'json',
            'error': function (xhr, status, msg) {
                setTimeout(getRandomPhoto, 1000);
            },
            'success': function (json) {
                    container = $('#picasa-random-photo');
                    anchor = $('#picasa-random-photo-link');
                    container.fadeOut('slow', function() {
                            container.css('background', "transparent url('" + json.image + "') center center no-repeat");
                            setTimeout(fadePhotoIn, 500);
                        });
                    anchor.attr('href', json.url);
                }
            });
}

function fadePhotoIn() {
    $('#picasa-random-photo').fadeIn('normal');
    setTimeout(getRandomPhoto, timeout);
}

setTimeout(getRandomPhoto, timeout);