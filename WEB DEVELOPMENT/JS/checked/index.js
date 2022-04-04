document.getElementById("click").onclick = function () {
    if (document.getElementById("check").checked == true) {
        console.log("You ARE subscribe");
    }

    else {
        console.log("You are NOT subscribe");
    }
}