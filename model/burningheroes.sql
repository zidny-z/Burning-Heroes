-- phpMyAdmin SQL Dump
-- version 5.0.3
-- https://www.phpmyadmin.net/
--
-- Host: 127.0.0.1
-- Waktu pembuatan: 11 Jan 2021 pada 00.04
-- Versi server: 10.4.14-MariaDB
-- Versi PHP: 7.2.34

SET SQL_MODE = "NO_AUTO_VALUE_ON_ZERO";
START TRANSACTION;
SET time_zone = "+00:00";


/*!40101 SET @OLD_CHARACTER_SET_CLIENT=@@CHARACTER_SET_CLIENT */;
/*!40101 SET @OLD_CHARACTER_SET_RESULTS=@@CHARACTER_SET_RESULTS */;
/*!40101 SET @OLD_COLLATION_CONNECTION=@@COLLATION_CONNECTION */;
/*!40101 SET NAMES utf8mb4 */;

--
-- Database: `burningheroes`
--

-- --------------------------------------------------------

--
-- Struktur dari tabel `hero`
--

CREATE TABLE `hero` (
  `HeroID` int(2) NOT NULL,
  `HeroName` char(10) DEFAULT NULL,
  `HeroRole` char(10) DEFAULT NULL,
  `HeroAttack` int(3) DEFAULT NULL,
  `HeroHP` int(3) DEFAULT NULL,
  `MaxHP` int(4) DEFAULT NULL,
  `username` char(10) DEFAULT NULL
) ENGINE=InnoDB DEFAULT CHARSET=utf8mb4;

--
-- Dumping data untuk tabel `hero`
--

INSERT INTO `hero` (`HeroID`, `HeroName`, `HeroRole`, `HeroAttack`, `HeroHP`, `MaxHP`, `username`) VALUES
(1, 'lucas', 'fist', 40, 150, 150, '6zero'),
(2, 'kimshin', 'Bow', 40, 0, 75, '6zero'),
(3, 'alibaba', 'sword', 55, 80, 80, '6zero'),
(13, 'lucas', 'fist', 15, 0, 210, 'poi'),
(14, 'kimshin', 'bow', 50, 95, 95, 'poi'),
(15, 'alibaba', 'sword', 35, 80, 80, 'poi'),
(16, 'lucas', 'fist', 15, 150, 150, 'pol'),
(17, 'kimshin', 'bow', 50, 75, 75, 'pol'),
(18, 'alibaba', 'sword', 35, 80, 80, 'pol'),
(19, 'lucas', 'fist', 15, 150, 150, 'kanzul'),
(20, 'kimshin', 'bow', 50, 75, 75, 'kanzul'),
(21, 'alibaba', 'sword', 35, 80, 80, 'kanzul');

-- --------------------------------------------------------

--
-- Struktur dari tabel `item`
--

CREATE TABLE `item` (
  `ItemID` int(1) NOT NULL,
  `NamaItem` char(20) DEFAULT NULL,
  `value` int(2) DEFAULT NULL,
  `storage` int(10) DEFAULT NULL,
  `price` int(4) DEFAULT NULL,
  `notes` char(255) DEFAULT NULL,
  `username` char(10) DEFAULT NULL
) ENGINE=InnoDB DEFAULT CHARSET=utf8mb4;

--
-- Dumping data untuk tabel `item`
--

INSERT INTO `item` (`ItemID`, `NamaItem`, `value`, `storage`, `price`, `notes`, `username`) VALUES
(1, 'potion', 10, 0, 10, 'Potion can be used to replenish hero hp', NULL),
(2, 'machinegun', 20, 0, 20, 'Machine gun can be used to increase heros attack demage', NULL),
(3, 'soultrap', 20, 0, 15, 'Soul trap can be used to increase heros max hp', NULL),
(4, 'potion', 10, 14, 10, 'Potion can be used to replenish hero hp', '6zero'),
(5, 'machinegun', 20, 19, 20, 'Machine gun can be used to increase heros attack demage', '6zero'),
(6, 'soultrap', 20, 0, 15, 'Soul trap can be used to increase heros max hp', '6zero'),
(16, 'potion', 20, 4, 15, 'Potion can be used to replenish hero hp', 'poi'),
(17, 'machinegun', 20, 0, 15, 'Machine gun can be used to increase heros attack demage', 'poi'),
(18, 'soultrap', 20, 1, 15, 'Soul Trap can be used to increase heros max hp', 'poi'),
(19, 'potion', 20, 0, 15, 'Potion can be used to replenish hero hp', 'pol'),
(20, 'machinegun', 20, 0, 15, 'Machine gun can be used to increase heros attack demage', 'pol'),
(21, 'soultrap', 20, 0, 15, 'Soul Trap can be used to increase heros max hp', 'pol'),
(22, 'potion', 20, 9, 15, 'Potion can be used to replenish hero hp', 'kanzul'),
(23, 'machinegun', 20, 0, 15, 'Machine gun can be used to increase heros attack demage', 'kanzul'),
(24, 'soultrap', 20, 0, 15, 'Soul Trap can be used to increase heros max hp', 'kanzul');

-- --------------------------------------------------------

--
-- Struktur dari tabel `user`
--

CREATE TABLE `user` (
  `username` char(10) NOT NULL,
  `password` char(10) NOT NULL,
  `stage` int(2) DEFAULT NULL,
  `koins` int(10) DEFAULT NULL
) ENGINE=InnoDB DEFAULT CHARSET=utf8mb4;

--
-- Dumping data untuk tabel `user`
--

INSERT INTO `user` (`username`, `password`, `stage`, `koins`) VALUES
('6zero', 'pboaman', 1, 1100),
('kanzul', 'kanzul', 1, 300),
('poi', 'poi', 1, 310),
('pol', 'pol', 0, 200);

--
-- Indexes for dumped tables
--

--
-- Indeks untuk tabel `hero`
--
ALTER TABLE `hero`
  ADD PRIMARY KEY (`HeroID`),
  ADD KEY `username` (`username`);

--
-- Indeks untuk tabel `item`
--
ALTER TABLE `item`
  ADD PRIMARY KEY (`ItemID`),
  ADD KEY `username` (`username`);

--
-- Indeks untuk tabel `user`
--
ALTER TABLE `user`
  ADD PRIMARY KEY (`username`);

--
-- AUTO_INCREMENT untuk tabel yang dibuang
--

--
-- AUTO_INCREMENT untuk tabel `hero`
--
ALTER TABLE `hero`
  MODIFY `HeroID` int(2) NOT NULL AUTO_INCREMENT, AUTO_INCREMENT=22;

--
-- AUTO_INCREMENT untuk tabel `item`
--
ALTER TABLE `item`
  MODIFY `ItemID` int(1) NOT NULL AUTO_INCREMENT, AUTO_INCREMENT=25;

--
-- Ketidakleluasaan untuk tabel pelimpahan (Dumped Tables)
--

--
-- Ketidakleluasaan untuk tabel `hero`
--
ALTER TABLE `hero`
  ADD CONSTRAINT `hero_ibfk_1` FOREIGN KEY (`username`) REFERENCES `user` (`username`) ON DELETE CASCADE ON UPDATE CASCADE;

--
-- Ketidakleluasaan untuk tabel `item`
--
ALTER TABLE `item`
  ADD CONSTRAINT `item_ibfk_2` FOREIGN KEY (`username`) REFERENCES `user` (`username`) ON DELETE CASCADE ON UPDATE CASCADE;
COMMIT;

/*!40101 SET CHARACTER_SET_CLIENT=@OLD_CHARACTER_SET_CLIENT */;
/*!40101 SET CHARACTER_SET_RESULTS=@OLD_CHARACTER_SET_RESULTS */;
/*!40101 SET COLLATION_CONNECTION=@OLD_COLLATION_CONNECTION */;
