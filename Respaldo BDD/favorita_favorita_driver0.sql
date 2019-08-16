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
-- Table structure for table `favorita_driver`
--

DROP TABLE IF EXISTS `favorita_driver`;
/*!40101 SET @saved_cs_client     = @@character_set_client */;
 SET character_set_client = utf8mb4 ;
CREATE TABLE `favorita_driver` (
  `id` int(11) NOT NULL AUTO_INCREMENT,
  `name` varchar(200) NOT NULL,
  `last_name` varchar(200) NOT NULL,
  `driver_hour_cost` double NOT NULL,
  `max_work_extra_time` time(6) NOT NULL,
  `max_work_time` time(6) NOT NULL,
  `driver_license_id` int(11) DEFAULT NULL,
  PRIMARY KEY (`id`),
  KEY `favorita_driver_driver_license_id_e646d9e8_fk_favorita_` (`driver_license_id`),
  CONSTRAINT `favorita_driver_driver_license_id_e646d9e8_fk_favorita_` FOREIGN KEY (`driver_license_id`) REFERENCES `favorita_driverlicense` (`id`)
) ENGINE=InnoDB AUTO_INCREMENT=12 DEFAULT CHARSET=utf8mb4 COLLATE=utf8mb4_0900_ai_ci;
/*!40101 SET character_set_client = @saved_cs_client */;

--
-- Dumping data for table `favorita_driver`
--

LOCK TABLES `favorita_driver` WRITE;
/*!40000 ALTER TABLE `favorita_driver` DISABLE KEYS */;
INSERT INTO `favorita_driver` VALUES (1,'Juan José','Ponce',15,'04:00:00.000000','08:00:00.000000',1),(2,'Pedro Andres','Perez',16.5,'04:00:00.000000','08:00:00.000000',2),(3,'Alexis','Zambonino',18,'04:00:00.000000','08:00:00.000000',3),(4,'Juan Sebastián','Rodríguez',19,'04:00:00.000000','08:00:00.000000',4),(5,'Juan Sebastián','Atiaga',15,'04:00:00.000000','08:00:00.000000',2),(6,'David','Barrera',14,'04:00:00.000000','08:00:00.000000',1),(7,'Diana','Paredes',15.4,'04:00:00.000000','08:00:00.000000',1),(8,'María José','Lalama',16,'04:00:00.000000','08:00:00.000000',2),(9,'Yuya','Martinez',22.3,'04:00:00.000000','08:00:00.000000',4),(10,'Eva','Titpantuña',19.3,'04:00:00.000000','08:00:00.000000',3),(11,'Erick','Pazmiño',16.8,'04:00:00.000000','08:00:00.000000',2);
/*!40000 ALTER TABLE `favorita_driver` ENABLE KEYS */;
UNLOCK TABLES;
/*!40103 SET TIME_ZONE=@OLD_TIME_ZONE */;

/*!40101 SET SQL_MODE=@OLD_SQL_MODE */;
/*!40014 SET FOREIGN_KEY_CHECKS=@OLD_FOREIGN_KEY_CHECKS */;
/*!40014 SET UNIQUE_CHECKS=@OLD_UNIQUE_CHECKS */;
/*!40101 SET CHARACTER_SET_CLIENT=@OLD_CHARACTER_SET_CLIENT */;
/*!40101 SET CHARACTER_SET_RESULTS=@OLD_CHARACTER_SET_RESULTS */;
/*!40101 SET COLLATION_CONNECTION=@OLD_COLLATION_CONNECTION */;
/*!40111 SET SQL_NOTES=@OLD_SQL_NOTES */;

-- Dump completed on 2019-07-18  6:53:31
