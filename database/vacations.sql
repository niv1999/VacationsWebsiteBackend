-- phpMyAdmin SQL Dump
-- version 5.2.1
-- https://www.phpmyadmin.net/
--
-- Host: 127.0.0.1
-- Generation Time: Nov 21, 2023 at 06:43 PM
-- Server version: 10.4.28-MariaDB
-- PHP Version: 8.2.4

SET SQL_MODE = "NO_AUTO_VALUE_ON_ZERO";
START TRANSACTION;
SET time_zone = "+00:00";


/*!40101 SET @OLD_CHARACTER_SET_CLIENT=@@CHARACTER_SET_CLIENT */;
/*!40101 SET @OLD_CHARACTER_SET_RESULTS=@@CHARACTER_SET_RESULTS */;
/*!40101 SET @OLD_COLLATION_CONNECTION=@@COLLATION_CONNECTION */;
/*!40101 SET NAMES utf8mb4 */;

--
-- Database: `vacations`
--

-- --------------------------------------------------------

--
-- Table structure for table `countries`
--

CREATE TABLE `countries` (
  `country_id` int(11) NOT NULL,
  `country_name` varchar(60) NOT NULL
) ENGINE=InnoDB DEFAULT CHARSET=utf8mb4 COLLATE=utf8mb4_general_ci;

--
-- Dumping data for table `countries`
--

INSERT INTO `countries` (`country_id`, `country_name`) VALUES
(1, 'France'),
(2, 'Greece'),
(3, 'Iceland'),
(4, 'Indonesia'),
(5, 'Israel'),
(6, 'Italy'),
(7, 'Japan'),
(8, 'Kenya'),
(9, 'Maldives'),
(10, 'Switzerland');

-- --------------------------------------------------------

--
-- Table structure for table `likes`
--

CREATE TABLE `likes` (
  `user_id` int(11) NOT NULL,
  `vacation_id` int(11) NOT NULL
) ENGINE=InnoDB DEFAULT CHARSET=utf8mb4 COLLATE=utf8mb4_general_ci;

-- --------------------------------------------------------

--
-- Table structure for table `roles`
--

CREATE TABLE `roles` (
  `role_id` int(11) NOT NULL,
  `role_name` varchar(10) NOT NULL
) ENGINE=InnoDB DEFAULT CHARSET=utf8mb4 COLLATE=utf8mb4_general_ci;

--
-- Dumping data for table `roles`
--

INSERT INTO `roles` (`role_id`, `role_name`) VALUES
(1, 'Admin'),
(2, 'User');

-- --------------------------------------------------------

--
-- Table structure for table `users`
--

CREATE TABLE `users` (
  `user_id` int(11) NOT NULL,
  `first_name` varchar(30) NOT NULL,
  `last_name` varchar(50) NOT NULL,
  `email` varchar(50) NOT NULL,
  `password` varchar(20) NOT NULL,
  `role_id` int(11) NOT NULL
) ENGINE=InnoDB DEFAULT CHARSET=utf8mb4 COLLATE=utf8mb4_general_ci;

--
-- Dumping data for table `users`
--

INSERT INTO `users` (`user_id`, `first_name`, `last_name`, `email`, `password`, `role_id`) VALUES
(1, 'Assaf', 'Finkelstein', 'assaffink@gmail.com', '12345678', 1),
(2, 'Mor', 'Rubisa', 'mor.rubisa@gmail.com', 'nyb2017', 2),
(3, 'Niv', 'Shteingart', 'niv1999@gmail.com', '314830365niv', 2);

-- --------------------------------------------------------

--
-- Table structure for table `vacations`
--

CREATE TABLE `vacations` (
  `vacation_id` int(11) NOT NULL,
  `country_id` int(11) NOT NULL,
  `description` varchar(1500) NOT NULL,
  `start_date` date NOT NULL,
  `end_date` date NOT NULL,
  `price` decimal(7,2) NOT NULL,
  `file_name` varchar(100) NOT NULL
) ENGINE=InnoDB DEFAULT CHARSET=utf8mb4 COLLATE=utf8mb4_general_ci;

--
-- Dumping data for table `vacations`
--

INSERT INTO `vacations` (`vacation_id`, `country_id`, `description`, `start_date`, `end_date`, `price`, `file_name`) VALUES
(1, 9, 'Escape to the breathtaking Maldives for a week of sun, sea, and serenity. Indulge in luxurious overwater bungalows, pristine white-sand beaches, and vibrant coral reefs. This tropical paradise retreat offers the perfect blend of relaxation and adventure.', '2024-07-15', '2024-07-22', 2500.00, 'tropical_paradise_retreat'),
(2, 10, 'Embark on an exhilarating alpine adventure in the heart of Switzerland. Enjoy snow-covered landscapes, world-class skiing, and cozy chalets. This winter getaway promises a magical experience surrounded by stunning mountain scenery.', '2024-01-10', '2024-01-18', 3000.00, 'alpine_adventure_gateaway'),
(3, 6, 'Immerse yourself in the rich history of Rome with this cultural exploration. Visit iconic landmarks such as the Colosseum, Vatican City, and the Roman Forum. Indulge in authentic Italian cuisine while strolling through charming cobblestone streets.', '2024-04-05', '2024-04-12', 1800.00, 'hostoric_exploration_in_rome'),
(4, 2, 'Experience the beauty of Greece by hopping between its picturesque islands. Discover ancient ruins, crystal-clear waters, and traditional Greek hospitality. Each island offers a unique blend of history and natural splendor.', '2024-09-08', '2024-09-15', 2200.00, 'island_hopping_in_greece'),
(5, 4, 'Rejuvenate your mind and body with a serene spa retreat in Bali. Relax in luxurious resorts surrounded by lush landscapes, explore ancient temples, and indulge in traditional Balinese spa treatments for the ultimate wellness experience.', '2024-06-20', '2024-06-27', 2800.00, 'serene_spa_retreat_in_bali'),
(6, 2, 'Discover the coastal charm of Santorini with its stunning sunsets, whitewashed buildings, and azure waters. Explore the narrow streets of Oia, unwind on black sand beaches, and savor delicious Greek cuisine overlooking the Aegean Sea.', '2024-10-03', '2024-10-10', 2000.00, 'coastal_charm_in_santorini'),
(7, 8, 'Embark on a thrilling safari adventure in the wild landscapes of Kenya. Witness majestic wildlife, including lions, elephants, and giraffes, as you explore national parks and reserves. Stay in luxurious lodges for an unforgettable African experience.', '2024-08-12', '2024-08-20', 3500.00, 'safar_adventure_in_kenya'),
(8, 7, 'Immerse yourself in the vibrant city lights of Tokyo, Japan. Explore futuristic technology, traditional temples, and bustling markets. Indulge in sushi delights and experience the unique blend of modernity and tradition in this dynamic city.', '2024-11-07', '2024-11-14', 2400.00, 'city_lights_in_tokyo'),
(9, 6, 'Escape to the picturesque Amalfi Coast for a coastal retreat filled with breathtaking views, seaside villages, and delectable Italian cuisine. Relax on scenic beaches, explore cliffside towns, and soak in the Mediterranean charm.', '2024-05-15', '2024-05-22', 1900.00, 'coastal_retreat_in_amalfi'),
(10, 3, 'Experience the wonders of a Nordic winter in Iceland. Marvel at the Northern Lights, relax in geothermal hot springs, and explore glaciers and waterfalls. This winter wonderland promises an enchanting escape.', '2024-02-08', '2024-02-15', 2800.00, 'nordic_wonderland_in_iceland'),
(11, 7, 'Immerse yourself in the cultural odyssey of Kyoto, Japan. Explore historic temples, traditional tea houses, and beautiful cherry blossoms. Delight in the serene ambiance and rich traditions of this ancient city.', '2024-03-20', '2024-03-28', 2100.00, 'cultural_odyssey_in_kyoto'),
(12, 1, 'Indulge in coastal bliss on the French Riviera, where glamour meets the Mediterranean. Relax on glamorous beaches, explore charming coastal towns, and savor exquisite French cuisine. This chic and sun-soaked retreat offers the epitome of luxury.', '2024-07-05', '2024-07-12', 3200.00, 'coastal_bliss_in_french_riviera');

--
-- Indexes for dumped tables
--

--
-- Indexes for table `countries`
--
ALTER TABLE `countries`
  ADD PRIMARY KEY (`country_id`);

--
-- Indexes for table `likes`
--
ALTER TABLE `likes`
  ADD PRIMARY KEY (`user_id`,`vacation_id`),
  ADD KEY `vacation_id` (`vacation_id`);

--
-- Indexes for table `roles`
--
ALTER TABLE `roles`
  ADD PRIMARY KEY (`role_id`);

--
-- Indexes for table `users`
--
ALTER TABLE `users`
  ADD PRIMARY KEY (`user_id`),
  ADD KEY `role_id` (`role_id`);

--
-- Indexes for table `vacations`
--
ALTER TABLE `vacations`
  ADD PRIMARY KEY (`vacation_id`),
  ADD KEY `country_id` (`country_id`);

--
-- AUTO_INCREMENT for dumped tables
--

--
-- AUTO_INCREMENT for table `countries`
--
ALTER TABLE `countries`
  MODIFY `country_id` int(11) NOT NULL AUTO_INCREMENT, AUTO_INCREMENT=11;

--
-- AUTO_INCREMENT for table `roles`
--
ALTER TABLE `roles`
  MODIFY `role_id` int(11) NOT NULL AUTO_INCREMENT, AUTO_INCREMENT=3;

--
-- AUTO_INCREMENT for table `users`
--
ALTER TABLE `users`
  MODIFY `user_id` int(11) NOT NULL AUTO_INCREMENT, AUTO_INCREMENT=4;

--
-- AUTO_INCREMENT for table `vacations`
--
ALTER TABLE `vacations`
  MODIFY `vacation_id` int(11) NOT NULL AUTO_INCREMENT, AUTO_INCREMENT=13;

--
-- Constraints for dumped tables
--

--
-- Constraints for table `likes`
--
ALTER TABLE `likes`
  ADD CONSTRAINT `likes_ibfk_1` FOREIGN KEY (`vacation_id`) REFERENCES `vacations` (`vacation_id`) ON DELETE CASCADE ON UPDATE CASCADE,
  ADD CONSTRAINT `likes_ibfk_2` FOREIGN KEY (`user_id`) REFERENCES `users` (`user_id`);

--
-- Constraints for table `users`
--
ALTER TABLE `users`
  ADD CONSTRAINT `users_ibfk_1` FOREIGN KEY (`role_id`) REFERENCES `roles` (`role_id`);

--
-- Constraints for table `vacations`
--
ALTER TABLE `vacations`
  ADD CONSTRAINT `vacations_ibfk_1` FOREIGN KEY (`country_id`) REFERENCES `countries` (`country_id`);
COMMIT;

/*!40101 SET CHARACTER_SET_CLIENT=@OLD_CHARACTER_SET_CLIENT */;
/*!40101 SET CHARACTER_SET_RESULTS=@OLD_CHARACTER_SET_RESULTS */;
/*!40101 SET COLLATION_CONNECTION=@OLD_COLLATION_CONNECTION */;
