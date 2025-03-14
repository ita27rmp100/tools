// fetch
// linkAPI = https://api.github.com/repos/
$("#preview , #dp").hide()
$("#title").text(document.title)
let repoName = ''
let widthRange= document.getElementById("widthController")
widthRange.addEventListener('input',()=>{$("#preview").css('width',`${$("#widthController").val()}px`)})
function fetchRepoDetails(){
    let repo = $("#repo-name").val().replace("https://github.com/",'')
    $.get(`https://api.github.com/repos/${repo}`,function(data){
        repoName = data.name
        $("#userrepo").html(
            `<h4 class="font-weight-bold mb-0 text-muted">
                    ${data.owner.login}/
                    <br> 
                    <span class="text-dark">${data.name}</span>
            </h4>`
        )
        $("#avatar").attr({
            'src': data.owner.avatar_url,
            'crossorigin': 'anonymous'
        });
        $("#fork").text(data.forks_count);
        $("#star").text(data.stargazers_count);
        $("#issue").text(data.open_issues_count);
        $("#cntrb").text(data.network_count)
        $("#desc").text(data.description.slice(0,100)+"...")
        $("#preview").fadeIn()
    $("#dp").show()
    })
}
function downloadPreview() {
    const preview = document.getElementById('preview');     
    html2canvas(preview, {
        useCORS: true,
        allowTaint: false,
        logging: true,
        proxy: "https://cors-anywhere.herokuapp.com/"
    }).then(canvas => {
        const link = document.createElement("a");
        link.download = `${repoName}_preview.png`;
        link.href = canvas.toDataURL("image/png");
        link.click();
    }).catch(error => console.error("Error generating the image:", error));
}