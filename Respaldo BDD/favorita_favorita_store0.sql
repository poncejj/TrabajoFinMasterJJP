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
-- Table structure for table `favorita_store`
--

DROP TABLE IF EXISTS `favorita_store`;
/*!40101 SET @saved_cs_client     = @@character_set_client */;
 SET character_set_client = utf8mb4 ;
CREATE TABLE `favorita_store` (
  `id` int(11) NOT NULL AUTO_INCREMENT,
  `city_id` int(11) NOT NULL,
  `store_type_id` int(11) NOT NULL,
  `cluster` int(11) NOT NULL,
  `location` varchar(200) NOT NULL,
  `close_hour` time(6) NOT NULL,
  `open_hour` time(6) NOT NULL,
  PRIMARY KEY (`id`),
  KEY `favorita_store_city_id_b75a2d47` (`city_id`),
  KEY `favorita_store_store_type_id_5e846d86` (`store_type_id`),
  CONSTRAINT `favorita_store_city_id_b75a2d47_fk_favorita_city_id` FOREIGN KEY (`city_id`) REFERENCES `favorita_city` (`id`),
  CONSTRAINT `favorita_store_store_type_id_5e846d86_fk_favorita_storetype_id` FOREIGN KEY (`store_type_id`) REFERENCES `favorita_storetype` (`id`)
) ENGINE=InnoDB AUTO_INCREMENT=63 DEFAULT CHARSET=utf8mb4 COLLATE=utf8mb4_0900_ai_ci;
/*!40101 SET character_set_client = @saved_cs_client */;

--
-- Dumping data for table `favorita_store`
--

LOCK TABLES `favorita_store` WRITE;
/*!40000 ALTER TABLE `favorita_store` DISABLE KEYS */;
INSERT INTO `favorita_store` VALUES (1,1,4,13,'(-0.1800503,-78.4803628)','22:00:00.000000','06:00:00.000000'),(2,1,4,13,'(-0.104177,-78.4929478)','22:00:00.000000','06:00:00.000000'),(3,1,4,8,'(-0.2508474,-78.5250348)','22:00:00.000000','06:00:00.000000'),(4,1,4,9,'(-0.2859509,-78.5454689)','22:00:00.000000','06:00:00.000000'),(5,2,4,4,'(-0.2523722,-79.1678399)','22:00:00.000000','06:00:00.000000'),(6,1,4,13,'(-0.3080687,-78.4532729)','22:00:00.000000','06:00:00.000000'),(7,1,4,8,'(-0.1979681,-78.4410095)','22:00:00.000000','06:00:00.000000'),(8,1,4,8,'(-0.2066792,-78.4893973)','22:00:00.000000','06:00:00.000000'),(9,1,2,6,'(-0.1966806,-78.5038161)','22:00:00.000000','06:00:00.000000'),(10,1,3,15,'(-0.0919246,-78.4766936)','22:00:00.000000','06:00:00.000000'),(11,3,2,6,'(0.0403424,-78.1475759)','22:00:00.000000','06:00:00.000000'),(12,4,3,15,'(-0.938345,-78.6213076)','22:00:00.000000','06:00:00.000000'),(13,4,3,15,'(-0.9401648,-78.61438)','22:00:00.000000','06:00:00.000000'),(14,5,3,7,'(-1.655851,-78.6671307)','22:00:00.000000','06:00:00.000000'),(15,6,3,15,'(0.3457668,-78.1380701)','22:00:00.000000','06:00:00.000000'),(16,2,3,3,'(-0.2548978,-79.1914052)','22:00:00.000000','06:00:00.000000'),(17,1,3,12,'(-0.1620481,-78.4999323)','22:00:00.000000','06:00:00.000000'),(18,1,2,16,'(-0.189943,-78.4894824)','22:00:00.000000','06:00:00.000000'),(19,7,3,15,'(-1.5928687,-79.0047586)','22:00:00.000000','06:00:00.000000'),(20,1,2,6,'(-0.1639467,-78.4695351)','22:00:00.000000','06:00:00.000000'),(21,2,2,6,'(-0.244118,-79.1745488)','22:00:00.000000','06:00:00.000000'),(22,8,3,7,'(-1.4859532,-78.007238)','22:00:00.000000','06:00:00.000000'),(23,9,4,9,'(-1.2653134,-78.6305833)','22:00:00.000000','06:00:00.000000'),(24,10,4,1,'(-2.1413573,-79.9110154)','22:00:00.000000','06:00:00.000000'),(25,11,4,1,'(-2.2213099,-80.9469949)','22:00:00.000000','06:00:00.000000'),(26,10,4,10,'(-2.155065,-79.8949599)','22:00:00.000000','06:00:00.000000'),(27,12,4,1,'(-2.0957955,-79.9390132)','22:00:00.000000','06:00:00.000000'),(28,10,5,10,'(-2.2293577,-79.900643)','22:00:00.000000','06:00:00.000000'),(29,10,5,10,'(-2.1736077,-79.9419338)','22:00:00.000000','06:00:00.000000'),(30,10,3,3,'(-2.1396331,-79.8668336)','22:00:00.000000','06:00:00.000000'),(31,13,2,10,'(-1.8044433,-79.5416414)','22:00:00.000000','06:00:00.000000'),(32,10,3,3,'(-2.1690398,-79.9189691)','22:00:00.000000','06:00:00.000000'),(33,14,3,3,'(-1.0321594,-79.4748203)','22:00:00.000000','06:00:00.000000'),(34,10,2,6,'(-2.072061,-79.8746367)','22:00:00.000000','06:00:00.000000'),(35,15,3,3,'(-2.1526688,-79.9076317)','22:00:00.000000','06:00:00.000000'),(36,16,5,10,'(-2.1453087,-79.8979908)','22:00:00.000000','06:00:00.000000'),(37,17,4,2,'(-2.9141413,-79.0305735)','22:00:00.000000','06:00:00.000000'),(38,18,4,4,'(-4.0126104,-79.2041838)','22:00:00.000000','06:00:00.000000'),(39,17,2,6,'(-2.9070684,-79.0062089)','22:00:00.000000','06:00:00.000000'),(40,19,3,3,'(-3.2710208,-79.9438653)','22:00:00.000000','06:00:00.000000'),(41,19,4,4,'(-3.2710206,-79.9591862)','22:00:00.000000','06:00:00.000000'),(42,17,4,2,'(-2.900513,-79.0168974)','22:00:00.000000','06:00:00.000000'),(43,20,5,10,'(0.9695775,-79.6538474)','22:00:00.000000','06:00:00.000000'),(44,1,1,5,'(-0.1774206,-78.4873095)','22:00:00.000000','06:00:00.000000'),(45,1,1,11,'(-0.1992173,-78.4879233)','22:00:00.000000','06:00:00.000000'),(46,1,1,14,'(-0.145794,-78.4939456)','22:00:00.000000','06:00:00.000000'),(47,1,1,14,'(-0.2504353,-78.5391869)','22:00:00.000000','06:00:00.000000'),(48,1,1,14,'(-0.1206524,-78.4947919)','22:00:00.000000','06:00:00.000000'),(49,1,1,11,'(-0.3162248,-78.5503434)','22:00:00.000000','06:00:00.000000'),(50,9,1,14,'(-1.2384283,-78.6358328)','22:00:00.000000','06:00:00.000000'),(51,10,1,17,'(-2.0496322,-79.9167234)','22:00:00.000000','06:00:00.000000'),(52,21,1,11,'(-0.9426926,-80.7347587)','22:00:00.000000','06:00:00.000000'),(53,21,4,13,'(-0.9753155,-80.7008666)','22:00:00.000000','06:00:00.000000'),(54,22,3,3,'(-1.0500043,-80.4662155)','22:00:00.000000','06:00:00.000000'),(55,1,6,0,'(-0.3553059,-78.4522125)','22:00:00.000000','06:00:00.000000');
/*!40000 ALTER TABLE `favorita_store` ENABLE KEYS */;
UNLOCK TABLES;
/*!40103 SET TIME_ZONE=@OLD_TIME_ZONE */;

/*!40101 SET SQL_MODE=@OLD_SQL_MODE */;
/*!40014 SET FOREIGN_KEY_CHECKS=@OLD_FOREIGN_KEY_CHECKS */;
/*!40014 SET UNIQUE_CHECKS=@OLD_UNIQUE_CHECKS */;
/*!40101 SET CHARACTER_SET_CLIENT=@OLD_CHARACTER_SET_CLIENT */;
/*!40101 SET CHARACTER_SET_RESULTS=@OLD_CHARACTER_SET_RESULTS */;
/*!40101 SET COLLATION_CONNECTION=@OLD_COLLATION_CONNECTION */;
/*!40111 SET SQL_NOTES=@OLD_SQL_NOTES */;

-- Dump completed on 2019-07-18  6:53:33
