# 🗄️ Base de datos de Tienda de Ropa

***

## 📝 Descripción breve

Base de datos sencilla diseñada y adaptada para un sistema en línea para una tienda de ropa que sea capaz de administrar la información de manera efectiva.

***

## 📋 Partes y estructura de la base de datos

### 👥 Usuarios

```json
{
    "nombre": "Juan Pérez",
    "correo": "juan.perez@example.com",
    "contrasena": "contraseña123",
    "direccion": "Calle Falsa 123, Ciudad, País",
    "rol": "cliente"
}
```

### 🏷️ Marcas

```json
{
    "nombre": "Nike",
    "pais": "Estados Unidos"
}
```

### 👚 Prendas

```json
{
    "nombre": "Camiseta Nike",
    "marca": "Nike",
    "precio": "25.99",
    "talla": "M",
    "color": "Rojo"
}
```

### 💰 Ventas

```json
{
    "producto": "a",
    "fecha_venta": "new Date("2024-07-15")",
    "cantidad": "1",
    "total": "89.99",
    "medio_pago": "Tarjeta",
    "cliente": "a"
}
```

***

## 👤 Integrante:
- José Andrés Mata Brenes

***

# Sección del ***API***

***

## 📘 Endpoints


### Obtener todos los libros a la vez

- **Tipo de método:** `GET`
- **Enlace del endpoint:**

    ```http
    GET http://127.0.0.1:5000/proyecto-BD-tienda-ropa/api/v1/libros
    ```

- **Descripción breve:** Obtiene todos los libros que se contienen dentro de la librería a la vez.

- **Ejemplo de estructura básica del JSON:**
    ```json
    [
        {
            "id": 1,
            "titulo": "Libro Alfa",
            "autor": "Primer autor",
            "anio": 2023
        },
        {
            "id": 2,
            "titulo": "Libro Beta",
            "autor": "Segundo autor",
            "anio": 2025
        }
    ]
    ```

### Obtener un solo libro por su id

- **Tipo de método:** `GET`
- **Enlace del endpoint:**

    ```http
    GET http://127.0.0.1:5000/proyecto-BD-tienda-ropa/api/v1/libros?id=1
    ```

- **Descripción breve:** A comparación del endpoint anterior, este solo obtiene un único libro y para ello utiliza la id específica del libro.

- **Ejemplo de estructura básica del JSON:**
    ```json
    {
        "id": 1,
        "titulo": "Libro Alfa",
        "autor": "Primer autor",
        "anio": 2023
    }
    ```

### Insertar un nuevo libro

- **Tipo de método:** `POST`
- **Enlace del endpoint:**

    ```http
    POST http://127.0.0.1:5000/proyecto-BD-tienda-ropa/api/v1/libros
    ```

- **Descripción breve:** Ingresa un nuevo libro con sus datos a la librería.

- **Ejemplo de estructura básica del JSON:**
    ```json
    {
        "titulo": "Ejemplo de libro",
        "autor": "Autor Ficticio",
        "anio": 2024
    }
    ```

- **Estructura básica de respuesta:**
    ```json
    {
        "mensaje": "Libro agregado exitosamente a la base de datos"
    }
    ```

### Actualizar un libro por su id

- **Tipo de método:** `PUT`
- **Enlace del endpoint:**

    ```http
    PUT http://127.0.0.1:5000/proyecto-BD-tienda-ropa/api/v1/libros?id=1
    ```

- **Descripción breve:** Este endpoint toma los datos de un libro y cambia sus datos actualizando la información.

- **Ejemplo de estructura básica del JSON:**
    ```json
    {
        "id": 1,
        "titulo": "Título actualizado",
        "autor": "Autor Actualizado",
        "anio": 2025
    }
    ```

- **Estructura básica de respuesta:**
    ```json
    {
        "mensaje": "Libro actualizado exitosamente"
    }
    ```

### Eliminar un libro por su id

- **Tipo de método:** `DELETE`
- **Enlace del endpoint:**

    ```http
    DELETE http://127.0.0.1:5000/proyecto-BD-tienda-ropa/api/v1/libros?id=1
    ```

- **Descripción breve:** Elimina por completo un libro de la librería.

- **Estructura básica de respuesta:**
    ```json
    {
        "mensaje": "Libro eliminado exitosamente"
    }
    ```

***