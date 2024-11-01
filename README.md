# examen3
<!DOCTYPE html>
<html lang="es">
<head>
    <meta charset="UTF-8">
    <meta name="viewport" content="width=device-width, initial-scale=1.0">
    <title>Servicio de Domicilios</title>
    <link rel="stylesheet" href="styles.css">
</head>
<body>
    <header>
        <h1>Tu Servicio de Domicilios</h1>
        <nav>
            <ul>
                <li><a href="#menu">Menú</a></li>
                <li><a href="#contact">Contáctanos</a></li>
                <li><a href="#about">Sobre Nosotros</a></li>
            </ul>
        </nav>
    </header>
    <main>
        <section id="menu">
            <h2>Menú</h2>
            <ul>
                <li>
                    <span>Pizza - $10</span>
                    <button onclick="orderItem('Pizza')">Ordenar</button>
                </li>
                <li>
                    <span>Burguer - $8</span>
                    <button onclick="orderItem('Burguer')">Ordenar</button>
                </li>
                <li>
                    <span>Sushi - $12</span>
                    <button onclick="orderItem('Sushi')">Ordenar</button>
                </li>
            </ul>
        </section>
        <section id="order-summary">
            <h2>Resumen de Pedido</h2>
            <ul id="summary-list"></ul>
        </section>
        <section id="contact">
            <h2>Contáctanos</h2>
            <p>Teléfono: 123-456-7890</p>
            <p>Email: contacto@domicilios.com</p>
        </section>
        <section id="about">
            <h2>Sobre Nosotros</h2>
            <p>Somos un servicio de domicilios que se dedica a llevar tus platos favoritos a la puerta de tu casa.</p>
        </section>
    </main>
    <footer>
        <p>&copy; 2024 Tu Servicio de Domicilios. Todos los derechos reservados.</p>
    </footer>
    <script src="script.js"></script>
</body>
</html>
