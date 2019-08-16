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
-- Table structure for table `django_migrations`
--

DROP TABLE IF EXISTS `django_migrations`;
/*!40101 SET @saved_cs_client     = @@character_set_client */;
 SET character_set_client = utf8mb4 ;
CREATE TABLE `django_migrations` (
  `id` int(11) NOT NULL AUTO_INCREMENT,
  `app` varchar(255) NOT NULL,
  `name` varchar(255) NOT NULL,
  `applied` datetime(6) NOT NULL,
  PRIMARY KEY (`id`)
) ENGINE=InnoDB AUTO_INCREMENT=56 DEFAULT CHARSET=utf8mb4 COLLATE=utf8mb4_0900_ai_ci;
/*!40101 SET character_set_client = @saved_cs_client */;

--
-- Dumping data for table `django_migrations`
--

LOCK TABLES `django_migrations` WRITE;
/*!40000 ALTER TABLE `django_migrations` DISABLE KEYS */;
INSERT INTO `django_migrations` VALUES (1,'contenttypes','0001_initial','2019-04-28 11:31:12.346238'),(2,'auth','0001_initial','2019-04-28 11:31:12.936660'),(3,'admin','0001_initial','2019-04-28 11:31:14.992164'),(4,'admin','0002_logentry_remove_auto_add','2019-04-28 11:31:15.472882'),(5,'admin','0003_logentry_add_action_flag_choices','2019-04-28 11:31:15.492825'),(6,'contenttypes','0002_remove_content_type_name','2019-04-28 11:31:15.878794'),(7,'auth','0002_alter_permission_name_max_length','2019-04-28 11:31:16.100203'),(8,'auth','0003_alter_user_email_max_length','2019-04-28 11:31:16.191956'),(9,'auth','0004_alter_user_username_opts','2019-04-28 11:31:16.215894'),(10,'auth','0005_alter_user_last_login_null','2019-04-28 11:31:16.543017'),(11,'auth','0006_require_contenttypes_0002','2019-04-28 11:31:16.552992'),(12,'auth','0007_alter_validators_add_error_messages','2019-04-28 11:31:16.563963'),(13,'auth','0008_alter_user_username_max_length','2019-04-28 11:31:16.802324'),(14,'auth','0009_alter_user_last_name_max_length','2019-04-28 11:31:17.007775'),(15,'auth','0010_alter_group_name_max_length','2019-04-28 11:31:17.046670'),(16,'auth','0011_update_proxy_permissions','2019-04-28 11:31:17.059636'),(17,'favorita','0001_initial','2019-04-28 11:31:17.158372'),(18,'favorita','0002_auto_20190427_1821','2019-04-28 11:31:17.201258'),(19,'favorita','0003_auto_20190427_1825','2019-04-28 11:31:17.396735'),(20,'favorita','0004_auto_20190427_1835','2019-04-28 11:31:18.999450'),(21,'favorita','0005_holidayevent_holidaylocale_holidaytype','2019-04-28 11:31:19.502106'),(22,'favorita','0006_classitem_familyitem_item','2019-04-28 11:31:20.494452'),(23,'favorita','0007_auto_20190427_2218','2019-04-28 11:31:21.186603'),(24,'favorita','0008_oil','2019-04-28 11:31:21.256415'),(25,'favorita','0009_salary','2019-04-28 11:31:21.416986'),(26,'favorita','0010_truck','2019-04-28 11:31:21.564591'),(27,'favorita','0011_transaction','2019-04-28 11:31:21.662331'),(28,'favorita','0012_auto_20190427_2333','2019-04-28 11:31:22.039323'),(29,'favorita','0013_delete_sale','2019-04-28 11:31:22.665647'),(30,'favorita','0014_sale','2019-04-28 11:31:22.767377'),(31,'favorita','0015_auto_20190428_1022','2019-04-28 11:31:23.234128'),(32,'sessions','0001_initial','2019-04-28 11:31:23.383731'),(33,'favorita','0016_auto_20190622_1851','2019-06-22 16:52:14.960676'),(34,'favorita','0017_auto_20190622_2224','2019-06-22 20:25:14.428257'),(35,'favorita','0018_auto_20190623_1003','2019-06-23 08:04:16.734989'),(36,'favorita','0019_auto_20190623_1107','2019-06-23 09:08:06.819600'),(37,'favorita','0016_auto_20190623_1145','2019-06-23 10:28:30.013457'),(38,'favorita','0017_auto_20190623_1225','2019-06-23 10:28:30.869458'),(39,'favorita','0018_auto_20190623_1332','2019-06-23 11:32:17.149844'),(40,'favorita','0019_auto_20190623_1333','2019-06-23 11:33:22.407843'),(41,'favorita','0020_auto_20190623_1716','2019-06-23 15:17:21.922061'),(42,'favorita','0021_auto_20190623_1717','2019-06-23 15:17:21.930058'),(43,'favorita','0022_results','2019-06-27 13:33:46.352577'),(44,'favorita','0023_auto_20190627_1917','2019-06-27 17:17:17.162042'),(45,'favorita','0024_auto_20190627_1920','2019-06-27 17:20:33.516512'),(46,'favorita','0023_auto_20190628_1937','2019-06-28 17:41:12.918957'),(47,'favorita','0024_auto_20190702_1437','2019-07-02 12:38:24.489969'),(48,'favorita','0024_auto_20190702_1439','2019-07-02 12:44:03.267858'),(49,'favorita','0025_auto_20190702_1954','2019-07-02 17:54:07.674377'),(50,'favorita','0026_configuration','2019-07-02 18:23:16.857054'),(51,'favorita','0027_vehicletype_km_per_galon','2019-07-03 21:09:47.957582'),(52,'favorita','0028_auto_20190704_0726','2019-07-04 05:26:05.953405'),(53,'favorita','0029_auto_20190704_0727','2019-07-04 05:27:22.511533'),(54,'favorita','0030_auto_20190704_0732','2019-07-04 05:32:21.784187'),(55,'favorita','0031_auto_20190710_0027','2019-07-09 22:27:54.526855');
/*!40000 ALTER TABLE `django_migrations` ENABLE KEYS */;
UNLOCK TABLES;
/*!40103 SET TIME_ZONE=@OLD_TIME_ZONE */;

/*!40101 SET SQL_MODE=@OLD_SQL_MODE */;
/*!40014 SET FOREIGN_KEY_CHECKS=@OLD_FOREIGN_KEY_CHECKS */;
/*!40014 SET UNIQUE_CHECKS=@OLD_UNIQUE_CHECKS */;
/*!40101 SET CHARACTER_SET_CLIENT=@OLD_CHARACTER_SET_CLIENT */;
/*!40101 SET CHARACTER_SET_RESULTS=@OLD_CHARACTER_SET_RESULTS */;
/*!40101 SET COLLATION_CONNECTION=@OLD_COLLATION_CONNECTION */;
/*!40111 SET SQL_NOTES=@OLD_SQL_NOTES */;

-- Dump completed on 2019-07-10 20:48:01
