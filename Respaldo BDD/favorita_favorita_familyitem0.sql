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
-- Table structure for table `favorita_familyitem`
--

DROP TABLE IF EXISTS `favorita_familyitem`;
/*!40101 SET @saved_cs_client     = @@character_set_client */;
 SET character_set_client = utf8mb4 ;
CREATE TABLE `favorita_familyitem` (
  `id` int(11) NOT NULL AUTO_INCREMENT,
  `name` varchar(200) NOT NULL,
  PRIMARY KEY (`id`)
) ENGINE=InnoDB AUTO_INCREMENT=35 DEFAULT CHARSET=utf8mb4 COLLATE=utf8mb4_0900_ai_ci;
/*!40101 SET character_set_client = @saved_cs_client */;

--
-- Dumping data for table `favorita_familyitem`
--

LOCK TABLES `favorita_familyitem` WRITE;
/*!40000 ALTER TABLE `favorita_familyitem` DISABLE KEYS */;
INSERT INTO `favorita_familyitem` VALUES (1,'GROCERY I'),(2,'CLEANING'),(3,'BREAD/BAKERY'),(4,'DELI'),(5,'POULTRY'),(6,'EGGS'),(7,'PERSONAL CARE'),(8,'LINGERIE'),(9,'BEVERAGES'),(10,'AUTOMOTIVE'),(11,'DAIRY'),(12,'GROCERY II'),(13,'MEATS'),(14,'FROZEN FOODS'),(15,'HOME APPLIANCES'),(16,'SEAFOOD'),(17,'PREPARED FOODS'),(18,'LIQUOR,WINE,BEER'),(19,'BEAUTY'),(20,'HARDWARE'),(21,'LAWN AND GARDEN'),(22,'PRODUCE'),(23,'HOME AND KITCHEN II'),(24,'HOME AND KITCHEN I'),(25,'MAGAZINES'),(26,'HOME CARE'),(27,'PET SUPPLIES'),(28,'BABY CARE'),(29,'SCHOOL AND OFFICE SUPPLIES'),(30,'PLAYERS AND ELECTRONICS'),(31,'CELEBRATION'),(32,'LADIESWEAR'),(33,'BOOKS');
/*!40000 ALTER TABLE `favorita_familyitem` ENABLE KEYS */;
UNLOCK TABLES;
/*!40103 SET TIME_ZONE=@OLD_TIME_ZONE */;

/*!40101 SET SQL_MODE=@OLD_SQL_MODE */;
/*!40014 SET FOREIGN_KEY_CHECKS=@OLD_FOREIGN_KEY_CHECKS */;
/*!40014 SET UNIQUE_CHECKS=@OLD_UNIQUE_CHECKS */;
/*!40101 SET CHARACTER_SET_CLIENT=@OLD_CHARACTER_SET_CLIENT */;
/*!40101 SET CHARACTER_SET_RESULTS=@OLD_CHARACTER_SET_RESULTS */;
/*!40101 SET COLLATION_CONNECTION=@OLD_COLLATION_CONNECTION */;
/*!40111 SET SQL_NOTES=@OLD_SQL_NOTES */;

-- Dump completed on 2019-07-18  6:53:34
