//data
let colors = {
    'red':0,
    'green':0,
    'blue':0
}
// degree of color 
function GetValue(id) {
    setInterval(() => {
        colors[id] = $(`#r${id}`).val()
    },1);
}
GetValue('red')
GetValue('green')
GetValue('blue')
// display the color
setInterval(() => {
    let color = 'rgb('+colors.red+','+colors.green+','+colors.blue+')'
    console.log(color)
    document.getElementById('crgb').innerHTML = color;
    document.getElementById('crgb').style = 'background-color:'+color
},1);