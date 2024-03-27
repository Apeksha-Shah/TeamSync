
document.addEventListener("DOMContentLoaded", function() {

    var btn1 = document.getElementById("btn1");
    let modal = document.getElementById("m1");  
    let span = document.getElementById("cancel");
    let bt2 = document.getElementById('bt2');
    let SuccessModal = document.getElementById('SuccessModal');

    if(btn1 && modal){
        btn1.onclick = show_option;
    }else{
        console.log("Button with id 'btn1' not found.");
    }

    if(span){
        span.onclick = closeModal;
    }
    else{
        console.log("'cancel' id not found.");
    }

    if(bt2){
        bt2.onclick = created;
    }
    else{
        console.log("Error in project Creation");
    }

    function show_option(){
        modal.style.display = "block";
    }
    
    function closeModal(){
        modal.style.display = "none";
    }

    function created(){
        alert("Project Created Successfully");
    }
    

    function joinProject(){
        // SuccessModal.style.display = "block";
        alert("Project Joined Successfully");
    }
});