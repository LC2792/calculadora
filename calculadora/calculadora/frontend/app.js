function enviar() {
    var contenido = document.querySelector('#contenido');
    var v1 = document.querySelector('#t1').value;
    var v2 = document.querySelector('#t2').value;
    var url = "";

    if (document.querySelector('#opcion1').checked)
        url = 'http://127.0.0.1:5000/' + v1 + '/' + v2;
    else if (document.querySelector('#opcion2').checked)
        url = 'http://127.0.0.1:5000/resta/' + v1 + '/' + v2;
    else if (document.querySelector('#opcion3').checked)
        url = 'http://127.0.0.1:5000/multiplicacion/' + v1 + '/' + v2;
    else if (document.querySelector('#opcion4').checked)
        url = 'http://127.0.0.1:5000/division/' + v1 + '/' + v2;
    else if (document.querySelector('#opcion5').checked)
        url = 'http://127.0.0.1:5000/potenciacion/' + v1 + '/' + v2;
    else if (document.querySelector('#opcion6').checked)
        url = 'http://127.0.0.1:5000/seno/' + v1;
    else if (document.querySelector('#opcion7').checked)
        url = 'http://127.0.0.1:5000/coseno/' + v1;
    else {
        swal("Mensaje", "Seleccione una opción", "warning");
        return; // Para evitar ejecutar el fetch si no se selecciona una opción
    }

    // Realizamos la llamada fetch
    fetch(url)
        .then(function (response) {
            if (response.ok) {
                return response.json(); // Asumiendo que la respuesta es un JSON
            } else {
                throw "Error en la llamada";
            }
        })
        .then(function (data) {
            console.log(data); // Mostrar la respuesta en la consola
            // Asegurándonos de que la respuesta tiene las propiedades 'Resultado' y 'Operacion'
            if (data.Resultado && data.Operacion) {
                var cadena = `<h3>Resultado: ${data.Resultado} Operación: ${data.Operacion}</h3>`;
                contenido.innerHTML = cadena;
            } else {
                contenido.innerHTML = "<h3>Error: No se pudo obtener el resultado.</h3>";
            }
        })
        .catch(function (error) {
            console.log(error);
            swal(error);
            swal({
                title: "Advertencia",
                text: error,
                icon: "warning",
                buttons: true,
                dangerMode: true,
            });
        });
}
