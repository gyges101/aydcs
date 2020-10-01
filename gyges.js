function gyges() {
				$("#btnEnviar").removeAttr("disabled");
				$("#btnSiguiente").removeAttr("disabled");
				$( "#datepicker" ).datepicker( "option", "disabled", false );
	                        document.getElementById("btnEnviar").click();
			}
