$(document).ready(
    function () {
        $.validator.addMethod('contraseñaFuerte', function (value, element) {
            return this.optional(element)
                || /\d/.test(value)
                && /[a-z]/i.test(value);
        }, 'Debe ingresar al menos un numero o una letra.')

        $("#formulario").validate(
            {
                rules: {
                    username: {
                        required: true
                    },
                    first_name: {
                        required: true
                    },
                    last_name: {
                        required: true
                    },
                    email: {
                        required: true,
                        email: true
                    },
                    password1: {
                        required: true,
                        contraseñaFuerte: true
                    },
                    password2: {
                        required: true,
                        equalTo: "#passw"
                    },
                    password: {
                        required: true,
                    }
                },
                
                messages: {
                    username: {

                        required: "Debe ingresar su usuario"
                    },
                    first_name: {
                        required: "Debe ingresar su nombre",
                    },
                    last_name: {
                        required: "Debe ingresar su apellido",
                    },
                    email: {
                        required: "Debe ingresar su correo.",
                        email: "Ingrese un correo valido."
                    },
                    password1: {
                        required: "Debe ingresar su contraseña.",
                        minlength: "La contraseña debe tener mas de 8 caracteres",
                    },
                    password2: {
                        required: "Debe confirmar su contraseña.",
                        minlength: "La contraseña debe tener mas de 8 caracteres",
                        equalTo: "Las contraseñas deben coincidir"
                    },
                    password: {
                        required: "Debe ingresar su contraseña.",
                    }
                }
            }
        )
    })
