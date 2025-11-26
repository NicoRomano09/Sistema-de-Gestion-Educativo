INSERT INTO Establecimiento(nombre_establecimiento, nivel_educativo, gestion)
VALUES ("Escuela Dr. Carlos Saavedra Lamas", "Primario", "Público");

INSERT INTO Curso(nombre_curso, id_establecimiento)
VALUES 
("1°", 1),
("2°", 1),
("3°", 1),
("4°", 1),
("5°", 1),
("6°", 1);

INSERT INTO Division(nombre_division, id_establecimiento)
VALUES
("A", 1),
("B", 1);

INSERT INTO Asignatura(nombre_asignatura)
VALUES 
("Matemática"),
("Lengua"),
("Ciencias Sociales"),
("Ciencias Naturales"),
("Música"),
("Educación Física"),
("Inglés");

INSERT INTO Estudiante(nombre_estudiante, apellido_estudiante, id_curso, id_division, estado_estudiante)
VALUES
("Valentino", "Ruiz", 1, 1, True),
("Julieta", "Ferreyra", 1, 1, True),
("Benjamín", "Cabrera", 1, 1, True),
("Martina", "Godoy", 1, 1, True),
("Thiago", "Álvarez", 1, 1, True),
("Lucía", "Benitez", 1, 1, True),
("Franco", "Villarreal", 1, 1, True),
("Zoe", "Paredes", 1, 1, True),
("Agustín", "Moyano", 1, 1, True),
("Mía", "Herrera", 1, 1, True);

INSERT INTO Estudiante(nombre_estudiante, apellido_estudiante, id_curso, id_division, estado_estudiante)
VALUES
("Santiago", "Córdoba", 1, 2, True),
("Camila", "Medina", 1, 2, True),
("Lautaro", "Giménez", 1, 2, True),
("Isabella", "Ríos", 1, 2, True),
("Tomás", "Pereyra", 1, 2, True),
("Emma", "Chávez", 1, 2, True),
("Bautista", "Toledo", 1, 2, True),
("Valentina", "Arce", 1, 2, True),
("Dylan", "López", 1, 2, True),
("Catalina", "Suárez", 1, 2, True);

INSERT INTO Estudiante(nombre_estudiante, apellido_estudiante, id_curso, id_division, estado_estudiante)
VALUES
("Valentina", "Romero", 2, 1, True),
("Tomás", "Cabrera", 2, 1, True),
("Agustina", "Molina", 2, 1, True),
("Lautaro", "Godoy", 2, 1, True),
("Mía", "Benítez", 2, 1, True),
("Santiago", "Peralta", 2, 1, True),
("Sofía", "Álvarez", 2, 1, True),
("Bruno", "Herrera", 2, 1, True);

INSERT INTO Estudiante(nombre_estudiante, apellido_estudiante, id_curso, id_division, estado_estudiante)
VALUES
("Martina", "Quiroga", 2, 2, True),
("Julián", "Medina", 2, 2, True),
("Emma", "Roldán", 2, 2, True),
("Federico", "Acosta", 2, 2, True),
("Camila", "Sosa", 2, 2, True),
("Joaquín", "Farías", 2, 2, True),
("Isabella", "Torres", 2, 2, True);

INSERT INTO Estudiante(nombre_estudiante, apellido_estudiante, id_curso, id_division, estado_estudiante)
VALUES
("Benjamín", "Ledesma", 3, 1, True),
("Clara", "Ramírez", 3, 1, True),
("Luciano", "Ferreyra", 3, 1, True),
("Abril", "Duarte", 3, 1, True),
("Felipe", "Ríos", 3, 1, True),
("Melina", "Torres", 3, 1, True),
("Ian", "Castro", 3, 1, True),
("Valeria", "Bustos", 3, 1, True),
("Nicolás", "Herrera", 3, 1, True),
("Renata", "Soria", 3, 1, True),
("Mateo", "Giménez", 3, 1, True);

INSERT INTO Estudiante(nombre_estudiante, apellido_estudiante, id_curso, id_division, estado_estudiante)
VALUES
("Luna", "Cabrera", 3, 2, True),
("Gonzalo", "Medina", 3, 2, True),
("Bárbara", "Toledo", 3, 2, True),
("Franco", "Loyola", 3, 2, True),
("Ariana", "Peralta", 3, 2, True),
("Lucas", "Benavídez", 3, 2, True),
("Selene", "Rivas", 3, 2, True),
("Tadeo", "Molina", 3, 2, True),
("Pilar", "Acuña", 3, 2, True);

INSERT INTO Estudiante(nombre_estudiante, apellido_estudiante, id_curso, id_division, estado_estudiante)
VALUES 
("Lautaro", "Gómez", 4, 1, True),
("Camila", "Sosa", 4, 1, True),
("Tomás", "Ferreyra", 4, 1, True),
("Abril", "Herrera", 4, 1, True),
("Bautista", "Molina", 4, 1, True),
("Valentina", "Carrizo", 4, 1, True),
("Mateo", "Córdoba", 4, 1, True),
("Lucía", "Pereyra", 4, 1, True);

INSERT INTO Estudiante(nombre_estudiante, apellido_estudiante, id_curso, id_division, estado_estudiante)
VALUES
("Juan Cruz", "Medina", 4, 2, True),
("Delfina", "Romero", 4, 2, True),
("Santiago", "Aguirre", 4, 2, True),
("Mía", "Torres", 4, 2, True),
("Thiago", "Salvatierra", 4, 2, True),
("Emma", "López", 4, 2, True),
("Franco", "Villalba", 4, 2, True),
("Julia", "Márquez", 4, 2, True),
("Benjamín", "Roldán", 4, 2, True);

INSERT INTO Estudiante(nombre_estudiante, apellido_estudiante, id_curso, id_division, estado_estudiante)
VALUES
("Lucía", "Fernández", 5, 1, True),
("Tomás", "Herrera", 5, 1, True),
("Julieta", "Soria", 5, 1, True),
("Bruno", "Gómez", 5, 1, True),
("Valentina", "Roldán", 5, 1, True),
("Mateo", "Oliva", 5, 1, True);

INSERT INTO Estudiante(nombre_estudiante, apellido_estudiante, id_curso, id_division, estado_estudiante)
VALUES
("Santiago", "Paredes", 5, 2, True),
("Camila", "Duarte", 5, 2, True),
("Agustín", "Molina", 5, 2, True),
("Micaela", "Ortiz", 5, 2, True),
("Franco", "Medina", 5, 2, True),
("Bárbara", "Escobar", 5, 2, True),
("Lautaro", "Quiroga", 5, 2, True);

INSERT INTO Estudiante(nombre_estudiante, apellido_estudiante, id_curso, id_division, estado_estudiante)
VALUES
("Mateo", "López", 6, 1, True),
("Valentina", "Pérez", 6, 1, True),
("Thiago", "Romero", 6, 1, True),
("Sofía", "González", 6, 1, True),
("Julián", "Cabrera", 6, 1, True),
("Morena", "Díaz", 6, 1, True),
("Benjamín", "Herrera", 6, 1, True),
("Alma", "Rodríguez", 6, 1, True),
("Joaquín", "Sosa", 6, 1, True),
("Isabella", "Medina", 6, 1, True);

INSERT INTO Estudiante(nombre_estudiante, apellido_estudiante, id_curso, id_division, estado_estudiante)
VALUES
("Santiago", "Torres", 6, 2, True),
("Lucía", "Cáceres", 6, 2, True),
("Lautaro", "Márquez", 6, 2, True),
("Martina", "Rivas", 6, 2, True),
("Tomás", "Ferreyra", 6, 2, True),
("Emilia", "Bustos", 6, 2, True),
("Agustín", "Duarte", 6, 2, True),
("Milagros", "Varela", 6, 2, True),
("Facundo", "Arias", 6, 2, True),
("Chiara", "Guzmán", 6, 2, True),
("Franco", "Molina", 6, 2, True);
