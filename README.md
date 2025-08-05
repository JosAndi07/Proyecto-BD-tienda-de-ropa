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

# Sección del *API*

***

## 📘 *Endpoints*

Solo se muestra el *endpoint* de Usuarios por motivo de practicidad, sin embargo la misma lógica opera para los otros *endpoints* de marcas, prendas y ventas.


### Obtener todos los usuarios a la vez

- **Tipo de método:** `GET`
- **Enlace del endpoint:**

    ```http
    GET http://127.0.0.1:5000/proyecto-BD-tienda-ropa/api/v1/usuarios
    ```

- **Descripción breve:** Obtiene todos los usuarios que se contienen dentro de la tienda de ropa a la vez.

- **Ejemplo de estructura básica del JSON:**
    ```json
    [
        {
            "id": 1,
            "titulo": "Usuario Alfa",
            "autor": "Primer autor",
            "anio": 2023
        },
        {
            "id": 2,
            "titulo": "Usuario Beta",
            "autor": "Segundo autor",
            "anio": 2025
        }
    ]
    ```

### Obtener un solo usuario por su id

- **Tipo de método:** `GET`
- **Enlace del endpoint:**

    ```http
    GET http://127.0.0.1:5000/proyecto-BD-tienda-ropa/api/v1/usuarios?id=1
    ```

- **Descripción breve:** A comparación del endpoint anterior, este solo obtiene un único usuario y para ello utiliza la id específica del usuario.

- **Ejemplo de estructura básica del JSON:**
    ```json
    {
        "id": 1,
        "titulo": "Usuario Alfa",
        "autor": "Primer autor",
        "anio": 2023
    }
    ```

### Insertar un nuevo usuario

- **Tipo de método:** `POST`
- **Enlace del endpoint:**

    ```http
    POST http://127.0.0.1:5000/proyecto-BD-tienda-ropa/api/v1/usuarios
    ```

- **Descripción breve:** Ingresa un nuevo usuario con sus datos a la tienda de ropa.

- **Ejemplo de estructura básica del JSON:**
    ```json
    {
        "titulo": "Ejemplo de usuario",
        "autor": "Autor Ficticio",
        "anio": 2024
    }
    ```

- **Estructura básica de respuesta:**
    ```json
    {
        "mensaje": "Usuario creado exitosamente en la base de datos con la siguiente ID: " "id"
    }
    ```

### Actualizar un usuario por su id

- **Tipo de método:** `PUT`
- **Enlace del endpoint:**

    ```http
    PUT http://127.0.0.1:5000/proyecto-BD-tienda-ropa/api/v1/usuarios?id=1
    ```

- **Descripción breve:** Este endpoint toma los datos de un usuario y cambia sus datos actualizando la información.

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
        "mensaje": "Información del usuario actualizada"
    }
    ```

### Eliminar un usuario por su id

- **Tipo de método:** `DELETE`
- **Enlace del endpoint:**

    ```http
    DELETE http://127.0.0.1:5000/proyecto-BD-tienda-ropa/api/v1/usuarios?id=1
    ```

- **Descripción breve:** Elimina por completo un usuario de la tienda de ropa.

- **Estructura básica de respuesta:**
    ```json
    {
        "mensaje": "Usuario eliminado con éxito"
    }
    ```

***