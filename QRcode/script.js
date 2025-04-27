window.onload = () =>{
    document.getElementById('site').focus()
}
async function generatoring() {
    const url = document.getElementById('site').value;
    const qr = document.getElementById('QR');
    const nav = document.getElementById('nav');
    if (url !== '') {
      const qrUrl = `https://api.qrserver.com/v1/create-qr-code/?size=150x150&data=${encodeURIComponent(url)}`;
      qr.src = qrUrl;
      await new Promise((resolve) => {
        qr.onload = () => resolve(); // wait until image fully loaded
      });
      nav.style.height = '425px';
    } else {
      alert('write url please');
    }
}