window.onload = () =>{
    document.getElementById('site').focus()
}
function generatoring() {
    let url = document.getElementById('site').value
    if (url!='') {
        document.getElementById('QR').src = `https://api.qrserver.com/v1/create-qr-code/?size=150x150&data=${url}`
        document.getElementById('nav').style.height = '425px'
    } else {
        alert('write url please')
    }
}