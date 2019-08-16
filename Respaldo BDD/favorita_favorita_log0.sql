-- MySQL dump 10.13  Distrib 8.0.16, for Win64 (x86_64)
--
-- Host: localhost    Database: favorita
-- ------------------------------------------------------
-- Server version	8.0.16

/*!40101 SET @OLD_CHARACTER_SET_CLIENT=@@CHARACTER_SET_CLIENT */;
/*!40101 SET @OLD_CHARACTER_SET_RESULTS=@@CHARACTER_SET_RESULTS */;
/*!40101 SET @OLD_COLLATION_CONNECTION=@@COLLATION_CONNECTION */;
 SET NAMES utf8 ;
/*!40103 SET @OLD_TIME_ZONE=@@TIME_ZONE */;
/*!40103 SET TIME_ZONE='+00:00' */;
/*!40014 SET @OLD_UNIQUE_CHECKS=@@UNIQUE_CHECKS, UNIQUE_CHECKS=0 */;
/*!40014 SET @OLD_FOREIGN_KEY_CHECKS=@@FOREIGN_KEY_CHECKS, FOREIGN_KEY_CHECKS=0 */;
/*!40101 SET @OLD_SQL_MODE=@@SQL_MODE, SQL_MODE='NO_AUTO_VALUE_ON_ZERO' */;
/*!40111 SET @OLD_SQL_NOTES=@@SQL_NOTES, SQL_NOTES=0 */;

--
-- Table structure for table `favorita_log`
--

DROP TABLE IF EXISTS `favorita_log`;
/*!40101 SET @saved_cs_client     = @@character_set_client */;
 SET character_set_client = utf8mb4 ;
CREATE TABLE `favorita_log` (
  `id` int(11) NOT NULL AUTO_INCREMENT,
  `algorithm` varchar(2) NOT NULL,
  `selected` tinyint(1) DEFAULT NULL,
  `route_date` date NOT NULL,
  `parameter1` double DEFAULT NULL,
  `parameter2` double DEFAULT NULL,
  `parameter3` double DEFAULT NULL,
  `parameter4` double DEFAULT NULL,
  `parameter5` double DEFAULT NULL,
  `parameter6` double DEFAULT NULL,
  `distance_rate` double NOT NULL,
  `num_trucks_rate` double NOT NULL,
  `staff_cost_rate` double NOT NULL,
  `fuel_cost_rate` double NOT NULL,
  `delivery_time_rate` double NOT NULL,
  `total_time` int(11) DEFAULT NULL,
  `distance_result` double DEFAULT NULL,
  `num_trucks_result` double DEFAULT NULL,
  `staff_cost_result` double DEFAULT NULL,
  `fuel_cost_result` double DEFAULT NULL,
  `delivery_time_result` double DEFAULT NULL,
  `errors` longtext,
  `created_date` datetime(6) DEFAULT NULL,
  PRIMARY KEY (`id`)
) ENGINE=InnoDB DEFAULT CHARSET=utf8mb4 COLLATE=utf8mb4_0900_ai_ci;
/*!40101 SET character_set_client = @saved_cs_client */;

--
-- Dumping data for table `favorita_log`
--

LOCK TABLES `favorita_log` WRITE;
/*!40000 ALTER TABLE `favorita_log` DISABLE KEYS */;
/*!40000 ALTER TABLE `favorita_log` ENABLE KEYS */;
UNLOCK TABLES;
/*!40103 SET TIME_ZONE=@OLD_TIME_ZONE */;

/*!40101 SET SQL_MODE=@OLD_SQL_MODE */;
/*!40014 SET FOREIGN_KEY_CHECKS=@OLD_FOREIGN_KEY_CHECKS */;
/*!40014 SET UNIQUE_CHECKS=@OLD_UNIQUE_CHECKS */;
/*!40101 SET CHARACTER_SET_CLIENT=@OLD_CHARACTER_SET_CLIENT */;
/*!40101 SET CHARACTER_SET_RESULTS=@OLD_CHARACTER_SET_RESULTS */;
/*!40101 SET COLLATION_CONNECTION=@OLD_COLLATION_CONNECTION */;
/*!40111 SET SQL_NOTES=@OLD_SQL_NOTES */;

-- Dump completed on 2019-07-18  6:53:39
