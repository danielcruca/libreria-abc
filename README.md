# Sistema online para Libreia ABC

Este proyecto consiste en la creación de una **API con MongoDB** para una **librería**, junto con un **frontend** que permite la gestión de usuarios, libros y ventas. El sistema completo ofrece operaciones básicas como inserción, actualización, eliminación y consultas avanzadas a través de una interfaz web.

## 📚 Colecciones y Ejemplos

### 👤 Usuarios
```json
{
  "username": "juanperez",
  "email": "juan@example.com",
  "password": "supersegura123",
  "rol": "cliente",
  "fecha_creacion": "2025-05-14T00:13:32.275Z"
}
```

### 📘 Libros
```json
{
  "titulo": "Rayuela",
  "autor": {
    "nombre": "Julio",
    "apellido": "Cortázar",
    "nacionalidad": "Argentina"
  },
  "precio": 18,
  "cantidad_stock": 12
}
```

### 🧾 Ventas
```json
{
  "libro": {
    "titulo": "El Aleph"
  },
  "fecha_venta": "2025-05-11T00:00:00.000Z",
  "cantidad": 3,
  "total": 37.5,
  "usuario": {
    "username": "librera99"
  }
}
```

---


## 👥 Integrantes del Proyecto

- Juan Rafael Mora Porras
- Pancha Carrasco


## 🔗 Endpoints de la API – Libros

### 1. Obtener todos los libros

* **Método:** `GET`
* **Endpoint:** `http://127.0.0.1:5000/libreria/api/v1/libros`
* **Descripción:** Obtiene una lista de todos los libros disponibles en el sistema.

```http
GET http://127.0.0.1:5000/libreria/api/v1/libros
```

**Ejemplo de respuesta:**

```json
[
  {
    "id": "1",
    "titulo": "Rayuela",
    "autor": {
      "nombre": "Julio",
      "apellido": "Cortázar",
      "nacionalidad": "Argentina"
    },
    "precio": 18,
    "cantidad_stock": 12
  },
  {
    "id": "2",
    "titulo": "El Aleph",
    "autor": {
      "nombre": "Jorge Luis",
      "apellido": "Borges",
      "nacionalidad": "Argentina"
    },
    "precio": 12.5,
    "cantidad_stock": 7
  }
]
```

---

### 2. Obtener un libro por ID

* **Método:** `GET`
* **Endpoint:** `http://127.0.0.1:5000/libreria/api/v1/libros/{id}`
* **Descripción:** Obtiene la información de un libro específico usando su ID.

```http
GET http://127.0.0.1:5000/libreria/api/v1/libros/1
```

**Ejemplo de respuesta:**

```json
{
  "id": "1",
  "titulo": "Rayuela",
  "autor": {
    "nombre": "Julio",
    "apellido": "Cortázar",
    "nacionalidad": "Argentina"
  },
  "precio": 18,
  "cantidad_stock": 12
}
```

---

### 3. Insertar un nuevo libro

* **Método:** `POST`
* **Endpoint:** `http://127.0.0.1:5000/libreria/api/v1/libros`
* **Descripción:** Inserta un nuevo libro en la base de datos.

```http
POST http://127.0.0.1:5000/libreria/api/v1/libros
```

**Cuerpo de la petición (JSON):**

```json
{
  "titulo": "Nuevo Libro",
  "autor": {
    "nombre": "Ana",
    "apellido": "Marquez",
    "nacionalidad": "Colombia"
  },
  "precio": 22,
  "cantidad_stock": 5
}
```

**Ejemplo de respuesta:**

```json
{
  "mensaje": "Libro insertado exitosamente"
}
```

---

### 4. Actualizar un libro por ID

* **Método:** `PUT`
* **Endpoint:** `http://127.0.0.1:5000/libreria/api/v1/libros/{id}`
* **Descripción:** Actualiza la información de un libro específico.

```http
PUT http://127.0.0.1:5000/libreria/api/v1/libros/1
```

**Cuerpo de la petición (JSON):**

```json
{
  "titulo": "Rayuela (Edición Actualizada)",
  "autor": {
    "nombre": "Julio",
    "apellido": "Cortázar",
    "nacionalidad": "Argentina"
  },
  "precio": 20,
  "cantidad_stock": 10
}
```

**Ejemplo de respuesta:**

```json
{
  "mensaje": "Libro actualizado exitosamente"
}
```

---

### 5. Eliminar un libro por ID

* **Método:** `DELETE`
* **Endpoint:** `http://127.0.0.1:5000/libreria/api/v1/libros/{id}`
* **Descripción:** Elimina un libro específico de la base de datos.

```http
DELETE http://127.0.0.1:5000/libreria/api/v1/libros/1
```

**Ejemplo de respuesta:**

```json
{
  "mensaje": "Libro eliminado exitosamente"
}
```

 