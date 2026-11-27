from pathlib import Path
from flask import Flask, render_template, request

app = Flask(__name__)
BASE_DIR = Path(__file__).resolve().parent

# Información confirmada del equipo y del producto.
# Los datos que todavía no se han proporcionado se dejan como "Pendiente".
equipo = {
    "escuela": "CECyTEJ 24 Ixtapa",
    "ubicacion": "Puerto Vallarta, Jalisco",
    "grupo": "3-E",
    "integrantes": [
        "MARIANA ALEJANDRA LORENZO PUERTO",
        "CITLALLI MAIRAM OCAMPO GOMEZ",
        "KIMBERLY NATASHA GONZALES AGUILAR",
    ],
    "marca": "SABICLEAN",
    "eslogan": "LIMPIEZA QUE INSPIRA, NATURALEZA QUE RESPIRA",
}

producto = {
    "nombre": "SABICLEAN",
    "descripcion": "Jabón biodegradable para pisos.",
    "investigacion": (
        "El jabón es uno de los productos de higiene que más consumimos a diario. "
        "Sin embargo, los jabones sintéticos convencionales vierten sulfatos, "
        "siliconas y conservantes a las tuberías que contaminan nuestros ríos y mares. "
        "Afortunadamente, utilizar un jabón biodegradable permite mantener una "
        "limpieza profunda y cuidar tu piel mientras proteges el medio ambiente."
    ),
    "ingredientes": [
        "300 g de pulpa de sábila cristalina (aproximadamente 2 pencas grandes, peladas y sin la parte verde).",
        "500 ml de agua caliente de garrafón.",
        "200 ml de agua fría de garrafón.",
        "50 g de bicarbonato de sodio (la receta indica 5 cucharadas).",
        "30 ml de vinagre blanco.",
        "30 ml de jugo de limón colado.",
        "La receta menciona 10 ml de alcohol de farmacia o Fabuloso de limón como opción para el olor; no combinar productos de limpieza ni agregar esta opción hasta que el docente revise la fórmula."
    ],
    "procedimiento": [
        "Licuar: la receta indica licuar la pulpa de sábila con los 500 ml de agua caliente hasta obtener una mezcla homogénea.",
        "Preparar la mezcla: pasar la preparación a un recipiente de capacidad suficiente. La receta indica agregar el bicarbonato y después el vinagre y el jugo de limón, mezclando con cuidado porque puede producir burbujeo.",
        "Agregar el agua fría. La opción de alcohol o limpiador comercial para perfumar queda pendiente de revisión del docente; no mezclar limpiadores entre sí.",
        "Envasar en recipientes limpios y adecuados. La receta propone dejar reposar para que baje la espuma antes de cerrar y etiquetar."
    ],
    "dosis": "La receta proporcionada indica 250 ml por cubeta de 5 L; verificar esta dosis con el docente antes de recomendar su uso.",
    "datos_declarados_pendientes_verificacion": [
        "pH 8.5",
        "Biodegradable 100% en 24 horas",
        "Costo de $15 pesos por litro",
        "Afirmación de que desinfecta naturalmente"
    ],
    "envase": {
        "medidas": "Aproximadamente 27 cm de alto",
        "volumen": "1 litro (1000 ml)",
        "masa": "20 a 25 gramos (dato proporcionado; confirmar si corresponde al envase vacío)",
        "tapa": "Tapa de plástico de rosca",
        "material": "Plástico PET",
    },
    "marca_comparacion": "Pendiente: SABICLEAN es la marca del equipo, no la marca comercial externa para comparar.",
    "comparacion": {
        "sabiclean_ventajas": ["El equipo señala que limpia rápido y quita las manchas."],
        "sabiclean_desventajas": [],
        "comercial_ventajas": [],
        "comercial_desventajas": ["Según la observación compartida por el equipo, hace poca espuma y su olor fuerte no permanece."],
        "observaciones": "Son observaciones proporcionadas por el equipo y no resultados de pruebas controladas. Falta identificar la marca comercial y comparar ambos productos en las mismas condiciones."
    },
}

def existe_archivo(ruta):
    """Comprueba si una fotografía o video fue agregado al proyecto."""
    return (BASE_DIR / "static" / ruta).is_file()


@app.route("/")
def inicio():
    return render_template("index.html", equipo=equipo, producto=producto,
                           logo=existe_archivo("img/logotipo.png"),
                           foto=existe_archivo("img/producto.jpg"))


@app.route("/investigacion")
def investigacion():
    return render_template("investigacion.html", equipo=equipo, producto=producto)


@app.route("/elaboracion")
def elaboracion():
    return render_template("elaboracion.html", equipo=equipo, producto=producto)


@app.route("/producto")
def ver_producto():
    archivos = {
        "logo": existe_archivo("img/logotipo.png"),
        "etiqueta": existe_archivo("img/etiqueta.png"),
        "envase": existe_archivo("img/envase.jpg"),
        "producto": existe_archivo("img/producto.jpg"),
    }
    return render_template("producto.html", equipo=equipo, producto=producto, archivos=archivos)


@app.route("/videos")
def videos():
    archivos = {
        "elaboracion": existe_archivo("videos/elaboracion.mp4"),
        "uso": existe_archivo("videos/uso_detergente.mp4"),
    }
    return render_template("videos.html", equipo=equipo, producto=producto, archivos=archivos)


@app.route("/comparativa")
def comparativa():
    return render_template("comparativa.html", equipo=equipo, producto=producto)


@app.route("/contacto", methods=["GET", "POST"])
def contacto():
    mensaje = None
    if request.method == "POST":
        nombre = request.form.get("nombre", "").strip()
        correo = request.form.get("correo", "").strip()
        asunto = request.form.get("asunto", "").strip()
        texto = request.form.get("mensaje", "").strip()

        if nombre and correo and asunto and texto:
            # Formulario escolar de demostración: no envía correos.
            mensaje = "¡Gracias! Tu mensaje se registró en esta demostración."
        else:
            mensaje = "Completa todos los campos para registrar el mensaje."

    return render_template("contacto.html", equipo=equipo, mensaje=mensaje)


if __name__ == "__main__":
    app.run(debug=True)
