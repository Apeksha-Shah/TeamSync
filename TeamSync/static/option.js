
document.addEventListener("DOMContentLoaded", function() {

    var btn1 = document.getElementById("btn1");
    let modal = document.getElementById("m1");  
    let close1 = document.getElementById("cancel");
    let close2 = document.getElementById("cancel2");
    let bt2 = document.getElementById('bt2');
    let join = document.getElementById('join');
    let modal2 = document.getElementById('m2');
    let create = document.getElementById('Create');
    let bt3 = document.getElementById('bt3');

    if(btn1 && modal){
        btn1.onclick = show_option;
    }else{
        console.log("Button with id 'btn1' not found.");
    }

    if(join){
        join.onclick = show_option2;
    }
    else{
        "Can't able to open 2nd modal";
    }

    if(create){
        create.onclick = show_option;
    }
    else{
        "Can't able to open 1st modal";
    }

    if(close1){
        close1.onclick = closeModal;
    }
    else{
        console.log("'cancel' id not found.");
    }

    if(close2){
        close2.onclick = closeModal2;
    }
    else{
        console.log("'cancel2' id not found.");
    }

    if(bt2){
        bt2.onclick = created;
    }
    else{
        console.log("Error in project Creation");
    }

    if(bt3){
        bt3.onclick = joinProject;
    }
    else{
        console.log("Error in project Joining");
    }

    function show_option(){
        modal2.style.display = "none";
        modal.style.display = "block";
    }

    function show_option2(){
        modal.style.display = "none";
        modal2.style.display = "block";
    }  
    
    function closeModal(){
        modal.style.display = "none";
    }

    function closeModal2(){
        modal2.style.display = "none";
    }

    function created(){
        alert("Project Created Successfully");
    }
    
    function joinProject(){
        alert("Joined Successfully");
    }
    
});