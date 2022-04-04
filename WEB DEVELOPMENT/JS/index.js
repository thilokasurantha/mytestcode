var num = Number(document.getElementById("num").innerHTML)

document.getElementById("increace").onclick = function() {
    num += 1
    document.getElementById("num").innerHTML = num
}



document.getElementById("g_zero").onclick = function() {
    num = 0
    document.getElementById("num").innerHTML = num
}


document.getElementById("decreace").onclick = function() {
    num -= 1
    document.getElementById("num").innerHTML = num
}
