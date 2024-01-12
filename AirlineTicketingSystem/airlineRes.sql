-- phpMyAdmin SQL Dump
-- version 5.2.0
-- https://www.phpmyadmin.net/
--
-- Host: localhost
-- Generation Time: Dec 22, 2022 at 12:00 AM
-- Server version: 10.4.21-MariaDB
-- PHP Version: 7.4.29

SET SQL_MODE = "NO_AUTO_VALUE_ON_ZERO";
START TRANSACTION;
SET time_zone = "+00:00";


/*!40101 SET @OLD_CHARACTER_SET_CLIENT=@@CHARACTER_SET_CLIENT */;
/*!40101 SET @OLD_CHARACTER_SET_RESULTS=@@CHARACTER_SET_RESULTS */;
/*!40101 SET @OLD_COLLATION_CONNECTION=@@COLLATION_CONNECTION */;
/*!40101 SET NAMES utf8mb4 */;

--
-- Database: `airlineRes`
--

-- --------------------------------------------------------

--
-- Table structure for table `Airline`
--

CREATE TABLE `Airline` (
  `name` char(50) NOT NULL,
  `number_of_airplanes` int(11) NOT NULL
) ENGINE=InnoDB DEFAULT CHARSET=utf8mb4;

--
-- Dumping data for table `Airline`
--

INSERT INTO `Airline` (`name`, `number_of_airplanes`) VALUES
('Jet Blue', 50);

-- --------------------------------------------------------

--
-- Table structure for table `Airline_Staff`
--

CREATE TABLE `Airline_Staff` (
  `username` char(50) NOT NULL,
  `password` char(50) NOT NULL,
  `first_name` char(50) DEFAULT NULL,
  `last_name` char(50) DEFAULT NULL,
  `date_of_birth` char(50) DEFAULT NULL,
  `phone_number` char(20) DEFAULT NULL,
  `email` char(50) NOT NULL,
  `airline_name` char(50) DEFAULT NULL
) ENGINE=InnoDB DEFAULT CHARSET=utf8mb4;

--
-- Dumping data for table `Airline_Staff`
--

INSERT INTO `Airline_Staff` (`username`, `password`, `first_name`, `last_name`, `date_of_birth`, `phone_number`, `email`, `airline_name`) VALUES
('dim10101', '12345', 'Dimitri', 'Belessakos', '05/05/2000', '9147088536', 'dab718@nyu.edu', 'Delta'),
('karenK123', '123456', 'Karen', 'Karens', '05/05/1980', '9174441111', 'KK@data.com', 'Jet Blue');

-- --------------------------------------------------------

--
-- Table structure for table `Airplane`
--

CREATE TABLE `Airplane` (
  `airline_name` char(50) NOT NULL,
  `airplane_id` int(11) NOT NULL,
  `number_of_seats` int(11) NOT NULL,
  `manufac` char(50) NOT NULL,
  `age` int(50) NOT NULL
) ENGINE=InnoDB DEFAULT CHARSET=utf8mb4;

--
-- Dumping data for table `Airplane`
--

INSERT INTO `Airplane` (`airline_name`, `airplane_id`, `number_of_seats`, `manufac`, `age`) VALUES
('Jet Blue', 11111111, 115, 'Boeing', 3),
('Delta', 12345678, 115, 'Boeing', 2),
('American Airlines', 87654321, 115, 'Boeing', 5);

-- --------------------------------------------------------

--
-- Table structure for table `Airport`
--

CREATE TABLE `Airport` (
  `name` char(50) NOT NULL,
  `city` char(50) NOT NULL,
  `country` char(50) NOT NULL,
  `type` char(50) NOT NULL
) ENGINE=InnoDB DEFAULT CHARSET=utf8mb4;

--
-- Dumping data for table `Airport`
--

INSERT INTO `Airport` (`name`, `city`, `country`, `type`) VALUES
('JFK', 'NYC', 'USA', 'International'),
('PVG', 'Shanghai', 'China', 'International');

-- --------------------------------------------------------

--
-- Table structure for table `Customer`
--

CREATE TABLE `Customer` (
  `customer_name` char(50) DEFAULT NULL,
  `customer_email` char(50) DEFAULT NULL,
  `password` char(50) DEFAULT NULL,
  `customer_address` char(200) DEFAULT NULL,
  `building_number` int(11) DEFAULT NULL,
  `street` char(50) DEFAULT NULL,
  `state` char(50) DEFAULT NULL,
  `phone_number` char(50) DEFAULT NULL,
  `passport_number` int(11) DEFAULT NULL,
  `passport_expiration` char(50) DEFAULT NULL,
  `passport_country` char(50) NOT NULL
) ENGINE=InnoDB DEFAULT CHARSET=utf8mb4;

--
-- Dumping data for table `Customer`
--

INSERT INTO `Customer` (`customer_name`, `customer_email`, `password`, `customer_address`, `building_number`, `street`, `state`, `phone_number`, `passport_number`, `passport_expiration`, `passport_country`) VALUES
('David Data', 'dd@data.com', '123456', '35 Cherry Lane', 35, 'Cherry Lane', 'NY', '9141112222', 5555555, '11/07/2023', 'USA'),
('Sophia Corner', 'SC@data.com', '123456', '22 Fish St', 22, 'Fish St', 'FL', '9142221111', 7777777, '12/015/2025', 'USA'),
('Jason Base', 'JB@data.com', '123456', '5 Airplane Way', 5, 'Airplane Way', 'CA', '9143334444', 1111111, '02/25/2028', 'USA'),
('Dimitri Belessakos', 'dimbob@gmail.com', '123', '22 huffing way', 22, 'huffing way', 'NY', 'phoneNumber', 912391293, '12/24/2022', 'USA');

-- --------------------------------------------------------

--
-- Table structure for table `Flight`
--

CREATE TABLE `Flight` (
  `flight_number` int(11) NOT NULL,
  `airline` char(50) NOT NULL,
  `departure_airport` char(50) DEFAULT NULL,
  `departure_time` char(50) DEFAULT NULL,
  `departure_date` char(50) DEFAULT NULL,
  `arrival_airport` char(50) NOT NULL,
  `arrival_time` char(50) DEFAULT NULL,
  `arrival_date` char(50) DEFAULT NULL,
  `base_price` int(11) NOT NULL,
  `flight_id` int(11) NOT NULL,
  `status` char(50) NOT NULL
) ENGINE=InnoDB DEFAULT CHARSET=utf8mb4;

--
-- Dumping data for table `Flight`
--

INSERT INTO `Flight` (`flight_number`, `airline`, `departure_airport`, `departure_time`, `departure_date`, `arrival_airport`, `arrival_time`, `arrival_date`, `base_price`, `flight_id`, `status`) VALUES
(111111, 'Delta', 'PVG', '11:56', '11/11/2022', 'JFK', '03:29', '11/12/2022', 220, 555, 'delayed'),
(222222, 'Delta', 'JFK', '11:56', '11/07/2022', 'PVG', '22:17', '11/08/2022', 256, 1234, 'on-time'),
(654321, 'Jet Blue', 'PVG', '9:00', '11/10/2022', 'JFK', '15:32', '11/10/2022', 250, 4321, 'delayed'),
(777777, 'American Airlines', 'JFK', '15:29', '11/15/2022', 'PVG', '23:45', '11/15/2022', 300, 4444, 'on-time');

-- --------------------------------------------------------

--
-- Table structure for table `Ticket`
--

CREATE TABLE `Ticket` (
  `customer_email` char(50) NOT NULL,
  `customer_address` char(200) NOT NULL,
  `airline_name` char(50) NOT NULL,
  `flight_number` int(11) NOT NULL,
  `sold_price` int(11) NOT NULL,
  `payment_information` char(200) NOT NULL,
  `purchase_time` char(20) DEFAULT NULL,
  `purchase_date` char(20) DEFAULT NULL,
  `ticket_id` char(32) NOT NULL
) ENGINE=InnoDB DEFAULT CHARSET=utf8mb4;

--
-- Dumping data for table `Ticket`
--

INSERT INTO `Ticket` (`customer_email`, `customer_address`, `airline_name`, `flight_number`, `sold_price`, `payment_information`, `purchase_time`, `purchase_date`, `ticket_id`) VALUES
('dd@data.com', '35 Cherry Lane', 'Delta', 222222, 256, 'credit-1234567-David Data-06/21/2027', '12:50', '11/07/2022', '9999'),
('JB@data.com', '5 Airplane Way', 'American Airlines', 777777, 300, 'credit-1928384-Jason Base-10/05/2026', '16:10', '11/07/2022', '2222'),
('SC@data.com', '22 Fish St', 'Jet Blue', 654321, 270, 'credit-7654321-Sophia Corner-12/15/2028', '14:30', '11/07/2022', '1111'),
('dim@www.com', '55 t street', 'Delta', 222222, 256, 'credit-9484848484-test TEst-12/15/2022', '12:32', 'purchase_date', 'ticket_id');

--
-- Indexes for dumped tables
--

--
-- Indexes for table `Airline`
--
ALTER TABLE `Airline`
  ADD UNIQUE KEY `name` (`name`);

--
-- Indexes for table `Airline_Staff`
--
ALTER TABLE `Airline_Staff`
  ADD UNIQUE KEY `username` (`username`);

--
-- Indexes for table `Airplane`
--
ALTER TABLE `Airplane`
  ADD PRIMARY KEY (`airplane_id`);

--
-- Indexes for table `Airport`
--
ALTER TABLE `Airport`
  ADD PRIMARY KEY (`name`);

--
-- Indexes for table `Customer`
--
ALTER TABLE `Customer`
  ADD UNIQUE KEY `customer_email` (`customer_email`);

--
-- Indexes for table `Flight`
--
ALTER TABLE `Flight`
  ADD PRIMARY KEY (`flight_number`);
COMMIT;

/*!40101 SET CHARACTER_SET_CLIENT=@OLD_CHARACTER_SET_CLIENT */;
/*!40101 SET CHARACTER_SET_RESULTS=@OLD_CHARACTER_SET_RESULTS */;
/*!40101 SET COLLATION_CONNECTION=@OLD_COLLATION_CONNECTION */;
