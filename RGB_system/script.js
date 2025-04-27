function getColor(){
    let color = `rgb(${$(`#red`).val()},${$(`#green`).val()},${$(`#blue`).val()})`
    $("#rgb").css("background-color",color)
    $("#rgb").text(color)
}
let colors = ['red','green','blue']
for (let i = 0; i < colors.length; i++) {
    $(`#${colors[i]}`).css('background',`linear-gradient(-45deg,${colors[i]},transparent)`)
}
getColor()
$(".resize").on(
    'input',function(){
          getColor()
    }
)