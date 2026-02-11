-- phpMyAdmin SQL Dump
-- version 5.2.1
-- https://www.phpmyadmin.net/
--
-- Host: 127.0.0.1
-- Generation Time: Feb 06, 2026 at 11:25 AM
-- Server version: 10.4.32-MariaDB
-- PHP Version: 8.2.12

SET SQL_MODE = "NO_AUTO_VALUE_ON_ZERO";
START TRANSACTION;
SET time_zone = "+00:00";


/*!40101 SET @OLD_CHARACTER_SET_CLIENT=@@CHARACTER_SET_CLIENT */;
/*!40101 SET @OLD_CHARACTER_SET_RESULTS=@@CHARACTER_SET_RESULTS */;
/*!40101 SET @OLD_COLLATION_CONNECTION=@@COLLATION_CONNECTION */;
/*!40101 SET NAMES utf8mb4 */;

--
-- Database: `demopisun`
--

-- --------------------------------------------------------

--
-- Table structure for table `creator`
--

CREATE TABLE `creator` (
  `id` int(11) NOT NULL,
  `name` varchar(30) NOT NULL
) ENGINE=InnoDB DEFAULT CHARSET=utf8mb4 COLLATE=utf8mb4_general_ci;

--
-- Dumping data for table `creator`
--

INSERT INTO `creator` (`id`, `name`) VALUES
(1, 'Kari'),
(2, 'Marco Tozzi'),
(3, 'Poc'),
(4, 'Rieker'),
(5, 'Alessio Nesca'),
(6, 'CROSBY');

-- --------------------------------------------------------

--
-- Table structure for table `stuff`
--

CREATE TABLE `stuff` (
  `id` varchar(8) NOT NULL,
  `name` varchar(30) NOT NULL,
  `unit` int(11) NOT NULL,
  `price` decimal(10,2) NOT NULL,
  `supplier_id` int(11) NOT NULL,
  `creator_id` int(11) NOT NULL,
  `category` tinyint(4) NOT NULL,
  `sale` int(11) NOT NULL,
  `quantity` int(11) NOT NULL,
  `discription` text NOT NULL,
  `photo` varchar(200) NOT NULL
) ENGINE=InnoDB DEFAULT CHARSET=utf8mb4 COLLATE=utf8mb4_general_ci;

--
-- Dumping data for table `stuff`
--

INSERT INTO `stuff` (`id`, `name`, `unit`, `price`, `supplier_id`, `creator_id`, `category`, `sale`, `quantity`, `discription`, `photo`) VALUES
('B320R5', 'Туфли', 0, 4300.00, 2, 4, 0, 2, 6, 'Туфли Rieker женские демисезонные, размер 41, цвет коричневый', '9.jpg'),
('B431R5', 'Ботинки', 0, 2700.00, 3, 4, 1, 2, 5, 'Мужские кожаные ботинки/мужские ботинки', ''),
('C436G5', 'Ботинки', 0, 10200.00, 2, 5, 0, 15, 9, 'Ботинки женские, ARGO, размер 40', ''),
('D268G5', 'Туфли', 0, 4399.00, 3, 4, 0, 3, 12, 'Туфли Rieker женские демисезонные, размер 36, цвет коричневый', ''),
('D329H3', 'Полуботинки', 0, 1890.00, 3, 5, 0, 4, 4, 'Полуботинки Alessio Nesca женские 3-30797-47, размер 37, цвет: бордовый', '8.jpg'),
('D364R4', 'Туфли', 0, 12400.00, 2, 1, 0, 16, 5, 'Туфли Luiza Belly женские Kate-lazo черные из натуральной замши', ''),
('D572U8', 'Кроссовки', 0, 4100.00, 3, 3, 1, 3, 6, '129615-4 Кроссовки мужские', '6.jpg'),
('E482R4', 'Полуботинки', 0, 1800.00, 2, 1, 0, 2, 14, 'Полуботинки kari женские MYZ20S-149, размер 41, цвет: черный', ''),
('F427R5', 'Ботинки', 0, 11800.00, 3, 4, 0, 15, 11, 'Ботинки на молнии с декоративной пряжкой FRAU', ''),
('F572H7', 'Туфли', 0, 2700.00, 2, 2, 0, 2, 14, 'Туфли Marco Tozzi женские летние, размер 39, цвет черный', '7.jpg'),
('F635R4', 'Ботинки', 0, 3244.00, 3, 2, 0, 2, 13, 'Ботинки Marco Tozzi женские демисезонные, размер 39, цвет бежевый', '2.jpg'),
('G432E4', 'Туфли', 0, 2800.00, 2, 1, 0, 3, 15, 'Туфли kari женские TR-YR-413017, размер 37, цвет: черный', '10.jpg'),
('G531F4', 'Ботинки', 0, 6600.00, 2, 1, 0, 12, 9, 'Ботинки женские зимние ROMER арт. 893167-01 Черный', ''),
('G783F5', 'Ботинки', 0, 5900.00, 2, 3, 1, 2, 8, 'Мужские ботинки Рос-Обувь кожаные с натуральным мехом', '4.jpg'),
('H535R5', 'Ботинки', 0, 2300.00, 3, 4, 0, 2, 7, 'Женские Ботинки демисезонные', ''),
('H782T5', 'Туфли', 0, 4499.00, 2, 1, 1, 4, 5, 'Туфли kari мужские классика MYZ21AW-450A, размер 43, цвет: черный', '3.jpg'),
('J384T6', 'Ботинки', 0, 3800.00, 3, 4, 1, 2, 16, 'B3430/14 Полуботинки мужские Rieker', '5.jpg'),
('J542F5', 'Тапочки', 0, 500.00, 2, 1, 1, 13, 0, 'Тапочки мужские Арт.70701-55-67син р.41', ''),
('K345R4', 'Полуботинки', 0, 2100.00, 3, 6, 1, 2, 3, '407700/01-02 Полуботинки мужские CROSBY', ''),
('K358H6', 'Тапочки', 0, 599.00, 2, 4, 1, 20, 2, 'Тапочки мужские син р.41', ''),
('L754R4', 'Полуботинки', 0, 1700.00, 2, 1, 0, 2, 7, 'Полуботинки kari женские WB2020SS-26, размер 38, цвет: черный', ''),
('M542T5', 'Кроссовки', 0, 2800.00, 3, 4, 1, 18, 3, 'Кроссовки мужские TOFA', ''),
('N457T5', 'Полуботинки', 0, 4600.00, 2, 6, 0, 3, 13, 'Полуботинки Ботинки черные зимние, мех', ''),
('O754F4', 'Туфли', 0, 5400.00, 3, 4, 0, 4, 18, 'Туфли женские демисезонные Rieker артикул 55073-68/37', ''),
('P764G4', 'Туфли', 0, 6800.00, 2, 6, 0, 15, 15, 'Туфли женские, ARGO, размер 38', ''),
('S213E3', 'Полуботинки', 0, 2156.00, 3, 6, 1, 3, 6, '407700/01-01 Полуботинки мужские CROSBY', ''),
('S326R5', 'Тапочки', 0, 9900.00, 3, 6, 1, 17, 15, 'Мужские кожаные тапочки \"Профиль С.Дали\" ', ''),
('S634B5', 'Кеды', 0, 5500.00, 3, 6, 1, 3, 0, 'Кеды Caprice мужские демисезонные, размер 42, цвет черный', ''),
('T324F5', 'Сапоги', 0, 4699.00, 2, 6, 0, 2, 5, 'Сапоги замша Цвет: синий', ''),
('А112Т4', 'Ботинки', 0, 4990.00, 2, 1, 0, 3, 6, 'Женские Ботинки демисезонные kari', '1.jpg');

-- --------------------------------------------------------

--
-- Table structure for table `supplier`
--

CREATE TABLE `supplier` (
  `id` int(11) NOT NULL,
  `name` varchar(30) NOT NULL
) ENGINE=InnoDB DEFAULT CHARSET=utf8mb4 COLLATE=utf8mb4_general_ci;

--
-- Dumping data for table `supplier`
--

INSERT INTO `supplier` (`id`, `name`) VALUES
(2, 'Kari'),
(3, 'Обувь для вас');

-- --------------------------------------------------------

--
-- Table structure for table `users`
--

CREATE TABLE `users` (
  `id` int(11) NOT NULL,
  `name` varchar(100) NOT NULL,
  `role` int(4) NOT NULL DEFAULT 0,
  `login` varchar(30) NOT NULL,
  `password` varchar(30) NOT NULL
) ENGINE=InnoDB DEFAULT CHARSET=utf8mb4 COLLATE=utf8mb4_general_ci;

--
-- Dumping data for table `users`
--

INSERT INTO `users` (`id`, `name`, `role`, `login`, `password`) VALUES
(18, 'Никифорова Весения Николаевна', 1, '94d5ous@gmail.com', 'uzWC67'),
(19, 'Сазонов Руслан Германович', 1, 'uth4iz@mail.com', '2L6KZG'),
(20, 'Одинцов Серафим Артёмович', 1, 'yzls62@outlook.com', 'JlFRCZ'),
(21, 'Степанов Михаил Артёмович', 2, '1diph5e@tutanota.com', '8ntwUp'),
(22, 'Ворсин Петр Евгеньевич', 2, 'tjde7c@yahoo.com', 'YOyhfR'),
(23, 'Старикова Елена Павловна', 2, 'wpmrc3do@tutanota.com', 'RSbvHv'),
(24, 'Михайлюк Анна Вячеславовна', 0, '5d4zbu@tutanota.com', 'rwVDh9'),
(25, 'Ситдикова Елена Анатольевна', 0, 'ptec8ym@yahoo.com', 'LdNyos'),
(26, 'Ворсин Петр Евгеньевич', 0, '1qz4kw@mail.com', 'gynQMT'),
(27, 'Старикова Елена Павловна', 0, '4np6se@mail.com', 'AtnDjr');

--
-- Indexes for dumped tables
--

--
-- Indexes for table `creator`
--
ALTER TABLE `creator`
  ADD PRIMARY KEY (`id`);

--
-- Indexes for table `stuff`
--
ALTER TABLE `stuff`
  ADD PRIMARY KEY (`id`);

--
-- Indexes for table `supplier`
--
ALTER TABLE `supplier`
  ADD PRIMARY KEY (`id`);

--
-- Indexes for table `users`
--
ALTER TABLE `users`
  ADD PRIMARY KEY (`id`);

--
-- AUTO_INCREMENT for dumped tables
--

--
-- AUTO_INCREMENT for table `creator`
--
ALTER TABLE `creator`
  MODIFY `id` int(11) NOT NULL AUTO_INCREMENT, AUTO_INCREMENT=7;

--
-- AUTO_INCREMENT for table `supplier`
--
ALTER TABLE `supplier`
  MODIFY `id` int(11) NOT NULL AUTO_INCREMENT, AUTO_INCREMENT=4;

--
-- AUTO_INCREMENT for table `users`
--
ALTER TABLE `users`
  MODIFY `id` int(11) NOT NULL AUTO_INCREMENT, AUTO_INCREMENT=28;
COMMIT;

/*!40101 SET CHARACTER_SET_CLIENT=@OLD_CHARACTER_SET_CLIENT */;
/*!40101 SET CHARACTER_SET_RESULTS=@OLD_CHARACTER_SET_RESULTS */;
/*!40101 SET COLLATION_CONNECTION=@OLD_COLLATION_CONNECTION */;
