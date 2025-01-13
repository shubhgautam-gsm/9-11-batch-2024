
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




function bulbon(){
    document.getElementById('bulb').src = '../images/pic_bulbon.gif'
     document.getElementById('bulb').style.border = '2px solid red'
}
function bulboff(){
    document.getElementById('bulb').src = '../images/pic_bulboff.gif'
}

