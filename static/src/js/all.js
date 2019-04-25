window.onload=function(){
	navEffect();
    //changetype(1);
    //$(".clr>li:first>a").click();
    $('#searchInput').bind('keypress',function(event){
        if(event.keyCode == "13"){
            $("#search_form").trigger("submit");
            return false;
            }
        });
    //$(".session").show();
}
function navEffect(){
	var startX, moveX, distanceX, currentX=0;
	var navBox = document.querySelector("nav");
	var navWidth = navBox.offsetWidth;
	// console.log(navWidth);
	var categoryBox = document.querySelector(".menu");
	// var cateWidth = categoryBox.offsetWidth;
	var lis=categoryBox.querySelectorAll("li");
	var count=lis.length;
	var cateWidth=lis[0].offsetWidth; // 一个分类的宽度
	categoryBox.style.width = count * cateWidth + "px";
	var categoryBoxWidth = count * cateWidth; // tab栏总长	

	var maxLeft=0;
	var minLeft= navWidth - categoryBoxWidth;

	var maxMoveLeft = maxLeft + cateWidth;
	var minMoveLeft = minLeft - cateWidth;

	console.log(maxMoveLeft+":"+minMoveLeft);
	// 1.add touch event 
	// 1.1 touch start
	categoryBox.addEventListener("touchstart", function(e){
		startX = e.targetTouches[0].clientX;
		// console.log(startX);
	});
	// 1.2 moving action
	categoryBox.addEventListener("touchmove", function(e){
		moveX = e.targetTouches[0].clientX;
		distanceX = moveX - startX;
		// 判断是否超出滑动范围
		if(currentX+distanceX>maxMoveLeft || currentX+distanceX<minMoveLeft){
			console.log("超出范围");
			return;
		}

		categoryBox.style.transition="none";
		categoryBox.style.left = distanceX + "px"

	});
	// 1.3 touch end
	categoryBox.addEventListener("touchend", function(e){
		if(currentX+distanceX < minLeft){
			currentX = minLeft;
			categoryBox.style.transition="left 0.5s";
			categoryBox.style.left = minLeft + "px"
		}else if(currentX+distanceX>maxLeft){
			currentX = maxLeft;
			categoryBox.style.transition="left 0.5s";
			categoryBox.style.left = maxLeft + "px"
		}else{currentX+=distanceX;};
	});

}

function changetype(n){
    //alert($(".clr>li").length);
    $(".clr>li").removeClass("active");
    $(".clr>#type"+n).addClass("active");
    $(".session").hide();
    $(".voicetype"+n).show();
}
