var pyleagueweb = (function (my) {
    my.changeColors = function (className) {
        elements = document.getElementsByClassName(className);
        for (var i = 0; i < elements.length; i++) {
            elements[i].style.backgroundColor='blue';
        }
    }

    return my;
}(pyleagueweb || {}));
