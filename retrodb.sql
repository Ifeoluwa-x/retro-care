-- phpMyAdmin SQL Dump
-- version 5.1.1
-- https://www.phpmyadmin.net/
--
-- Host: localhost
-- Generation Time: Apr 29, 2022 at 03:49 PM
-- Server version: 10.4.20-MariaDB
-- PHP Version: 7.3.29

SET SQL_MODE = "NO_AUTO_VALUE_ON_ZERO";
START TRANSACTION;
SET time_zone = "+00:00";


/*!40101 SET @OLD_CHARACTER_SET_CLIENT=@@CHARACTER_SET_CLIENT */;
/*!40101 SET @OLD_CHARACTER_SET_RESULTS=@@CHARACTER_SET_RESULTS */;
/*!40101 SET @OLD_COLLATION_CONNECTION=@@COLLATION_CONNECTION */;
/*!40101 SET NAMES utf8mb4 */;

--
-- Database: `retrodb`
--

-- --------------------------------------------------------

--
-- Table structure for table `admin`
--

CREATE TABLE `admin` (
  `admin_id` int(11) NOT NULL,
  `admin_username` varchar(255) NOT NULL,
  `admin_password` varchar(255) NOT NULL,
  `admin_lastlogin` datetime DEFAULT NULL
) ENGINE=InnoDB DEFAULT CHARSET=utf8mb4;

--
-- Dumping data for table `admin`
--

INSERT INTO `admin` (`admin_id`, `admin_username`, `admin_password`, `admin_lastlogin`) VALUES
(1, 'ariboifeoluwa@gmail.com', '1234', '2022-04-23 03:53:30');

-- --------------------------------------------------------

--
-- Table structure for table `booking`
--

CREATE TABLE `booking` (
  `booking_id` int(11) NOT NULL,
  `caregiver_id` int(11) DEFAULT NULL,
  `user_id` int(11) DEFAULT NULL,
  `client_id` int(11) DEFAULT NULL,
  `booking_amt` float DEFAULT NULL,
  `pay_id` int(11) DEFAULT NULL,
  `booking_start_date` datetime DEFAULT NULL,
  `booking_end_date` datetime DEFAULT NULL,
  `booking_status` enum('Ongoing','Completed') NOT NULL
) ENGINE=InnoDB DEFAULT CHARSET=utf8mb4;

-- --------------------------------------------------------

--
-- Table structure for table `caregiver`
--

CREATE TABLE `caregiver` (
  `care_id` int(11) NOT NULL,
  `care_email` varchar(255) NOT NULL,
  `care_pass` varchar(255) NOT NULL,
  `care_fname` varchar(255) NOT NULL,
  `care_lname` varchar(255) NOT NULL,
  `care_kin` varchar(255) NOT NULL,
  `care_kin_relationship` varchar(255) NOT NULL,
  `care_address` text NOT NULL,
  `care_gender` enum('male','female') NOT NULL,
  `care_phone` varchar(255) NOT NULL,
  `care_status` enum('pending','completed','verified') DEFAULT NULL,
  `care_pic` varchar(255) DEFAULT NULL,
  `g_fullname1` varchar(255) DEFAULT NULL,
  `g_address1` text DEFAULT NULL,
  `g_phone1` varchar(255) DEFAULT NULL,
  `g_fullname2` varchar(255) DEFAULT NULL,
  `g_address2` text DEFAULT NULL,
  `g_phone2` varchar(255) DEFAULT NULL,
  `state_id` int(11) DEFAULT NULL,
  `care_assign_status` enum('unassigned','assigned') DEFAULT NULL,
  `care_reg` datetime DEFAULT NULL
) ENGINE=InnoDB DEFAULT CHARSET=utf8mb4;

-- --------------------------------------------------------

--
-- Table structure for table `gender`
--

CREATE TABLE `gender` (
  `gender_id` int(11) NOT NULL,
  `gender` varchar(255) NOT NULL
) ENGINE=InnoDB DEFAULT CHARSET=utf8mb4;

--
-- Dumping data for table `gender`
--

INSERT INTO `gender` (`gender_id`, `gender`) VALUES
(1, 'Male'),
(2, 'Female');

-- --------------------------------------------------------

--
-- Table structure for table `payment`
--

CREATE TABLE `payment` (
  `pay_id` int(11) NOT NULL,
  `pay_userid` int(11) DEFAULT NULL,
  `pay_userclient_id` int(11) DEFAULT NULL,
  `pay_ref` varchar(255) NOT NULL,
  `pay_date` datetime DEFAULT NULL,
  `pay_status` varchar(255) NOT NULL,
  `pay_amt` float DEFAULT NULL,
  `pay_response` text DEFAULT NULL
) ENGINE=InnoDB DEFAULT CHARSET=utf8mb4;

-- --------------------------------------------------------

--
-- Table structure for table `state`
--

CREATE TABLE `state` (
  `state_id` int(11) NOT NULL,
  `state_name` varchar(255) NOT NULL
) ENGINE=InnoDB DEFAULT CHARSET=utf8mb4;

--
-- Dumping data for table `state`
--

INSERT INTO `state` (`state_id`, `state_name`) VALUES
(1, 'Lagos'),
(2, 'Abuja');

-- --------------------------------------------------------

--
-- Table structure for table `status`
--

CREATE TABLE `status` (
  `status_id` int(11) NOT NULL,
  `status` varchar(255) NOT NULL,
  `status_price` text NOT NULL
) ENGINE=InnoDB DEFAULT CHARSET=utf8mb4;

--
-- Dumping data for table `status`
--

INSERT INTO `status` (`status_id`, `status`, `status_price`) VALUES
(1, 'independent', '15000000'),
(2, 'semi-independent', '20000000'),
(3, 'fully dependent', '30000000');

-- --------------------------------------------------------

--
-- Table structure for table `user`
--

CREATE TABLE `user` (
  `user_id` int(11) NOT NULL,
  `user_email` varchar(255) NOT NULL,
  `user_pass` varchar(255) NOT NULL,
  `user_fname` varchar(255) NOT NULL,
  `user_lname` varchar(255) NOT NULL,
  `user_address` text NOT NULL,
  `user_gender` int(11) DEFAULT NULL,
  `user_phone` varchar(255) NOT NULL,
  `user_reg` datetime DEFAULT NULL,
  `state_id` int(11) DEFAULT NULL
) ENGINE=InnoDB DEFAULT CHARSET=utf8mb4;

--
-- Dumping data for table `user`
--

INSERT INTO `user` (`user_id`, `user_email`, `user_pass`, `user_fname`, `user_lname`, `user_address`, `user_gender`, `user_phone`, `user_reg`, `state_id`) VALUES
(7, 'Ariboifeoluwa@gmail.com', 'nnnn', 'Aribo', 'ifeoluwa', 'N0 8, Ariyo cresent Somolu', 1, '07036661621', '2022-04-13 16:06:23', 2),
(8, 'tolani@gmail.com', '1234', 'Tolani', 'ifeoluwa', 'N0 8, Ariyo cresent Somolu', 2, '07036661621', '2022-04-13 16:06:23', 1),
(9, 'ariboifeoluwa@gmail.com', '1234', 'Aribo', 'ifeoluwa', 'N0 8, Ariyo cresent Somolu', 1, '07036661621', '2022-04-26 16:26:20', 1),
(10, 'ariboifeoluwa@gmail.com', '1234', 'Aribo', 'ifeoluwa', 'N0 8, Ariyo cresent Somolu', 1, '07036661621', '2022-04-26 16:26:20', 1),
(11, 'ariboifeoluwa@gmail.com', '1234kpetrh', 'Aribo', 'ifeoluwa', 'N0 8, Ariyo cresent Somolu', 1, '07036661621', '2022-04-26 16:26:20', 2),
(12, 'Ariboifeoluwa@gmail.com', '1234', 'Aribo', 'ifeoluwa', 'N0 8, Ariyo cresent Somolu', 1, '07036661621', '2022-04-26 18:01:11', 2),
(13, 'Ariboifeoluwa@gmail.com', '1234', 'Aribo', 'ifeoluwa', 'N0 8, Ariyo cresent Somolu', 1, '07036661621', '2022-04-26 18:01:11', 1),
(14, 'Ariboifeoluwa@gmail.com', '1234', 'Aribo', 'ifeoluwa', 'N0 8, Ariyo cresent Somolu', 1, '07036661621', '2022-04-26 18:10:42', 1),
(15, 'Ariboifeoluwa@gmail.com', '1234', 'Aribo', 'ifeoluwa', 'N0 8, Ariyo cresent Somolu', 2, '07036661621', '2022-04-26 18:13:03', 2),
(16, 'Ariboifeoluwa@gmail.com', '12345', 'Aribo', 'ifeoluwa', 'N0 8, Ariyo cresent Somolu', 1, '07036661621', '2022-04-26 18:17:01', 2),
(17, 'Ariboifeoluwa@gmail.com', '1234h', 'Aribo', 'ifeoluwa', 'N0 8, Ariyo cresent Somolu', 1, '07036661621', '2022-04-26 18:42:02', 1),
(18, 'Ariboifeoluwa@gmail.com', '12343', 'Aribo3', 'ifeoluwa', 'N0 8, Ariyo cresent Somolu', 1, '07036661621', '2022-04-26 19:02:37', 1),
(19, 'Ariboifeoluwa@gmail.com', '12wqqq', 'Aribo', 'ifeoluwa', 'N0 8, Ariyo cresent Somolu', 1, '07036661621', '2022-04-26 19:02:37', 1),
(20, 'Ariboifeoluwa@gmail.com', '12345', 'Aribo', 'ifeoluwa', 'N0 8, Ariyo cresent Somolu', 1, '07036661621', '2022-04-26 19:02:37', 2),
(21, 'Ariboifeoluwa@gmail.com', '1234f', 'Aribo', 'ifeoluwa', 'N0 8, Ariyo cresent Somolu', 2, '07036661621', '2022-04-26 19:02:37', 1),
(22, 'Ariboifeoluwa@gmail.com', '12345', 'Aribo', 'ifeoluwa', 'N0 8, Ariyo cresent Somolu', 1, '07036661621', '2022-04-26 19:09:43', 2),
(23, 'Ariboifeoluwa@gmail.com', '1234.', 'Aribo', 'ifeoluwa', 'N0 8, Ariyo cresent Somolu', 1, '07036661621', '2022-04-26 19:10:22', 2),
(24, 'Ariboifeoluwa@gmail.com', '1234d.', 'Aribo', 'ifeoluwa', 'N0 8, Ariyo cresent Somolu', 1, '07036661621', '2022-04-26 19:10:22', 1),
(25, 'Ariboiawfhjna@gmail.com', 'pbkdf2:sha256:260000$nVkpBFgn7diYUhC8$3ebc01f905561722265127c0025a70afe58cf9f57265229aa6f5b892f671306c', 'Olaitan', 'Shegin', 'canada', 2, '07036661621', '2022-04-26 19:32:47', 2),
(26, 'Ariboifeoluwa@gmail.com', 'pbkdf2:sha256:260000$pZNdyxFbdZ4viDAM$455d78a6f24ab15b371f1d949921d2d90bb45e6e1556f4181244b963593151d5', 'Aribo', 'ifeoluwa', 'N0 8, Ariyo cresent Somolu', 1, '07036661621', '2022-04-27 13:50:28', 1),
(27, 'victorifeoluwa@gmail.com', 'pbkdf2:sha256:260000$psGvqzVmrqPOpgjS$449de5fe2e54401d32edd7b0f6f8b124c618604fa90271555baf9e0364e249cc', 'Victor', 'ifeoluwa', 'N0 8, Ariyo cresent Somolu', 1, '07036661621', '2022-04-29 12:00:23', 1);

-- --------------------------------------------------------

--
-- Table structure for table `userclient`
--

CREATE TABLE `userclient` (
  `client_id` int(11) NOT NULL,
  `client_fullname` varchar(255) NOT NULL,
  `client_address` text NOT NULL,
  `client_gender` int(11) DEFAULT NULL,
  `user_relationship` text NOT NULL,
  `status_id` int(11) DEFAULT NULL,
  `user_id` int(11) DEFAULT NULL
) ENGINE=InnoDB DEFAULT CHARSET=utf8mb4;

--
-- Indexes for dumped tables
--

--
-- Indexes for table `admin`
--
ALTER TABLE `admin`
  ADD PRIMARY KEY (`admin_id`);

--
-- Indexes for table `booking`
--
ALTER TABLE `booking`
  ADD PRIMARY KEY (`booking_id`),
  ADD KEY `caregiver_id` (`caregiver_id`),
  ADD KEY `user_id` (`user_id`),
  ADD KEY `client_id` (`client_id`),
  ADD KEY `pay_id` (`pay_id`);

--
-- Indexes for table `caregiver`
--
ALTER TABLE `caregiver`
  ADD PRIMARY KEY (`care_id`),
  ADD KEY `state_id` (`state_id`);

--
-- Indexes for table `gender`
--
ALTER TABLE `gender`
  ADD PRIMARY KEY (`gender_id`);

--
-- Indexes for table `payment`
--
ALTER TABLE `payment`
  ADD PRIMARY KEY (`pay_id`),
  ADD KEY `pay_userid` (`pay_userid`),
  ADD KEY `pay_userclient_id` (`pay_userclient_id`);

--
-- Indexes for table `state`
--
ALTER TABLE `state`
  ADD PRIMARY KEY (`state_id`);

--
-- Indexes for table `status`
--
ALTER TABLE `status`
  ADD PRIMARY KEY (`status_id`);

--
-- Indexes for table `user`
--
ALTER TABLE `user`
  ADD PRIMARY KEY (`user_id`),
  ADD KEY `user_gender` (`user_gender`),
  ADD KEY `state_id` (`state_id`);

--
-- Indexes for table `userclient`
--
ALTER TABLE `userclient`
  ADD PRIMARY KEY (`client_id`),
  ADD KEY `client_gender` (`client_gender`),
  ADD KEY `status_id` (`status_id`),
  ADD KEY `user_id` (`user_id`);

--
-- AUTO_INCREMENT for dumped tables
--

--
-- AUTO_INCREMENT for table `admin`
--
ALTER TABLE `admin`
  MODIFY `admin_id` int(11) NOT NULL AUTO_INCREMENT, AUTO_INCREMENT=2;

--
-- AUTO_INCREMENT for table `booking`
--
ALTER TABLE `booking`
  MODIFY `booking_id` int(11) NOT NULL AUTO_INCREMENT;

--
-- AUTO_INCREMENT for table `caregiver`
--
ALTER TABLE `caregiver`
  MODIFY `care_id` int(11) NOT NULL AUTO_INCREMENT, AUTO_INCREMENT=13;

--
-- AUTO_INCREMENT for table `gender`
--
ALTER TABLE `gender`
  MODIFY `gender_id` int(11) NOT NULL AUTO_INCREMENT, AUTO_INCREMENT=3;

--
-- AUTO_INCREMENT for table `payment`
--
ALTER TABLE `payment`
  MODIFY `pay_id` int(11) NOT NULL AUTO_INCREMENT, AUTO_INCREMENT=23;

--
-- AUTO_INCREMENT for table `state`
--
ALTER TABLE `state`
  MODIFY `state_id` int(11) NOT NULL AUTO_INCREMENT, AUTO_INCREMENT=3;

--
-- AUTO_INCREMENT for table `status`
--
ALTER TABLE `status`
  MODIFY `status_id` int(11) NOT NULL AUTO_INCREMENT, AUTO_INCREMENT=4;

--
-- AUTO_INCREMENT for table `user`
--
ALTER TABLE `user`
  MODIFY `user_id` int(11) NOT NULL AUTO_INCREMENT, AUTO_INCREMENT=28;

--
-- AUTO_INCREMENT for table `userclient`
--
ALTER TABLE `userclient`
  MODIFY `client_id` int(11) NOT NULL AUTO_INCREMENT, AUTO_INCREMENT=23;

--
-- Constraints for dumped tables
--

--
-- Constraints for table `booking`
--
ALTER TABLE `booking`
  ADD CONSTRAINT `booking_ibfk_1` FOREIGN KEY (`caregiver_id`) REFERENCES `caregiver` (`care_id`),
  ADD CONSTRAINT `booking_ibfk_2` FOREIGN KEY (`user_id`) REFERENCES `user` (`user_id`),
  ADD CONSTRAINT `booking_ibfk_3` FOREIGN KEY (`client_id`) REFERENCES `userclient` (`client_id`),
  ADD CONSTRAINT `booking_ibfk_4` FOREIGN KEY (`pay_id`) REFERENCES `payment` (`pay_id`);

--
-- Constraints for table `caregiver`
--
ALTER TABLE `caregiver`
  ADD CONSTRAINT `caregiver_ibfk_1` FOREIGN KEY (`state_id`) REFERENCES `state` (`state_id`);

--
-- Constraints for table `payment`
--
ALTER TABLE `payment`
  ADD CONSTRAINT `payment_ibfk_1` FOREIGN KEY (`pay_userid`) REFERENCES `user` (`user_id`),
  ADD CONSTRAINT `payment_ibfk_2` FOREIGN KEY (`pay_userclient_id`) REFERENCES `userclient` (`client_id`);

--
-- Constraints for table `user`
--
ALTER TABLE `user`
  ADD CONSTRAINT `user_ibfk_1` FOREIGN KEY (`user_gender`) REFERENCES `gender` (`gender_id`),
  ADD CONSTRAINT `user_ibfk_2` FOREIGN KEY (`state_id`) REFERENCES `state` (`state_id`);

--
-- Constraints for table `userclient`
--
ALTER TABLE `userclient`
  ADD CONSTRAINT `userclient_ibfk_1` FOREIGN KEY (`client_gender`) REFERENCES `gender` (`gender_id`),
  ADD CONSTRAINT `userclient_ibfk_2` FOREIGN KEY (`status_id`) REFERENCES `status` (`status_id`),
  ADD CONSTRAINT `userclient_ibfk_3` FOREIGN KEY (`user_id`) REFERENCES `user` (`user_id`);
COMMIT;

/*!40101 SET CHARACTER_SET_CLIENT=@OLD_CHARACTER_SET_CLIENT */;
/*!40101 SET CHARACTER_SET_RESULTS=@OLD_CHARACTER_SET_RESULTS */;
/*!40101 SET COLLATION_CONNECTION=@OLD_COLLATION_CONNECTION */;
