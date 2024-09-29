
-- Base de Datos
CREATE DATABASE IF NOT EXISTS gestion_de_transporte_y_reservas;
USE gestion_de_transporte_y_reservas;

-- Tabla: Vehículo
CREATE TABLE Vehiculo (
    idVehiculo INT AUTO_INCREMENT PRIMARY KEY,
    matricula VARCHAR(20) NOT NULL,
    marca VARCHAR(50) NOT NULL,
    modelo VARCHAR(50) NOT NULL,
    año INT NOT NULL,
    capacidad INT NOT NULL,
    estado VARCHAR(20) NOT NULL
);

-- Tabla: Conductor
CREATE TABLE Conductor (
    idConductor INT AUTO_INCREMENT PRIMARY KEY,
    nombre VARCHAR(50) NOT NULL,
    numeroLicencia VARCHAR(20) NOT NULL,
    contacto VARCHAR(50) NOT NULL
);

-- Tabla: Ruta
CREATE TABLE Ruta (
    idRuta INT AUTO_INCREMENT PRIMARY KEY,
    origen VARCHAR(100) NOT NULL,
    destino VARCHAR(100) NOT NULL,
    distancia DECIMAL(10,2) NOT NULL,
    duracionEstimado TIME NOT NULL
);

-- Tabla: ReservaPasaje
CREATE TABLE ReservaPasaje (
    idReserva INT AUTO_INCREMENT PRIMARY KEY,
    idCliente INT,
    idRuta INT,
    fechaViaje DATE NOT NULL,
    numeroAsiento INT NOT NULL,
    estado VARCHAR(20) NOT NULL,
    FOREIGN KEY (idCliente) REFERENCES Cliente(idCliente),
    FOREIGN KEY (idRuta) REFERENCES Ruta(idRuta)
);

-- Tabla: Cliente
CREATE TABLE Cliente (
    idCliente INT AUTO_INCREMENT PRIMARY KEY,
    nombre VARCHAR(50) NOT NULL,
    contacto VARCHAR(50) NOT NULL,
    direccion VARCHAR(100) NOT NULL
);

-- Tabla: Tarifa
CREATE TABLE Tarifa (
    idTarifa INT AUTO_INCREMENT PRIMARY KEY,
    idRuta INT,
    tipoPasajero VARCHAR(20) NOT NULL,
    precio DECIMAL(10,2) NOT NULL,
    FOREIGN KEY (idRuta) REFERENCES Ruta(idRuta)
);

-- Tabla: Pago
CREATE TABLE Pago (
    idPago INT AUTO_INCREMENT PRIMARY KEY,
    idReserva INT,
    monto DECIMAL(10,2) NOT NULL,
    fechaPago DATE NOT NULL,
    FOREIGN KEY (idReserva) REFERENCES ReservaPasaje(idReserva)
);

-- Tabla: Reclamo
CREATE TABLE Reclamo (
    idReclamo INT AUTO_INCREMENT PRIMARY KEY,
    idCliente INT,
    descripcion TEXT NOT NULL,
    estado VARCHAR(20) NOT NULL,
    FOREIGN KEY (idCliente) REFERENCES Cliente(idCliente)
);

-- Tabla: Mantenimiento
CREATE TABLE Mantenimiento (
    idMantenimiento INT AUTO_INCREMENT PRIMARY KEY,
    idVehiculo INT,
    fecha DATE NOT NULL,
    descripcion TEXT NOT NULL,
    costo DECIMAL(10,2) NOT NULL,
    FOREIGN KEY (idVehiculo) REFERENCES Vehiculo(idVehiculo)
);

-- Tabla: HistorialViaje
CREATE TABLE HistorialViaje (
    idHistorial INT AUTO_INCREMENT PRIMARY KEY,
    idVehiculo INT,
    idConductor INT,
    idRuta INT,
    fechaViaje DATE NOT NULL,
    FOREIGN KEY (idVehiculo) REFERENCES Vehiculo(idVehiculo),
    FOREIGN KEY (idConductor) REFERENCES Conductor(idConductor),
    FOREIGN KEY (idRuta) REFERENCES Ruta(idRuta)
);

-- Tabla: Combustible
CREATE TABLE Combustible (
    idCombustible INT AUTO_INCREMENT PRIMARY KEY,
    idVehiculo INT,
    fecha DATE NOT NULL,
    cantidad DECIMAL(10,2) NOT NULL,
    FOREIGN KEY (idVehiculo) REFERENCES Vehiculo(idVehiculo)
);

-- Tabla: Proveedor
CREATE TABLE Proveedor (
    idProveedor INT AUTO_INCREMENT PRIMARY KEY,
    nombre VARCHAR(50) NOT NULL,
    contacto VARCHAR(50) NOT NULL,
    servicio VARCHAR(100) NOT NULL
);

-- Tabla: SeguroVehiculo
CREATE TABLE SeguroVehiculo (
    idSeguro INT AUTO_INCREMENT PRIMARY KEY,
    idVehiculo INT,
    compania VARCHAR(50) NOT NULL,
    cobertura VARCHAR(100) NOT NULL,
    fechaInicio DATE NOT NULL,
    fechaFin DATE NOT NULL,
    FOREIGN KEY (idVehiculo) REFERENCES Vehiculo(idVehiculo)
);

-- Tabla: Incidente
CREATE TABLE Incidente (
    idIncidente INT AUTO_INCREMENT PRIMARY KEY,
    idVehiculo INT,
    idConductor INT,
    idRuta INT,
    descripcion TEXT NOT NULL,
    fecha DATE NOT NULL,
    FOREIGN KEY (idVehiculo) REFERENCES Vehiculo(idVehiculo),
    FOREIGN KEY (idConductor) REFERENCES Conductor(idConductor),
    FOREIGN KEY (idRuta) REFERENCES Ruta(idRuta)
);

-- Tabla: Contrato
CREATE TABLE Contrato (
    idContrato INT AUTO_INCREMENT PRIMARY KEY,
    idProveedor INT,
    idSeguro INT,
    idConductor INT,
    fechaInicio DATE NOT NULL,
    fechaFin DATE NOT NULL,
    FOREIGN KEY (idProveedor) REFERENCES Proveedor(idProveedor),
    FOREIGN KEY (idSeguro) REFERENCES SeguroVehiculo(idSeguro),
    FOREIGN KEY (idConductor) REFERENCES Conductor(idConductor)
);

-- Tabla: ConductorVehiculo
CREATE TABLE ConductorVehiculo (
    idConductorVehiculo INT AUTO_INCREMENT PRIMARY KEY,
    idConductor INT,
    idVehiculo INT,
    FOREIGN KEY (idConductor) REFERENCES Conductor(idConductor),
    FOREIGN KEY (idVehiculo) REFERENCES Vehiculo(idVehiculo)
);

-- Tabla: Pasaje
CREATE TABLE Pasaje (
    idPasaje INT AUTO_INCREMENT PRIMARY KEY,
    idCliente INT,
    idRuta INT,
    fechaViaje DATE NOT NULL,
    numeroAsiento INT NOT NULL,
    FOREIGN KEY (idCliente) REFERENCES Cliente(idCliente),
    FOREIGN KEY (idRuta) REFERENCES Ruta(idRuta)
    );


DELIMITER $$

CREATE PROCEDURE RegistrarConductor(
    IN p_nombre VARCHAR(50),
    IN p_apellido VARCHAR(50),
    IN p_dni VARCHAR(15),
    IN p_telefono VARCHAR(20)
)
BEGIN
    INSERT INTO Conductor (nombre, apellido, dni, telefono)
    VALUES (p_nombre, p_apellido, p_dni, p_telefono);
END$$

DELIMITER ;


DELIMITER $$

CREATE TRIGGER actualizar_estado_vehiculo_reserva
AFTER INSERT ON ReservaPasaje
FOR EACH ROW
BEGIN
    DECLARE asientos_ocupados INT;

    SELECT COUNT(*) INTO asientos_ocupados 
    FROM ReservaPasaje 
    WHERE idRuta = NEW.idRuta AND fechaViaje = NEW.fechaViaje;

    IF asientos_ocupados >= (SELECT capacidad FROM Vehiculo WHERE idVehiculo = (SELECT idVehiculo FROM Ruta WHERE idRuta = NEW.idRuta)) THEN
        UPDATE Vehiculo 
        SET estado = 'Ocupado'
        WHERE idVehiculo = (SELECT idVehiculo FROM Ruta WHERE idRuta = NEW.idRuta);
    END IF;
END$$

DELIMITER ;


CREATE VIEW VistaEstadoVehiculos AS
SELECT 
    v.matricula, 
    v.marca, 
    v.modelo, 
    v.año, 
    v.capacidad, 
    v.estado
FROM Vehiculo v;
select * from conductor;
-- vistas 
CREATE VIEW VistaHistorialViajes AS
SELECT 
    hv.idHistorial, 
    c.nombre AS Conductor, 
    v.matricula AS Vehiculo, 
    r.origen, 
    r.destino, 
    hv.fechaViaje
FROM HistorialViaje hv
JOIN Conductor c ON hv.idConductor = c.idConductor
JOIN Vehiculo v ON hv.idVehiculo = v.idVehiculo
JOIN Ruta r ON hv.idRuta = r.idRuta;


select * from cliente;
select * from conductor;
select * from ruta;
select * from reservapasaje;

-- Crear el usuario 'jhona' con la contraseña 'gatito'
CREATE USER 'jhona'@'localhost' IDENTIFIED BY 'gatito';

-- Otorgar todos los privilegios al usuario 'jhona' en todas las bases de datos y tablas
GRANT ALL PRIVILEGES ON *.* TO 'jhona'@'localhost' WITH GRANT OPTION;

-- Aplicar los cambios de privilegios
FLUSH PRIVILEGES;
