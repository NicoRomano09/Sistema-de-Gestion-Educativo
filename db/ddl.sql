CREATE DATABASE IF NOT EXISTS sistema_gestion_educativo;

USE sistema_gestion_educativo;

CREATE TABLE IF NOT EXISTS Establecimiento (
id_establecimiento INT AUTO_INCREMENT,
nombre_establecimiento VARCHAR(60) NOT NULL,
nivel_educativo VARCHAR(60) NOT NULL,
gestion VARCHAR(60) NOT NULL,
PRIMARY KEY (id_establecimiento)
);

CREATE TABLE IF NOT EXISTS Division(
id_division INT AUTO_INCREMENT,
nombre_division VARCHAR(60) NOT NULL,
id_establecimiento INT NOT NULL,
PRIMARY KEY (id_division),
FOREIGN KEY (id_establecimiento) REFERENCES Establecimiento(id_establecimiento) ON DELETE CASCADE
);

CREATE TABLE IF NOT EXISTS Curso(
id_curso INT AUTO_INCREMENT,
nombre_curso VARCHAR(60) NOT NULL,
id_establecimiento INT NOT NULL,
PRIMARY KEY (id_curso),
FOREIGN KEY (id_establecimiento) REFERENCES Establecimiento(id_establecimiento) ON DELETE CASCADE
);

CREATE TABLE IF NOT EXISTS Docente(
id_docente INT AUTO_INCREMENT,
nombre_docente VARCHAR(60) NOT NULL,
apellido_docente VARCHAR(60) NOT NULL,
email VARCHAR(60) NOT NULL UNIQUE,
contrasena_hash VARCHAR(60) NOT NULL,
PRIMARY KEY (id_docente)
);

CREATE TABLE IF NOT EXISTS Asignatura(
id_asignatura INT AUTO_INCREMENT,
nombre_asignatura VARCHAR(60) NOT NULL,
PRIMARY KEY (id_asignatura)
);

CREATE TABLE IF NOT EXISTS DocenteAsignatura(
id_docente INT,
id_asignatura INT,
PRIMARY KEY (id_docente, id_asignatura),
FOREIGN KEY (id_docente) REFERENCES Docente(id_docente) ON DELETE CASCADE,
FOREIGN KEY (id_asignatura) REFERENCES Asignatura(id_asignatura) ON DELETE CASCADE
);

CREATE TABLE IF NOT EXISTS DocenteCurso(
id_docente INT,
id_curso INT,
PRIMARY KEY (id_docente, id_curso),
FOREIGN KEY (id_docente) REFERENCES Docente(id_docente) ON DELETE CASCADE,
FOREIGN KEY (id_curso) REFERENCES Curso(id_curso) ON DELETE CASCADE
);

CREATE TABLE IF NOT EXISTS DocenteDivision(
id_docente INT,
id_division INT,
PRIMARY KEY (id_docente, id_division),
FOREIGN KEY (id_docente) REFERENCES Docente(id_docente) ON DELETE CASCADE,
FOREIGN KEY (id_division) REFERENCES Division(id_division) ON DELETE CASCADE
);

CREATE TABLE IF NOT EXISTS Estudiante(
id_estudiante INT AUTO_INCREMENT,
nombre_estudiante VARCHAR(60) NOT NULL,
apellido_estudiante VARCHAR(60) NOT NULL,
id_curso INT NOT NULL,
id_division INT NOT NULL,
estado_estudiante BOOLEAN NOT NULL,
PRIMARY KEY (id_estudiante),
FOREIGN KEY (id_curso) REFERENCES Curso(id_curso) ON DELETE CASCADE,
FOREIGN KEY (id_division) REFERENCES Division(id_division) ON DELETE CASCADE
);

CREATE TABLE IF NOT EXISTS Calificacion(
id_calificacion INT AUTO_INCREMENT,
id_estudiante INT NOT NULL,
id_asignatura INT NOT NULL,
nota INT NOT NULL,
fecha DATE NOT NULL,
descripcion VARCHAR(60),
PRIMARY KEY (id_calificacion),
FOREIGN KEY (id_estudiante) REFERENCES Estudiante(id_estudiante) ON DELETE CASCADE,
FOREIGN KEY (id_asignatura) REFERENCES Asignatura(id_asignatura) ON DELETE CASCADE
);
