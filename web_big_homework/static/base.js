function createLine(){
	node_list = document.getElementsByTagName("g");
	for (let i = node_list.length - 1; i >= 0; i--) {
		node_list[i].addEventListener("click", function(){
			removeLine(document.getElementById("main"))
			var node_name = this.getElementsByTagName("title")[0].innerHTML
			$.getJSON('/line_info/'+node_name, function(ret){
				for(let i = ret.length - 1; i >= 0; i--){
					var line = document.createElementNS("http://www.w3.org/2000/svg", "line")
					if(line){
						line.setAttribute("x1", ret[i].x1);
						line.setAttribute("y1", ret[i].y1);
						line.setAttribute("x2", ret[i].x2);
						line.setAttribute("y2", ret[i].y2);
						line.style.stroke = "rgb(255,0,0)";
						line.style.strokeWidth = 2;
					}
					document.getElementById("main").appendChild(line);
				}
			})
		})
	}
}

function removeLine(root){
	line_list = root.getElementsByTagName("line");
	for (var i = line_list.length - 1; i >= 0; i--) {
		root.removeChild(line_list[i]);
	}
}


window.onload = createLine;