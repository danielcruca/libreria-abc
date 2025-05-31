// 📚 CRUD para Librería usando MongoDB

// Conexión a la base de datos
use libreriaDB;

// ---------------------------------------------
// Colección: usuarios
// ---------------------------------------------

// Crear usuarios
db.usuarios.insertMany([
  {
    username: "carlos23",
    email: "carlos@example.com",
    password: "segura123",
    rol: "cliente",
    fecha_creacion: new Date("2025-05-25")
  },
  {
    username: "admin2",
    email: "admin2@example.com",
    password: "adminsecure",
    rol: "admin",
    fecha_creacion: new Date("2025-05-25")
  }
]);

// Actualizar usuario
db.usuarios.updateOne(
  { username: "carlos23" },
  { $set: { email: "nuevo_correo@example.com" } }
);

// Eliminar usuario
db.usuarios.deleteOne({ username: "admin2" });

// ---------------------------------------------
// Colección: libros
// ---------------------------------------------

// Insertar un libro
db.libros.insertOne({
  titulo: "El túnel",
  autor: {
    nombre: "Ernesto",
    apellido: "Sábato",
    nacionalidad: "Argentina"
  },
  precio: 14.5,
  cantidad_stock: 25
});

// Insertar varios libros
db.libros.insertMany([
  {
    titulo: "Ficciones",
    autor: {
      nombre: "Jorge Luis",
      apellido: "Borges",
      nacionalidad: "Argentina"
    },
    precio: 13.5,
    cantidad_stock: 18
  },
  {
    titulo: "Aura",
    autor: {
      nombre: "Carlos",
      apellido: "Fuentes",
      nacionalidad: "México"
    },
    precio: 12.0,
    cantidad_stock: 22
  }
]);

// Actualizar precio de un libro
db.libros.updateOne(
  { titulo: "El túnel" },
  { $set: { precio: 15.0 } }
);

// Eliminar un libro
db.libros.deleteOne({ titulo: "Aura" });

// ---------------------------------------------
// Colección: ventas
// ---------------------------------------------

// Insertar una venta
db.ventas.insertOne({
  libro: { titulo: "Ficciones" },
  fecha_venta: new Date("2025-05-30"),
  cantidad: 2,
  total: 27.0,
  usuario: { username: "carlos23" }
});

// Insertar varias ventas
db.ventas.insertMany([
  {
    libro: { titulo: "El túnel" },
    fecha_venta: new Date("2025-05-31"),
    cantidad: 1,
    total: 15.0,
    usuario: { username: "carlos23" }
  },
  {
    libro: { titulo: "Rayuela" },
    fecha_venta: new Date("2025-05-28"),
    cantidad: 2,
    total: 36.0,
    usuario: { username: "juanperez" }
  }
]);

// Actualizar total de una venta
db.ventas.updateOne(
  { "libro.titulo": "Ficciones", cantidad: 2 },
  { $set: { total: 30.0 } }
);

// Eliminar una venta
db.ventas.deleteOne({ "libro.titulo": "Rayuela", cantidad: 2 });

/// Consultas para reportes:

/// la cantidad vendida de libros por fecha específica
db.ventas.aggregate([
  {
    $match: {
      fecha_venta: {
        $eq: new Date("2025-05-10") // Cambiar fecha según necesidad
      }
    }
  },
  {
    $group: {
      _id: "$fecha_venta",
      total_libros_vendidos: { $sum: "$cantidad" }
    }
  }
]);

// la lista de todos los autores que tienen al menos una venta

db.ventas.aggregate([
  {
    $lookup: {
      from: "libros",
      localField: "libro.titulo",
      foreignField: "titulo",
      as: "info_libro"
    }
  },
  { $unwind: "$info_libro" },
  {
    $group: {
      _id: {
        nombre: "$info_libro.autor.nombre",
        apellido: "$info_libro.autor.apellido"
      }
    }
  }
]);

