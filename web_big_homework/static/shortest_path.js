var clicked_items = [];

function main(){
	document.addEventListener("click", removeTag(document.getElementById("main"), "line"));
	createLine();
}

function createLine(){
	node_list = document.getElementsByTagName("g");
	for (let i = node_list.length - 1; i >= 0; i--) {
		node_list[i].addEventListener("click", function(){
			removeTag(document.getElementById("main"), "line");
			var node_name = this.getElementsByTagName("title")[0].innerHTML;
			clicked_items.push(node_name);
			if (clicked_items.length > 2){
				clicked_items.shift();
			}
			if (clicked_items.length == 2){
				$.getJSON('/shortest_path/'+clicked_items[0]+'/'+clicked_items[1], function(ret){
					for(let i = ret.length - 1; i >= 0; i--){
						var line = document.createElementNS("http://www.w3.org/2000/svg", "line")
						if(line){
							line.setAttribute("x1", ret[i].x1);
							line.setAttribute("y1", ret[i].y1);
							line.setAttribute("x2", ret[i].x2);
							line.setAttribute("y2", ret[i].y2);
							line.style.stroke = "rgb(255,0,0)";
							line.style.strokeWidth = 2;
							line.start = ret[i].start;
							line.end = ret[i].end;
						}
						document.getElementById("main").appendChild(line);
					}
				})
			}
			$.getJSON('/cv_info/'+node_name, function(ret){
				document.getElementById("cv_picture").src = ret.src;
				document.getElementById("cv_intro").innerHTML = ret.intro;
			})
		})
	}
}

function addLiChild(root, info){
	var temp = document.createElement("li");
	temp.innerHTML = info;
	root.appendChild(temp);
}

function removeTag(root, tag_name){
	line_list = root.getElementsByTagName(tag_name);
	for (var i = line_list.length - 1; i >= 0; i--) {
		root.removeChild(line_list[i]);
	}
}

function fill_edge_info(start, end){
	removeTag(document.getElementById("edge_list"), "ul");
	removeTag(document.getElementById("edge_list"), "hr");
	$.getJSON('/line_info/'+start+'/'+end, function(ret){
		for(let i = ret.length - 1; i >= 0; i--){
			var container = document.createElement("ul");
			addLiChild(container, ret[i].anime_name+", "+ret[i].year);
			addLiChild(container, ret[i].start_cv+": "+ret[i].start_char);
			addLiChild(container, ret[i].end_cv+": "+ret[i].end_char);
			document.getElementById("edge_list").appendChild(container);
			document.getElementById("edge_list").appendChild(document.createElement("hr"));
		}
	})
}

window.onload = main;