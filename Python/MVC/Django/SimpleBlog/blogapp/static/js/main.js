
var position = 0;
var hamburgerBtn = document.getElementById("hamburger-btn");
var closeBtn = document.getElementById("close-btn");
var rightDrawer = document.getElementById("rightDrawer");
isOpen = false;

function toggle(evt) {
    position++;

    if (!isOpen) {
        rightDrawer.classList.add("open");
        isOpen = true;
    } else {
        rightDrawer.classList.remove("open");
        isOpen = false;
    }
}

hamburgerBtn.addEventListener("click", toggle);
closeBtn.addEventListener("click", toggle);




function open_sidenav() {
    document.getElementById("mySidebar").style.display = "block";
}
function close_sidenav() {
    document.getElementById("mySidebar").style.display = "none";
}