
function mostrarFecha(){
    document.getElementById('parrafo3').innerHTML = Date();
}


function apagarLuz() {
    var colorOscuro = '#343a40';
    var letraClara = '#ffffff';
    document.body.style.background = colorOscuro;
    document.body.style.color = letraClara;
    


}


function encenderLuz() {
    var colorClaro = '#ffffff';
    var letraOscura =  '#343a40';
    document.body.style.background= colorClaro;
    document.body.style.color = letraOscura;
    document.body.style.background.color= colorClaro;
   
}




function sumar() {
    var valor1 = document.getElementById("num1").value;
    var valor2 = document.getElementById("num2").value;
    try
    {
        if (valor1 == "" || valor2 == "") throw "Debes ingresar todos los valores numéricos a operar...";

        if (isNaN(valor1) || isNaN(valor2)) throw "Debes ingresar solo números para operar...";

        valor1 = Number(valor1);
        valor2 = Number(valor2);
        document.getElementById("resultado").innerHTML = valor1 + " + " + valor2 + " = " + (valor1 + valor2);
    }
    catch(err) 
    {
        document.getElementById("error").innerHTML = err;
    }
    
}



function restar() {
    var valor1 = parseInt(document.getElementById("num1").value);
    var valor2 = parseInt(document.getElementById("num2").value);
    document.getElementById("resultado").innerHTML = valor1 + " - " + valor2 + " = " + (valor1 - valor2);
}



function multiplicar() {
    var valor1 = parseInt(document.getElementById("num1").value);
    var valor2 = parseInt(document.getElementById("num2").value);
    document.getElementById("resultado").innerHTML = valor1 + " x " + valor2 + " = " + (valor1 * valor2);
}



function dividir() {
    var valor1 = parseInt(document.getElementById("num1").value);
    var valor2 = parseInt(document.getElementById("num2").value);
    document.getElementById("resultado").innerHTML = valor1 + " / " + valor2 + " = " + (valor1 / valor2);
}



function saludar() {
    var fecha = new Date();
    document.getElementById("saludo").innerHTML = "  " + fecha;
    var tiempo = setTimeout(function() { saludar()},1000);
}


//Consumir API mindicador.cl
$(document).ready(function() {
    var xmlhttp = new XMLHttpRequest();
    xmlhttp.open ('GET','https://mindicador.cl/api',true);
    xmlhttp.send();

    var uf = 0;
    var dolar = 0;
    var euro = 0;

    xmlhttp.onreadystatechange = function() {
        if (this.readyState == 4 && this.status == 200)
        {
            var data = JSON.parse(this.responseText);
            uf = data.uf.valor;
            dolar = data.dolar.valor;
            euro = data.euro.valor;
        }
        document.getElementById("valorUF").innerHTML = data.uf.nombre + ": " + new Intl.NumberFormat('es-CL',{style:'currency',currency:'CLP',maximumFractionDigits:2}).format(uf);
        document.getElementById("valorDolar").innerHTML = data.dolar.nombre + ": " + new Intl.NumberFormat('es-CL',{style:'currency',currency:'CLP',maximumFractionDigits:2}).format(dolar);
        document.getElementById("valorEuro").innerHTML = data.euro.nombre + ": " + new Intl.NumberFormat('es-CL',{style:'currency',currency:'CLP',maximumFractionDigits:2}).format(euro);
    }
});

function actual() {
    fecha=new Date(); //Actualizar fecha.
    hora=fecha.getHours(); //hora actual
    minuto=fecha.getMinutes(); //minuto actual
    segundo=fecha.getSeconds(); //segundo actual
    if (hora<10) { //dos cifras para la hora
       hora="0"+hora;
       }
    if (minuto<10) { //dos cifras para el minuto
       minuto="0"+minuto;
       }
    if (segundo<10) { //dos cifras para el segundo
       segundo="0"+segundo;
       }
    //ver en el recuadro del reloj:
    mireloj = hora+" : "+minuto+" : "+segundo;
            return mireloj; 
    }


function actualizar() { //función del temporizador
mihora=actual(); //recoger hora actual
mireloj=document.getElementById("reloj"); //buscar elemento reloj
mireloj.innerHTML=mihora; //incluir hora en elemento
}
setInterval(actualizar,1000); //iniciar temporizador
