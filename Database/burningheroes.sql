-- phpMyAdmin SQL Dump
-- version 5.0.3
-- https://www.phpmyadmin.net/
--
-- Host: 127.0.0.1
-- Waktu pembuatan: 11 Jun 2021 pada 10.26
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
  `HeroName` char(20) DEFAULT NULL,
  `HeroAttack` int(3) DEFAULT NULL,
  `HeroHP` int(3) DEFAULT NULL,
  `MaxHP` int(4) DEFAULT NULL,
  `username` char(10) DEFAULT NULL
) ENGINE=InnoDB DEFAULT CHARSET=utf8mb4;

--
-- Dumping data untuk tabel `hero`
--

INSERT INTO `hero` (`HeroID`, `HeroName`, `HeroAttack`, `HeroHP`, `MaxHP`, `username`) VALUES
(5, 'Batman', 35, 90, 90, 'Username'),
(6, 'Superman', 25, 150, 150, 'Username'),
(7, 'Joker', 40, 80, 80, 'Username'),
(8, 'Wonder Women', 30, 100, 100, 'Username'),
(24, 'Batman', 35, 90, 90, 'bot'),
(25, 'Superman', 25, 150, 150, 'bot'),
(26, 'Joker', 40, 80, 80, 'bot'),
(27, 'Wonder Women', 30, 100, 100, 'bot');

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
  `username` char(10) DEFAULT NULL
) ENGINE=InnoDB DEFAULT CHARSET=utf8mb4;

--
-- Dumping data untuk tabel `item`
--

INSERT INTO `item` (`ItemID`, `NamaItem`, `value`, `storage`, `price`, `username`) VALUES
(1, 'potion', 130, 0, 10, 'bot'),
(2, 'meat', 50, 0, 10, 'bot'),
(3, 'Sharpener', 20, 0, 15, 'bot'),
(4, 'Giant Potion', 140, 0, 20, 'bot'),
(5, 'potion', NULL, 0, 10, 'Username'),
(6, 'meat', NULL, 0, 10, 'Username'),
(7, 'Sharpener', NULL, 0, 15, 'Username'),
(8, 'Giant Potion', NULL, 0, 20, 'Username');

-- --------------------------------------------------------

--
-- Struktur dari tabel `user`
--

CREATE TABLE `user` (
  `username` char(10) NOT NULL,
  `password` char(10) NOT NULL,
  `stage` int(2) DEFAULT NULL,
  `koins` int(10) DEFAULT NULL,
  `hint` varchar(35) DEFAULT NULL,
  `login_status` tinyint(1) DEFAULT NULL
) ENGINE=InnoDB DEFAULT CHARSET=utf8mb4;

--
-- Dumping data untuk tabel `user`
--

INSERT INTO `user` (`username`, `password`, `stage`, `koins`, `hint`, `login_status`) VALUES
('bot', 'bot', 1, 1000, 'bot', 0),
('Username', 'Password', 5, 1040, 'Hint', 1);

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
  MODIFY `HeroID` int(2) NOT NULL AUTO_INCREMENT, AUTO_INCREMENT=60;

--
-- AUTO_INCREMENT untuk tabel `item`
--
ALTER TABLE `item`
  MODIFY `ItemID` int(1) NOT NULL AUTO_INCREMENT, AUTO_INCREMENT=17;

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
