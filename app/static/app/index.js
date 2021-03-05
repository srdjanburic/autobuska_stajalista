const sacuvaj = document.getElementById("sacuvaj")
function checkboxes(){
    let inputElems = document.getElementsByTagName("input"),
    count = 0;
    for (let i=0; i<inputElems.length; i++) {
    if (inputElems[i].type === "checkbox" && inputElems[i].checked === true){
        count++;
        console.log(count);
    }
	if(count >=3){
		sacuvaj.disabled = false
	}else{
		sacuvaj.disabled = true
	}
    
}}

