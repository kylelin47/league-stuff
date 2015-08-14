var pyleagueweb = (function (my) {
    var bigFont = '200px';

    my.changeColors = function(className) {
        elements = document.getElementsByClassName(className);
        for (var i = 0; i < elements.length; i++) {
            elements[i].style.backgroundColor=my.colorScheme;
            elements[i].style.fontSize=bigFont;
        }
    };

    my.goPlaces = function(place) {
        location = place;
    };

    return my;
}(pyleagueweb || {}));
