function resize (target) {
        console.log('Resizing...');
    console.log(window.innerWidth);
    
    var win = window.innerWidth;
    var rate1 = 0.325*(win-940) + 269;
    var rate2 = 0.36*(win-940) + 300;
    
    var size = rate2
    console.log("size =",rate2);

    if (window.innerWidth<940){
    	resizeTarget(target,size,size)
    }
}

function resizeTarget(Target,Width,Height){
	var count = document.getElementsByClassName(Target).length;
	console.log(count);
    for(var i=0; i<count; i++){
        document.getElementsByClassName(Target)[i].style.width=Width+"px";
        document.getElementsByClassName(Target)[i].style.height=Height+"px";
        }
}


