-- MySQL dump 10.13  Distrib 8.0.13, for Win64 (x86_64)
--
-- Host: localhost    Database: favorita
-- ------------------------------------------------------
-- Server version	8.0.13

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
-- Table structure for table `favorita_driverlicense_vehicle_type`
--

DROP TABLE IF EXISTS `favorita_driverlicense_vehicle_type`;
/*!40101 SET @saved_cs_client     = @@character_set_client */;
 SET character_set_client = utf8mb4 ;
CREATE TABLE `favorita_driverlicense_vehicle_type` (
  `id` int(11) NOT NULL AUTO_INCREMENT,
  `driverlicense_id` int(11) NOT NULL,
  `vehicletype_id` int(11) NOT NULL,
  PRIMARY KEY (`id`),
  UNIQUE KEY `favorita_driverlicense_v_driverlicense_id_vehicle_b4586b24_uniq` (`driverlicense_id`,`vehicletype_id`),
  KEY `favorita_driverlicen_vehicletype_id_9bf72498_fk_favorita_` (`vehicletype_id`),
  CONSTRAINT `favorita_driverlicen_driverlicense_id_792f391f_fk_favorita_` FOREIGN KEY (`driverlicense_id`) REFERENCES `favorita_driverlicense` (`id`),
  CONSTRAINT `favorita_driverlicen_vehicletype_id_9bf72498_fk_favorita_` FOREIGN KEY (`vehicletype_id`) REFERENCES `favorita_vehicletype` (`id`)
) ENGINE=InnoDB AUTO_INCREMENT=11 DEFAULT CHARSET=utf8mb4 COLLATE=utf8mb4_0900_ai_ci;
/*!40101 SET character_set_client = @saved_cs_client */;

--
-- Dumping data for table `favorita_driverlicense_vehicle_type`
--

LOCK TABLES `favorita_driverlicense_vehicle_type` WRITE;
/*!40000 ALTER TABLE `favorita_driverlicense_vehicle_type` DISABLE KEYS */;
INSERT INTO `favorita_driverlicense_vehicle_type` VALUES (1,1,3),(2,2,3),(3,2,4),(4,3,2),(5,3,3),(6,3,4),(7,4,1),(8,4,2),(9,4,3),(10,4,4);
/*!40000 ALTER TABLE `favorita_driverlicense_vehicle_type` ENABLE KEYS */;
UNLOCK TABLES;
/*!40103 SET TIME_ZONE=@OLD_TIME_ZONE */;

/*!40101 SET SQL_MODE=@OLD_SQL_MODE */;
/*!40014 SET FOREIGN_KEY_CHECKS=@OLD_FOREIGN_KEY_CHECKS */;
/*!40014 SET UNIQUE_CHECKS=@OLD_UNIQUE_CHECKS */;
/*!40101 SET CHARACTER_SET_CLIENT=@OLD_CHARACTER_SET_CLIENT */;
/*!40101 SET CHARACTER_SET_RESULTS=@OLD_CHARACTER_SET_RESULTS */;
/*!40101 SET COLLATION_CONNECTION=@OLD_COLLATION_CONNECTION */;
/*!40111 SET SQL_NOTES=@OLD_SQL_NOTES */;

-- Dump completed on 2019-07-10 20:48:07
