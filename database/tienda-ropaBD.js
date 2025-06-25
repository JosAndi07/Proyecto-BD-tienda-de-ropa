//Base de datos para la tienda de ropa

//Iniciar conexion con la base de datos
use tienda-ropaBD;

//Colección: Usuarios

//Insertar
db.a.insertMany([
    {
        nombre: "Juan Pérez",
        correo: "juan.perez@example.com",
        contrasena: "contraseña123",
        direccion: "Calle Falsa 123, Ciudad, País",
        rol: "cliente"
    },
    {
        nombre: "María López",
        correo: "maria.lopez@example.com",
        contrasena: "contraseña456",
        direccion: "Avenida Siempre Viva 742, Ciudad, País",
        rol: "cliente"
    },
    {
        nombre: "Carlos García",
        email: "carlos.garcia@example.com",
        contraseña: "contraseña789",
        direccion: "Calle de la Amistad 456, Ciudad, País",
        rol: "cliente"
    },
    {
        nombre: "Laura Martínez",
        email: "laura.martinez@example.com",
        contraseña: "contraseña101",
        direccion: "Boulevard de la Esperanza 789, Ciudad, País",
        rol: "admin"
    }
]);

//Actualizar
db.a.updateOne(
    { nombre: "Juan Pérez" },
    { $set: { direccion: "Calle Nueva 456, Ciudad, País" } }
);

//Eliminar
db.a.deleteOne({ nombre: "Carlos García" });

//Colección: Marcas

//Insertar
db.a.insertMany([
    {
        nombre: "Nike",
        pais: "Estados Unidos"
    },
    {
        nombre: "Adidas",
        pais: "Alemania"
    },
    {
        nombre: "Zara",
        pais: "España"
    }
]);

//Actualizar
db.a.updateOne(
    { nombre: "Adidas" },
    { $set: { pais: "Francia" } }
);

//Eliminar
db.a.deleteOne({ nombre: "Nike" });

//Colección: Prendas

//Insertar
db.a.insertMany([
    {
        nombre: "Camiseta Nike",
        marca: "Nike",
        precio: 25.99,
        talla: "M",
        color: "Rojo"
    },
    {
        nombre: "Pantalones Adidas",
        marca: "Adidas",
        precio: 49.99,
        talla: "L",
        color: "Negro"
    },
    {
        nombre: "Vestido Zara",
        marca: "Zara",
        precio: 39.99,
        talla: "S",
        color: "Azul"
    },
    {
        nombre: "Chaqueta de Cuero",
        marca: "Zara",
        precio: 89.99,
        talla: "L",
        color: "Negro"
    },
    {
        nombre: "Sudadera con Capucha",
        marca: "Nike",
        precio: 45.50,
        talla: "XL",
        color: "Gris"
    },
    {
        nombre: "Falda Plisada",
        marca: "Adidas",
        precio: 35.75,
        talla: "S",
        color: "Azul marino"
    }
]);

//Actualizar
db.a.updateOne(
    { nombre: "Camiseta Nike" },
    { $set: { precio: 27.99 } }
);

//Eliminar
db.a.deleteOne({ nombre: "Vestido Zara" });

//Colección: Ventas

//Insertar
db.a.insertMany([
    {
    producto: { 
      nombre: "Chaqueta de Cuero",
      marca: "Zara",
      talla: "L" 
    },
    fecha_venta: new Date("2024-07-15"),
    cantidad: 1,
    total: 89.99,
    medio_pago: "Tarjeta",
    cliente: { 
      nombre: "Carlos García",
      correo: "carlos.garcia@example.com" 
    }
    },
    {
    producto: { 
      nombre: "Pantalones Adidas",
      marca: "Adidas",
      talla: "L" 
    },
    fecha_venta: new Date("2024-07-14"),
    cantidad: 2,
    total: 99.98, // 2 x 49.99
    medio_pago: "Efectivo",
    cliente: { 
      nombre: "María López",
      email: "maria.lopez@example.com" 
    }
    },
    {
    producto: { 
      nombre: "Sudadera con Capucha",
      marca: "Nike",
      talla: "XL" 
    },
    fecha_venta: new Date("2024-07-10"),
    cantidad: 1,
    total: 45.50,
    medio_pago: "Transferencia",
    cliente: { 
      nombre: "Laura Martínez",
      email: "laura.martinez@example.com" 
    },
    descuento_aplicado: 5.0
    }
]);

//Actualizar
db.a.updateOne(
    { "producto.nombre": "Chaqueta de Cuero" },
    { $set: { medio_pago: "PayPal" } }
);

//Eliminar
db.a.deleteOne({ "producto.nombre": "Sudadera con Capucha" });

//Consultas

//Cantidad vendida de prendas por fecha

const fechaEspecifica = new Date("2024-07-14");
db.ventas.aggregate([
    {
        $match: { fecha_venta: fechaEspecifica }
    },
    {
        $group: {
            _id: "$fecha_venta",
            total_vendido: { $sum: "$cantidad" }
        }
    }
]);

//Marcas con al menos una venta

db.ventas.aggregate([
    {
        $group: {
            _id: "$producto.marca"
        }
    }
]);

//Prendas vendidas y cantidad restante en inventario

db.ventas.aggregate([
    {
        $group: {
            _id: "$producto.nombre",
            total_vendido: { $sum: "$cantidad" }
        }
    },
    {
        $lookup: {
            from: "stock",
            localField: "_id",
            foreignField: "nombre",
            as: "stock_info"
        }
    },
    {
        $unwind: "$stock_info"
    },
    {
        $project: {
            nombre: "$_id",
            total_vendido: 1,
            cantidad_restante: { $subtract: ["$stock_info.cantidad", "$total_vendido"] }
        }
    }
]);

//5 marcas más vendidas y cantidad de ventas

db.ventas.aggregate([
    {
        $group: {
            _id: "$producto.marca",
            total_vendido: { $sum: "$cantidad" }
        }
    },
    {
        $sort: { total_vendido: -1 }
    },
    {
        $limit: 5
    }
]);