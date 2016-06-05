
// amap
 	var map = new AMap.Map("AmapContainer", {
        resizeEnable: true,
        center: [104.06, 30.67],
        zoom: 11
    });

    if (!isSupportCanvas()) {
        alert('SafeMove安全地图仅对支持canvas的浏览器适用,您所使用的浏览器不能使用热力图功能,请换个浏览器试试~')
    }
    var heatmap;
    map.plugin(["AMap.Heatmap"], function() {
        heatmap = new AMap.Heatmap(map, {
            radius: 25, //给定半径
            opacity: [0, 0.5],
            gradient:{
             // 0.65: 'rgb(117,211,248)',
             0.5: 'rgb(0, 0, 255)',
             0.6: 'rgb(125, 125, 200)',
             1: 'rgb(200, 100, 100)'
             }
        });
        heatmap.setDataSet({
            data: 
            // testdata,
            "http://beta.json-generator.com/api/json/get/E1WJDHBQZ",
            max: 10
        });
    });
    //判断浏览区是否支持canvas
    function isSupportCanvas() {
        var elem = document.createElement('canvas');
        return !!(elem.getContext && elem.getContext('2d'));
    }


// circle menu
	// var buttons = document.querySelectorAll(".radmenu a");
	// for (var i=0, l=buttons.length; i<l; i++) {
 //  	var button = buttons[i];
 //  	button.onclick = setSelected;
	// }

	// function setSelected(e) {
 //    	if (this.classList.contains("selected")) {
 //      	this.classList.remove("selected");
 //      	if (!this.parentNode.classList.contains("radmenu")) {
 //        	this.parentNode.parentNode.parentNode.querySelector("a").classList.add("selected")
 //      	} else {
 //        	this.classList.add("show");
 //      	}
 //    	} else {
 //      	this.classList.add("selected");
 //      	if (!this.parentNode.classList.contains("radmenu")) {
 //        	this.parentNode.parentNode.parentNode.querySelector("a").classList.remove("selected")
 //      	} else {
 //        	this.classList.remove("show");
 //      	}
 //    	}
 //    	return false;
	// }