-- phpMyAdmin SQL Dump
-- version 5.2.1
-- https://www.phpmyadmin.net/
--
-- Servidor: 127.0.0.1
-- Tiempo de generación: 07-07-2024 a las 15:16:54
-- Versión del servidor: 10.4.28-MariaDB
-- Versión de PHP: 8.2.4

SET SQL_MODE = "NO_AUTO_VALUE_ON_ZERO";
START TRANSACTION;
SET time_zone = "+00:00";


/*!40101 SET @OLD_CHARACTER_SET_CLIENT=@@CHARACTER_SET_CLIENT */;
/*!40101 SET @OLD_CHARACTER_SET_RESULTS=@@CHARACTER_SET_RESULTS */;
/*!40101 SET @OLD_COLLATION_CONNECTION=@@COLLATION_CONNECTION */;
/*!40101 SET NAMES utf8mb4 */;

--
-- Base de datos: `cocteleria`
--

-- --------------------------------------------------------

--
-- Estructura de tabla para la tabla `cocteles`
--

CREATE TABLE `cocteles` (
  `ID` int(11) NOT NULL,
  `idUsuario` int(11) NOT NULL,
  `Nombre` varchar(30) NOT NULL,
  `Preparacion` varchar(1000) NOT NULL,
  `deAutor` int(11) NOT NULL,
  `FechaCreacion` datetime NOT NULL DEFAULT current_timestamp(),
  `imagen` varchar(255) NOT NULL,
  `tipo` int(11) DEFAULT NULL,
  `ingrediente` int(11) DEFAULT NULL
) ENGINE=InnoDB DEFAULT CHARSET=utf8mb4 COLLATE=utf8mb4_general_ci;

--
-- Volcado de datos para la tabla `cocteles`
--

INSERT INTO `cocteles` (`ID`, `idUsuario`, `Nombre`, `Preparacion`, `deAutor`, `FechaCreacion`, `imagen`, `tipo`, `ingrediente`) VALUES
(1, 1, 'Bombay', 'Se echan en vaso mezclador con unos cubitos de hielo. Remover y servir en vaso bajo y ancho(old fashioned), agregando uno odos cubitos de hielo', 0, '2024-06-30 17:31:03', '../img/bombay.jpg', 1, 1),
(2, 1, 'Brandy Alexander', 'Agite bien todos los ingredientes en una coctelera con hielo picado. Sírvalo sin colar en copa de cóctel.Si se desea añada un poco de nuez moscada.', 0, '2024-06-30 18:06:22', '/img/brandyalexander.webp', 2, 1),
(3, 1, 'French Connection', 'Vierta todos los ingredientes directamente en un vaso bajo y ancho (old fashioned) con cubitos de hielo. Revuelva suavemente.', 0, '2024-06-30 18:06:22', '/img/frenchconnection.webp', 1, 1),
(4, 1, 'Stinger', 'Mezclar en la coctelera con un poco de hielo picado. Agitar y servir en copa de cóctel previamente enfriada.', 0, '2024-06-30 18:08:17', '/img/stinger.webp', 2, 1),
(5, 1, 'Daikiri de frutilla', 'Colocar todos los ingredientes en el vaso de la licuadora. Licuar hasta que quede una mezcla cremosa. Si se desea, decorar el borde del vaso con azúcar. Servir', 0, '2024-06-30 18:09:17', '/img/daikiri.jpg', 1, 2);

-- --------------------------------------------------------

--
-- Estructura de tabla para la tabla `favoritos`
--

CREATE TABLE `favoritos` (
  `id` int(11) NOT NULL,
  `Usuario` int(11) NOT NULL,
  `Coctel` int(11) NOT NULL
) ENGINE=InnoDB DEFAULT CHARSET=utf8mb4 COLLATE=utf8mb4_general_ci;

-- --------------------------------------------------------

--
-- Estructura de tabla para la tabla `ingredientepri`
--

CREATE TABLE `ingredientepri` (
  `id` int(11) NOT NULL,
  `nombre` varchar(100) NOT NULL
) ENGINE=InnoDB DEFAULT CHARSET=utf8mb4 COLLATE=utf8mb4_general_ci;

--
-- Volcado de datos para la tabla `ingredientepri`
--

INSERT INTO `ingredientepri` (`id`, `nombre`) VALUES
(1, 'brandy'),
(2, 'ron'),
(3, 'Ginebra'),
(4, 'Whisky'),
(5, 'Cava'),
(6, 'Tequila');

-- --------------------------------------------------------

--
-- Estructura de tabla para la tabla `ingredientes`
--

CREATE TABLE `ingredientes` (
  `id` int(11) NOT NULL,
  `nombre` varchar(100) NOT NULL
) ENGINE=InnoDB DEFAULT CHARSET=utf8mb4 COLLATE=utf8mb4_general_ci;

--
-- Volcado de datos para la tabla `ingredientes`
--

INSERT INTO `ingredientes` (`id`, `nombre`) VALUES
(1, '1/4 de vermut blanco seco'),
(2, '1/4 de vermut rojo'),
(3, '2 golpes de Curaçao (naranja a ser posible)'),
(4, '1/3 de brandy'),
(5, '1/4 de vermut rojo'),
(6, '1/3 de crema de cacao'),
(7, '1/3 de nata liquida o crema de leche'),
(8, '1/2 de brandy'),
(9, '1/2 de Amaretto'),
(10, '2/3 de brandy'),
(11, '1/3 de crema de menta'),
(12, '1 puñado de frutillas frescas (6 o 7 u)'),
(13, 'Una cucharada panzona de azúcar'),
(14, '2 cdas de jugo del lima o limón'),
(15, '1/2 taza de ron blanco o dorado'),
(16, 'Hielo');

-- --------------------------------------------------------

--
-- Estructura de tabla para la tabla `ingredientescoctel`
--

CREATE TABLE `ingredientescoctel` (
  `id` int(11) NOT NULL,
  `coctel` int(11) NOT NULL,
  `ingrediente` int(11) NOT NULL
) ENGINE=InnoDB DEFAULT CHARSET=utf8mb4 COLLATE=utf8mb4_general_ci;

--
-- Volcado de datos para la tabla `ingredientescoctel`
--

INSERT INTO `ingredientescoctel` (`id`, `coctel`, `ingrediente`) VALUES
(1, 1, 1),
(2, 1, 2),
(3, 1, 3),
(4, 2, 4),
(5, 2, 2),
(6, 2, 6),
(7, 2, 7),
(8, 3, 8),
(9, 3, 9),
(10, 4, 10),
(11, 4, 11),
(12, 5, 12),
(13, 5, 13),
(14, 5, 14),
(15, 5, 15),
(16, 5, 16);

-- --------------------------------------------------------

--
-- Estructura de tabla para la tabla `tipos`
--

CREATE TABLE `tipos` (
  `id` int(11) NOT NULL,
  `tipo` varchar(200) NOT NULL
) ENGINE=InnoDB DEFAULT CHARSET=utf8mb4 COLLATE=utf8mb4_general_ci;

--
-- Volcado de datos para la tabla `tipos`
--

INSERT INTO `tipos` (`id`, `tipo`) VALUES
(1, 'directo'),
(2, 'coctelera'),
(3, 'En vaso mezclador'),
(4, 'En licuadora'),
(5, 'Flambeados');

-- --------------------------------------------------------

--
-- Estructura de tabla para la tabla `usuarios`
--

CREATE TABLE `usuarios` (
  `id` int(11) NOT NULL,
  `Usuario` varchar(20) NOT NULL,
  `Pass` varchar(100) NOT NULL,
  `Nick` varchar(20) NOT NULL,
  `Correo` varchar(250) NOT NULL,
  `NivelUs` varchar(1) NOT NULL DEFAULT '0',
  `FechaRegistro` datetime NOT NULL DEFAULT current_timestamp()
) ENGINE=InnoDB DEFAULT CHARSET=utf8mb4 COLLATE=utf8mb4_general_ci;

--
-- Índices para tablas volcadas
--

--
-- Indices de la tabla `cocteles`
--
ALTER TABLE `cocteles`
  ADD PRIMARY KEY (`ID`),
  ADD KEY `fk_tipo` (`tipo`),
  ADD KEY `fk_ingrediente` (`ingrediente`);

--
-- Indices de la tabla `favoritos`
--
ALTER TABLE `favoritos`
  ADD PRIMARY KEY (`id`),
  ADD KEY `Usuario` (`Usuario`),
  ADD KEY `Coctel` (`Coctel`);

--
-- Indices de la tabla `ingredientepri`
--
ALTER TABLE `ingredientepri`
  ADD PRIMARY KEY (`id`);

--
-- Indices de la tabla `ingredientes`
--
ALTER TABLE `ingredientes`
  ADD PRIMARY KEY (`id`);

--
-- Indices de la tabla `ingredientescoctel`
--
ALTER TABLE `ingredientescoctel`
  ADD PRIMARY KEY (`id`),
  ADD KEY `fk_coctel` (`coctel`),
  ADD KEY `fk_ingredientec` (`ingrediente`);

--
-- Indices de la tabla `tipos`
--
ALTER TABLE `tipos`
  ADD PRIMARY KEY (`id`);

--
-- Indices de la tabla `usuarios`
--
ALTER TABLE `usuarios`
  ADD PRIMARY KEY (`id`);

--
-- AUTO_INCREMENT de las tablas volcadas
--

--
-- AUTO_INCREMENT de la tabla `cocteles`
--
ALTER TABLE `cocteles`
  MODIFY `ID` int(11) NOT NULL AUTO_INCREMENT, AUTO_INCREMENT=6;

--
-- AUTO_INCREMENT de la tabla `favoritos`
--
ALTER TABLE `favoritos`
  MODIFY `id` int(11) NOT NULL AUTO_INCREMENT;

--
-- AUTO_INCREMENT de la tabla `ingredientepri`
--
ALTER TABLE `ingredientepri`
  MODIFY `id` int(11) NOT NULL AUTO_INCREMENT, AUTO_INCREMENT=7;

--
-- AUTO_INCREMENT de la tabla `ingredientes`
--
ALTER TABLE `ingredientes`
  MODIFY `id` int(11) NOT NULL AUTO_INCREMENT, AUTO_INCREMENT=17;

--
-- AUTO_INCREMENT de la tabla `ingredientescoctel`
--
ALTER TABLE `ingredientescoctel`
  MODIFY `id` int(11) NOT NULL AUTO_INCREMENT, AUTO_INCREMENT=17;

--
-- AUTO_INCREMENT de la tabla `tipos`
--
ALTER TABLE `tipos`
  MODIFY `id` int(11) NOT NULL AUTO_INCREMENT, AUTO_INCREMENT=6;

--
-- AUTO_INCREMENT de la tabla `usuarios`
--
ALTER TABLE `usuarios`
  MODIFY `id` int(11) NOT NULL AUTO_INCREMENT;

--
-- Restricciones para tablas volcadas
--

--
-- Filtros para la tabla `cocteles`
--
ALTER TABLE `cocteles`
  ADD CONSTRAINT `fk_ingrediente` FOREIGN KEY (`ingrediente`) REFERENCES `ingredientepri` (`id`),
  ADD CONSTRAINT `fk_tipo` FOREIGN KEY (`tipo`) REFERENCES `tipos` (`id`);

--
-- Filtros para la tabla `favoritos`
--
ALTER TABLE `favoritos`
  ADD CONSTRAINT `favoritos_ibfk_1` FOREIGN KEY (`Usuario`) REFERENCES `usuarios` (`id`),
  ADD CONSTRAINT `favoritos_ibfk_2` FOREIGN KEY (`Coctel`) REFERENCES `cocteles` (`ID`);

--
-- Filtros para la tabla `ingredientescoctel`
--
ALTER TABLE `ingredientescoctel`
  ADD CONSTRAINT `fk_coctel` FOREIGN KEY (`coctel`) REFERENCES `cocteles` (`ID`),
  ADD CONSTRAINT `fk_ingredientec` FOREIGN KEY (`ingrediente`) REFERENCES `ingredientes` (`id`);
COMMIT;

/*!40101 SET CHARACTER_SET_CLIENT=@OLD_CHARACTER_SET_CLIENT */;
/*!40101 SET CHARACTER_SET_RESULTS=@OLD_CHARACTER_SET_RESULTS */;
/*!40101 SET COLLATION_CONNECTION=@OLD_COLLATION_CONNECTION */;
