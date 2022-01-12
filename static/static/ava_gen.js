function generate(e) {
    e.preventDefault();

    let request = new XMLHttpRequest();

    request.open("POST", "/admin/ava/gen", true);   

    request.setRequestHeader("Content-Type", "application/json");

    request.addEventListener("load", function () {
        let url = JSON.parse(request.response).url;
        let div = document.querySelector('#frame_ava')
        div.innerHTML = `<iframe src="${url}" frameborder="0"></iframe>`
    });
    request.send();
}