-- MySQL dump 10.13  Distrib 8.0.35, for Win64 (x86_64)
--
-- Host: localhost    Database: web_shop
-- ------------------------------------------------------
-- Server version	8.0.35

/*!40101 SET @OLD_CHARACTER_SET_CLIENT=@@CHARACTER_SET_CLIENT */;
/*!40101 SET @OLD_CHARACTER_SET_RESULTS=@@CHARACTER_SET_RESULTS */;
/*!40101 SET @OLD_COLLATION_CONNECTION=@@COLLATION_CONNECTION */;
/*!50503 SET NAMES utf8mb4 */;
/*!40103 SET @OLD_TIME_ZONE=@@TIME_ZONE */;
/*!40103 SET TIME_ZONE='+00:00' */;
/*!40014 SET @OLD_UNIQUE_CHECKS=@@UNIQUE_CHECKS, UNIQUE_CHECKS=0 */;
/*!40014 SET @OLD_FOREIGN_KEY_CHECKS=@@FOREIGN_KEY_CHECKS, FOREIGN_KEY_CHECKS=0 */;
/*!40101 SET @OLD_SQL_MODE=@@SQL_MODE, SQL_MODE='NO_AUTO_VALUE_ON_ZERO' */;
/*!40111 SET @OLD_SQL_NOTES=@@SQL_NOTES, SQL_NOTES=0 */;

--
-- Table structure for table `auth_group`
--

DROP TABLE IF EXISTS `auth_group`;
/*!40101 SET @saved_cs_client     = @@character_set_client */;
/*!50503 SET character_set_client = utf8mb4 */;
CREATE TABLE `auth_group` (
  `id` int NOT NULL AUTO_INCREMENT,
  `name` varchar(150) NOT NULL,
  PRIMARY KEY (`id`),
  UNIQUE KEY `name` (`name`)
) ENGINE=InnoDB DEFAULT CHARSET=utf8mb4 COLLATE=utf8mb4_0900_ai_ci;
/*!40101 SET character_set_client = @saved_cs_client */;

--
-- Dumping data for table `auth_group`
--

LOCK TABLES `auth_group` WRITE;
/*!40000 ALTER TABLE `auth_group` DISABLE KEYS */;
/*!40000 ALTER TABLE `auth_group` ENABLE KEYS */;
UNLOCK TABLES;

--
-- Table structure for table `auth_group_permissions`
--

DROP TABLE IF EXISTS `auth_group_permissions`;
/*!40101 SET @saved_cs_client     = @@character_set_client */;
/*!50503 SET character_set_client = utf8mb4 */;
CREATE TABLE `auth_group_permissions` (
  `id` bigint NOT NULL AUTO_INCREMENT,
  `group_id` int NOT NULL,
  `permission_id` int NOT NULL,
  PRIMARY KEY (`id`),
  UNIQUE KEY `auth_group_permissions_group_id_permission_id_0cd325b0_uniq` (`group_id`,`permission_id`),
  KEY `auth_group_permissio_permission_id_84c5c92e_fk_auth_perm` (`permission_id`),
  CONSTRAINT `auth_group_permissio_permission_id_84c5c92e_fk_auth_perm` FOREIGN KEY (`permission_id`) REFERENCES `auth_permission` (`id`),
  CONSTRAINT `auth_group_permissions_group_id_b120cbf9_fk_auth_group_id` FOREIGN KEY (`group_id`) REFERENCES `auth_group` (`id`)
) ENGINE=InnoDB DEFAULT CHARSET=utf8mb4 COLLATE=utf8mb4_0900_ai_ci;
/*!40101 SET character_set_client = @saved_cs_client */;

--
-- Dumping data for table `auth_group_permissions`
--

LOCK TABLES `auth_group_permissions` WRITE;
/*!40000 ALTER TABLE `auth_group_permissions` DISABLE KEYS */;
/*!40000 ALTER TABLE `auth_group_permissions` ENABLE KEYS */;
UNLOCK TABLES;

--
-- Table structure for table `auth_permission`
--

DROP TABLE IF EXISTS `auth_permission`;
/*!40101 SET @saved_cs_client     = @@character_set_client */;
/*!50503 SET character_set_client = utf8mb4 */;
CREATE TABLE `auth_permission` (
  `id` int NOT NULL AUTO_INCREMENT,
  `name` varchar(255) NOT NULL,
  `content_type_id` int NOT NULL,
  `codename` varchar(100) NOT NULL,
  PRIMARY KEY (`id`),
  UNIQUE KEY `auth_permission_content_type_id_codename_01ab375a_uniq` (`content_type_id`,`codename`),
  CONSTRAINT `auth_permission_content_type_id_2f476e4b_fk_django_co` FOREIGN KEY (`content_type_id`) REFERENCES `django_content_type` (`id`)
) ENGINE=InnoDB AUTO_INCREMENT=157 DEFAULT CHARSET=utf8mb4 COLLATE=utf8mb4_0900_ai_ci;
/*!40101 SET character_set_client = @saved_cs_client */;

--
-- Dumping data for table `auth_permission`
--

LOCK TABLES `auth_permission` WRITE;
/*!40000 ALTER TABLE `auth_permission` DISABLE KEYS */;
INSERT INTO `auth_permission` VALUES (1,'Can add log entry',1,'add_logentry'),(2,'Can change log entry',1,'change_logentry'),(3,'Can delete log entry',1,'delete_logentry'),(4,'Can view log entry',1,'view_logentry'),(5,'Can add permission',2,'add_permission'),(6,'Can change permission',2,'change_permission'),(7,'Can delete permission',2,'delete_permission'),(8,'Can view permission',2,'view_permission'),(9,'Can add group',3,'add_group'),(10,'Can change group',3,'change_group'),(11,'Can delete group',3,'delete_group'),(12,'Can view group',3,'view_group'),(13,'Can add content type',4,'add_contenttype'),(14,'Can change content type',4,'change_contenttype'),(15,'Can delete content type',4,'delete_contenttype'),(16,'Can view content type',4,'view_contenttype'),(17,'Can add session',5,'add_session'),(18,'Can change session',5,'change_session'),(19,'Can delete session',5,'delete_session'),(20,'Can view session',5,'view_session'),(21,'Can add 鐢ㄦ埛',6,'add_user'),(22,'Can change 鐢ㄦ埛',6,'change_user'),(23,'Can delete 鐢ㄦ埛',6,'delete_user'),(24,'Can view 鐢ㄦ埛',6,'view_user'),(25,'Can add 鐪佸競鍖?,7,'add_area'),(26,'Can change 鐪佸競鍖?,7,'change_area'),(27,'Can delete 鐪佸競鍖?,7,'delete_area'),(28,'Can view 鐪佸競鍖?,7,'view_area'),(29,'Can add 楠岃瘉鐮?,8,'add_verifycode'),(30,'Can change 楠岃瘉鐮?,8,'change_verifycode'),(31,'Can delete 楠岃瘉鐮?,8,'delete_verifycode'),(32,'Can view 楠岃瘉鐮?,8,'view_verifycode'),(33,'Can add 鍦板潃',9,'add_address'),(34,'Can change 鍦板潃',9,'change_address'),(35,'Can delete 鍦板潃',9,'delete_address'),(36,'Can view 鍦板潃',9,'view_address'),(37,'Can add 鍏憡',10,'add_announcement'),(38,'Can change 鍏憡',10,'change_announcement'),(39,'Can delete 鍏憡',10,'delete_announcement'),(40,'Can view 鍏憡',10,'view_announcement'),(41,'Can add app閰嶇疆',11,'add_appconfiguration'),(42,'Can change app閰嶇疆',11,'change_appconfiguration'),(43,'Can delete app閰嶇疆',11,'delete_appconfiguration'),(44,'Can view app閰嶇疆',11,'view_appconfiguration'),(45,'Can add 杞挱鍥?,12,'add_carousel'),(46,'Can change 杞挱鍥?,12,'change_carousel'),(47,'Can delete 杞挱鍥?,12,'delete_carousel'),(48,'Can view 杞挱鍥?,12,'view_carousel'),(49,'Can add 閭閰嶇疆',13,'add_emailconfiguration'),(50,'Can change 閭閰嶇疆',13,'change_emailconfiguration'),(51,'Can delete 閭閰嶇疆',13,'delete_emailconfiguration'),(52,'Can view 閭閰嶇疆',13,'view_emailconfiguration'),(53,'Can add 棣栭〉閰嶇疆',14,'add_indexconfiguration'),(54,'Can change 棣栭〉閰嶇疆',14,'change_indexconfiguration'),(55,'Can delete 棣栭〉閰嶇疆',14,'delete_indexconfiguration'),(56,'Can view 棣栭〉閰嶇疆',14,'view_indexconfiguration'),(57,'Can add 绔欏唴淇?,15,'add_message'),(58,'Can change 绔欏唴淇?,15,'change_message'),(59,'Can delete 绔欏唴淇?,15,'delete_message'),(60,'Can view 绔欏唴淇?,15,'view_message'),(61,'Can add 绯荤粺閰嶇疆',16,'add_siteconfiguration'),(62,'Can change 绯荤粺閰嶇疆',16,'change_siteconfiguration'),(63,'Can delete 绯荤粺閰嶇疆',16,'delete_siteconfiguration'),(64,'Can view 绯荤粺閰嶇疆',16,'view_siteconfiguration'),(65,'Can add 寰俊閰嶇疆',17,'add_wechatconfiguration'),(66,'Can change 寰俊閰嶇疆',17,'change_wechatconfiguration'),(67,'Can delete 寰俊閰嶇疆',17,'delete_wechatconfiguration'),(68,'Can view 寰俊閰嶇疆',17,'view_wechatconfiguration'),(69,'Can add 涓汉涓績閰嶇疆',18,'add_usercenterconfiguration'),(70,'Can change 涓汉涓績閰嶇疆',18,'change_usercenterconfiguration'),(71,'Can delete 涓汉涓績閰嶇疆',18,'delete_usercenterconfiguration'),(72,'Can view 涓汉涓績閰嶇疆',18,'view_usercenterconfiguration'),(73,'Can add 鐭俊閰嶇疆',19,'add_smsconfiguration'),(74,'Can change 鐭俊閰嶇疆',19,'change_smsconfiguration'),(75,'Can delete 鐭俊閰嶇疆',19,'delete_smsconfiguration'),(76,'Can view 鐭俊閰嶇疆',19,'view_smsconfiguration'),(77,'Can add QQ閰嶇疆',20,'add_qqconfiguration'),(78,'Can change QQ閰嶇疆',20,'change_qqconfiguration'),(79,'Can delete QQ閰嶇疆',20,'delete_qqconfiguration'),(80,'Can view QQ閰嶇疆',20,'view_qqconfiguration'),(81,'Can add 涓冪墰浜戦厤缃?,21,'add_qiniuconfiguration'),(82,'Can change 涓冪墰浜戦厤缃?,21,'change_qiniuconfiguration'),(83,'Can delete 涓冪墰浜戦厤缃?,21,'delete_qiniuconfiguration'),(84,'Can view 涓冪墰浜戦厤缃?,21,'view_qiniuconfiguration'),(85,'Can add 瀛︽牎',22,'add_school'),(86,'Can change 瀛︽牎',22,'change_school'),(87,'Can delete 瀛︽牎',22,'delete_school'),(88,'Can view 瀛︽牎',22,'view_school'),(89,'Can add 瀛︽牎鏉冮檺鍏宠仈',23,'add_schooluserpermissions'),(90,'Can change 瀛︽牎鏉冮檺鍏宠仈',23,'change_schooluserpermissions'),(91,'Can delete 瀛︽牎鏉冮檺鍏宠仈',23,'delete_schooluserpermissions'),(92,'Can view 瀛︽牎鏉冮檺鍏宠仈',23,'view_schooluserpermissions'),(93,'Can add 鍟嗗搧杞挱鍥?,24,'add_goodsbanner'),(94,'Can change 鍟嗗搧杞挱鍥?,24,'change_goodsbanner'),(95,'Can delete 鍟嗗搧杞挱鍥?,24,'delete_goodsbanner'),(96,'Can view 鍟嗗搧杞挱鍥?,24,'view_goodsbanner'),(97,'Can add 鍟嗗搧鍒嗙被',25,'add_goodsgroup'),(98,'Can change 鍟嗗搧鍒嗙被',25,'change_goodsgroup'),(99,'Can delete 鍟嗗搧鍒嗙被',25,'delete_goodsgroup'),(100,'Can view 鍟嗗搧鍒嗙被',25,'view_goodsgroup'),(101,'Can add 鍟嗗搧',26,'add_goods'),(102,'Can change 鍟嗗搧',26,'change_goods'),(103,'Can delete 鍟嗗搧',26,'delete_goods'),(104,'Can view 鍟嗗搧',26,'view_goods'),(105,'Can add 娲诲姩',27,'add_activity'),(106,'Can change 娲诲姩',27,'change_activity'),(107,'Can delete 娲诲姩',27,'delete_activity'),(108,'Can view 娲诲姩',27,'view_activity'),(109,'Can add 娴忚绠＄悊',28,'add_activitybrowse'),(110,'Can change 娴忚绠＄悊',28,'change_activitybrowse'),(111,'Can delete 娴忚绠＄悊',28,'delete_activitybrowse'),(112,'Can view 娴忚绠＄悊',28,'view_activitybrowse'),(113,'Can add 鐢ㄦ埛绠＄悊',29,'add_activityuser'),(114,'Can change 鐢ㄦ埛绠＄悊',29,'change_activityuser'),(115,'Can delete 鐢ㄦ埛绠＄悊',29,'delete_activityuser'),(116,'Can view 鐢ㄦ埛绠＄悊',29,'view_activityuser'),(117,'Can add 浠ｅ彇蹇€掍换鍔?,30,'add_deliverytask'),(118,'Can change 浠ｅ彇蹇€掍换鍔?,30,'change_deliverytask'),(119,'Can delete 浠ｅ彇蹇€掍换鍔?,30,'delete_deliverytask'),(120,'Can view 浠ｅ彇蹇€掍换鍔?,30,'view_deliverytask'),(121,'Can add 璺戣吙浠诲姟',31,'add_errandtask'),(122,'Can change 璺戣吙浠诲姟',31,'change_errandtask'),(123,'Can delete 璺戣吙浠诲姟',31,'delete_errandtask'),(124,'Can view 璺戣吙浠诲姟',31,'view_errandtask'),(125,'Can add 浠诲姟',32,'add_task'),(126,'Can change 浠诲姟',32,'change_task'),(127,'Can delete 浠诲姟',32,'delete_task'),(128,'Can view 浠诲姟',32,'view_task'),(129,'Can add 浠诲姟鎺ュ彈鑰?,33,'add_taskuser'),(130,'Can change 浠诲姟鎺ュ彈鑰?,33,'change_taskuser'),(131,'Can delete 浠诲姟鎺ュ彈鑰?,33,'delete_taskuser'),(132,'Can view 浠诲姟鎺ュ彈鑰?,33,'view_taskuser'),(133,'Can add 闇€姹傝鍗?,34,'add_order'),(134,'Can change 闇€姹傝鍗?,34,'change_order'),(135,'Can delete 闇€姹傝鍗?,34,'delete_order'),(136,'Can view 闇€姹傝鍗?,34,'view_order'),(137,'Can add 鏂囩珷甯栧瓙',35,'add_article'),(138,'Can change 鏂囩珷甯栧瓙',35,'change_article'),(139,'Can delete 鏂囩珷甯栧瓙',35,'delete_article'),(140,'Can view 鏂囩珷甯栧瓙',35,'view_article'),(141,'Can add 璇勮',36,'add_articlecomment'),(142,'Can change 璇勮',36,'change_articlecomment'),(143,'Can delete 璇勮',36,'delete_articlecomment'),(144,'Can view 璇勮',36,'view_articlecomment'),(145,'Can add 鐐硅禐',37,'add_articlelike'),(146,'Can change 鐐硅禐',37,'change_articlelike'),(147,'Can delete 鐐硅禐',37,'delete_articlelike'),(148,'Can view 鐐硅禐',37,'view_articlelike'),(149,'Can add 娴忚',38,'add_articleview'),(150,'Can change 娴忚',38,'change_articleview'),(151,'Can delete 娴忚',38,'delete_articleview'),(152,'Can view 娴忚',38,'view_articleview'),(153,'Can add 鏂囦欢',39,'add_file'),(154,'Can change 鏂囦欢',39,'change_file'),(155,'Can delete 鏂囦欢',39,'delete_file'),(156,'Can view 鏂囦欢',39,'view_file');
/*!40000 ALTER TABLE `auth_permission` ENABLE KEYS */;
UNLOCK TABLES;

--
-- Table structure for table `demand_deliverytask`
--

DROP TABLE IF EXISTS `demand_deliverytask`;
/*!40101 SET @saved_cs_client     = @@character_set_client */;
/*!50503 SET character_set_client = utf8mb4 */;
CREATE TABLE `demand_deliverytask` (
  `id` bigint NOT NULL AUTO_INCREMENT,
  `create_time` datetime(6) NOT NULL,
  `update_time` datetime(6) NOT NULL,
  `is_delete` tinyint(1) NOT NULL,
  `package_size` varchar(50) NOT NULL,
  `package_image` varchar(100) DEFAULT NULL,
  `package_info` varchar(200) DEFAULT NULL,
  `pickup_location` varchar(200) DEFAULT NULL,
  `expected_time` varchar(50) NOT NULL,
  `gender` varchar(50) NOT NULL,
  `task_id` bigint NOT NULL,
  PRIMARY KEY (`id`),
  UNIQUE KEY `task_id` (`task_id`),
  CONSTRAINT `demand_deliverytask_task_id_42011894_fk_demand_task_id` FOREIGN KEY (`task_id`) REFERENCES `demand_task` (`id`)
) ENGINE=InnoDB DEFAULT CHARSET=utf8mb4 COLLATE=utf8mb4_0900_ai_ci;
/*!40101 SET character_set_client = @saved_cs_client */;

--
-- Dumping data for table `demand_deliverytask`
--

LOCK TABLES `demand_deliverytask` WRITE;
/*!40000 ALTER TABLE `demand_deliverytask` DISABLE KEYS */;
/*!40000 ALTER TABLE `demand_deliverytask` ENABLE KEYS */;
UNLOCK TABLES;

--
-- Table structure for table `demand_errandtask`
--

DROP TABLE IF EXISTS `demand_errandtask`;
/*!40101 SET @saved_cs_client     = @@character_set_client */;
/*!50503 SET character_set_client = utf8mb4 */;
CREATE TABLE `demand_errandtask` (
  `id` bigint NOT NULL AUTO_INCREMENT,
  `create_time` datetime(6) NOT NULL,
  `update_time` datetime(6) NOT NULL,
  `is_delete` tinyint(1) NOT NULL,
  `start_location` varchar(200) NOT NULL,
  `end_location` varchar(200) NOT NULL,
  `task_id` bigint NOT NULL,
  PRIMARY KEY (`id`),
  UNIQUE KEY `task_id` (`task_id`),
  CONSTRAINT `demand_errandtask_task_id_27b3d538_fk_demand_task_id` FOREIGN KEY (`task_id`) REFERENCES `demand_task` (`id`)
) ENGINE=InnoDB DEFAULT CHARSET=utf8mb4 COLLATE=utf8mb4_0900_ai_ci;
/*!40101 SET character_set_client = @saved_cs_client */;

--
-- Dumping data for table `demand_errandtask`
--

LOCK TABLES `demand_errandtask` WRITE;
/*!40000 ALTER TABLE `demand_errandtask` DISABLE KEYS */;
/*!40000 ALTER TABLE `demand_errandtask` ENABLE KEYS */;
UNLOCK TABLES;

--
-- Table structure for table `demand_task`
--

DROP TABLE IF EXISTS `demand_task`;
/*!40101 SET @saved_cs_client     = @@character_set_client */;
/*!50503 SET character_set_client = utf8mb4 */;
CREATE TABLE `demand_task` (
  `id` bigint NOT NULL AUTO_INCREMENT,
  `create_time` datetime(6) NOT NULL,
  `update_time` datetime(6) NOT NULL,
  `is_delete` tinyint(1) NOT NULL,
  `title` varchar(100) NOT NULL,
  `description` longtext NOT NULL,
  `type` varchar(50) NOT NULL,
  `status` varchar(50) NOT NULL,
  `created_at` datetime(6) NOT NULL,
  `commission` decimal(10,2) NOT NULL,
  `remark` longtext,
  `deadline` datetime(6) DEFAULT NULL,
  `creator_id` bigint NOT NULL,
  PRIMARY KEY (`id`),
  KEY `demand_task_creator_id_8e01f058_fk_ta_user_id` (`creator_id`),
  CONSTRAINT `demand_task_creator_id_8e01f058_fk_ta_user_id` FOREIGN KEY (`creator_id`) REFERENCES `ta_user` (`id`)
) ENGINE=InnoDB DEFAULT CHARSET=utf8mb4 COLLATE=utf8mb4_0900_ai_ci;
/*!40101 SET character_set_client = @saved_cs_client */;

--
-- Dumping data for table `demand_task`
--

LOCK TABLES `demand_task` WRITE;
/*!40000 ALTER TABLE `demand_task` DISABLE KEYS */;
/*!40000 ALTER TABLE `demand_task` ENABLE KEYS */;
UNLOCK TABLES;

--
-- Table structure for table `demand_taskuser`
--

DROP TABLE IF EXISTS `demand_taskuser`;
/*!40101 SET @saved_cs_client     = @@character_set_client */;
/*!50503 SET character_set_client = utf8mb4 */;
CREATE TABLE `demand_taskuser` (
  `id` bigint NOT NULL AUTO_INCREMENT,
  `create_time` datetime(6) NOT NULL,
  `update_time` datetime(6) NOT NULL,
  `is_delete` tinyint(1) NOT NULL,
  `accepted_at` datetime(6) NOT NULL,
  `task_id` bigint NOT NULL,
  `user_id` bigint NOT NULL,
  PRIMARY KEY (`id`),
  KEY `demand_taskuser_task_id_5f009562_fk_demand_task_id` (`task_id`),
  KEY `demand_taskuser_user_id_9c815bc9_fk_ta_user_id` (`user_id`),
  CONSTRAINT `demand_taskuser_task_id_5f009562_fk_demand_task_id` FOREIGN KEY (`task_id`) REFERENCES `demand_task` (`id`),
  CONSTRAINT `demand_taskuser_user_id_9c815bc9_fk_ta_user_id` FOREIGN KEY (`user_id`) REFERENCES `ta_user` (`id`)
) ENGINE=InnoDB DEFAULT CHARSET=utf8mb4 COLLATE=utf8mb4_0900_ai_ci;
/*!40101 SET character_set_client = @saved_cs_client */;

--
-- Dumping data for table `demand_taskuser`
--

LOCK TABLES `demand_taskuser` WRITE;
/*!40000 ALTER TABLE `demand_taskuser` DISABLE KEYS */;
/*!40000 ALTER TABLE `demand_taskuser` ENABLE KEYS */;
UNLOCK TABLES;

--
-- Table structure for table `django_admin_log`
--

DROP TABLE IF EXISTS `django_admin_log`;
/*!40101 SET @saved_cs_client     = @@character_set_client */;
/*!50503 SET character_set_client = utf8mb4 */;
CREATE TABLE `django_admin_log` (
  `id` int NOT NULL AUTO_INCREMENT,
  `action_time` datetime(6) NOT NULL,
  `object_id` longtext,
  `object_repr` varchar(200) NOT NULL,
  `action_flag` smallint unsigned NOT NULL,
  `change_message` longtext NOT NULL,
  `content_type_id` int DEFAULT NULL,
  `user_id` bigint NOT NULL,
  PRIMARY KEY (`id`),
  KEY `django_admin_log_content_type_id_c4bce8eb_fk_django_co` (`content_type_id`),
  KEY `django_admin_log_user_id_c564eba6_fk_ta_user_id` (`user_id`),
  CONSTRAINT `django_admin_log_content_type_id_c4bce8eb_fk_django_co` FOREIGN KEY (`content_type_id`) REFERENCES `django_content_type` (`id`),
  CONSTRAINT `django_admin_log_user_id_c564eba6_fk_ta_user_id` FOREIGN KEY (`user_id`) REFERENCES `ta_user` (`id`),
  CONSTRAINT `django_admin_log_chk_1` CHECK ((`action_flag` >= 0))
) ENGINE=InnoDB AUTO_INCREMENT=18 DEFAULT CHARSET=utf8mb4 COLLATE=utf8mb4_0900_ai_ci;
/*!40101 SET character_set_client = @saved_cs_client */;

--
-- Dumping data for table `django_admin_log`
--

LOCK TABLES `django_admin_log` WRITE;
/*!40000 ALTER TABLE `django_admin_log` DISABLE KEYS */;
INSERT INTO `django_admin_log` VALUES (1,'2023-11-20 05:08:41.748965','1','1',1,'[{\"added\": {}}]',39,1),(2,'2023-11-20 05:09:02.864367','1','閲嶅簡绉戞妧瀛﹂櫌',1,'[{\"added\": {}}]',22,1),(3,'2023-11-20 05:09:19.436052','1','123123',1,'[{\"added\": {}}]',35,1),(4,'2023-11-20 06:35:46.438688','1','娴嬭瘯',1,'[{\"added\": {}}]',12,1),(5,'2023-11-20 06:35:58.131135','2','娴嬭瘯2',1,'[{\"added\": {}}]',12,1),(6,'2023-11-20 06:36:37.160432','1','灏廜鏍″洯',2,'[{\"changed\": {\"fields\": [\"App\\u540d\\u79f0\", \"App\\u63cf\\u8ff0\", \"Applogo\"]}}, {\"added\": {\"name\": \"\\u9996\\u9875\\u914d\\u7f6e\", \"object\": \"\\u9996\\u9875\\u914d\\u7f6e\"}}]',11,1),(7,'2023-11-20 06:36:43.324677','1','灏廜鏍″洯',2,'[{\"added\": {\"name\": \"\\u4e2a\\u4eba\\u4e2d\\u5fc3\\u914d\\u7f6e\", \"object\": \"\\u4e2a\\u4eba\\u4e2d\\u5fc3\\u914d\\u7f6e\"}}]',11,1),(8,'2023-11-20 06:37:32.489153','1','灏廜鏍″洯',2,'[{\"changed\": {\"fields\": [\"\\u7cfb\\u7edf\\u540d\\u79f0\", \"\\u7cfb\\u7edfLOGO\", \"\\u7cfb\\u7edf\\u63cf\\u8ff0\", \"\\u7cfb\\u7edf\\u5907\\u6848\\u53f7\"]}}]',16,1),(9,'2023-11-20 06:38:51.038544','1','灏廜鏍″洯',2,'[{\"added\": {\"name\": \"\\u5fae\\u4fe1\\u914d\\u7f6e\", \"object\": \"\\u4fe1\\u7eb8\"}}, {\"added\": {\"name\": \"\\u90ae\\u7bb1\\u914d\\u7f6e\", \"object\": \"smtp.ym.163.com\"}}, {\"added\": {\"name\": \"\\u77ed\\u4fe1\\u914d\\u7f6e\", \"object\": \"1400740456\"}}, {\"added\": {\"name\": \"\\u4e03\\u725b\\u4e91\\u914d\\u7f6e\", \"object\": \"MlcQsURM35WJS1UONJ2gLerZfyvd1cryTw0atSz3\"}}]',16,1),(10,'2023-11-20 06:41:11.196524','1','灏廜鏍″洯',2,'[{\"changed\": {\"fields\": [\"\\u624b\\u673a\\u53f7\\u662f\\u5426\\u5fc5\\u7ed1\\u5b9a\", \"\\u90ae\\u7bb1\\u662f\\u5426\\u5fc5\\u7ed1\\u5b9a\", \"\\u5e16\\u5b50\\u662f\\u5426\\u9700\\u8981\\u5ba1\\u6838\"]}}]',11,1),(11,'2023-11-20 07:55:08.679731','1','姘存灉',1,'[{\"added\": {}}]',25,1),(12,'2023-11-20 08:01:37.641196','2','钄彍',1,'[{\"added\": {}}]',25,1),(13,'2023-11-20 08:02:00.784830','3','鐢靛瓙浜у搧',1,'[{\"added\": {}}]',25,1),(14,'2023-11-20 08:02:36.805694','1','娴嬭瘯',1,'[{\"added\": {}}]',26,1),(15,'2023-11-20 08:10:22.401648','33','2023/11/20/20231112_1699765597_3186.jpg',1,'[{\"added\": {}}]',39,1),(16,'2023-11-20 08:11:18.298843','34','2023/11/20/20231112_1699765636_8603.jpg',1,'[{\"added\": {}}]',39,1),(17,'2023-11-20 08:11:19.676976','1','娴嬭瘯',2,'[{\"added\": {\"name\": \"goods-file\\u5173\\u7cfb\", \"object\": \"Goods_images object (1)\"}}]',26,1);
/*!40000 ALTER TABLE `django_admin_log` ENABLE KEYS */;
UNLOCK TABLES;

--
-- Table structure for table `django_content_type`
--

DROP TABLE IF EXISTS `django_content_type`;
/*!40101 SET @saved_cs_client     = @@character_set_client */;
/*!50503 SET character_set_client = utf8mb4 */;
CREATE TABLE `django_content_type` (
  `id` int NOT NULL AUTO_INCREMENT,
  `app_label` varchar(100) NOT NULL,
  `model` varchar(100) NOT NULL,
  PRIMARY KEY (`id`),
  UNIQUE KEY `django_content_type_app_label_model_76bd3d3b_uniq` (`app_label`,`model`)
) ENGINE=InnoDB AUTO_INCREMENT=40 DEFAULT CHARSET=utf8mb4 COLLATE=utf8mb4_0900_ai_ci;
/*!40101 SET character_set_client = @saved_cs_client */;

--
-- Dumping data for table `django_content_type`
--

LOCK TABLES `django_content_type` WRITE;
/*!40000 ALTER TABLE `django_content_type` DISABLE KEYS */;
INSERT INTO `django_content_type` VALUES (27,'activity','activity'),(28,'activity','activitybrowse'),(29,'activity','activityuser'),(1,'admin','logentry'),(35,'article','article'),(36,'article','articlecomment'),(37,'article','articlelike'),(38,'article','articleview'),(3,'auth','group'),(2,'auth','permission'),(4,'contenttypes','contenttype'),(30,'demand','deliverytask'),(31,'demand','errandtask'),(32,'demand','task'),(33,'demand','taskuser'),(39,'file','file'),(10,'global_system','announcement'),(11,'global_system','appconfiguration'),(12,'global_system','carousel'),(13,'global_system','emailconfiguration'),(14,'global_system','indexconfiguration'),(15,'global_system','message'),(21,'global_system','qiniuconfiguration'),(20,'global_system','qqconfiguration'),(16,'global_system','siteconfiguration'),(19,'global_system','smsconfiguration'),(18,'global_system','usercenterconfiguration'),(17,'global_system','wechatconfiguration'),(26,'good','goods'),(24,'good','goodsbanner'),(25,'good','goodsgroup'),(34,'order','order'),(22,'school','school'),(23,'school','schooluserpermissions'),(5,'sessions','session'),(9,'user','address'),(7,'user','area'),(6,'user','user'),(8,'user','verifycode');
/*!40000 ALTER TABLE `django_content_type` ENABLE KEYS */;
UNLOCK TABLES;

--
-- Table structure for table `django_migrations`
--

DROP TABLE IF EXISTS `django_migrations`;
/*!40101 SET @saved_cs_client     = @@character_set_client */;
/*!50503 SET character_set_client = utf8mb4 */;
CREATE TABLE `django_migrations` (
  `id` bigint NOT NULL AUTO_INCREMENT,
  `app` varchar(255) NOT NULL,
  `name` varchar(255) NOT NULL,
  `applied` datetime(6) NOT NULL,
  PRIMARY KEY (`id`)
) ENGINE=InnoDB AUTO_INCREMENT=39 DEFAULT CHARSET=utf8mb4 COLLATE=utf8mb4_0900_ai_ci;
/*!40101 SET character_set_client = @saved_cs_client */;

--
-- Dumping data for table `django_migrations`
--

LOCK TABLES `django_migrations` WRITE;
/*!40000 ALTER TABLE `django_migrations` DISABLE KEYS */;
INSERT INTO `django_migrations` VALUES (1,'contenttypes','0001_initial','2023-11-20 05:06:41.598919'),(2,'contenttypes','0002_remove_content_type_name','2023-11-20 05:06:41.694861'),(3,'auth','0001_initial','2023-11-20 05:06:42.091311'),(4,'auth','0002_alter_permission_name_max_length','2023-11-20 05:06:42.206119'),(5,'auth','0003_alter_user_email_max_length','2023-11-20 05:06:42.212117'),(6,'auth','0004_alter_user_username_opts','2023-11-20 05:06:42.220388'),(7,'auth','0005_alter_user_last_login_null','2023-11-20 05:06:42.226396'),(8,'auth','0006_require_contenttypes_0002','2023-11-20 05:06:42.230396'),(9,'auth','0007_alter_validators_add_error_messages','2023-11-20 05:06:42.238410'),(10,'auth','0008_alter_user_username_max_length','2023-11-20 05:06:42.243410'),(11,'auth','0009_alter_user_last_name_max_length','2023-11-20 05:06:42.254411'),(12,'auth','0010_alter_group_name_max_length','2023-11-20 05:06:42.270275'),(13,'auth','0011_update_proxy_permissions','2023-11-20 05:06:42.276275'),(14,'auth','0012_alter_user_first_name_max_length','2023-11-20 05:06:42.282283'),(15,'school','0001_initial','2023-11-20 05:06:42.706437'),(16,'user','0001_initial','2023-11-20 05:06:43.479895'),(17,'activity','0001_initial','2023-11-20 05:06:43.671237'),(18,'activity','0002_initial','2023-11-20 05:06:44.081842'),(19,'admin','0001_initial','2023-11-20 05:06:44.293783'),(20,'admin','0002_logentry_remove_auto_add','2023-11-20 05:06:44.302783'),(21,'admin','0003_logentry_add_action_flag_choices','2023-11-20 05:06:44.310783'),(22,'file','0001_initial','2023-11-20 05:06:44.350190'),(23,'article','0001_initial','2023-11-20 05:06:44.533374'),(24,'article','0002_initial','2023-11-20 05:06:45.631235'),(25,'demand','0001_initial','2023-11-20 05:06:45.875609'),(26,'demand','0002_initial','2023-11-20 05:06:46.244984'),(27,'global_system','0001_initial','2023-11-20 05:06:47.063287'),(28,'global_system','0002_initial','2023-11-20 05:06:47.778627'),(29,'good','0001_initial','2023-11-20 05:06:47.948862'),(30,'good','0002_initial','2023-11-20 05:06:48.050996'),(31,'order','0001_initial','2023-11-20 05:06:48.083018'),(32,'order','0002_initial','2023-11-20 05:06:48.393227'),(33,'school','0002_initial','2023-11-20 05:06:48.514804'),(34,'sessions','0001_initial','2023-11-20 05:06:48.565082'),(35,'file','0002_alter_file_file','2023-11-20 08:06:34.012971'),(36,'good','0003_delete_goodsbanner','2023-11-20 08:06:34.051662'),(37,'user','0002_alter_user_sex','2023-11-20 08:06:34.066173'),(38,'good','0004_goods_images','2023-11-20 08:09:58.160728');
/*!40000 ALTER TABLE `django_migrations` ENABLE KEYS */;
UNLOCK TABLES;

--
-- Table structure for table `django_session`
--

DROP TABLE IF EXISTS `django_session`;
/*!40101 SET @saved_cs_client     = @@character_set_client */;
/*!50503 SET character_set_client = utf8mb4 */;
CREATE TABLE `django_session` (
  `session_key` varchar(40) NOT NULL,
  `session_data` longtext NOT NULL,
  `expire_date` datetime(6) NOT NULL,
  PRIMARY KEY (`session_key`),
  KEY `django_session_expire_date_a5c62663` (`expire_date`)
) ENGINE=InnoDB DEFAULT CHARSET=utf8mb4 COLLATE=utf8mb4_0900_ai_ci;
/*!40101 SET character_set_client = @saved_cs_client */;

--
-- Dumping data for table `django_session`
--

LOCK TABLES `django_session` WRITE;
/*!40000 ALTER TABLE `django_session` DISABLE KEYS */;
INSERT INTO `django_session` VALUES ('x0uy6oyiiypqv8ddyl0fncn1a2rnedf7','.eJzNmdtyozgQhl8l5etkzEEn5m53n2Gv1lMpIQmbCgcXgkylpvLuK0GyIYpsS4Ia9gYlUquhv78RLfnX7pEO_elxkKJ7LPnu-y7e3c_7csqeRKMHWFvXbfNND4mmLxntxbe_Btm39Z9vNp8mnqg8qVk54gTEoMAQopxmmUgp5KKABOMEcwgFhzklmOURIQzRNFZWhWCYkoJgkQPttBbNIJWvf34ddg2txWH3_e6wOxwGGCOiGwYi1eCcxroBETrs7pVFydpmsi1od1fQB1Z2rBLTYN1yUUk9_NntH-ezcpLFgGtfBRIOvoaumsb2lNdlsz9WbU6rR_kie1Hv6fmsJhflcehoX7bNfppEOf97mtcMVaV78k5Qzrqhzi3PtSDc1_u7RSG-_tDDouR6NI6ixHQ4PRvTDQB0ObCmaYeGCaV7_wWWyxxl_TbvdyH1ImDyTC3eMOXZ6JRA1YBCxIux1kJKehSuRN_NN4HpHb7JFNicsiLXjeDFyq-4LHvx_3rHF4RrooQW30S7OQwIUO0UomI5Q0a7Vn05Ktf8_M9-kwT1BmBSRWZHbFtTcoT0XUgSr_aBM9z6yybZqW2r9-aiWp_NPEQKjPkGPj91yE0xEAapfq0QjMbMwvo_EkGwlKiuns6iq0sp1UIiHQGbszbnHU7I1CIzO7Dl1khVlPpLIQq05psyd-uva1FWYrpcFPHDxF2x0FhvYPNSJY7Njuiye0zFegX6F7dQxGhMPpVn_hrRTu1lNP639qJSpqG3Xt4UbgJ1j9wUy1ZyIg50oUAyRpZzfC7FT2eWo_E2PJ1jNglaC8wo11Ur4TCkHDKgVOWTezaOxpsQdI_ZJGitK3MGxiYP2UYaUPSJxdUt5AX7TTi6R25yNCvJ2LY_RzzVmwGYULLqSjxzG6AX68vnsn_5-OOyVF9MPVQKjP0GRj-VbBXlfPXxFeUmy7xrf8prK8iFCRtxDSNhUs5sKxRMtFOUpHh9yrru9mA8mm9COJSCQTiJTOS2anwJ8mv7VpyOZY_yFKDdO_tOyCu7qk9W7koF47XsopyjNLWxLfzzB7N70xFfIXY9wz9MNmHlGp1JynrkiqN4LKqjRDdpGlKCTCgUgFsZpk22QeYbpsnOVvlmlLCpiBkfjEQhB0sjmGfRlcULU4vADYIzw004eodscoRmh-0EkOR0kgnCNVfSDEd6jUEMJMZN_GVrO67kmK4XJZsbucsVGr1NrsCITZGw2YHsqoGP3IBgzBSUkjH39LHYl3tKfU95KkXFH2jV3xQQC2Y5R5PvK558YO3xQgkz9Kf9sWuH85W65cPGS6ylQduWK6dATVHMM8PEVn5nsNBJgKej_PWqFAjGUxnAgn6za1s-Xq7UKDMbd3lCo7VVKM4RGjKk1h85Zt50rRuNp5oM54vo3chw03Bzjj6Rm1QTs8N2Fvt5AVwt24EQ6biS8jGUQugNSxbFyThWvG1fQt4ELmracNVUpfrWv_RUPl3W02bsoWkgGwvmdXiYgtpqrlXoOlHdkmYoMdvp4tyb_jRROCmla0ESRSHFz4zQ9Y2Sabg5zgAAJmNr6cO59k1iXKyVo6LrVOOUqTPTTQCHRm-SNavMNH39sXv9FzUYYmM:1r5czU:2dKJpeI1jwkOqZaQp3ZqGa6rir6M0IZYfTtMuifjV24','2023-12-06 02:29:24.377133');
/*!40000 ALTER TABLE `django_session` ENABLE KEYS */;
UNLOCK TABLES;

--
-- Table structure for table `global_system_announcement`
--

DROP TABLE IF EXISTS `global_system_announcement`;
/*!40101 SET @saved_cs_client     = @@character_set_client */;
/*!50503 SET character_set_client = utf8mb4 */;
CREATE TABLE `global_system_announcement` (
  `id` bigint NOT NULL AUTO_INCREMENT,
  `create_time` datetime(6) NOT NULL,
  `update_time` datetime(6) NOT NULL,
  `is_delete` tinyint(1) NOT NULL,
  `title` varchar(200) NOT NULL,
  `content` longtext NOT NULL,
  `detail` longtext,
  `notice_time` datetime(6) DEFAULT NULL,
  PRIMARY KEY (`id`)
) ENGINE=InnoDB DEFAULT CHARSET=utf8mb4 COLLATE=utf8mb4_0900_ai_ci;
/*!40101 SET character_set_client = @saved_cs_client */;

--
-- Dumping data for table `global_system_announcement`
--

LOCK TABLES `global_system_announcement` WRITE;
/*!40000 ALTER TABLE `global_system_announcement` DISABLE KEYS */;
/*!40000 ALTER TABLE `global_system_announcement` ENABLE KEYS */;
UNLOCK TABLES;

--
-- Table structure for table `global_system_appconfiguration`
--

DROP TABLE IF EXISTS `global_system_appconfiguration`;
/*!40101 SET @saved_cs_client     = @@character_set_client */;
/*!50503 SET character_set_client = utf8mb4 */;
CREATE TABLE `global_system_appconfiguration` (
  `id` bigint NOT NULL AUTO_INCREMENT,
  `app_name` varchar(200) NOT NULL,
  `app_description` longtext,
  `app_status` tinyint(1) NOT NULL,
  `app_logo` varchar(100) DEFAULT NULL,
  `app_bind_phone` tinyint(1) NOT NULL,
  `app_bind_email` tinyint(1) NOT NULL,
  `app_post_audit` tinyint(1) NOT NULL,
  `app_activity_audit` tinyint(1) NOT NULL,
  `app_idle_audit` tinyint(1) NOT NULL,
  `app_demand_audit` tinyint(1) NOT NULL,
  `app_comment_audit` tinyint(1) NOT NULL,
  `app_post_anonymous` tinyint(1) NOT NULL,
  `app_comment_anonymous` tinyint(1) NOT NULL,
  PRIMARY KEY (`id`)
) ENGINE=InnoDB AUTO_INCREMENT=2 DEFAULT CHARSET=utf8mb4 COLLATE=utf8mb4_0900_ai_ci;
/*!40101 SET character_set_client = @saved_cs_client */;

--
-- Dumping data for table `global_system_appconfiguration`
--

LOCK TABLES `global_system_appconfiguration` WRITE;
/*!40000 ALTER TABLE `global_system_appconfiguration` DISABLE KEYS */;
INSERT INTO `global_system_appconfiguration` VALUES (1,'灏廜鏍″洯','娴嬭瘯鐗?,1,'app/2023/11/20/20231031_1698740550_6823.jpg',0,0,0,1,1,1,1,1,1);
/*!40000 ALTER TABLE `global_system_appconfiguration` ENABLE KEYS */;
UNLOCK TABLES;

--
-- Table structure for table `global_system_carousel`
--

DROP TABLE IF EXISTS `global_system_carousel`;
/*!40101 SET @saved_cs_client     = @@character_set_client */;
/*!50503 SET character_set_client = utf8mb4 */;
CREATE TABLE `global_system_carousel` (
  `id` bigint NOT NULL AUTO_INCREMENT,
  `create_time` datetime(6) NOT NULL,
  `update_time` datetime(6) NOT NULL,
  `is_delete` tinyint(1) NOT NULL,
  `carousel_name` varchar(200) NOT NULL,
  `carousel_image` varchar(100) DEFAULT NULL,
  `carousel_link` varchar(200) DEFAULT NULL,
  `carousel_status` tinyint(1) NOT NULL,
  `carousel_order` int NOT NULL,
  PRIMARY KEY (`id`)
) ENGINE=InnoDB AUTO_INCREMENT=3 DEFAULT CHARSET=utf8mb4 COLLATE=utf8mb4_0900_ai_ci;
/*!40101 SET character_set_client = @saved_cs_client */;

--
-- Dumping data for table `global_system_carousel`
--

LOCK TABLES `global_system_carousel` WRITE;
/*!40000 ALTER TABLE `global_system_carousel` DISABLE KEYS */;
INSERT INTO `global_system_carousel` VALUES (1,'2023-11-20 06:35:46.435718','2023-11-20 06:35:46.436686',0,'娴嬭瘯','carousel/2023/11/20/20231031_1698740539_7082.jpg',NULL,1,0),(2,'2023-11-20 06:35:58.130135','2023-11-20 06:35:58.130135',0,'娴嬭瘯2','carousel/2023/11/20/20231031_1698740536_3342.jpg',NULL,1,0);
/*!40000 ALTER TABLE `global_system_carousel` ENABLE KEYS */;
UNLOCK TABLES;

--
-- Table structure for table `global_system_emailconfiguration`
--

DROP TABLE IF EXISTS `global_system_emailconfiguration`;
/*!40101 SET @saved_cs_client     = @@character_set_client */;
/*!50503 SET character_set_client = utf8mb4 */;
CREATE TABLE `global_system_emailconfiguration` (
  `id` bigint NOT NULL AUTO_INCREMENT,
  `email_host` varchar(200) DEFAULT NULL,
  `email_port` varchar(200) DEFAULT NULL,
  `email_host_user` varchar(200) DEFAULT NULL,
  `email_host_password` varchar(200) DEFAULT NULL,
  `email_use_ssl` tinyint(1) NOT NULL,
  `site_configuration_id` bigint NOT NULL,
  PRIMARY KEY (`id`),
  UNIQUE KEY `site_configuration_id` (`site_configuration_id`),
  CONSTRAINT `global_system_emailc_site_configuration_i_0a07d07c_fk_global_sy` FOREIGN KEY (`site_configuration_id`) REFERENCES `global_system_siteconfiguration` (`id`)
) ENGINE=InnoDB AUTO_INCREMENT=2 DEFAULT CHARSET=utf8mb4 COLLATE=utf8mb4_0900_ai_ci;
/*!40101 SET character_set_client = @saved_cs_client */;

--
-- Dumping data for table `global_system_emailconfiguration`
--

LOCK TABLES `global_system_emailconfiguration` WRITE;
/*!40000 ALTER TABLE `global_system_emailconfiguration` DISABLE KEYS */;
INSERT INTO `global_system_emailconfiguration` VALUES (1,'smtp.ym.163.com','465','max@tabz.work','LIpaoxiao0829',1,1);
/*!40000 ALTER TABLE `global_system_emailconfiguration` ENABLE KEYS */;
UNLOCK TABLES;

--
-- Table structure for table `global_system_indexconfiguration`
--

DROP TABLE IF EXISTS `global_system_indexconfiguration`;
/*!40101 SET @saved_cs_client     = @@character_set_client */;
/*!50503 SET character_set_client = utf8mb4 */;
CREATE TABLE `global_system_indexconfiguration` (
  `id` bigint NOT NULL AUTO_INCREMENT,
  `index_title` varchar(200) DEFAULT NULL,
  `index_description` longtext,
  `index_activity_bg` varchar(100) DEFAULT NULL,
  `index_idle_bg` varchar(100) DEFAULT NULL,
  `index_demand_bg` varchar(100) DEFAULT NULL,
  `index_demand_publish_bg` varchar(100) DEFAULT NULL,
  `index_ai_bg` varchar(100) DEFAULT NULL,
  `app_configuration_id` bigint NOT NULL,
  PRIMARY KEY (`id`),
  UNIQUE KEY `app_configuration_id` (`app_configuration_id`),
  CONSTRAINT `global_system_indexc_app_configuration_id_d99edf14_fk_global_sy` FOREIGN KEY (`app_configuration_id`) REFERENCES `global_system_appconfiguration` (`id`)
) ENGINE=InnoDB AUTO_INCREMENT=2 DEFAULT CHARSET=utf8mb4 COLLATE=utf8mb4_0900_ai_ci;
/*!40101 SET character_set_client = @saved_cs_client */;

--
-- Dumping data for table `global_system_indexconfiguration`
--

LOCK TABLES `global_system_indexconfiguration` WRITE;
/*!40000 ALTER TABLE `global_system_indexconfiguration` DISABLE KEYS */;
INSERT INTO `global_system_indexconfiguration` VALUES (1,'hi 鏃╁畨','姣忓ぉ閮藉揩涔愶紒锛侊紒','index/2023/11/20/20231112_1699765637_4120.jpg','index/2023/11/20/20231112_1699765631_9384.jpg','index/2023/11/20/20231112_1699765638_8044.jpg','index/2023/11/20/20231112_1699765660_7624.jpg','index/2023/11/20/20231112_1699765686_3395.jpg',1);
/*!40000 ALTER TABLE `global_system_indexconfiguration` ENABLE KEYS */;
UNLOCK TABLES;

--
-- Table structure for table `global_system_indexconfiguration_index_carousel`
--

DROP TABLE IF EXISTS `global_system_indexconfiguration_index_carousel`;
/*!40101 SET @saved_cs_client     = @@character_set_client */;
/*!50503 SET character_set_client = utf8mb4 */;
CREATE TABLE `global_system_indexconfiguration_index_carousel` (
  `id` bigint NOT NULL AUTO_INCREMENT,
  `indexconfiguration_id` bigint NOT NULL,
  `carousel_id` bigint NOT NULL,
  PRIMARY KEY (`id`),
  UNIQUE KEY `global_system_indexconfi_indexconfiguration_id_ca_66aa7870_uniq` (`indexconfiguration_id`,`carousel_id`),
  KEY `global_system_indexc_carousel_id_68cda2e3_fk_global_sy` (`carousel_id`),
  CONSTRAINT `global_system_indexc_carousel_id_68cda2e3_fk_global_sy` FOREIGN KEY (`carousel_id`) REFERENCES `global_system_carousel` (`id`),
  CONSTRAINT `global_system_indexc_indexconfiguration_i_ee9f170b_fk_global_sy` FOREIGN KEY (`indexconfiguration_id`) REFERENCES `global_system_indexconfiguration` (`id`)
) ENGINE=InnoDB AUTO_INCREMENT=3 DEFAULT CHARSET=utf8mb4 COLLATE=utf8mb4_0900_ai_ci;
/*!40101 SET character_set_client = @saved_cs_client */;

--
-- Dumping data for table `global_system_indexconfiguration_index_carousel`
--

LOCK TABLES `global_system_indexconfiguration_index_carousel` WRITE;
/*!40000 ALTER TABLE `global_system_indexconfiguration_index_carousel` DISABLE KEYS */;
INSERT INTO `global_system_indexconfiguration_index_carousel` VALUES (1,1,1),(2,1,2);
/*!40000 ALTER TABLE `global_system_indexconfiguration_index_carousel` ENABLE KEYS */;
UNLOCK TABLES;

--
-- Table structure for table `global_system_message`
--

DROP TABLE IF EXISTS `global_system_message`;
/*!40101 SET @saved_cs_client     = @@character_set_client */;
/*!50503 SET character_set_client = utf8mb4 */;
CREATE TABLE `global_system_message` (
  `id` bigint NOT NULL AUTO_INCREMENT,
  `create_time` datetime(6) NOT NULL,
  `update_time` datetime(6) NOT NULL,
  `is_delete` tinyint(1) NOT NULL,
  `subject` varchar(200) NOT NULL,
  `content` longtext NOT NULL,
  `message_type` varchar(10) NOT NULL,
  `related_id` int unsigned DEFAULT NULL,
  `is_read` tinyint(1) NOT NULL,
  `sender_id` bigint NOT NULL,
  PRIMARY KEY (`id`),
  KEY `global_system_message_sender_id_09ddb6e2_fk_ta_user_id` (`sender_id`),
  CONSTRAINT `global_system_message_sender_id_09ddb6e2_fk_ta_user_id` FOREIGN KEY (`sender_id`) REFERENCES `ta_user` (`id`),
  CONSTRAINT `global_system_message_chk_1` CHECK ((`related_id` >= 0))
) ENGINE=InnoDB DEFAULT CHARSET=utf8mb4 COLLATE=utf8mb4_0900_ai_ci;
/*!40101 SET character_set_client = @saved_cs_client */;

--
-- Dumping data for table `global_system_message`
--

LOCK TABLES `global_system_message` WRITE;
/*!40000 ALTER TABLE `global_system_message` DISABLE KEYS */;
/*!40000 ALTER TABLE `global_system_message` ENABLE KEYS */;
UNLOCK TABLES;

--
-- Table structure for table `global_system_message_recipients`
--

DROP TABLE IF EXISTS `global_system_message_recipients`;
/*!40101 SET @saved_cs_client     = @@character_set_client */;
/*!50503 SET character_set_client = utf8mb4 */;
CREATE TABLE `global_system_message_recipients` (
  `id` bigint NOT NULL AUTO_INCREMENT,
  `message_id` bigint NOT NULL,
  `user_id` bigint NOT NULL,
  PRIMARY KEY (`id`),
  UNIQUE KEY `global_system_message_re_message_id_user_id_1b60b596_uniq` (`message_id`,`user_id`),
  KEY `global_system_message_recipients_user_id_20ed0250_fk_ta_user_id` (`user_id`),
  CONSTRAINT `global_system_messag_message_id_d8c8eacc_fk_global_sy` FOREIGN KEY (`message_id`) REFERENCES `global_system_message` (`id`),
  CONSTRAINT `global_system_message_recipients_user_id_20ed0250_fk_ta_user_id` FOREIGN KEY (`user_id`) REFERENCES `ta_user` (`id`)
) ENGINE=InnoDB DEFAULT CHARSET=utf8mb4 COLLATE=utf8mb4_0900_ai_ci;
/*!40101 SET character_set_client = @saved_cs_client */;

--
-- Dumping data for table `global_system_message_recipients`
--

LOCK TABLES `global_system_message_recipients` WRITE;
/*!40000 ALTER TABLE `global_system_message_recipients` DISABLE KEYS */;
/*!40000 ALTER TABLE `global_system_message_recipients` ENABLE KEYS */;
UNLOCK TABLES;

--
-- Table structure for table `global_system_qiniuconfiguration`
--

DROP TABLE IF EXISTS `global_system_qiniuconfiguration`;
/*!40101 SET @saved_cs_client     = @@character_set_client */;
/*!50503 SET character_set_client = utf8mb4 */;
CREATE TABLE `global_system_qiniuconfiguration` (
  `id` bigint NOT NULL AUTO_INCREMENT,
  `qiniu_access_key` varchar(200) DEFAULT NULL,
  `qiniu_secret_key` varchar(200) DEFAULT NULL,
  `qiniu_bucket_name` varchar(200) DEFAULT NULL,
  `qiniu_bucket_domain` varchar(200) DEFAULT NULL,
  `qiniu_enable` tinyint(1) NOT NULL,
  `site_configuration_id` bigint NOT NULL,
  PRIMARY KEY (`id`),
  UNIQUE KEY `site_configuration_id` (`site_configuration_id`),
  CONSTRAINT `global_system_qiniuc_site_configuration_i_4ca982d2_fk_global_sy` FOREIGN KEY (`site_configuration_id`) REFERENCES `global_system_siteconfiguration` (`id`)
) ENGINE=InnoDB AUTO_INCREMENT=2 DEFAULT CHARSET=utf8mb4 COLLATE=utf8mb4_0900_ai_ci;
/*!40101 SET character_set_client = @saved_cs_client */;

--
-- Dumping data for table `global_system_qiniuconfiguration`
--

LOCK TABLES `global_system_qiniuconfiguration` WRITE;
/*!40000 ALTER TABLE `global_system_qiniuconfiguration` DISABLE KEYS */;
INSERT INTO `global_system_qiniuconfiguration` VALUES (1,'MlcQsURM35WJS1UONJ2gLerZfyvd1cryTw0atSz3','DMLOS432S_l8DBF6PFmRn9uau_i6VUl0phefDsq7','cloudreve-xiaohu','https://qiniu.tabz.work/',0,1);
/*!40000 ALTER TABLE `global_system_qiniuconfiguration` ENABLE KEYS */;
UNLOCK TABLES;

--
-- Table structure for table `global_system_qqconfiguration`
--

DROP TABLE IF EXISTS `global_system_qqconfiguration`;
/*!40101 SET @saved_cs_client     = @@character_set_client */;
/*!50503 SET character_set_client = utf8mb4 */;
CREATE TABLE `global_system_qqconfiguration` (
  `id` bigint NOT NULL AUTO_INCREMENT,
  `qq_appid` varchar(200) DEFAULT NULL,
  `qq_appkey` varchar(200) DEFAULT NULL,
  `site_configuration_id` bigint NOT NULL,
  PRIMARY KEY (`id`),
  UNIQUE KEY `site_configuration_id` (`site_configuration_id`),
  CONSTRAINT `global_system_qqconf_site_configuration_i_79d2b2c9_fk_global_sy` FOREIGN KEY (`site_configuration_id`) REFERENCES `global_system_siteconfiguration` (`id`)
) ENGINE=InnoDB DEFAULT CHARSET=utf8mb4 COLLATE=utf8mb4_0900_ai_ci;
/*!40101 SET character_set_client = @saved_cs_client */;

--
-- Dumping data for table `global_system_qqconfiguration`
--

LOCK TABLES `global_system_qqconfiguration` WRITE;
/*!40000 ALTER TABLE `global_system_qqconfiguration` DISABLE KEYS */;
/*!40000 ALTER TABLE `global_system_qqconfiguration` ENABLE KEYS */;
UNLOCK TABLES;

--
-- Table structure for table `global_system_siteconfiguration`
--

DROP TABLE IF EXISTS `global_system_siteconfiguration`;
/*!40101 SET @saved_cs_client     = @@character_set_client */;
/*!50503 SET character_set_client = utf8mb4 */;
CREATE TABLE `global_system_siteconfiguration` (
  `id` bigint NOT NULL AUTO_INCREMENT,
  `site_name` varchar(200) NOT NULL,
  `site_logo` varchar(100) DEFAULT NULL,
  `site_description` longtext,
  `site_icp` varchar(200) DEFAULT NULL,
  `site_status` tinyint(1) NOT NULL,
  PRIMARY KEY (`id`)
) ENGINE=InnoDB AUTO_INCREMENT=2 DEFAULT CHARSET=utf8mb4 COLLATE=utf8mb4_0900_ai_ci;
/*!40101 SET character_set_client = @saved_cs_client */;

--
-- Dumping data for table `global_system_siteconfiguration`
--

LOCK TABLES `global_system_siteconfiguration` WRITE;
/*!40000 ALTER TABLE `global_system_siteconfiguration` DISABLE KEYS */;
INSERT INTO `global_system_siteconfiguration` VALUES (1,'灏廜鏍″洯','site/2023/11/20/20231112_1699765632_4767.jpg','娴嬭瘯','娓漇DASA',1);
/*!40000 ALTER TABLE `global_system_siteconfiguration` ENABLE KEYS */;
UNLOCK TABLES;

--
-- Table structure for table `global_system_smsconfiguration`
--

DROP TABLE IF EXISTS `global_system_smsconfiguration`;
/*!40101 SET @saved_cs_client     = @@character_set_client */;
/*!50503 SET character_set_client = utf8mb4 */;
CREATE TABLE `global_system_smsconfiguration` (
  `id` bigint NOT NULL AUTO_INCREMENT,
  `tencent_sms_app_id` varchar(200) DEFAULT NULL,
  `tencent_sms_app_key` varchar(200) DEFAULT NULL,
  `tencent_sms_sign` varchar(200) DEFAULT NULL,
  `tencent_sms_template_id` varchar(200) DEFAULT NULL,
  `tencent_sms_secretid` varchar(200) DEFAULT NULL,
  `tencent_sms_secretkey` varchar(200) DEFAULT NULL,
  `site_configuration_id` bigint NOT NULL,
  PRIMARY KEY (`id`),
  UNIQUE KEY `site_configuration_id` (`site_configuration_id`),
  CONSTRAINT `global_system_smscon_site_configuration_i_cadea44d_fk_global_sy` FOREIGN KEY (`site_configuration_id`) REFERENCES `global_system_siteconfiguration` (`id`)
) ENGINE=InnoDB AUTO_INCREMENT=2 DEFAULT CHARSET=utf8mb4 COLLATE=utf8mb4_0900_ai_ci;
/*!40101 SET character_set_client = @saved_cs_client */;

--
-- Dumping data for table `global_system_smsconfiguration`
--

LOCK TABLES `global_system_smsconfiguration` WRITE;
/*!40000 ALTER TABLE `global_system_smsconfiguration` DISABLE KEYS */;
INSERT INTO `global_system_smsconfiguration` VALUES (1,'1400740456','1d2f79486e383269a90e4151c41f869a','灏廜鏍″洯鍏紬鍙?,'1566290','AKIDBjEYgcOwGLCpEON7ewiIivugEYKyVrzA','2ayBE4g4EAuSyISSJzRghT0KSO8e081g',1);
/*!40000 ALTER TABLE `global_system_smsconfiguration` ENABLE KEYS */;
UNLOCK TABLES;

--
-- Table structure for table `global_system_usercenterconfiguration`
--

DROP TABLE IF EXISTS `global_system_usercenterconfiguration`;
/*!40101 SET @saved_cs_client     = @@character_set_client */;
/*!50503 SET character_set_client = utf8mb4 */;
CREATE TABLE `global_system_usercenterconfiguration` (
  `id` bigint NOT NULL AUTO_INCREMENT,
  `user_center_vip` tinyint(1) NOT NULL,
  `user_center_wallet` tinyint(1) NOT NULL,
  `app_configuration_id` bigint NOT NULL,
  PRIMARY KEY (`id`),
  UNIQUE KEY `app_configuration_id` (`app_configuration_id`),
  CONSTRAINT `global_system_userce_app_configuration_id_d91e6f72_fk_global_sy` FOREIGN KEY (`app_configuration_id`) REFERENCES `global_system_appconfiguration` (`id`)
) ENGINE=InnoDB AUTO_INCREMENT=2 DEFAULT CHARSET=utf8mb4 COLLATE=utf8mb4_0900_ai_ci;
/*!40101 SET character_set_client = @saved_cs_client */;

--
-- Dumping data for table `global_system_usercenterconfiguration`
--

LOCK TABLES `global_system_usercenterconfiguration` WRITE;
/*!40000 ALTER TABLE `global_system_usercenterconfiguration` DISABLE KEYS */;
INSERT INTO `global_system_usercenterconfiguration` VALUES (1,1,1,1);
/*!40000 ALTER TABLE `global_system_usercenterconfiguration` ENABLE KEYS */;
UNLOCK TABLES;

--
-- Table structure for table `global_system_wechatconfiguration`
--

DROP TABLE IF EXISTS `global_system_wechatconfiguration`;
/*!40101 SET @saved_cs_client     = @@character_set_client */;
/*!50503 SET character_set_client = utf8mb4 */;
CREATE TABLE `global_system_wechatconfiguration` (
  `id` bigint NOT NULL AUTO_INCREMENT,
  `wechat_pay_mch_id` varchar(200) DEFAULT NULL,
  `wechat_pay_api_key` varchar(200) DEFAULT NULL,
  `wechat_name` varchar(200) NOT NULL,
  `wechat_qrcode` varchar(100) DEFAULT NULL,
  `wechat_appid` varchar(200) DEFAULT NULL,
  `wechat_appsecret` varchar(200) DEFAULT NULL,
  `wechat_token` varchar(200) DEFAULT NULL,
  `wechat_app_name` varchar(200) DEFAULT NULL,
  `wechat_app_appid` varchar(200) DEFAULT NULL,
  `wechat_app_appsecret` varchar(200) DEFAULT NULL,
  `site_configuration_id` bigint NOT NULL,
  PRIMARY KEY (`id`),
  UNIQUE KEY `site_configuration_id` (`site_configuration_id`),
  CONSTRAINT `global_system_wechat_site_configuration_i_a2d71bb6_fk_global_sy` FOREIGN KEY (`site_configuration_id`) REFERENCES `global_system_siteconfiguration` (`id`)
) ENGINE=InnoDB AUTO_INCREMENT=2 DEFAULT CHARSET=utf8mb4 COLLATE=utf8mb4_0900_ai_ci;
/*!40101 SET character_set_client = @saved_cs_client */;

--
-- Dumping data for table `global_system_wechatconfiguration`
--

LOCK TABLES `global_system_wechatconfiguration` WRITE;
/*!40000 ALTER TABLE `global_system_wechatconfiguration` DISABLE KEYS */;
INSERT INTO `global_system_wechatconfiguration` VALUES (1,'1620982159','cj9d8cjdh3ma9djs7zjd8ska7zj4ke7a','淇＄焊','wechat/2023/11/20/20231112_1699765625_2005.jpg','wx472cdcb7ed4e1d7f','9dfa5fb1d675192be82c7cd93dd3c333','pcfkufk63hglkf','淇＄焊','wx2f0318ada4cb186e','e2f918fb2b5acfc8c2a1b78f58a34a94',1);
/*!40000 ALTER TABLE `global_system_wechatconfiguration` ENABLE KEYS */;
UNLOCK TABLES;

--
-- Table structure for table `ta_activity`
--

DROP TABLE IF EXISTS `ta_activity`;
/*!40101 SET @saved_cs_client     = @@character_set_client */;
/*!50503 SET character_set_client = utf8mb4 */;
CREATE TABLE `ta_activity` (
  `id` bigint NOT NULL AUTO_INCREMENT,
  `create_time` datetime(6) NOT NULL,
  `update_time` datetime(6) NOT NULL,
  `name` varchar(20) NOT NULL,
  `address` varchar(50) NOT NULL,
  `start_time` datetime(6) NOT NULL,
  `end_time` datetime(6) NOT NULL,
  `number_limit` int NOT NULL,
  `detail` longtext,
  `status` tinyint(1) NOT NULL,
  `is_delete` tinyint(1) NOT NULL,
  `creator_id` bigint NOT NULL,
  PRIMARY KEY (`id`),
  KEY `ta_activity_creator_id_886665b2_fk_ta_user_id` (`creator_id`),
  CONSTRAINT `ta_activity_creator_id_886665b2_fk_ta_user_id` FOREIGN KEY (`creator_id`) REFERENCES `ta_user` (`id`)
) ENGINE=InnoDB DEFAULT CHARSET=utf8mb4 COLLATE=utf8mb4_0900_ai_ci;
/*!40101 SET character_set_client = @saved_cs_client */;

--
-- Dumping data for table `ta_activity`
--

LOCK TABLES `ta_activity` WRITE;
/*!40000 ALTER TABLE `ta_activity` DISABLE KEYS */;
/*!40000 ALTER TABLE `ta_activity` ENABLE KEYS */;
UNLOCK TABLES;

--
-- Table structure for table `ta_activity_browse`
--

DROP TABLE IF EXISTS `ta_activity_browse`;
/*!40101 SET @saved_cs_client     = @@character_set_client */;
/*!50503 SET character_set_client = utf8mb4 */;
CREATE TABLE `ta_activity_browse` (
  `id` bigint NOT NULL AUTO_INCREMENT,
  `create_time` datetime(6) NOT NULL,
  `update_time` datetime(6) NOT NULL,
  `is_delete` tinyint(1) NOT NULL,
  `activity_id` bigint NOT NULL,
  `user_id` bigint NOT NULL,
  PRIMARY KEY (`id`),
  KEY `ta_activity_browse_activity_id_909fe647_fk_ta_activity_id` (`activity_id`),
  KEY `ta_activity_browse_user_id_ab2d8a6e_fk_ta_user_id` (`user_id`),
  CONSTRAINT `ta_activity_browse_activity_id_909fe647_fk_ta_activity_id` FOREIGN KEY (`activity_id`) REFERENCES `ta_activity` (`id`),
  CONSTRAINT `ta_activity_browse_user_id_ab2d8a6e_fk_ta_user_id` FOREIGN KEY (`user_id`) REFERENCES `ta_user` (`id`)
) ENGINE=InnoDB DEFAULT CHARSET=utf8mb4 COLLATE=utf8mb4_0900_ai_ci;
/*!40101 SET character_set_client = @saved_cs_client */;

--
-- Dumping data for table `ta_activity_browse`
--

LOCK TABLES `ta_activity_browse` WRITE;
/*!40000 ALTER TABLE `ta_activity_browse` DISABLE KEYS */;
/*!40000 ALTER TABLE `ta_activity_browse` ENABLE KEYS */;
UNLOCK TABLES;

--
-- Table structure for table `ta_activity_user`
--

DROP TABLE IF EXISTS `ta_activity_user`;
/*!40101 SET @saved_cs_client     = @@character_set_client */;
/*!50503 SET character_set_client = utf8mb4 */;
CREATE TABLE `ta_activity_user` (
  `id` bigint NOT NULL AUTO_INCREMENT,
  `create_time` datetime(6) NOT NULL,
  `update_time` datetime(6) NOT NULL,
  `join_status` int NOT NULL,
  `is_delete` tinyint(1) NOT NULL,
  `activity_id` bigint NOT NULL,
  `user_id` bigint NOT NULL,
  PRIMARY KEY (`id`),
  KEY `ta_activity_user_activity_id_0cc54386_fk_ta_activity_id` (`activity_id`),
  KEY `ta_activity_user_user_id_f2692ed6_fk_ta_user_id` (`user_id`),
  CONSTRAINT `ta_activity_user_activity_id_0cc54386_fk_ta_activity_id` FOREIGN KEY (`activity_id`) REFERENCES `ta_activity` (`id`),
  CONSTRAINT `ta_activity_user_user_id_f2692ed6_fk_ta_user_id` FOREIGN KEY (`user_id`) REFERENCES `ta_user` (`id`)
) ENGINE=InnoDB DEFAULT CHARSET=utf8mb4 COLLATE=utf8mb4_0900_ai_ci;
/*!40101 SET character_set_client = @saved_cs_client */;

--
-- Dumping data for table `ta_activity_user`
--

LOCK TABLES `ta_activity_user` WRITE;
/*!40000 ALTER TABLE `ta_activity_user` DISABLE KEYS */;
/*!40000 ALTER TABLE `ta_activity_user` ENABLE KEYS */;
UNLOCK TABLES;

--
-- Table structure for table `ta_address`
--

DROP TABLE IF EXISTS `ta_address`;
/*!40101 SET @saved_cs_client     = @@character_set_client */;
/*!50503 SET character_set_client = utf8mb4 */;
CREATE TABLE `ta_address` (
  `id` bigint NOT NULL AUTO_INCREMENT,
  `create_time` datetime(6) NOT NULL,
  `update_time` datetime(6) NOT NULL,
  `is_delete` tinyint(1) NOT NULL,
  `phone` varchar(11) NOT NULL,
  `receiver` varchar(20) NOT NULL,
  `province` varchar(20) NOT NULL,
  `city` varchar(20) NOT NULL,
  `county` varchar(20) NOT NULL,
  `detail` varchar(256) NOT NULL,
  `is_default` tinyint(1) NOT NULL,
  `user_id` bigint NOT NULL,
  PRIMARY KEY (`id`),
  KEY `ta_address_user_id_8817168f_fk_ta_user_id` (`user_id`),
  CONSTRAINT `ta_address_user_id_8817168f_fk_ta_user_id` FOREIGN KEY (`user_id`) REFERENCES `ta_user` (`id`)
) ENGINE=InnoDB DEFAULT CHARSET=utf8mb4 COLLATE=utf8mb4_0900_ai_ci;
/*!40101 SET character_set_client = @saved_cs_client */;

--
-- Dumping data for table `ta_address`
--

LOCK TABLES `ta_address` WRITE;
/*!40000 ALTER TABLE `ta_address` DISABLE KEYS */;
/*!40000 ALTER TABLE `ta_address` ENABLE KEYS */;
UNLOCK TABLES;

--
-- Table structure for table `ta_area`
--

DROP TABLE IF EXISTS `ta_area`;
/*!40101 SET @saved_cs_client     = @@character_set_client */;
/*!50503 SET character_set_client = utf8mb4 */;
CREATE TABLE `ta_area` (
  `id` bigint NOT NULL AUTO_INCREMENT,
  `pid` int NOT NULL,
  `name` varchar(20) NOT NULL,
  `level` int NOT NULL,
  PRIMARY KEY (`id`)
) ENGINE=InnoDB DEFAULT CHARSET=utf8mb4 COLLATE=utf8mb4_0900_ai_ci;
/*!40101 SET character_set_client = @saved_cs_client */;

--
-- Dumping data for table `ta_area`
--

LOCK TABLES `ta_area` WRITE;
/*!40000 ALTER TABLE `ta_area` DISABLE KEYS */;
/*!40000 ALTER TABLE `ta_area` ENABLE KEYS */;
UNLOCK TABLES;

--
-- Table structure for table `ta_article`
--

DROP TABLE IF EXISTS `ta_article`;
/*!40101 SET @saved_cs_client     = @@character_set_client */;
/*!50503 SET character_set_client = utf8mb4 */;
CREATE TABLE `ta_article` (
  `id` bigint NOT NULL AUTO_INCREMENT,
  `create_time` datetime(6) NOT NULL,
  `update_time` datetime(6) NOT NULL,
  `content` longtext NOT NULL,
  `status` tinyint(1) NOT NULL,
  `is_delete` tinyint(1) NOT NULL,
  `is_top` tinyint(1) NOT NULL,
  `is_hot` tinyint(1) NOT NULL,
  `is_anonymous` tinyint(1) NOT NULL,
  `is_audit` int NOT NULL,
  `audit_user_id` bigint DEFAULT NULL,
  `school_id` bigint NOT NULL,
  `user_id` bigint NOT NULL,
  PRIMARY KEY (`id`),
  KEY `ta_article_audit_user_id_42c286f5_fk_ta_user_id` (`audit_user_id`),
  KEY `ta_article_school_id_757f2806_fk_ta_school_id` (`school_id`),
  KEY `ta_article_user_id_9ba5cfa3_fk_ta_user_id` (`user_id`),
  CONSTRAINT `ta_article_audit_user_id_42c286f5_fk_ta_user_id` FOREIGN KEY (`audit_user_id`) REFERENCES `ta_user` (`id`),
  CONSTRAINT `ta_article_school_id_757f2806_fk_ta_school_id` FOREIGN KEY (`school_id`) REFERENCES `ta_school` (`id`),
  CONSTRAINT `ta_article_user_id_9ba5cfa3_fk_ta_user_id` FOREIGN KEY (`user_id`) REFERENCES `ta_user` (`id`)
) ENGINE=InnoDB AUTO_INCREMENT=4 DEFAULT CHARSET=utf8mb4 COLLATE=utf8mb4_0900_ai_ci;
/*!40101 SET character_set_client = @saved_cs_client */;

--
-- Dumping data for table `ta_article`
--

LOCK TABLES `ta_article` WRITE;
/*!40000 ALTER TABLE `ta_article` DISABLE KEYS */;
INSERT INTO `ta_article` VALUES (1,'2023-11-20 05:09:19.434053','2023-11-20 05:09:19.434053','123123',1,0,0,0,0,1,1,1,1),(2,'2023-11-20 07:02:09.829665','2023-11-20 07:02:09.829665','1231',1,0,0,0,0,1,NULL,1,2),(3,'2023-11-20 07:06:41.177067','2023-11-20 07:06:41.177067','娴嬭瘯鍖垮悕',1,0,0,0,1,1,NULL,1,2);
/*!40000 ALTER TABLE `ta_article` ENABLE KEYS */;
UNLOCK TABLES;

--
-- Table structure for table `ta_article_comment`
--

DROP TABLE IF EXISTS `ta_article_comment`;
/*!40101 SET @saved_cs_client     = @@character_set_client */;
/*!50503 SET character_set_client = utf8mb4 */;
CREATE TABLE `ta_article_comment` (
  `id` bigint NOT NULL AUTO_INCREMENT,
  `create_time` datetime(6) NOT NULL,
  `update_time` datetime(6) NOT NULL,
  `content` longtext NOT NULL,
  `is_anonymous` tinyint(1) NOT NULL,
  `is_audit` int NOT NULL,
  `is_delete` tinyint(1) NOT NULL,
  `article_id` bigint NOT NULL,
  `parent_id` bigint DEFAULT NULL,
  `user_id` bigint NOT NULL,
  PRIMARY KEY (`id`),
  KEY `ta_article_comment_article_id_c52e2266_fk_ta_article_id` (`article_id`),
  KEY `ta_article_comment_parent_id_12ade368_fk_ta_article_comment_id` (`parent_id`),
  KEY `ta_article_comment_user_id_83c0f3d6_fk_ta_user_id` (`user_id`),
  CONSTRAINT `ta_article_comment_article_id_c52e2266_fk_ta_article_id` FOREIGN KEY (`article_id`) REFERENCES `ta_article` (`id`),
  CONSTRAINT `ta_article_comment_parent_id_12ade368_fk_ta_article_comment_id` FOREIGN KEY (`parent_id`) REFERENCES `ta_article_comment` (`id`),
  CONSTRAINT `ta_article_comment_user_id_83c0f3d6_fk_ta_user_id` FOREIGN KEY (`user_id`) REFERENCES `ta_user` (`id`)
) ENGINE=InnoDB DEFAULT CHARSET=utf8mb4 COLLATE=utf8mb4_0900_ai_ci;
/*!40101 SET character_set_client = @saved_cs_client */;

--
-- Dumping data for table `ta_article_comment`
--

LOCK TABLES `ta_article_comment` WRITE;
/*!40000 ALTER TABLE `ta_article_comment` DISABLE KEYS */;
/*!40000 ALTER TABLE `ta_article_comment` ENABLE KEYS */;
UNLOCK TABLES;

--
-- Table structure for table `ta_article_files`
--

DROP TABLE IF EXISTS `ta_article_files`;
/*!40101 SET @saved_cs_client     = @@character_set_client */;
/*!50503 SET character_set_client = utf8mb4 */;
CREATE TABLE `ta_article_files` (
  `id` bigint NOT NULL AUTO_INCREMENT,
  `article_id` bigint NOT NULL,
  `file_id` bigint NOT NULL,
  PRIMARY KEY (`id`),
  UNIQUE KEY `ta_article_files_article_id_file_id_99f79485_uniq` (`article_id`,`file_id`),
  KEY `ta_article_files_file_id_5c8f689a_fk_ta_file_id` (`file_id`),
  CONSTRAINT `ta_article_files_article_id_1c8b0d50_fk_ta_article_id` FOREIGN KEY (`article_id`) REFERENCES `ta_article` (`id`),
  CONSTRAINT `ta_article_files_file_id_5c8f689a_fk_ta_file_id` FOREIGN KEY (`file_id`) REFERENCES `ta_file` (`id`)
) ENGINE=InnoDB AUTO_INCREMENT=5 DEFAULT CHARSET=utf8mb4 COLLATE=utf8mb4_0900_ai_ci;
/*!40101 SET character_set_client = @saved_cs_client */;

--
-- Dumping data for table `ta_article_files`
--

LOCK TABLES `ta_article_files` WRITE;
/*!40000 ALTER TABLE `ta_article_files` DISABLE KEYS */;
INSERT INTO `ta_article_files` VALUES (1,2,29),(2,2,30),(4,3,31),(3,3,32);
/*!40000 ALTER TABLE `ta_article_files` ENABLE KEYS */;
UNLOCK TABLES;

--
-- Table structure for table `ta_article_like`
--

DROP TABLE IF EXISTS `ta_article_like`;
/*!40101 SET @saved_cs_client     = @@character_set_client */;
/*!50503 SET character_set_client = utf8mb4 */;
CREATE TABLE `ta_article_like` (
  `id` bigint NOT NULL AUTO_INCREMENT,
  `create_time` datetime(6) NOT NULL,
  `update_time` datetime(6) NOT NULL,
  `is_delete` tinyint(1) NOT NULL,
  `article_id` bigint NOT NULL,
  `user_id` bigint NOT NULL,
  PRIMARY KEY (`id`),
  KEY `ta_article_like_article_id_4539f9c7_fk_ta_article_id` (`article_id`),
  KEY `ta_article_like_user_id_33ae3116_fk_ta_user_id` (`user_id`),
  CONSTRAINT `ta_article_like_article_id_4539f9c7_fk_ta_article_id` FOREIGN KEY (`article_id`) REFERENCES `ta_article` (`id`),
  CONSTRAINT `ta_article_like_user_id_33ae3116_fk_ta_user_id` FOREIGN KEY (`user_id`) REFERENCES `ta_user` (`id`)
) ENGINE=InnoDB DEFAULT CHARSET=utf8mb4 COLLATE=utf8mb4_0900_ai_ci;
/*!40101 SET character_set_client = @saved_cs_client */;

--
-- Dumping data for table `ta_article_like`
--

LOCK TABLES `ta_article_like` WRITE;
/*!40000 ALTER TABLE `ta_article_like` DISABLE KEYS */;
/*!40000 ALTER TABLE `ta_article_like` ENABLE KEYS */;
UNLOCK TABLES;

--
-- Table structure for table `ta_article_view`
--

DROP TABLE IF EXISTS `ta_article_view`;
/*!40101 SET @saved_cs_client     = @@character_set_client */;
/*!50503 SET character_set_client = utf8mb4 */;
CREATE TABLE `ta_article_view` (
  `id` bigint NOT NULL AUTO_INCREMENT,
  `create_time` datetime(6) NOT NULL,
  `update_time` datetime(6) NOT NULL,
  `is_delete` tinyint(1) NOT NULL,
  `article_id` bigint NOT NULL,
  `user_id` bigint NOT NULL,
  PRIMARY KEY (`id`),
  KEY `ta_article_view_article_id_cd5f97a5_fk_ta_article_id` (`article_id`),
  KEY `ta_article_view_user_id_05723159_fk_ta_user_id` (`user_id`),
  CONSTRAINT `ta_article_view_article_id_cd5f97a5_fk_ta_article_id` FOREIGN KEY (`article_id`) REFERENCES `ta_article` (`id`),
  CONSTRAINT `ta_article_view_user_id_05723159_fk_ta_user_id` FOREIGN KEY (`user_id`) REFERENCES `ta_user` (`id`)
) ENGINE=InnoDB AUTO_INCREMENT=3 DEFAULT CHARSET=utf8mb4 COLLATE=utf8mb4_0900_ai_ci;
/*!40101 SET character_set_client = @saved_cs_client */;

--
-- Dumping data for table `ta_article_view`
--

LOCK TABLES `ta_article_view` WRITE;
/*!40000 ALTER TABLE `ta_article_view` DISABLE KEYS */;
INSERT INTO `ta_article_view` VALUES (1,'2023-11-20 07:05:04.427365','2023-11-20 07:05:04.427365',0,2,2),(2,'2023-11-20 07:06:44.735459','2023-11-20 07:06:52.122924',0,3,2);
/*!40000 ALTER TABLE `ta_article_view` ENABLE KEYS */;
UNLOCK TABLES;

--
-- Table structure for table `ta_file`
--

DROP TABLE IF EXISTS `ta_file`;
/*!40101 SET @saved_cs_client     = @@character_set_client */;
/*!50503 SET character_set_client = utf8mb4 */;
CREATE TABLE `ta_file` (
  `id` bigint NOT NULL AUTO_INCREMENT,
  `file` varchar(100) NOT NULL,
  PRIMARY KEY (`id`)
) ENGINE=InnoDB AUTO_INCREMENT=35 DEFAULT CHARSET=utf8mb4 COLLATE=utf8mb4_0900_ai_ci;
/*!40101 SET character_set_client = @saved_cs_client */;

--
-- Dumping data for table `ta_file`
--

LOCK TABLES `ta_file` WRITE;
/*!40000 ALTER TABLE `ta_file` DISABLE KEYS */;
INSERT INTO `ta_file` VALUES (1,'2023/11/20/20231031_1698740527_3282.jpg'),(3,'2023/11/20/20231031_1698740186_9063.jpg'),(4,'2023/11/20/20231031_1698740195_4408_ddewEyB.jpg'),(5,'2023/11/20/20231031_1698740195_4408_ClNk4Ry.jpg'),(6,'2023/11/20/20231031_1698740195_4408_K3itlk0.jpg'),(7,'2023/11/20/20231031_1698740195_4408_tVfoan0.jpg'),(8,'2023/11/20/20231031_1698740195_4408_wtc3DAt.jpg'),(9,'2023/11/20/20231031_1698740195_4408_4egXPvG.jpg'),(10,'2023/11/20/20231031_1698740195_4408_tafRpBP.jpg'),(11,'2023/11/20/20231031_1698740195_4408_ltGDtwD.jpg'),(12,'2023/11/20/20231031_1698740195_4408_WFOmam9.jpg'),(13,'2023/11/20/20231031_1698740195_4408_JrRM59s.jpg'),(14,'2023/11/20/20231031_1698740537_1753.jpg'),(15,'2023/11/20/20231031_1698740537_6757.jpg'),(16,'2023/11/20/20231031_1698740537_1753_AME9BEZ.jpg'),(17,'2023/11/20/20231031_1698740537_6757_wfk5U21.jpg'),(18,'2023/11/20/20231031_1698740537_6757_ZQbXIHA.jpg'),(19,'2023/11/20/20231031_1698740539_7082.jpg'),(20,'2023/11/20/20231031_1698740537_6757_UCvCb1m.jpg'),(21,'2023/11/20/20231031_1698740539_7082_lmqZLJ0.jpg'),(22,'2023/11/20/20231031_1698740537_6757_9Ei0NrK.jpg'),(23,'2023/11/20/20231031_1698740544_3229_KLz85vY.jpg'),(24,'2023/11/20/20231031_1698740537_1753_IcGnGBK.jpg'),(25,'2023/11/20/20231031_1698740539_7082_PpXnron.jpg'),(26,'2023/11/20/20231031_1698740537_1753_HiLMwR7.jpg'),(27,'2023/11/20/20231031_1698740539_7082_U3D0siS.jpg'),(28,'2023/11/20/20231031_1698740537_6757_b34W9ez.jpg'),(29,'2023/11/20/20231031_1698740537_1753_rjRRm3S.jpg'),(30,'2023/11/20/20231031_1698740537_6757_46eG9M7.jpg'),(31,'2023/11/20/20231112_1699765637_4120.jpg'),(32,'2023/11/20/20231112_1699765652_8709.jpg'),(33,'2023/11/20/20231112_1699765597_3186.jpg'),(34,'2023/11/20/20231112_1699765636_8603.jpg');
/*!40000 ALTER TABLE `ta_file` ENABLE KEYS */;
UNLOCK TABLES;

--
-- Table structure for table `ta_goods`
--

DROP TABLE IF EXISTS `ta_goods`;
/*!40101 SET @saved_cs_client     = @@character_set_client */;
/*!50503 SET character_set_client = utf8mb4 */;
CREATE TABLE `ta_goods` (
  `id` bigint NOT NULL AUTO_INCREMENT,
  `create_time` datetime(6) NOT NULL,
  `update_time` datetime(6) NOT NULL,
  `is_delete` tinyint(1) NOT NULL,
  `title` varchar(20) NOT NULL,
  `desc` varchar(50) NOT NULL,
  `price` decimal(10,2) NOT NULL,
  `cover` varchar(100) DEFAULT NULL,
  `stock` int NOT NULL,
  `is_on_sale` tinyint(1) NOT NULL,
  `recommend` tinyint(1) NOT NULL,
  `group_id` bigint NOT NULL,
  `school_id` bigint NOT NULL,
  PRIMARY KEY (`id`),
  KEY `ta_goods_group_id_efa5c6cf_fk_ta_goods_group_id` (`group_id`),
  KEY `ta_goods_school_id_3a8625f7_fk_ta_school_id` (`school_id`),
  CONSTRAINT `ta_goods_group_id_efa5c6cf_fk_ta_goods_group_id` FOREIGN KEY (`group_id`) REFERENCES `ta_goods_group` (`id`),
  CONSTRAINT `ta_goods_school_id_3a8625f7_fk_ta_school_id` FOREIGN KEY (`school_id`) REFERENCES `ta_school` (`id`)
) ENGINE=InnoDB AUTO_INCREMENT=2 DEFAULT CHARSET=utf8mb4 COLLATE=utf8mb4_0900_ai_ci;
/*!40101 SET character_set_client = @saved_cs_client */;

--
-- Dumping data for table `ta_goods`
--

LOCK TABLES `ta_goods` WRITE;
/*!40000 ALTER TABLE `ta_goods` DISABLE KEYS */;
INSERT INTO `ta_goods` VALUES (1,'2023-11-20 08:02:36.803695','2023-11-20 08:11:19.674976',0,'娴嬭瘯','娴嬭瘯娴嬭瘯',12.00,'good/20231112_1699765652_8709.jpg',1,1,0,1,1);
/*!40000 ALTER TABLE `ta_goods` ENABLE KEYS */;
UNLOCK TABLES;

--
-- Table structure for table `ta_goods_group`
--

DROP TABLE IF EXISTS `ta_goods_group`;
/*!40101 SET @saved_cs_client     = @@character_set_client */;
/*!50503 SET character_set_client = utf8mb4 */;
CREATE TABLE `ta_goods_group` (
  `id` bigint NOT NULL AUTO_INCREMENT,
  `create_time` datetime(6) NOT NULL,
  `update_time` datetime(6) NOT NULL,
  `is_delete` tinyint(1) NOT NULL,
  `name` varchar(20) NOT NULL,
  `image` varchar(100) DEFAULT NULL,
  `status` tinyint(1) NOT NULL,
  PRIMARY KEY (`id`)
) ENGINE=InnoDB AUTO_INCREMENT=4 DEFAULT CHARSET=utf8mb4 COLLATE=utf8mb4_0900_ai_ci;
/*!40101 SET character_set_client = @saved_cs_client */;

--
-- Dumping data for table `ta_goods_group`
--

LOCK TABLES `ta_goods_group` WRITE;
/*!40000 ALTER TABLE `ta_goods_group` DISABLE KEYS */;
INSERT INTO `ta_goods_group` VALUES (1,'2023-11-20 07:55:08.669069','2023-11-20 07:55:08.669069',0,'姘存灉','good/group/20231112_1699765668_9824.jpg',1),(2,'2023-11-20 08:01:37.640196','2023-11-20 08:01:37.640196',0,'钄彍','good/group/20231112_1699765652_8709.jpg',1),(3,'2023-11-20 08:02:00.784830','2023-11-20 08:02:00.784830',0,'鐢靛瓙浜у搧','',1);
/*!40000 ALTER TABLE `ta_goods_group` ENABLE KEYS */;
UNLOCK TABLES;

--
-- Table structure for table `ta_goods_images`
--

DROP TABLE IF EXISTS `ta_goods_images`;
/*!40101 SET @saved_cs_client     = @@character_set_client */;
/*!50503 SET character_set_client = utf8mb4 */;
CREATE TABLE `ta_goods_images` (
  `id` bigint NOT NULL AUTO_INCREMENT,
  `goods_id` bigint NOT NULL,
  `file_id` bigint NOT NULL,
  PRIMARY KEY (`id`),
  UNIQUE KEY `ta_goods_images_goods_id_file_id_79b4084e_uniq` (`goods_id`,`file_id`),
  KEY `ta_goods_images_file_id_2a9d42a0_fk_ta_file_id` (`file_id`),
  CONSTRAINT `ta_goods_images_file_id_2a9d42a0_fk_ta_file_id` FOREIGN KEY (`file_id`) REFERENCES `ta_file` (`id`),
  CONSTRAINT `ta_goods_images_goods_id_2f80020e_fk_ta_goods_id` FOREIGN KEY (`goods_id`) REFERENCES `ta_goods` (`id`)
) ENGINE=InnoDB AUTO_INCREMENT=2 DEFAULT CHARSET=utf8mb4 COLLATE=utf8mb4_0900_ai_ci;
/*!40101 SET character_set_client = @saved_cs_client */;

--
-- Dumping data for table `ta_goods_images`
--

LOCK TABLES `ta_goods_images` WRITE;
/*!40000 ALTER TABLE `ta_goods_images` DISABLE KEYS */;
INSERT INTO `ta_goods_images` VALUES (1,1,34);
/*!40000 ALTER TABLE `ta_goods_images` ENABLE KEYS */;
UNLOCK TABLES;

--
-- Table structure for table `ta_order`
--

DROP TABLE IF EXISTS `ta_order`;
/*!40101 SET @saved_cs_client     = @@character_set_client */;
/*!50503 SET character_set_client = utf8mb4 */;
CREATE TABLE `ta_order` (
  `id` bigint NOT NULL AUTO_INCREMENT,
  `create_time` datetime(6) NOT NULL,
  `update_time` datetime(6) NOT NULL,
  `is_delete` tinyint(1) NOT NULL,
  `order_status` varchar(50) NOT NULL,
  `order_no` varchar(50) NOT NULL,
  `order_amount` decimal(10,2) NOT NULL,
  `remark` longtext,
  `payment_method` varchar(50) DEFAULT NULL,
  `address_id` bigint DEFAULT NULL,
  `task_id` bigint DEFAULT NULL,
  `user_id` bigint NOT NULL,
  PRIMARY KEY (`id`),
  KEY `ta_order_address_id_e126ab17_fk_ta_address_id` (`address_id`),
  KEY `ta_order_task_id_7ae5a976_fk_demand_task_id` (`task_id`),
  KEY `ta_order_user_id_9130ac76_fk_ta_user_id` (`user_id`),
  CONSTRAINT `ta_order_address_id_e126ab17_fk_ta_address_id` FOREIGN KEY (`address_id`) REFERENCES `ta_address` (`id`),
  CONSTRAINT `ta_order_task_id_7ae5a976_fk_demand_task_id` FOREIGN KEY (`task_id`) REFERENCES `demand_task` (`id`),
  CONSTRAINT `ta_order_user_id_9130ac76_fk_ta_user_id` FOREIGN KEY (`user_id`) REFERENCES `ta_user` (`id`)
) ENGINE=InnoDB DEFAULT CHARSET=utf8mb4 COLLATE=utf8mb4_0900_ai_ci;
/*!40101 SET character_set_client = @saved_cs_client */;

--
-- Dumping data for table `ta_order`
--

LOCK TABLES `ta_order` WRITE;
/*!40000 ALTER TABLE `ta_order` DISABLE KEYS */;
/*!40000 ALTER TABLE `ta_order` ENABLE KEYS */;
UNLOCK TABLES;

--
-- Table structure for table `ta_school`
--

DROP TABLE IF EXISTS `ta_school`;
/*!40101 SET @saved_cs_client     = @@character_set_client */;
/*!50503 SET character_set_client = utf8mb4 */;
CREATE TABLE `ta_school` (
  `id` bigint NOT NULL AUTO_INCREMENT,
  `create_time` datetime(6) NOT NULL,
  `update_time` datetime(6) NOT NULL,
  `name` varchar(20) NOT NULL,
  `address` varchar(50) NOT NULL,
  `status` tinyint(1) NOT NULL,
  `is_delete` tinyint(1) NOT NULL,
  PRIMARY KEY (`id`)
) ENGINE=InnoDB AUTO_INCREMENT=2 DEFAULT CHARSET=utf8mb4 COLLATE=utf8mb4_0900_ai_ci;
/*!40101 SET character_set_client = @saved_cs_client */;

--
-- Dumping data for table `ta_school`
--

LOCK TABLES `ta_school` WRITE;
/*!40000 ALTER TABLE `ta_school` DISABLE KEYS */;
INSERT INTO `ta_school` VALUES (1,'2023-11-20 05:09:02.863366','2023-11-20 05:09:02.863366','閲嶅簡绉戞妧瀛﹂櫌','閲嶅簡鏄矙鍧潩',1,0);
/*!40000 ALTER TABLE `ta_school` ENABLE KEYS */;
UNLOCK TABLES;

--
-- Table structure for table `ta_school_user_permissions`
--

DROP TABLE IF EXISTS `ta_school_user_permissions`;
/*!40101 SET @saved_cs_client     = @@character_set_client */;
/*!50503 SET character_set_client = utf8mb4 */;
CREATE TABLE `ta_school_user_permissions` (
  `id` bigint NOT NULL AUTO_INCREMENT,
  `create_time` datetime(6) NOT NULL,
  `update_time` datetime(6) NOT NULL,
  `is_delete` tinyint(1) NOT NULL,
  `permission` int NOT NULL,
  `is_disable` tinyint(1) NOT NULL,
  `group_id` int DEFAULT NULL,
  `school_id` bigint NOT NULL,
  `user_id` bigint NOT NULL,
  PRIMARY KEY (`id`),
  KEY `ta_school_user_permissions_group_id_883523df_fk_auth_group_id` (`group_id`),
  KEY `ta_school_user_permissions_school_id_4fd99c17_fk_ta_school_id` (`school_id`),
  KEY `ta_school_user_permissions_user_id_d55a8b5a_fk_ta_user_id` (`user_id`),
  CONSTRAINT `ta_school_user_permissions_group_id_883523df_fk_auth_group_id` FOREIGN KEY (`group_id`) REFERENCES `auth_group` (`id`),
  CONSTRAINT `ta_school_user_permissions_school_id_4fd99c17_fk_ta_school_id` FOREIGN KEY (`school_id`) REFERENCES `ta_school` (`id`),
  CONSTRAINT `ta_school_user_permissions_user_id_d55a8b5a_fk_ta_user_id` FOREIGN KEY (`user_id`) REFERENCES `ta_user` (`id`)
) ENGINE=InnoDB DEFAULT CHARSET=utf8mb4 COLLATE=utf8mb4_0900_ai_ci;
/*!40101 SET character_set_client = @saved_cs_client */;

--
-- Dumping data for table `ta_school_user_permissions`
--

LOCK TABLES `ta_school_user_permissions` WRITE;
/*!40000 ALTER TABLE `ta_school_user_permissions` DISABLE KEYS */;
/*!40000 ALTER TABLE `ta_school_user_permissions` ENABLE KEYS */;
UNLOCK TABLES;

--
-- Table structure for table `ta_user`
--

DROP TABLE IF EXISTS `ta_user`;
/*!40101 SET @saved_cs_client     = @@character_set_client */;
/*!50503 SET character_set_client = utf8mb4 */;
CREATE TABLE `ta_user` (
  `id` bigint NOT NULL AUTO_INCREMENT,
  `password` varchar(128) NOT NULL,
  `last_login` datetime(6) DEFAULT NULL,
  `is_superuser` tinyint(1) NOT NULL,
  `username` varchar(150) NOT NULL,
  `first_name` varchar(150) NOT NULL,
  `last_name` varchar(150) NOT NULL,
  `email` varchar(254) NOT NULL,
  `is_staff` tinyint(1) NOT NULL,
  `is_active` tinyint(1) NOT NULL,
  `date_joined` datetime(6) NOT NULL,
  `create_time` datetime(6) NOT NULL,
  `update_time` datetime(6) NOT NULL,
  `is_delete` tinyint(1) NOT NULL,
  `mobile` varchar(11) DEFAULT NULL,
  `avatar` varchar(100) DEFAULT NULL,
  `money` decimal(10,2) NOT NULL,
  `integral` int NOT NULL,
  `sex` int NOT NULL,
  `description` varchar(100) DEFAULT NULL,
  `openid` varchar(100) DEFAULT NULL,
  `user_type` int NOT NULL,
  `school_id` bigint DEFAULT NULL,
  PRIMARY KEY (`id`),
  UNIQUE KEY `username` (`username`),
  KEY `ta_user_school_id_4db56c4f_fk_ta_school_id` (`school_id`),
  CONSTRAINT `ta_user_school_id_4db56c4f_fk_ta_school_id` FOREIGN KEY (`school_id`) REFERENCES `ta_school` (`id`)
) ENGINE=InnoDB AUTO_INCREMENT=3 DEFAULT CHARSET=utf8mb4 COLLATE=utf8mb4_0900_ai_ci;
/*!40101 SET character_set_client = @saved_cs_client */;

--
-- Dumping data for table `ta_user`
--

LOCK TABLES `ta_user` WRITE;
/*!40000 ALTER TABLE `ta_user` DISABLE KEYS */;
INSERT INTO `ta_user` VALUES (1,'pbkdf2_sha256$600000$5wRKVVwzj4SSc81pdoSFMc$7urVC7MBO9V81A+H5CcdRsi7yZW1AXlyBAznp7oLn0c=','2023-11-20 05:08:29.968296',1,'admin','','','927266886@qq.com',1,1,'2023-11-20 05:07:51.213283','2023-11-20 05:07:51.352771','2023-11-20 05:07:51.352771',0,NULL,'',0.00,0,2,NULL,NULL,1,NULL),(2,'pbkdf2_sha256$600000$RvdjH2W1QtOeyyIzcsPKil$sr8CCZY6lJWrLXOJx+76mvvtnDvMNvxHJu6mK9bq4C0=','2023-11-20 06:46:21.061036',0,'user850477','','','',0,1,'2023-11-20 06:41:51.290794','2023-11-20 06:41:51.464295','2023-11-20 07:09:12.540604',0,'17749998266','avatar/20231112_1699765632_4767.jpg',0.00,0,0,'杩欎釜浜哄緢鎳掞紝浠€涔堥兘娌℃湁鐣欎笅',NULL,1,1);
/*!40000 ALTER TABLE `ta_user` ENABLE KEYS */;
UNLOCK TABLES;

--
-- Table structure for table `ta_user_groups`
--

DROP TABLE IF EXISTS `ta_user_groups`;
/*!40101 SET @saved_cs_client     = @@character_set_client */;
/*!50503 SET character_set_client = utf8mb4 */;
CREATE TABLE `ta_user_groups` (
  `id` bigint NOT NULL AUTO_INCREMENT,
  `user_id` bigint NOT NULL,
  `group_id` int NOT NULL,
  PRIMARY KEY (`id`),
  UNIQUE KEY `ta_user_groups_user_id_group_id_5e9d3925_uniq` (`user_id`,`group_id`),
  KEY `ta_user_groups_group_id_ecc12758_fk_auth_group_id` (`group_id`),
  CONSTRAINT `ta_user_groups_group_id_ecc12758_fk_auth_group_id` FOREIGN KEY (`group_id`) REFERENCES `auth_group` (`id`),
  CONSTRAINT `ta_user_groups_user_id_3de45900_fk_ta_user_id` FOREIGN KEY (`user_id`) REFERENCES `ta_user` (`id`)
) ENGINE=InnoDB DEFAULT CHARSET=utf8mb4 COLLATE=utf8mb4_0900_ai_ci;
/*!40101 SET character_set_client = @saved_cs_client */;

--
-- Dumping data for table `ta_user_groups`
--

LOCK TABLES `ta_user_groups` WRITE;
/*!40000 ALTER TABLE `ta_user_groups` DISABLE KEYS */;
/*!40000 ALTER TABLE `ta_user_groups` ENABLE KEYS */;
UNLOCK TABLES;

--
-- Table structure for table `ta_user_user_permissions`
--

DROP TABLE IF EXISTS `ta_user_user_permissions`;
/*!40101 SET @saved_cs_client     = @@character_set_client */;
/*!50503 SET character_set_client = utf8mb4 */;
CREATE TABLE `ta_user_user_permissions` (
  `id` bigint NOT NULL AUTO_INCREMENT,
  `user_id` bigint NOT NULL,
  `permission_id` int NOT NULL,
  PRIMARY KEY (`id`),
  UNIQUE KEY `ta_user_user_permissions_user_id_permission_id_e410f8fc_uniq` (`user_id`,`permission_id`),
  KEY `ta_user_user_permiss_permission_id_9c86ab66_fk_auth_perm` (`permission_id`),
  CONSTRAINT `ta_user_user_permiss_permission_id_9c86ab66_fk_auth_perm` FOREIGN KEY (`permission_id`) REFERENCES `auth_permission` (`id`),
  CONSTRAINT `ta_user_user_permissions_user_id_5a092685_fk_ta_user_id` FOREIGN KEY (`user_id`) REFERENCES `ta_user` (`id`)
) ENGINE=InnoDB DEFAULT CHARSET=utf8mb4 COLLATE=utf8mb4_0900_ai_ci;
/*!40101 SET character_set_client = @saved_cs_client */;

--
-- Dumping data for table `ta_user_user_permissions`
--

LOCK TABLES `ta_user_user_permissions` WRITE;
/*!40000 ALTER TABLE `ta_user_user_permissions` DISABLE KEYS */;
/*!40000 ALTER TABLE `ta_user_user_permissions` ENABLE KEYS */;
UNLOCK TABLES;

--
-- Table structure for table `ta_verifycode`
--

DROP TABLE IF EXISTS `ta_verifycode`;
/*!40101 SET @saved_cs_client     = @@character_set_client */;
/*!50503 SET character_set_client = utf8mb4 */;
CREATE TABLE `ta_verifycode` (
  `id` bigint NOT NULL AUTO_INCREMENT,
  `code` varchar(10) NOT NULL,
  `mobile` varchar(20) NOT NULL,
  `create_time` datetime(6) NOT NULL,
  PRIMARY KEY (`id`),
  KEY `ta_verifyco_mobile_796474_idx` (`mobile`)
) ENGINE=InnoDB AUTO_INCREMENT=2 DEFAULT CHARSET=utf8mb4 COLLATE=utf8mb4_0900_ai_ci;
/*!40101 SET character_set_client = @saved_cs_client */;

--
-- Dumping data for table `ta_verifycode`
--

LOCK TABLES `ta_verifycode` WRITE;
/*!40000 ALTER TABLE `ta_verifycode` DISABLE KEYS */;
/*!40000 ALTER TABLE `ta_verifycode` ENABLE KEYS */;
UNLOCK TABLES;
/*!40103 SET TIME_ZONE=@OLD_TIME_ZONE */;

/*!40101 SET SQL_MODE=@OLD_SQL_MODE */;
/*!40014 SET FOREIGN_KEY_CHECKS=@OLD_FOREIGN_KEY_CHECKS */;
/*!40014 SET UNIQUE_CHECKS=@OLD_UNIQUE_CHECKS */;
/*!40101 SET CHARACTER_SET_CLIENT=@OLD_CHARACTER_SET_CLIENT */;
/*!40101 SET CHARACTER_SET_RESULTS=@OLD_CHARACTER_SET_RESULTS */;
/*!40101 SET COLLATION_CONNECTION=@OLD_COLLATION_CONNECTION */;
/*!40111 SET SQL_NOTES=@OLD_SQL_NOTES */;

-- Dump completed on 2023-11-22 16:45:22
