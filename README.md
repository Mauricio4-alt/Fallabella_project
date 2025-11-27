# Fallabella Inventories Prices
## Descripción

*Este proyecto tiene como objetivo simular un gestor básico de inventarios para tiendas Falabella (no real).
El sistema está dividido en tres microservicios: usuarios, ventas y productos. El proyecto cubre los conceptos esenciales de un CRUD (creación, lectura, actualización y eliminación de información).*
Los microservicios incluidos son:

Usuarios/Vendedores: gestión de dependientes de tienda.

Productos y Stock: permite administrar artículos disponibles e inventario.

Facturación: almacena la información relacionada con ventas y comprobantes.

## Alcance

Este proyecto se desarrolla desde un enfoque introductorio, por lo que su funcionalidad se limita a la transmisión y gestión básica de datos.
Por esta razón no incluye:

Autenticación avanzada (tokens, encriptación, OAuth, etc.).

Módulos de análisis o exportación de hojas de cálculo (e.g., Excel).

Manejo de información mediante códigos de barras.

Sin embargo, sí incluye:

Conexión a base de datos.

Arquitectura basada en microservicios utilizando Docker.

Consumo de APIs.

Gestión básica de productos y proveedores.

## Instalación

1. Instale Docker.

2. Ejecute:

     docker-compose up