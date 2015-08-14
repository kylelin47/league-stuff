function redirect() {
    var dropdown = document.getElementById('region');
    var region = dropdown.options[dropdown.selectedIndex].value.toLowerCase();
    var name = document.getElementById('name').value;
    location = '/players/' + region + '/' + name;
    return false;
}
