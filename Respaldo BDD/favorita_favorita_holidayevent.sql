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
-- Table structure for table `favorita_holidayevent`
--

DROP TABLE IF EXISTS `favorita_holidayevent`;
/*!40101 SET @saved_cs_client     = @@character_set_client */;
 SET character_set_client = utf8mb4 ;
CREATE TABLE `favorita_holidayevent` (
  `id` int(11) NOT NULL AUTO_INCREMENT,
  `date` date NOT NULL,
  `description` varchar(200) NOT NULL,
  `transferred` tinyint(1) NOT NULL,
  `city_id` int(11) NOT NULL,
  `holiday_type_id` int(11) NOT NULL,
  `locale_id` int(11) NOT NULL,
  PRIMARY KEY (`id`),
  KEY `favorita_holidayevent_city_id_a4d91215_fk_favorita_city_id` (`city_id`),
  KEY `favorita_holidayeven_holiday_type_id_fa944287_fk_favorita_` (`holiday_type_id`),
  KEY `favorita_holidayeven_locale_id_5e89ef5f_fk_favorita_` (`locale_id`),
  CONSTRAINT `favorita_holidayeven_holiday_type_id_fa944287_fk_favorita_` FOREIGN KEY (`holiday_type_id`) REFERENCES `favorita_holidaytype` (`id`),
  CONSTRAINT `favorita_holidayeven_locale_id_5e89ef5f_fk_favorita_` FOREIGN KEY (`locale_id`) REFERENCES `favorita_holidaylocale` (`id`),
  CONSTRAINT `favorita_holidayevent_city_id_a4d91215_fk_favorita_city_id` FOREIGN KEY (`city_id`) REFERENCES `favorita_city` (`id`)
) ENGINE=InnoDB AUTO_INCREMENT=352 DEFAULT CHARSET=utf8mb4 COLLATE=utf8mb4_0900_ai_ci;
/*!40101 SET character_set_client = @saved_cs_client */;

--
-- Dumping data for table `favorita_holidayevent`
--

LOCK TABLES `favorita_holidayevent` WRITE;
/*!40000 ALTER TABLE `favorita_holidayevent` DISABLE KEYS */;
INSERT INTO `favorita_holidayevent` VALUES (1,'2012-03-02','Fundacion de 21',0,21,1,1),(2,'2012-04-01','Provincializacion de 4',0,4,1,2),(3,'2012-04-12','Fundacion de 17',0,17,1,1),(4,'2012-04-14','Cantonizacion de 16',0,16,1,1),(5,'2012-04-21','Cantonizacion de 5',0,5,1,1),(6,'2012-05-12','Cantonizacion del 8',0,8,1,1),(7,'2012-06-23','Cantonizacion de 7',0,7,1,1),(8,'2012-06-25','Provincializacion de 5',0,5,1,2),(9,'2012-06-25','Cantonizacion de 4',0,4,1,1),(10,'2012-06-25','Fundacion de 19',0,19,1,1),(11,'2012-07-03','Fundacion de Santo Domingo',0,2,1,1),(12,'2012-07-03','Cantonizacion de 22',0,22,1,1),(13,'2012-07-23','Cantonizacion de 3',0,3,1,1),(14,'2012-08-05','Fundacion de 20',0,20,1,1),(15,'2012-08-10','Primer Grito de Independencia',0,23,1,3),(16,'2012-08-15','Fundacion de 5',0,5,1,1),(17,'2012-08-24','Fundacion de 9',0,9,1,1),(18,'2012-09-28','Fundacion de 6',0,6,1,1),(19,'2012-10-07','Cantonizacion de 14',0,14,1,1),(20,'2012-10-09','Independencia de 10',1,23,1,3),(21,'2012-10-12','Traslado Independencia de 10',0,23,2,3),(22,'2012-11-02','Dia de Difuntos',0,23,1,3),(23,'2012-11-03','Independencia de 17',0,23,1,3),(24,'2012-11-06','Provincializacion de Santo Domingo',0,2,1,2),(25,'2012-11-07','Provincializacion 10',0,10,1,2),(26,'2012-11-10','Independencia de 7',0,7,1,1),(27,'2012-11-11','Independencia de 4',0,4,1,1),(28,'2012-11-12','Independencia de 9',0,9,1,1),(29,'2012-12-05','Fundacion de Quito-1',0,1,3,1),(30,'2012-12-06','Fundacion de Quito',0,1,1,1),(31,'2012-12-08','Fundacion de 18',0,18,1,1),(32,'2012-12-21','Navidad-4',0,23,3,3),(33,'2012-12-22','Cantonizacion de 11',0,11,1,1),(34,'2012-12-22','Navidad-3',0,23,3,3),(35,'2012-12-23','Navidad-2',0,23,3,3),(36,'2012-12-24','Puente Navidad',0,23,4,3),(37,'2012-12-24','Navidad-1',0,23,3,3),(38,'2012-12-25','Navidad',0,23,1,3),(39,'2012-12-26','Navidad+1',0,23,3,3),(40,'2012-12-31','Puente Primer dia del ano',0,23,4,3),(41,'2012-12-31','Primer dia del ano-1',0,23,3,3),(42,'2013-01-01','Primer dia del ano',0,23,1,3),(43,'2013-01-05','Recupero puente Navidad',0,23,5,3),(44,'2013-01-12','Recupero puente primer dia del ano',0,23,5,3),(45,'2013-02-11','Carnaval',0,23,1,3),(46,'2013-02-12','Carnaval',0,23,1,3),(47,'2013-03-02','Fundacion de 21',0,21,1,1),(48,'2013-04-01','Provincializacion de 4',0,4,1,2),(49,'2013-04-12','Fundacion de 17',0,17,1,1),(50,'2013-04-14','Cantonizacion de 16',0,16,1,1),(51,'2013-04-21','Cantonizacion de 5',0,5,1,1),(52,'2013-04-29','Viernes Santo',0,23,1,3),(53,'2013-05-01','Dia del Trabajo',0,23,1,3),(54,'2013-05-11','Dia de la Madre-1',0,23,3,3),(55,'2013-05-12','Cantonizacion del 8',0,8,1,1),(56,'2013-05-12','Dia de la Madre',0,23,6,3),(57,'2013-05-24','Batalla de Pichincha',0,23,1,3),(58,'2013-06-23','Cantonizacion de 7',0,7,1,1),(59,'2013-06-25','Provincializacion de 5',0,5,1,2),(60,'2013-06-25','Fundacion de 19',0,19,1,1),(61,'2013-06-25','Cantonizacion de 4',0,4,1,1),(62,'2013-07-03','Cantonizacion de 22',0,22,1,1),(63,'2013-07-03','Fundacion de Santo Domingo',0,2,1,1),(64,'2013-07-23','Cantonizacion de 3',0,3,1,1),(65,'2013-07-24','Fundacion de 10-1',0,10,3,1),(66,'2013-07-25','Fundacion de 10',0,10,1,1),(67,'2013-08-05','Fundacion de 20',0,20,1,1),(68,'2013-08-10','Primer Grito de Independencia',0,23,1,3),(69,'2013-08-15','Fundacion de 5',0,5,1,1),(70,'2013-08-24','Fundacion de 9',0,9,1,1),(71,'2013-09-28','Fundacion de 6',0,6,1,1),(72,'2013-10-07','Cantonizacion de 14',0,14,1,1),(73,'2013-10-09','Independencia de 10',1,23,1,3),(74,'2013-10-11','Traslado Independencia de 10',0,23,2,3),(75,'2013-11-02','Dia de Difuntos',0,23,1,3),(76,'2013-11-03','Independencia de 17',0,23,1,3),(77,'2013-11-06','Provincializacion de Santo Domingo',0,2,1,2),(78,'2013-11-07','Provincializacion 10',0,10,1,2),(79,'2013-11-10','Independencia de 7',0,7,1,1),(80,'2013-11-11','Independencia de 4',0,4,1,1),(81,'2013-11-12','Independencia de 9',0,9,1,1),(82,'2013-12-05','Fundacion de Quito-1',0,1,3,1),(83,'2013-12-06','Fundacion de Quito',0,1,1,1),(84,'2013-12-08','Fundacion de 18',0,18,1,1),(85,'2013-12-21','Navidad-4',0,23,3,3),(86,'2013-12-22','Navidad-3',0,23,3,3),(87,'2013-12-22','Cantonizacion de 11',0,11,1,1),(88,'2013-12-23','Navidad-2',0,23,3,3),(89,'2013-12-24','Navidad-1',0,23,3,3),(90,'2013-12-25','Navidad',0,23,1,3),(91,'2013-12-26','Navidad+1',0,23,3,3),(92,'2013-12-31','Primer dia del ano-1',0,23,3,3),(93,'2014-01-01','Primer dia del ano',0,23,1,3),(94,'2014-03-02','Fundacion de 21',0,21,1,1),(95,'2014-03-03','Carnaval',0,23,1,3),(96,'2014-03-04','Carnaval',0,23,1,3),(97,'2014-04-01','Provincializacion de 4',0,4,1,2),(98,'2014-04-12','Fundacion de 17',0,17,1,1),(99,'2014-04-14','Cantonizacion de 16',0,16,1,1),(100,'2014-04-18','Viernes Santo',0,23,1,3),(101,'2014-04-21','Cantonizacion de 5',0,5,1,1),(102,'2014-05-01','Dia del Trabajo',0,23,1,3),(103,'2014-05-10','Dia de la Madre-1',0,23,3,3),(104,'2014-05-11','Dia de la Madre',0,23,6,3),(105,'2014-05-12','Cantonizacion del 8',0,8,1,1),(106,'2014-05-24','Batalla de Pichincha',0,23,1,3),(107,'2014-06-12','Inauguracion Mundial de futbol Brasil',0,23,6,3),(108,'2014-06-15','Mundial de futbol Brasil: 23-Suiza',0,23,6,3),(109,'2014-06-20','Mundial de futbol Brasil: 23-Honduras',0,23,6,3),(110,'2014-06-23','Cantonizacion de 7',0,7,1,1),(111,'2014-06-25','Cantonizacion de 4',0,4,1,1),(112,'2014-06-25','Fundacion de 19',0,19,1,1),(113,'2014-06-25','Provincializacion de 5',0,5,1,2),(114,'2014-06-25','Mundial de futbol Brasil: 23-Francia',0,23,6,3),(115,'2014-06-28','Mundial de futbol Brasil: Octavos de Final',0,23,6,3),(116,'2014-06-29','Mundial de futbol Brasil: Octavos de Final',0,23,6,3),(117,'2014-06-30','Mundial de futbol Brasil: Octavos de Final',0,23,6,3),(118,'2014-07-01','Mundial de futbol Brasil: Octavos de Final',0,23,6,3),(119,'2014-07-03','Cantonizacion de 22',0,22,1,1),(120,'2014-07-03','Fundacion de Santo Domingo',0,2,1,1),(121,'2014-07-04','Mundial de futbol Brasil: Cuartos de Final',0,23,6,3),(122,'2014-07-05','Mundial de futbol Brasil: Cuartos de Final',0,23,6,3),(123,'2014-07-08','Mundial de futbol Brasil: Semifinales',0,23,6,3),(124,'2014-07-09','Mundial de futbol Brasil: Semifinales',0,23,6,3),(125,'2014-07-12','Mundial de futbol Brasil: Tercer y cuarto lugar',0,23,6,3),(126,'2014-07-13','Mundial de futbol Brasil: Final',0,23,6,3),(127,'2014-07-23','Cantonizacion de 3',0,3,1,1),(128,'2014-07-24','Fundacion de 10-1',0,10,3,1),(129,'2014-07-25','Fundacion de 10',0,10,1,1),(130,'2014-08-05','Fundacion de 20',0,20,1,1),(131,'2014-08-10','Primer Grito de Independencia',0,23,1,3),(132,'2014-08-15','Fundacion de 5',0,5,1,1),(133,'2014-08-24','Fundacion de 9',0,9,1,1),(134,'2014-09-28','Fundacion de 6',0,6,1,1),(135,'2014-10-07','Cantonizacion de 14',0,14,1,1),(136,'2014-10-09','Independencia de 10',1,23,1,3),(137,'2014-10-10','Traslado Independencia de 10',0,23,2,3),(138,'2014-11-02','Dia de Difuntos',0,23,1,3),(139,'2014-11-03','Independencia de 17',0,23,1,3),(140,'2014-11-06','Provincializacion de Santo Domingo',0,2,1,2),(141,'2014-11-07','Provincializacion 10',0,10,1,2),(142,'2014-11-10','Independencia de 7',0,7,1,1),(143,'2014-11-11','Independencia de 4',0,4,1,1),(144,'2014-11-12','Independencia de 9',0,9,1,1),(145,'2014-11-28','Black Friday',0,23,6,3),(146,'2014-12-01','Cyber Monday',0,23,6,3),(147,'2014-12-05','Fundacion de Quito-1',0,1,3,1),(148,'2014-12-06','Fundacion de Quito',0,1,1,1),(149,'2014-12-08','Fundacion de 18',0,18,1,1),(150,'2014-12-20','Recupero Puente Navidad',0,23,5,3),(151,'2014-12-21','Navidad-4',0,23,3,3),(152,'2014-12-22','Cantonizacion de 11',0,11,1,1),(153,'2014-12-22','Navidad-3',0,23,3,3),(154,'2014-12-23','Navidad-2',0,23,3,3),(155,'2014-12-24','Navidad-1',0,23,3,3),(156,'2014-12-25','Navidad',0,23,1,3),(157,'2014-12-26','Puente Navidad',0,23,4,3),(158,'2014-12-26','Navidad+1',0,23,3,3),(159,'2014-12-31','Primer dia del ano-1',0,23,3,3),(160,'2015-01-01','Primer dia del ano',0,23,1,3),(161,'2015-01-02','Puente Primer dia del ano',0,23,4,3),(162,'2015-01-10','Recupero Puente Primer dia del ano',0,23,5,3),(163,'2015-02-16','Carnaval',0,23,1,3),(164,'2015-02-17','Carnaval',0,23,1,3),(165,'2015-03-02','Fundacion de 21',0,21,1,1),(166,'2015-04-01','Provincializacion de 4',0,4,1,2),(167,'2015-04-03','Viernes Santo',0,23,1,3),(168,'2015-04-12','Fundacion de 17',0,17,1,1),(169,'2015-04-14','Cantonizacion de 16',0,16,1,1),(170,'2015-04-21','Cantonizacion de 5',0,5,1,1),(171,'2015-05-01','Dia del Trabajo',0,23,1,3),(172,'2015-05-09','Dia de la Madre-1',0,23,3,3),(173,'2015-05-10','Dia de la Madre',0,23,6,3),(174,'2015-05-12','Cantonizacion del 8',0,8,1,1),(175,'2015-05-24','Batalla de Pichincha',0,23,1,3),(176,'2015-06-23','Cantonizacion de 7',0,7,1,1),(177,'2015-06-25','Fundacion de 19',0,19,1,1),(178,'2015-06-25','Provincializacion de 5',0,5,1,2),(179,'2015-06-25','Cantonizacion de 4',0,4,1,1),(180,'2015-07-03','Cantonizacion de 22',0,22,1,1),(181,'2015-07-03','Fundacion de Santo Domingo',0,2,1,1),(182,'2015-07-23','Cantonizacion de 3',0,3,1,1),(183,'2015-07-24','Fundacion de 10-1',0,10,1,1),(184,'2015-07-25','Fundacion de 10',0,10,1,1),(185,'2015-08-05','Fundacion de 20',0,20,1,1),(186,'2015-08-10','Primer Grito de Independencia',0,23,1,3),(187,'2015-08-15','Fundacion de 5',0,5,1,1),(188,'2015-08-24','Fundacion de 9',0,9,1,1),(189,'2015-09-28','Fundacion de 6',0,6,1,1),(190,'2015-10-07','Cantonizacion de 14',0,14,1,1),(191,'2015-10-09','Independencia de 10',0,23,1,3),(192,'2015-11-02','Dia de Difuntos',0,23,1,3),(193,'2015-11-03','Independencia de 17',0,23,1,3),(194,'2015-11-06','Provincializacion de Santo Domingo',0,2,1,2),(195,'2015-11-07','Provincializacion 10',0,10,1,2),(196,'2015-11-10','Independencia de 7',0,7,1,1),(197,'2015-11-11','Independencia de 4',0,4,1,1),(198,'2015-11-12','Independencia de 9',0,9,1,1),(199,'2015-11-27','Black Friday',0,23,6,3),(200,'2015-11-30','Cyber Monday',0,23,6,3),(201,'2015-12-05','Fundacion de Quito-1',0,1,3,1),(202,'2015-12-06','Fundacion de Quito',0,1,1,1),(203,'2015-12-08','Fundacion de 18',0,18,1,1),(204,'2015-12-21','Navidad-4',0,23,3,3),(205,'2015-12-22','Navidad-3',0,23,3,3),(206,'2015-12-22','Cantonizacion de 11',0,11,1,1),(207,'2015-12-23','Navidad-2',0,23,3,3),(208,'2015-12-24','Navidad-1',0,23,3,3),(209,'2015-12-25','Navidad',0,23,1,3),(210,'2015-12-26','Navidad+1',0,23,3,3),(211,'2015-12-31','Primer dia del ano-1',0,23,3,3),(212,'2016-01-01','Primer dia del ano',0,23,1,3),(213,'2016-02-08','Carnaval',0,23,1,3),(214,'2016-02-09','Carnaval',0,23,1,3),(215,'2016-03-02','Fundacion de 21',0,21,1,1),(216,'2016-03-25','Viernes Santo',0,23,1,3),(217,'2016-04-01','Provincializacion de 4',0,4,1,2),(218,'2016-04-12','Fundacion de 17',0,17,1,1),(219,'2016-04-14','Cantonizacion de 16',0,16,1,1),(220,'2016-04-16','Terremoto Manabi',0,23,6,3),(221,'2016-04-17','Terremoto Manabi+1',0,23,6,3),(222,'2016-04-18','Terremoto Manabi+2',0,23,6,3),(223,'2016-04-19','Terremoto Manabi+3',0,23,6,3),(224,'2016-04-20','Terremoto Manabi+4',0,23,6,3),(225,'2016-04-21','Cantonizacion de 5',0,5,1,1),(226,'2016-04-21','Terremoto Manabi+5',0,23,6,3),(227,'2016-04-22','Terremoto Manabi+6',0,23,6,3),(228,'2016-04-23','Terremoto Manabi+7',0,23,6,3),(229,'2016-04-24','Terremoto Manabi+8',0,23,6,3),(230,'2016-04-25','Terremoto Manabi+9',0,23,6,3),(231,'2016-04-26','Terremoto Manabi+10',0,23,6,3),(232,'2016-04-27','Terremoto Manabi+11',0,23,6,3),(233,'2016-04-28','Terremoto Manabi+12',0,23,6,3),(234,'2016-04-29','Terremoto Manabi+13',0,23,6,3),(235,'2016-04-30','Terremoto Manabi+14',0,23,6,3),(236,'2016-05-01','Dia del Trabajo',0,23,1,3),(237,'2016-05-01','Terremoto Manabi+15',0,23,6,3),(238,'2016-05-02','Terremoto Manabi+16',0,23,6,3),(239,'2016-05-03','Terremoto Manabi+17',0,23,6,3),(240,'2016-05-04','Terremoto Manabi+18',0,23,6,3),(241,'2016-05-05','Terremoto Manabi+19',0,23,6,3),(242,'2016-05-06','Terremoto Manabi+20',0,23,6,3),(243,'2016-05-07','Dia de la Madre-1',0,23,3,3),(244,'2016-05-07','Terremoto Manabi+21',0,23,6,3),(245,'2016-05-08','Terremoto Manabi+22',0,23,6,3),(246,'2016-05-08','Dia de la Madre',0,23,6,3),(247,'2016-05-09','Terremoto Manabi+23',0,23,6,3),(248,'2016-05-10','Terremoto Manabi+24',0,23,6,3),(249,'2016-05-11','Terremoto Manabi+25',0,23,6,3),(250,'2016-05-12','Cantonizacion del 8',0,8,1,1),(251,'2016-05-12','Terremoto Manabi+26',0,23,6,3),(252,'2016-05-13','Terremoto Manabi+27',0,23,6,3),(253,'2016-05-14','Terremoto Manabi+28',0,23,6,3),(254,'2016-05-15','Terremoto Manabi+29',0,23,6,3),(255,'2016-05-16','Terremoto Manabi+30',0,23,6,3),(256,'2016-05-24','Batalla de Pichincha',1,23,1,3),(257,'2016-05-27','Traslado Batalla de Pichincha',0,23,2,3),(258,'2016-06-23','Cantonizacion de 7',0,7,1,1),(259,'2016-06-25','Fundacion de 19',0,19,1,1),(260,'2016-06-25','Provincializacion de 5',0,5,1,2),(261,'2016-06-25','Cantonizacion de 4',0,4,1,1),(262,'2016-07-03','Cantonizacion de 22',0,22,1,1),(263,'2016-07-03','Fundacion de Santo Domingo',0,2,1,1),(264,'2016-07-23','Cantonizacion de 3',0,3,1,1),(265,'2016-07-24','Fundacion de 10-1',0,10,3,1),(266,'2016-07-24','Traslado Fundacion de 10',0,10,2,1),(267,'2016-07-25','Fundacion de 10',1,10,1,1),(268,'2016-08-05','Fundacion de 20',0,20,1,1),(269,'2016-08-10','Primer Grito de Independencia',1,23,1,3),(270,'2016-08-12','Traslado Primer Grito de Independencia',0,23,2,3),(271,'2016-08-15','Fundacion de 5',0,5,1,1),(272,'2016-08-24','Fundacion de 9',0,9,1,1),(273,'2016-09-28','Fundacion de 6',0,6,1,1),(274,'2016-10-07','Cantonizacion de 14',0,14,1,1),(275,'2016-10-09','Independencia de 10',0,23,1,3),(276,'2016-11-02','Dia de Difuntos',0,23,1,3),(277,'2016-11-03','Independencia de 17',0,23,1,3),(278,'2016-11-04','Puente Dia de Difuntos',0,23,4,3),(279,'2016-11-06','Provincializacion de Santo Domingo',0,2,1,2),(280,'2016-11-07','Provincializacion 10',0,10,1,2),(281,'2016-11-10','Independencia de 7',0,7,1,1),(282,'2016-11-11','Independencia de 4',0,4,1,1),(283,'2016-11-12','Independencia de 9',0,9,1,1),(284,'2016-11-12','Recupero Puente Dia de Difuntos',0,23,5,3),(285,'2016-11-25','Black Friday',0,23,6,3),(286,'2016-11-28','Cyber Monday',0,23,6,3),(287,'2016-12-05','Fundacion de Quito-1',0,1,3,1),(288,'2016-12-06','Fundacion de Quito',0,1,1,1),(289,'2016-12-08','Fundacion de 18',0,18,1,1),(290,'2016-12-21','Navidad-4',0,23,3,3),(291,'2016-12-22','Navidad-3',0,23,3,3),(292,'2016-12-22','Cantonizacion de 11',0,11,1,1),(293,'2016-12-23','Navidad-2',0,23,3,3),(294,'2016-12-24','Navidad-1',0,23,3,3),(295,'2016-12-25','Navidad',0,23,1,3),(296,'2016-12-26','Navidad+1',0,23,3,3),(297,'2016-12-31','Primer dia del ano-1',0,23,3,3),(298,'2017-01-01','Primer dia del ano',1,23,1,3),(299,'2017-01-02','Traslado Primer dia del ano',0,23,2,3),(300,'2017-02-27','Carnaval',0,23,1,3),(301,'2017-02-28','Carnaval',0,23,1,3),(302,'2017-03-02','Fundacion de 21',0,21,1,1),(303,'2017-04-01','Provincializacion de 4',0,4,1,2),(304,'2017-04-12','Fundacion de 17',1,17,1,1),(305,'2017-04-13','Fundacion de 17',0,17,2,1),(306,'2017-04-14','Cantonizacion de 16',0,16,1,1),(307,'2017-04-14','Viernes Santo',0,23,1,3),(308,'2017-04-21','Cantonizacion de 5',0,5,1,1),(309,'2017-05-01','Dia del Trabajo',0,23,1,3),(310,'2017-05-12','Cantonizacion del 8',0,8,1,1),(311,'2017-05-13','Dia de la Madre-1',0,23,3,3),(312,'2017-05-14','Dia de la Madre',0,23,6,3),(313,'2017-05-24','Batalla de Pichincha',1,23,1,3),(314,'2017-05-26','Traslado Batalla de Pichincha',0,23,2,3),(315,'2017-06-23','Cantonizacion de 7',0,7,1,1),(316,'2017-06-25','Provincializacion de 5',0,5,1,2),(317,'2017-06-25','Cantonizacion de 4',0,4,1,1),(318,'2017-06-25','Fundacion de 19',0,19,1,1),(319,'2017-07-03','Cantonizacion de 22',0,22,1,1),(320,'2017-07-03','Fundacion de Santo Domingo',0,2,1,1),(321,'2017-07-23','Cantonizacion de 3',0,3,1,1),(322,'2017-07-24','Fundacion de 10-1',0,10,3,1),(323,'2017-07-25','Fundacion de 10',0,10,3,1),(324,'2017-08-05','Fundacion de 20',0,20,1,1),(325,'2017-08-10','Primer Grito de Independencia',1,23,1,3),(326,'2017-08-11','Traslado Primer Grito de Independencia',0,23,2,3),(327,'2017-08-15','Fundacion de 5',0,5,1,1),(328,'2017-08-24','Fundacion de 9',0,9,1,1),(329,'2017-09-28','Fundacion de 6',1,6,1,1),(330,'2017-09-29','Fundacion de 6',0,6,2,1),(331,'2017-10-07','Cantonizacion de 14',0,14,1,1),(332,'2017-10-09','Independencia de 10',0,23,1,3),(333,'2017-11-02','Dia de Difuntos',0,23,1,3),(334,'2017-11-03','Independencia de 17',0,23,1,3),(335,'2017-11-06','Provincializacion de Santo Domingo',0,2,1,2),(336,'2017-11-07','Provincializacion 10',0,10,1,2),(337,'2017-11-10','Independencia de 7',0,7,1,1),(338,'2017-11-11','Independencia de 4',0,4,1,1),(339,'2017-11-12','Independencia de 9',0,9,1,1),(340,'2017-12-05','Fundacion de Quito-1',0,1,3,1),(341,'2017-12-06','Fundacion de Quito',1,1,1,1),(342,'2017-12-08','Fundacion de 18',0,18,1,1),(343,'2017-12-08','Traslado Fundacion de Quito',0,1,2,1),(344,'2017-12-21','Navidad-4',0,23,3,3),(345,'2017-12-22','Cantonizacion de 11',0,11,1,1),(346,'2017-12-22','Navidad-3',0,23,3,3),(347,'2017-12-23','Navidad-2',0,23,3,3),(348,'2017-12-24','Navidad-1',0,23,3,3),(349,'2017-12-25','Navidad',0,23,1,3),(350,'2017-12-26','Navidad+1',0,23,3,3);
/*!40000 ALTER TABLE `favorita_holidayevent` ENABLE KEYS */;
UNLOCK TABLES;
/*!40103 SET TIME_ZONE=@OLD_TIME_ZONE */;

/*!40101 SET SQL_MODE=@OLD_SQL_MODE */;
/*!40014 SET FOREIGN_KEY_CHECKS=@OLD_FOREIGN_KEY_CHECKS */;
/*!40014 SET UNIQUE_CHECKS=@OLD_UNIQUE_CHECKS */;
/*!40101 SET CHARACTER_SET_CLIENT=@OLD_CHARACTER_SET_CLIENT */;
/*!40101 SET CHARACTER_SET_RESULTS=@OLD_CHARACTER_SET_RESULTS */;
/*!40101 SET COLLATION_CONNECTION=@OLD_COLLATION_CONNECTION */;
/*!40111 SET SQL_NOTES=@OLD_SQL_NOTES */;

-- Dump completed on 2019-07-10 20:48:00
