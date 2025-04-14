//data
let colors = {
    'red':0,
    'green':0,
    'blue':0
}
// choose color
class Color extends HTMLElement{
    connectedCallback(){
        let color = this.getAttribute('color')
        this.innerHTML = "<label class='label'>"+color+'</label><label '+'id='+color+'></label>' 
    }
}
customElements.define("chose-color",Color)
// degree of color 
function GetValue(id) {
    setInterval(() => {
        colors[id] = document.getElementById('r'+id).value
        document.getElementById(id).innerHTML = colors[id];
    },1);
}
GetValue('red')
GetValue('green')
GetValue('blue')
// display the color
setInterval(() => {
    let color = 'rgb('+colors.red+','+colors.green+','+colors.blue+')'
    document.getElementById('crgb').innerHTML = color;
    document.getElementById('crgb').style = 'background-color:'+color
},1);