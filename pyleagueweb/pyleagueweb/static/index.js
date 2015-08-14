var pyleagueweb = (function (my) {
    my.colorScheme = 'blue';

    my.redirect = function() {
        var info = getPageInformation();
        location = '/players/' + info.region + '/' + info.name;
        return false;
    };

    function getPageInformation() {
        var dropdown = document.getElementById('region');
        var region = dropdown.options[dropdown.selectedIndex].value.toLowerCase();
        var name = document.getElementById('name').value;
        var info = {
            name:  name,
            region: region
        };
        return info;
    }

    return my;
}(pyleagueweb || {}));
