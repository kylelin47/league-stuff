function checkAnswer() {
  var response = document.getElementById('answer').value;
  location = '/' + response;
  return false;
}