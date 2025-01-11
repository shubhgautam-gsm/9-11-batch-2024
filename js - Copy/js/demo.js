
var i = 0;
function change() {
    if (i == 0) {
        i++
        document.getElementById('chg').style.display = 'none';
    }
    else {
        i--;
        document.getElementById('chg').style.display = 'block';
    }
}
