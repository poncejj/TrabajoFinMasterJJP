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
-- Table structure for table `auth_permission`
--

DROP TABLE IF EXISTS `auth_permission`;
/*!40101 SET @saved_cs_client     = @@character_set_client */;
 SET character_set_client = utf8mb4 ;
CREATE TABLE `auth_permission` (
  `id` int(11) NOT NULL AUTO_INCREMENT,
  `name` varchar(255) NOT NULL,
  `content_type_id` int(11) NOT NULL,
  `codename` varchar(100) NOT NULL,
  PRIMARY KEY (`id`),
  UNIQUE KEY `auth_permission_content_type_id_codename_01ab375a_uniq` (`content_type_id`,`codename`),
  CONSTRAINT `auth_permission_content_type_id_2f476e4b_fk_django_co` FOREIGN KEY (`content_type_id`) REFERENCES `django_content_type` (`id`)
) ENGINE=InnoDB AUTO_INCREMENT=113 DEFAULT CHARSET=utf8mb4 COLLATE=utf8mb4_0900_ai_ci;
/*!40101 SET character_set_client = @saved_cs_client */;

--
-- Dumping data for table `auth_permission`
--

LOCK TABLES `auth_permission` WRITE;
/*!40000 ALTER TABLE `auth_permission` DISABLE KEYS */;
INSERT INTO `auth_permission` VALUES (1,'Can add store',1,'add_store'),(2,'Can change store',1,'change_store'),(3,'Can delete store',1,'delete_store'),(4,'Can view store',1,'view_store'),(5,'Can add city',2,'add_city'),(6,'Can change city',2,'change_city'),(7,'Can delete city',2,'delete_city'),(8,'Can view city',2,'view_city'),(9,'Can add state',3,'add_state'),(10,'Can change state',3,'change_state'),(11,'Can delete state',3,'delete_state'),(12,'Can view state',3,'view_state'),(13,'Can add store type',4,'add_storetype'),(14,'Can change store type',4,'change_storetype'),(15,'Can delete store type',4,'delete_storetype'),(16,'Can view store type',4,'view_storetype'),(17,'Can add holiday locale',5,'add_holidaylocale'),(18,'Can change holiday locale',5,'change_holidaylocale'),(19,'Can delete holiday locale',5,'delete_holidaylocale'),(20,'Can view holiday locale',5,'view_holidaylocale'),(21,'Can add holiday type',6,'add_holidaytype'),(22,'Can change holiday type',6,'change_holidaytype'),(23,'Can delete holiday type',6,'delete_holidaytype'),(24,'Can view holiday type',6,'view_holidaytype'),(25,'Can add holiday event',7,'add_holidayevent'),(26,'Can change holiday event',7,'change_holidayevent'),(27,'Can delete holiday event',7,'delete_holidayevent'),(28,'Can view holiday event',7,'view_holidayevent'),(29,'Can add family item',8,'add_familyitem'),(30,'Can change family item',8,'change_familyitem'),(31,'Can delete family item',8,'delete_familyitem'),(32,'Can view family item',8,'view_familyitem'),(33,'Can add item',9,'add_item'),(34,'Can change item',9,'change_item'),(35,'Can delete item',9,'delete_item'),(36,'Can view item',9,'view_item'),(37,'Can add oil',10,'add_oil'),(38,'Can change oil',10,'change_oil'),(39,'Can delete oil',10,'delete_oil'),(40,'Can view oil',10,'view_oil'),(41,'Can add salary',11,'add_salary'),(42,'Can change salary',11,'change_salary'),(43,'Can delete salary',11,'delete_salary'),(44,'Can view salary',11,'view_salary'),(45,'Can add truck',12,'add_truck'),(46,'Can change truck',12,'change_truck'),(47,'Can delete truck',12,'delete_truck'),(48,'Can view truck',12,'view_truck'),(49,'Can add transaction',13,'add_transaction'),(50,'Can change transaction',13,'change_transaction'),(51,'Can delete transaction',13,'delete_transaction'),(52,'Can view transaction',13,'view_transaction'),(53,'Can add sale',14,'add_sale'),(54,'Can change sale',14,'change_sale'),(55,'Can delete sale',14,'delete_sale'),(56,'Can view sale',14,'view_sale'),(57,'Can add log entry',15,'add_logentry'),(58,'Can change log entry',15,'change_logentry'),(59,'Can delete log entry',15,'delete_logentry'),(60,'Can view log entry',15,'view_logentry'),(61,'Can add permission',16,'add_permission'),(62,'Can change permission',16,'change_permission'),(63,'Can delete permission',16,'delete_permission'),(64,'Can view permission',16,'view_permission'),(65,'Can add group',17,'add_group'),(66,'Can change group',17,'change_group'),(67,'Can delete group',17,'delete_group'),(68,'Can view group',17,'view_group'),(69,'Can add user',18,'add_user'),(70,'Can change user',18,'change_user'),(71,'Can delete user',18,'delete_user'),(72,'Can view user',18,'view_user'),(73,'Can add content type',19,'add_contenttype'),(74,'Can change content type',19,'change_contenttype'),(75,'Can delete content type',19,'delete_contenttype'),(76,'Can view content type',19,'view_contenttype'),(77,'Can add session',20,'add_session'),(78,'Can change session',20,'change_session'),(79,'Can delete session',20,'delete_session'),(80,'Can view session',20,'view_session'),(81,'Can add driver',21,'add_driver'),(82,'Can change driver',21,'change_driver'),(83,'Can delete driver',21,'delete_driver'),(84,'Can view driver',21,'view_driver'),(85,'Can add vehicle',22,'add_vehicle'),(86,'Can change vehicle',22,'change_vehicle'),(87,'Can delete vehicle',22,'delete_vehicle'),(88,'Can view vehicle',22,'view_vehicle'),(89,'Can add vehicle type',23,'add_vehicletype'),(90,'Can change vehicle type',23,'change_vehicletype'),(91,'Can delete vehicle type',23,'delete_vehicletype'),(92,'Can view vehicle type',23,'view_vehicletype'),(93,'Can add results',24,'add_results'),(94,'Can change results',24,'change_results'),(95,'Can delete results',24,'delete_results'),(96,'Can view results',24,'view_results'),(97,'Can add log',25,'add_log'),(98,'Can change log',25,'change_log'),(99,'Can delete log',25,'delete_log'),(100,'Can view log',25,'view_log'),(101,'Can add fuel type',26,'add_fueltype'),(102,'Can change fuel type',26,'change_fueltype'),(103,'Can delete fuel type',26,'delete_fueltype'),(104,'Can view fuel type',26,'view_fueltype'),(105,'Can add configuration',27,'add_configuration'),(106,'Can change configuration',27,'change_configuration'),(107,'Can delete configuration',27,'delete_configuration'),(108,'Can view configuration',27,'view_configuration'),(109,'Can add driver license',28,'add_driverlicense'),(110,'Can change driver license',28,'change_driverlicense'),(111,'Can delete driver license',28,'delete_driverlicense'),(112,'Can view driver license',28,'view_driverlicense');
/*!40000 ALTER TABLE `auth_permission` ENABLE KEYS */;
UNLOCK TABLES;
/*!40103 SET TIME_ZONE=@OLD_TIME_ZONE */;

/*!40101 SET SQL_MODE=@OLD_SQL_MODE */;
/*!40014 SET FOREIGN_KEY_CHECKS=@OLD_FOREIGN_KEY_CHECKS */;
/*!40014 SET UNIQUE_CHECKS=@OLD_UNIQUE_CHECKS */;
/*!40101 SET CHARACTER_SET_CLIENT=@OLD_CHARACTER_SET_CLIENT */;
/*!40101 SET CHARACTER_SET_RESULTS=@OLD_CHARACTER_SET_RESULTS */;
/*!40101 SET COLLATION_CONNECTION=@OLD_COLLATION_CONNECTION */;
/*!40111 SET SQL_NOTES=@OLD_SQL_NOTES */;

-- Dump completed on 2019-07-10 20:47:58
