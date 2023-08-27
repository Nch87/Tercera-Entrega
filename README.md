# Tercera-Entrega
Tercera Pre-Entrega Natalia Chazarreta
# Aplicación de Gestión de Clientes, Productos, Proveedores y Vendedores

Esta es una aplicación de gestión básica para administrar clientes, productos, proveedores y vendedores. La aplicación está desarrollada utilizando el framework Django.

## Modelos

La aplicación tiene los siguientes modelos:

### Cliente

- `nombre`: campo de texto para almacenar el nombre del cliente.
- `apellido`: campo de texto para almacenar el apellido del cliente.
- `dni`: campo de texto para almacenar el número de identificación del cliente.
- `telefono`: campo de texto para almacenar el número de teléfono del cliente.
- `email`: campo de correo electrónico para almacenar la dirección de correo electrónico del cliente.
- `direccion`: campo de texto para almacenar la dirección del cliente.

### Proveedor

- `nombre`: campo de texto para almacenar el nombre del proveedor.
- `direccion`: campo de texto para almacenar la dirección del proveedor.
- `telefono`: campo de texto para almacenar el número de teléfono del proveedor.

### Producto

- `nombre`: campo de texto para almacenar el nombre del producto.
- `descripcion`: campo de texto para almacenar la descripción del producto.
- `precio`: campo decimal para almacenar el precio del producto.

### Vendedor

- `nombre`: campo de texto para almacenar el nombre del vendedor.
- `direccion`: campo de texto para almacenar la dirección del vendedor.
- `telefono`: campo de texto para almacenar el número de teléfono del vendedor.
- `legajo`: campo de texto para almacenar el número de legajo del vendedor.

## Formularios

La aplicación utiliza formularios para capturar los datos ingresados por el usuario. Los formularios correspondientes a cada modelo son:

### ClienteForm

- `nombre`: campo de texto para ingresar el nombre del cliente.
- `apellido`: campo de texto para ingresar el apellido del cliente.
- `dni`: campo de texto para ingresar el número de identificación del cliente.
- `telefono`: campo de texto para ingresar el número de teléfono del cliente.
- `email`: campo de correo electrónico para ingresar la dirección de correo electrónico del cliente.
- `direccion`: campo de texto para ingresar la dirección del cliente.

### ProveedorForm

- `nombre`: campo de texto para ingresar el nombre del proveedor.
- `direccion`: campo de texto para ingresar la dirección del proveedor.
- `telefono`: campo de texto para ingresar el número de teléfono del proveedor.

### ProductoForm

- `nombre`: campo de texto para ingresar el nombre del producto.
- `descripcion`: campo de texto (área de texto) para ingresar la descripción del producto.
- `precio`: campo decimal para ingresar el precio del producto.

### VendedorForm

- `nombre`: campo de texto para ingresar el nombre del vendedor.
- `direccion`: campo de texto para ingresar la dirección del vendedor.
- `telefono`: campo de texto para ingresar el número de teléfono del vendedor.
- `legajo`: campo de texto para ingresar el número de legajo del vendedor.

## Vistas

La aplicación tiene las siguientes vistas:

### inicio

Esta vista muestra una página inicial básica.

### cliente

Esta vista permite crear un nuevo cliente. Si se envía un formulario válido a través del método POST, se crea un nuevo objeto Cliente con los datos ingresados y se guarda en la base de datos. Si el formulario no es válido, se muestra un mensaje de error. Siempre se muestra un formulario vacío al cargar la página.

### producto

Esta vista permite crear un nuevo producto. Al igual que en la vista "cliente", si se envía un formulario válido a través del método POST, se crea un nuevo objeto Producto con los datos ingresados y se guarda en la base de datos. Si el formulario no es válido, se muestra un mensaje de error. Siempre se muestra un formulario vacío al cargar la página.

### proveedor

Esta vista permite crear un nuevo proveedor. Al igual que en las vistas anteriores, si se envía un formulario válido a través del método POST, se crea un nuevo objeto Proveedor con los datos ingresados y se guarda en la base de datos. Si el formulario no es válido, se muestra un mensaje de error. Siempre se muestra un formulario vacío al cargar la página.

### vendedor

Esta vista permite crear un nuevo vendedor. Al igual que en las vistas anteriores, si se envía un formulario válido a través del método POST, se crea un nuevo objeto Vendedor con los datos ingresados y se guarda en la base de datos. Si el formulario no es válido, se muestra un mensaje de error. Siempre se muestra un formulario vacío al cargar la página.

### busquedaClientes

Esta vista muestra una página donde se puede realizar una búsqueda de clientes por su número de identificación (DNI). Se muestra un formulario con un campo para ingresar el DNI.

### buscar

Esta vista procesa la búsqueda realizada en la vista "busquedaClientes". Si se ingresa un DNI válido, se realiza una consulta a la base de datos y se muestran los resultados en una página separada. Si no se ingresa ningún DNI, se muestra un mensaje de error.
