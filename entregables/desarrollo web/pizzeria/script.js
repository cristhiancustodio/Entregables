
var resultado; 
function opcion1() {
    calculo1();
    document.getElementById("cantidad2").value.innerHTML=0;
}
function opcion2() {
    calculo2();
} 
function opcion3() {
    calculo3();
}
function calculo1(){
    
    let numero=document.getElementById("cantidad").value;
    const medi=12.90;
    resultado=medi*numero;
    document.getElementById("total").innerHTML=(resultado).toFixed(2);
    
}
function calculo2(){
    let numero=document.getElementById("cantidad").value;
    const fami=23.90;
    resultado=fami*numero;
    document.getElementById("total").innerHTML=(resultado).toFixed(2);
}
function calculo3(){
    let numero=document.getElementById("cantidad").value;
    const giga=29.90;
    resultado=giga*numero;
    document.getElementById("total").innerHTML=(resultado).toFixed(2);
}
function registro(){
    alert("Pedido registrado con exito");
}
function op1(){
    resultado=resultado+3.50;
    document.getElementById("total").innerHTML=(resultado).toFixed(2);
}
function op2(){
    resultado=resultado+6.00;
    document.getElementById("total").innerHTML=(resultado).toFixed(2);
}
function op3(){
    resultado=resultado+3.00;
    document.getElementById("total").innerHTML=(resultado).toFixed(2);
}
function op4(){
    resultado=resultado+4.00;
    document.getElementById("total").innerHTML=(resultado).toFixed(2);
}
/*function calculo() {
    let medi=document.getElementById("mediana").value;
    let fami=document.getElementById("familiar").value;
    let giga=document.getElementById("gigante").value;
    if(medi==12.90){
        calculo1();
    }  
    else if (fami==23.90){
        calculo2();
    }
    else if(giga==29.90){
        calculo3();
    }
}*/
