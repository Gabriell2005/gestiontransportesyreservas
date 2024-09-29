-- Inserción de vehículos
INSERT INTO Vehiculo (matricula, marca, modelo, año, capacidad, estado)
VALUES 
('ABC123', 'Toyota', 'Corolla', 2020, 4, 'Disponible'),
('DEF456', 'Ford', 'Focus', 2018, 5, 'Disponible');

-- Inserción de conductores
INSERT INTO Conductor (nombre, numeroLicencia, contacto)
VALUES 
('Juan Perez', '123456789', 'juan.perez@gmail.com'),
('Carlos Lopez', '987654321', 'carlos.lopez@gmail.com');

-- Inserción de rutas
INSERT INTO Ruta (origen, destino, distancia, duracionEstimado)
VALUES 
('Ciudad A', 'Ciudad B', 150.5, '02:30:00'),
('Ciudad C', 'Ciudad D', 200.0, '03:45:00');

-- Inserción de clientes
INSERT INTO Cliente (nombre, contacto, direccion)
VALUES 
('Pedro Gonzales', 'pedro.g@gmail.com', 'Calle Falsa 123'),
('Ana Gomez', 'ana.gomez@gmail.com', 'Calle Real 456');

-- Inserción de reservas de pasajes
INSERT INTO ReservaPasaje (idCliente, idRuta, fechaViaje, numeroAsiento, estado)
VALUES 
(1, 1, '2024-10-01', 1, 'Confirmada'),
(2, 2, '2024-10-02', 2, 'Pendiente');

-- Actualización del estado de un vehículo
UPDATE Vehiculo
SET estado = 'En mantenimiento'
WHERE matricula = 'ABC123';

-- Actualización de un cliente
UPDATE Cliente
SET direccion = 'Calle Nueva 789'
WHERE nombre = 'Pedro Gonzales';

-- Eliminar una reserva de pasaje
DELETE FROM ReservaPasaje
WHERE idReserva = 2;

-- Eliminar un vehículo
DELETE FROM Vehiculo
WHERE idVehiculo = 1;

-- Obtener todos los vehículos disponibles
SELECT * FROM Vehiculo WHERE estado = 'Disponible';

-- Obtener todas las reservas de un cliente específico
SELECT * FROM ReservaPasaje 
WHERE idCliente = (SELECT idCliente FROM Cliente WHERE nombre = 'Pedro Gonzales');

-- Obtener los conductores y las rutas asignadas
SELECT c.nombre AS Conductor, r.origen, r.destino
FROM Conductor c
JOIN ReservaPasaje rp ON c.idConductor = rp.idReserva
JOIN Ruta r ON rp.idRuta = r.idRuta;

-- Obtener las reservas de pasaje confirmadas
SELECT * FROM ReservaPasaje WHERE estado = 'Confirmada';

-- Contar cuántos asientos están reservados en una ruta específica
SELECT COUNT(*) AS AsientosReservados 
FROM ReservaPasaje 
WHERE idRuta = 1 AND fechaViaje = '2024-10-01';
