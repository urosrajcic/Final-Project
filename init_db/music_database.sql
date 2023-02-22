-- MySQL dump 10.13  Distrib 8.0.31, for Win64 (x86_64)
--
-- Host: 127.0.0.1    Database: music_db
-- ------------------------------------------------------
-- Server version	8.0.31

/*!40101 SET @OLD_CHARACTER_SET_CLIENT=@@CHARACTER_SET_CLIENT */;
/*!40101 SET @OLD_CHARACTER_SET_RESULTS=@@CHARACTER_SET_RESULTS */;
/*!40101 SET @OLD_COLLATION_CONNECTION=@@COLLATION_CONNECTION */;
/*!50503 SET NAMES utf8 */;
/*!40103 SET @OLD_TIME_ZONE=@@TIME_ZONE */;
/*!40103 SET TIME_ZONE='+00:00' */;
/*!40014 SET @OLD_UNIQUE_CHECKS=@@UNIQUE_CHECKS, UNIQUE_CHECKS=0 */;
/*!40014 SET @OLD_FOREIGN_KEY_CHECKS=@@FOREIGN_KEY_CHECKS, FOREIGN_KEY_CHECKS=0 */;
/*!40101 SET @OLD_SQL_MODE=@@SQL_MODE, SQL_MODE='NO_AUTO_VALUE_ON_ZERO' */;
/*!40111 SET @OLD_SQL_NOTES=@@SQL_NOTES, SQL_NOTES=0 */;

--
-- Table structure for table `album`
--

DROP TABLE IF EXISTS `album`;
/*!40101 SET @saved_cs_client     = @@character_set_client */;
/*!50503 SET character_set_client = utf8mb4 */;
CREATE TABLE `album` (
  `id` varchar(50) NOT NULL,
  `name` varchar(50) DEFAULT NULL,
  `length` int DEFAULT NULL,
  `date_of_release` date DEFAULT NULL,
  `items_sold` int DEFAULT NULL,
  `ratings` float DEFAULT NULL,
  `explicit` tinyint(1) DEFAULT NULL,
  `lp` tinyint(1) DEFAULT NULL,
  `ep` tinyint(1) DEFAULT NULL,
  `single` tinyint(1) DEFAULT NULL,
  `mixtape` tinyint(1) DEFAULT NULL,
  PRIMARY KEY (`id`)
) ENGINE=InnoDB DEFAULT CHARSET=utf8mb4 COLLATE=utf8mb4_0900_ai_ci;
/*!40101 SET character_set_client = @saved_cs_client */;

--
-- Dumping data for table `album`
--

LOCK TABLES `album` WRITE;
/*!40000 ALTER TABLE `album` DISABLE KEYS */;
INSERT INTO `album` VALUES ('370929bc-acb4-45ac-8256-af759f4fafb2','Lemonade',42,'2016-04-26',NULL,10,0,0,0,0,0),('389f6e9c-ca3d-474e-9686-76d9101dc7f2','folkore',63,'2020-07-22',NULL,8.33333,0,0,0,0,0),('618d65fa-7746-4e1a-addf-eeadf9eab7c2','After Hours',56,'2020-06-25',NULL,9,0,0,0,0,0),('c13fa464-783d-42eb-8d68-874f80ddb121','Renaissance',62,'2022-06-29',NULL,10,0,0,0,0,0);
/*!40000 ALTER TABLE `album` ENABLE KEYS */;
UNLOCK TABLES;

--
-- Table structure for table `album_awards`
--

DROP TABLE IF EXISTS `album_awards`;
/*!40101 SET @saved_cs_client     = @@character_set_client */;
/*!50503 SET character_set_client = utf8mb4 */;
CREATE TABLE `album_awards` (
  `album_id` varchar(50) NOT NULL,
  `award_id` varchar(50) NOT NULL,
  PRIMARY KEY (`album_id`,`award_id`),
  KEY `award_id` (`award_id`),
  CONSTRAINT `album_awards_ibfk_1` FOREIGN KEY (`album_id`) REFERENCES `album` (`id`),
  CONSTRAINT `album_awards_ibfk_2` FOREIGN KEY (`award_id`) REFERENCES `award` (`id`)
) ENGINE=InnoDB DEFAULT CHARSET=utf8mb4 COLLATE=utf8mb4_0900_ai_ci;
/*!40101 SET character_set_client = @saved_cs_client */;

--
-- Dumping data for table `album_awards`
--

LOCK TABLES `album_awards` WRITE;
/*!40000 ALTER TABLE `album_awards` DISABLE KEYS */;
INSERT INTO `album_awards` VALUES ('389f6e9c-ca3d-474e-9686-76d9101dc7f2','fc440184-af9a-492d-ac4b-9132155e8703');
/*!40000 ALTER TABLE `album_awards` ENABLE KEYS */;
UNLOCK TABLES;

--
-- Table structure for table `album_comments`
--

DROP TABLE IF EXISTS `album_comments`;
/*!40101 SET @saved_cs_client     = @@character_set_client */;
/*!50503 SET character_set_client = utf8mb4 */;
CREATE TABLE `album_comments` (
  `album_id` varchar(50) NOT NULL,
  `comment_id` varchar(50) NOT NULL,
  PRIMARY KEY (`album_id`,`comment_id`),
  KEY `comment_id` (`comment_id`),
  CONSTRAINT `album_comments_ibfk_1` FOREIGN KEY (`album_id`) REFERENCES `album` (`id`),
  CONSTRAINT `album_comments_ibfk_2` FOREIGN KEY (`comment_id`) REFERENCES `comment` (`id`)
) ENGINE=InnoDB DEFAULT CHARSET=utf8mb4 COLLATE=utf8mb4_0900_ai_ci;
/*!40101 SET character_set_client = @saved_cs_client */;

--
-- Dumping data for table `album_comments`
--

LOCK TABLES `album_comments` WRITE;
/*!40000 ALTER TABLE `album_comments` DISABLE KEYS */;
/*!40000 ALTER TABLE `album_comments` ENABLE KEYS */;
UNLOCK TABLES;

--
-- Table structure for table `album_genres`
--

DROP TABLE IF EXISTS `album_genres`;
/*!40101 SET @saved_cs_client     = @@character_set_client */;
/*!50503 SET character_set_client = utf8mb4 */;
CREATE TABLE `album_genres` (
  `album_id` varchar(50) NOT NULL,
  `genre_name` varchar(50) NOT NULL,
  PRIMARY KEY (`album_id`,`genre_name`),
  KEY `genre_name` (`genre_name`),
  CONSTRAINT `album_genres_ibfk_1` FOREIGN KEY (`album_id`) REFERENCES `album` (`id`),
  CONSTRAINT `album_genres_ibfk_2` FOREIGN KEY (`genre_name`) REFERENCES `genre` (`name`)
) ENGINE=InnoDB DEFAULT CHARSET=utf8mb4 COLLATE=utf8mb4_0900_ai_ci;
/*!40101 SET character_set_client = @saved_cs_client */;

--
-- Dumping data for table `album_genres`
--

LOCK TABLES `album_genres` WRITE;
/*!40000 ALTER TABLE `album_genres` DISABLE KEYS */;
/*!40000 ALTER TABLE `album_genres` ENABLE KEYS */;
UNLOCK TABLES;

--
-- Table structure for table `album_song_association`
--

DROP TABLE IF EXISTS `album_song_association`;
/*!40101 SET @saved_cs_client     = @@character_set_client */;
/*!50503 SET character_set_client = utf8mb4 */;
CREATE TABLE `album_song_association` (
  `album_id` varchar(50) NOT NULL,
  `song_id` varchar(50) NOT NULL,
  PRIMARY KEY (`album_id`,`song_id`),
  KEY `song_id` (`song_id`),
  CONSTRAINT `album_song_association_ibfk_1` FOREIGN KEY (`album_id`) REFERENCES `album` (`id`),
  CONSTRAINT `album_song_association_ibfk_2` FOREIGN KEY (`song_id`) REFERENCES `song` (`id`)
) ENGINE=InnoDB DEFAULT CHARSET=utf8mb4 COLLATE=utf8mb4_0900_ai_ci;
/*!40101 SET character_set_client = @saved_cs_client */;

--
-- Dumping data for table `album_song_association`
--

LOCK TABLES `album_song_association` WRITE;
/*!40000 ALTER TABLE `album_song_association` DISABLE KEYS */;
/*!40000 ALTER TABLE `album_song_association` ENABLE KEYS */;
UNLOCK TABLES;

--
-- Table structure for table `artist`
--

DROP TABLE IF EXISTS `artist`;
/*!40101 SET @saved_cs_client     = @@character_set_client */;
/*!50503 SET character_set_client = utf8mb4 */;
CREATE TABLE `artist` (
  `id` varchar(50) NOT NULL,
  `name` varchar(50) DEFAULT NULL,
  `date_of_birth` date DEFAULT NULL,
  `date_of_death` date DEFAULT NULL,
  `ratings` float DEFAULT NULL,
  `vocalist` tinyint(1) DEFAULT NULL,
  `musician` tinyint(1) DEFAULT NULL,
  `producer` tinyint(1) DEFAULT NULL,
  `writer` tinyint(1) DEFAULT NULL,
  `engineer` tinyint(1) DEFAULT NULL,
  `biography` text,
  `country_name` varchar(25) NOT NULL,
  `record_label_id` varchar(25) DEFAULT NULL,
  PRIMARY KEY (`id`),
  KEY `country_name` (`country_name`),
  KEY `record_label_id` (`record_label_id`),
  CONSTRAINT `artist_ibfk_1` FOREIGN KEY (`country_name`) REFERENCES `country` (`name`),
  CONSTRAINT `artist_ibfk_2` FOREIGN KEY (`record_label_id`) REFERENCES `record_label` (`id`)
) ENGINE=InnoDB DEFAULT CHARSET=utf8mb4 COLLATE=utf8mb4_0900_ai_ci;
/*!40101 SET character_set_client = @saved_cs_client */;

--
-- Dumping data for table `artist`
--

LOCK TABLES `artist` WRITE;
/*!40000 ALTER TABLE `artist` DISABLE KEYS */;
INSERT INTO `artist` VALUES ('3bb6f5f0-f4e4-4c18-91e6-4de888eb717e','The Weeknd','1990-02-16',NULL,NULL,1,1,1,1,1,NULL,'usa',NULL),('56157736-32aa-429f-a80f-08cac7e39eda','Taylor Swift','1989-12-13',NULL,NULL,1,1,1,1,1,NULL,'usa',NULL),('793faf81-b5d3-462b-a96b-6e44b4733b2f','Beyonce','1981-09-03',NULL,NULL,1,1,1,1,1,NULL,'usa',NULL);
/*!40000 ALTER TABLE `artist` ENABLE KEYS */;
UNLOCK TABLES;

--
-- Table structure for table `artist_album_association`
--

DROP TABLE IF EXISTS `artist_album_association`;
/*!40101 SET @saved_cs_client     = @@character_set_client */;
/*!50503 SET character_set_client = utf8mb4 */;
CREATE TABLE `artist_album_association` (
  `artist_id` varchar(50) NOT NULL,
  `album_id` varchar(50) NOT NULL,
  PRIMARY KEY (`artist_id`,`album_id`),
  KEY `album_id` (`album_id`),
  CONSTRAINT `artist_album_association_ibfk_1` FOREIGN KEY (`artist_id`) REFERENCES `artist` (`id`),
  CONSTRAINT `artist_album_association_ibfk_2` FOREIGN KEY (`album_id`) REFERENCES `album` (`id`)
) ENGINE=InnoDB DEFAULT CHARSET=utf8mb4 COLLATE=utf8mb4_0900_ai_ci;
/*!40101 SET character_set_client = @saved_cs_client */;

--
-- Dumping data for table `artist_album_association`
--

LOCK TABLES `artist_album_association` WRITE;
/*!40000 ALTER TABLE `artist_album_association` DISABLE KEYS */;
INSERT INTO `artist_album_association` VALUES ('793faf81-b5d3-462b-a96b-6e44b4733b2f','370929bc-acb4-45ac-8256-af759f4fafb2'),('56157736-32aa-429f-a80f-08cac7e39eda','389f6e9c-ca3d-474e-9686-76d9101dc7f2'),('3bb6f5f0-f4e4-4c18-91e6-4de888eb717e','618d65fa-7746-4e1a-addf-eeadf9eab7c2'),('793faf81-b5d3-462b-a96b-6e44b4733b2f','c13fa464-783d-42eb-8d68-874f80ddb121');
/*!40000 ALTER TABLE `artist_album_association` ENABLE KEYS */;
UNLOCK TABLES;

--
-- Table structure for table `artist_awards`
--

DROP TABLE IF EXISTS `artist_awards`;
/*!40101 SET @saved_cs_client     = @@character_set_client */;
/*!50503 SET character_set_client = utf8mb4 */;
CREATE TABLE `artist_awards` (
  `artist_id` varchar(50) NOT NULL,
  `award_id` varchar(50) NOT NULL,
  PRIMARY KEY (`artist_id`,`award_id`),
  KEY `award_id` (`award_id`),
  CONSTRAINT `artist_awards_ibfk_1` FOREIGN KEY (`artist_id`) REFERENCES `artist` (`id`),
  CONSTRAINT `artist_awards_ibfk_2` FOREIGN KEY (`award_id`) REFERENCES `award` (`id`)
) ENGINE=InnoDB DEFAULT CHARSET=utf8mb4 COLLATE=utf8mb4_0900_ai_ci;
/*!40101 SET character_set_client = @saved_cs_client */;

--
-- Dumping data for table `artist_awards`
--

LOCK TABLES `artist_awards` WRITE;
/*!40000 ALTER TABLE `artist_awards` DISABLE KEYS */;
/*!40000 ALTER TABLE `artist_awards` ENABLE KEYS */;
UNLOCK TABLES;

--
-- Table structure for table `artist_comments`
--

DROP TABLE IF EXISTS `artist_comments`;
/*!40101 SET @saved_cs_client     = @@character_set_client */;
/*!50503 SET character_set_client = utf8mb4 */;
CREATE TABLE `artist_comments` (
  `artist_id` varchar(50) NOT NULL,
  `comment_id` varchar(50) NOT NULL,
  PRIMARY KEY (`artist_id`,`comment_id`),
  KEY `comment_id` (`comment_id`),
  CONSTRAINT `artist_comments_ibfk_1` FOREIGN KEY (`artist_id`) REFERENCES `artist` (`id`),
  CONSTRAINT `artist_comments_ibfk_2` FOREIGN KEY (`comment_id`) REFERENCES `comment` (`id`)
) ENGINE=InnoDB DEFAULT CHARSET=utf8mb4 COLLATE=utf8mb4_0900_ai_ci;
/*!40101 SET character_set_client = @saved_cs_client */;

--
-- Dumping data for table `artist_comments`
--

LOCK TABLES `artist_comments` WRITE;
/*!40000 ALTER TABLE `artist_comments` DISABLE KEYS */;
/*!40000 ALTER TABLE `artist_comments` ENABLE KEYS */;
UNLOCK TABLES;

--
-- Table structure for table `artist_genres`
--

DROP TABLE IF EXISTS `artist_genres`;
/*!40101 SET @saved_cs_client     = @@character_set_client */;
/*!50503 SET character_set_client = utf8mb4 */;
CREATE TABLE `artist_genres` (
  `artist_id` varchar(50) NOT NULL,
  `genre_name` varchar(50) NOT NULL,
  PRIMARY KEY (`artist_id`,`genre_name`),
  KEY `genre_name` (`genre_name`),
  CONSTRAINT `artist_genres_ibfk_1` FOREIGN KEY (`artist_id`) REFERENCES `artist` (`id`),
  CONSTRAINT `artist_genres_ibfk_2` FOREIGN KEY (`genre_name`) REFERENCES `genre` (`name`)
) ENGINE=InnoDB DEFAULT CHARSET=utf8mb4 COLLATE=utf8mb4_0900_ai_ci;
/*!40101 SET character_set_client = @saved_cs_client */;

--
-- Dumping data for table `artist_genres`
--

LOCK TABLES `artist_genres` WRITE;
/*!40000 ALTER TABLE `artist_genres` DISABLE KEYS */;
/*!40000 ALTER TABLE `artist_genres` ENABLE KEYS */;
UNLOCK TABLES;

--
-- Table structure for table `artist_song_association`
--

DROP TABLE IF EXISTS `artist_song_association`;
/*!40101 SET @saved_cs_client     = @@character_set_client */;
/*!50503 SET character_set_client = utf8mb4 */;
CREATE TABLE `artist_song_association` (
  `artist_id` varchar(50) NOT NULL,
  `song_id` varchar(50) NOT NULL,
  PRIMARY KEY (`artist_id`,`song_id`),
  KEY `song_id` (`song_id`),
  CONSTRAINT `artist_song_association_ibfk_1` FOREIGN KEY (`artist_id`) REFERENCES `artist` (`id`),
  CONSTRAINT `artist_song_association_ibfk_2` FOREIGN KEY (`song_id`) REFERENCES `song` (`id`)
) ENGINE=InnoDB DEFAULT CHARSET=utf8mb4 COLLATE=utf8mb4_0900_ai_ci;
/*!40101 SET character_set_client = @saved_cs_client */;

--
-- Dumping data for table `artist_song_association`
--

LOCK TABLES `artist_song_association` WRITE;
/*!40000 ALTER TABLE `artist_song_association` DISABLE KEYS */;
/*!40000 ALTER TABLE `artist_song_association` ENABLE KEYS */;
UNLOCK TABLES;

--
-- Table structure for table `award`
--

DROP TABLE IF EXISTS `award`;
/*!40101 SET @saved_cs_client     = @@character_set_client */;
/*!50503 SET character_set_client = utf8mb4 */;
CREATE TABLE `award` (
  `id` varchar(50) NOT NULL,
  `name` varchar(50) DEFAULT NULL,
  `category` varchar(50) DEFAULT NULL,
  `award_date` date DEFAULT NULL,
  PRIMARY KEY (`id`),
  UNIQUE KEY `award_uc` (`name`,`category`,`award_date`)
) ENGINE=InnoDB DEFAULT CHARSET=utf8mb4 COLLATE=utf8mb4_0900_ai_ci;
/*!40101 SET character_set_client = @saved_cs_client */;

--
-- Dumping data for table `award`
--

LOCK TABLES `award` WRITE;
/*!40000 ALTER TABLE `award` DISABLE KEYS */;
INSERT INTO `award` VALUES ('fc440184-af9a-492d-ac4b-9132155e8703','Grammy Awards','Best Album','2021-03-14'),('e7663c74-7741-441b-a7d1-2a911695e247','Grammy Awards','Best Electro/Dance Album','2023-02-14'),('131c66f7-8276-40c4-9a48-bb16333edef5','Grammy Awards','Best R&B Song','2023-02-14');
/*!40000 ALTER TABLE `award` ENABLE KEYS */;
UNLOCK TABLES;

--
-- Table structure for table `comment`
--

DROP TABLE IF EXISTS `comment`;
/*!40101 SET @saved_cs_client     = @@character_set_client */;
/*!50503 SET character_set_client = utf8mb4 */;
CREATE TABLE `comment` (
  `id` varchar(50) NOT NULL,
  `header` varchar(25) DEFAULT NULL,
  `text` varchar(1000) DEFAULT NULL,
  `date_time` datetime DEFAULT NULL,
  `ratings` float DEFAULT NULL,
  `user_username` varchar(50) NOT NULL,
  PRIMARY KEY (`id`),
  KEY `user_username` (`user_username`),
  CONSTRAINT `comment_ibfk_1` FOREIGN KEY (`user_username`) REFERENCES `user` (`username`)
) ENGINE=InnoDB DEFAULT CHARSET=utf8mb4 COLLATE=utf8mb4_0900_ai_ci;
/*!40101 SET character_set_client = @saved_cs_client */;

--
-- Dumping data for table `comment`
--

LOCK TABLES `comment` WRITE;
/*!40000 ALTER TABLE `comment` DISABLE KEYS */;
/*!40000 ALTER TABLE `comment` ENABLE KEYS */;
UNLOCK TABLES;

--
-- Table structure for table `country`
--

DROP TABLE IF EXISTS `country`;
/*!40101 SET @saved_cs_client     = @@character_set_client */;
/*!50503 SET character_set_client = utf8mb4 */;
CREATE TABLE `country` (
  `name` varchar(50) NOT NULL,
  PRIMARY KEY (`name`),
  KEY `ix_country_name` (`name`)
) ENGINE=InnoDB DEFAULT CHARSET=utf8mb4 COLLATE=utf8mb4_0900_ai_ci;
/*!40101 SET character_set_client = @saved_cs_client */;

--
-- Dumping data for table `country`
--

LOCK TABLES `country` WRITE;
/*!40000 ALTER TABLE `country` DISABLE KEYS */;
INSERT INTO `country` VALUES ('Serbia'),('usa');
/*!40000 ALTER TABLE `country` ENABLE KEYS */;
UNLOCK TABLES;

--
-- Table structure for table `genre`
--

DROP TABLE IF EXISTS `genre`;
/*!40101 SET @saved_cs_client     = @@character_set_client */;
/*!50503 SET character_set_client = utf8mb4 */;
CREATE TABLE `genre` (
  `name` varchar(50) NOT NULL,
  PRIMARY KEY (`name`)
) ENGINE=InnoDB DEFAULT CHARSET=utf8mb4 COLLATE=utf8mb4_0900_ai_ci;
/*!40101 SET character_set_client = @saved_cs_client */;

--
-- Dumping data for table `genre`
--

LOCK TABLES `genre` WRITE;
/*!40000 ALTER TABLE `genre` DISABLE KEYS */;
INSERT INTO `genre` VALUES ('disco'),('folk'),('r&b');
/*!40000 ALTER TABLE `genre` ENABLE KEYS */;
UNLOCK TABLES;

--
-- Table structure for table `record_label`
--

DROP TABLE IF EXISTS `record_label`;
/*!40101 SET @saved_cs_client     = @@character_set_client */;
/*!50503 SET character_set_client = utf8mb4 */;
CREATE TABLE `record_label` (
  `id` varchar(50) NOT NULL,
  `name` varchar(50) DEFAULT NULL,
  `address` varchar(50) DEFAULT NULL,
  `date_founded` date DEFAULT NULL,
  `ceo` varchar(50) DEFAULT NULL,
  `ratings` float DEFAULT NULL,
  `biography` text,
  `country_name` varchar(25) NOT NULL,
  PRIMARY KEY (`id`),
  KEY `ix_record_label_country_name` (`country_name`),
  CONSTRAINT `record_label_ibfk_1` FOREIGN KEY (`country_name`) REFERENCES `country` (`name`)
) ENGINE=InnoDB DEFAULT CHARSET=utf8mb4 COLLATE=utf8mb4_0900_ai_ci;
/*!40101 SET character_set_client = @saved_cs_client */;

--
-- Dumping data for table `record_label`
--

LOCK TABLES `record_label` WRITE;
/*!40000 ALTER TABLE `record_label` DISABLE KEYS */;
INSERT INTO `record_label` VALUES ('64fe8277-5fcd-4664-b786-16ce3291f60c','Parkwood-Entertainment','Somwere in America','2010-09-09','Beyonce',0,'','usa');
/*!40000 ALTER TABLE `record_label` ENABLE KEYS */;
UNLOCK TABLES;

--
-- Table structure for table `song`
--

DROP TABLE IF EXISTS `song`;
/*!40101 SET @saved_cs_client     = @@character_set_client */;
/*!50503 SET character_set_client = utf8mb4 */;
CREATE TABLE `song` (
  `id` varchar(50) NOT NULL,
  `name` varchar(50) NOT NULL,
  `length` int NOT NULL,
  `date_of_release` date NOT NULL,
  `items_sold` int DEFAULT NULL,
  `lyrics` text,
  `ratings` float DEFAULT NULL,
  `explicit` tinyint(1) DEFAULT NULL,
  PRIMARY KEY (`id`)
) ENGINE=InnoDB DEFAULT CHARSET=utf8mb4 COLLATE=utf8mb4_0900_ai_ci;
/*!40101 SET character_set_client = @saved_cs_client */;

--
-- Dumping data for table `song`
--

LOCK TABLES `song` WRITE;
/*!40000 ALTER TABLE `song` DISABLE KEYS */;
INSERT INTO `song` VALUES ('1a6d567b-2695-4087-9b3f-4297b98683ae','the 1',227,'2020-07-29',NULL,NULL,NULL,0),('3c6688f4-7e34-440a-9538-6d89c2ee463d','Blinding Lights',200,'2020-05-02',NULL,NULL,NULL,0),('c51a5350-86f1-46ab-a6bb-e0de8ff51ab6','In Your Eyes',237,'2020-05-02',NULL,NULL,NULL,0),('c557df4a-51dd-43c5-98ad-5b2e2d2c875a','CUFF IT',240,'2022-06-22',NULL,NULL,NULL,0);
/*!40000 ALTER TABLE `song` ENABLE KEYS */;
UNLOCK TABLES;

--
-- Table structure for table `song_awards`
--

DROP TABLE IF EXISTS `song_awards`;
/*!40101 SET @saved_cs_client     = @@character_set_client */;
/*!50503 SET character_set_client = utf8mb4 */;
CREATE TABLE `song_awards` (
  `song_id` varchar(50) NOT NULL,
  `award_id` varchar(50) NOT NULL,
  PRIMARY KEY (`song_id`,`award_id`),
  KEY `award_id` (`award_id`),
  CONSTRAINT `song_awards_ibfk_1` FOREIGN KEY (`song_id`) REFERENCES `song` (`id`),
  CONSTRAINT `song_awards_ibfk_2` FOREIGN KEY (`award_id`) REFERENCES `award` (`id`)
) ENGINE=InnoDB DEFAULT CHARSET=utf8mb4 COLLATE=utf8mb4_0900_ai_ci;
/*!40101 SET character_set_client = @saved_cs_client */;

--
-- Dumping data for table `song_awards`
--

LOCK TABLES `song_awards` WRITE;
/*!40000 ALTER TABLE `song_awards` DISABLE KEYS */;
/*!40000 ALTER TABLE `song_awards` ENABLE KEYS */;
UNLOCK TABLES;

--
-- Table structure for table `song_comments`
--

DROP TABLE IF EXISTS `song_comments`;
/*!40101 SET @saved_cs_client     = @@character_set_client */;
/*!50503 SET character_set_client = utf8mb4 */;
CREATE TABLE `song_comments` (
  `song_id` varchar(50) NOT NULL,
  `comment_id` varchar(50) NOT NULL,
  PRIMARY KEY (`song_id`,`comment_id`),
  KEY `comment_id` (`comment_id`),
  CONSTRAINT `song_comments_ibfk_1` FOREIGN KEY (`song_id`) REFERENCES `song` (`id`),
  CONSTRAINT `song_comments_ibfk_2` FOREIGN KEY (`comment_id`) REFERENCES `comment` (`id`)
) ENGINE=InnoDB DEFAULT CHARSET=utf8mb4 COLLATE=utf8mb4_0900_ai_ci;
/*!40101 SET character_set_client = @saved_cs_client */;

--
-- Dumping data for table `song_comments`
--

LOCK TABLES `song_comments` WRITE;
/*!40000 ALTER TABLE `song_comments` DISABLE KEYS */;
/*!40000 ALTER TABLE `song_comments` ENABLE KEYS */;
UNLOCK TABLES;

--
-- Table structure for table `song_genres`
--

DROP TABLE IF EXISTS `song_genres`;
/*!40101 SET @saved_cs_client     = @@character_set_client */;
/*!50503 SET character_set_client = utf8mb4 */;
CREATE TABLE `song_genres` (
  `song_id` varchar(50) NOT NULL,
  `genre_name` varchar(50) NOT NULL,
  PRIMARY KEY (`song_id`,`genre_name`),
  KEY `genre_name` (`genre_name`),
  CONSTRAINT `song_genres_ibfk_1` FOREIGN KEY (`song_id`) REFERENCES `song` (`id`),
  CONSTRAINT `song_genres_ibfk_2` FOREIGN KEY (`genre_name`) REFERENCES `genre` (`name`)
) ENGINE=InnoDB DEFAULT CHARSET=utf8mb4 COLLATE=utf8mb4_0900_ai_ci;
/*!40101 SET character_set_client = @saved_cs_client */;

--
-- Dumping data for table `song_genres`
--

LOCK TABLES `song_genres` WRITE;
/*!40000 ALTER TABLE `song_genres` DISABLE KEYS */;
/*!40000 ALTER TABLE `song_genres` ENABLE KEYS */;
UNLOCK TABLES;

--
-- Table structure for table `user`
--

DROP TABLE IF EXISTS `user`;
/*!40101 SET @saved_cs_client     = @@character_set_client */;
/*!50503 SET character_set_client = utf8mb4 */;
CREATE TABLE `user` (
  `username` varchar(50) NOT NULL,
  `email` varchar(100) DEFAULT NULL,
  `password` varchar(100) DEFAULT NULL,
  `name` varchar(25) DEFAULT NULL,
  `surname` varchar(25) DEFAULT NULL,
  `date_of_birth` date DEFAULT NULL,
  `critic` tinyint(1) DEFAULT NULL,
  `writer` tinyint(1) DEFAULT NULL,
  `super_user` tinyint(1) DEFAULT NULL,
  `country_name` varchar(25) NOT NULL,
  PRIMARY KEY (`username`),
  UNIQUE KEY `email` (`email`),
  KEY `ix_user_country_name` (`country_name`),
  CONSTRAINT `user_ibfk_1` FOREIGN KEY (`country_name`) REFERENCES `country` (`name`)
) ENGINE=InnoDB DEFAULT CHARSET=utf8mb4 COLLATE=utf8mb4_0900_ai_ci;
/*!40101 SET character_set_client = @saved_cs_client */;

--
-- Dumping data for table `user`
--

LOCK TABLES `user` WRITE;
/*!40000 ALTER TABLE `user` DISABLE KEYS */;
INSERT INTO `user` VALUES ('critic1','critci1@gmail.com','d74ff0ee8da3b9806b18c877dbf29bbde50b5bd8e4dad7a3a725000feb82e8f1','crtitic','critikovic','1981-02-02',1,0,0,'usa'),('critic2','critci2@gmail.com','d74ff0ee8da3b9806b18c877dbf29bbde50b5bd8e4dad7a3a725000feb82e8f1','bad','guy','1931-02-02',1,0,0,'usa'),('critic3','critci3@gmail.com','d74ff0ee8da3b9806b18c877dbf29bbde50b5bd8e4dad7a3a725000feb82e8f1','good','guy','1944-02-02',1,0,0,'usa'),('superuser','super@hotmail.com','73d1b1b1bc1dabfb97f216d897b7968e44b06457920f00f2dc6c1ed3be25ad4c','super','user','2012-12-21',0,0,1,'usa'),('user1','user1@hotmail.com','04f8996da763b7a969b1028ee3007569eaf3a635486ddab211d512c85b9df8fb','neko','tamo','1995-01-01',0,0,0,'serbia'),('user2','user2@hotmail.com','04f8996da763b7a969b1028ee3007569eaf3a635486ddab211d512c85b9df8fb','neko','tamo','1992-01-01',0,0,0,'serbia'),('user3','user3@hotmail.com','04f8996da763b7a969b1028ee3007569eaf3a635486ddab211d512c85b9df8fb','neko','tamo','1993-01-01',0,0,0,'serbia'),('writer','writer1@gmail.com','d74ff0ee8da3b9806b18c877dbf29bbde50b5bd8e4dad7a3a725000feb82e8f1','pisac','vesti','1971-01-01',0,1,0,'serbia');
/*!40000 ALTER TABLE `user` ENABLE KEYS */;
UNLOCK TABLES;

--
-- Table structure for table `user_ratings`
--

DROP TABLE IF EXISTS `user_ratings`;
/*!40101 SET @saved_cs_client     = @@character_set_client */;
/*!50503 SET character_set_client = utf8mb4 */;
CREATE TABLE `user_ratings` (
  `id` varchar(50) NOT NULL,
  `user_username` varchar(50) DEFAULT NULL,
  `album_id` varchar(50) DEFAULT NULL,
  `artist_id` varchar(50) DEFAULT NULL,
  `song_id` varchar(50) DEFAULT NULL,
  `rating` int DEFAULT NULL,
  PRIMARY KEY (`id`),
  UNIQUE KEY `album_user_rating_uc` (`user_username`,`album_id`),
  UNIQUE KEY `artist_user_rating_uc` (`user_username`,`artist_id`),
  UNIQUE KEY `song_user_rating_uc` (`user_username`,`song_id`),
  KEY `album_id` (`album_id`),
  KEY `artist_id` (`artist_id`),
  KEY `song_id` (`song_id`),
  CONSTRAINT `user_ratings_ibfk_1` FOREIGN KEY (`user_username`) REFERENCES `user` (`username`),
  CONSTRAINT `user_ratings_ibfk_2` FOREIGN KEY (`album_id`) REFERENCES `album` (`id`),
  CONSTRAINT `user_ratings_ibfk_3` FOREIGN KEY (`artist_id`) REFERENCES `artist` (`id`),
  CONSTRAINT `user_ratings_ibfk_4` FOREIGN KEY (`song_id`) REFERENCES `song` (`id`)
) ENGINE=InnoDB DEFAULT CHARSET=utf8mb4 COLLATE=utf8mb4_0900_ai_ci;
/*!40101 SET character_set_client = @saved_cs_client */;

--
-- Dumping data for table `user_ratings`
--

LOCK TABLES `user_ratings` WRITE;
/*!40000 ALTER TABLE `user_ratings` DISABLE KEYS */;
INSERT INTO `user_ratings` VALUES ('1b341653-f1c0-4d63-a3c0-d7d48d6742d7','user2','389f6e9c-ca3d-474e-9686-76d9101dc7f2',NULL,NULL,7),('68144aeb-d34f-476a-be28-2ef5dde57896','user1','618d65fa-7746-4e1a-addf-eeadf9eab7c2',NULL,NULL,9),('7950bdef-e6e4-4154-9e3a-458dc8a3c662','user1','389f6e9c-ca3d-474e-9686-76d9101dc7f2',NULL,NULL,9),('914a601f-f273-4c44-8cc0-0fe42f49661f','user1','c13fa464-783d-42eb-8d68-874f80ddb121',NULL,NULL,10),('cedf2d57-cad5-4dc8-822d-4cb3acf1f766','user1','370929bc-acb4-45ac-8256-af759f4fafb2',NULL,NULL,10),('e9631e77-c12c-4a9b-b195-43de090ea8c1','user3','389f6e9c-ca3d-474e-9686-76d9101dc7f2',NULL,NULL,9);
/*!40000 ALTER TABLE `user_ratings` ENABLE KEYS */;
UNLOCK TABLES;
/*!40103 SET TIME_ZONE=@OLD_TIME_ZONE */;

/*!40101 SET SQL_MODE=@OLD_SQL_MODE */;
/*!40014 SET FOREIGN_KEY_CHECKS=@OLD_FOREIGN_KEY_CHECKS */;
/*!40014 SET UNIQUE_CHECKS=@OLD_UNIQUE_CHECKS */;
/*!40101 SET CHARACTER_SET_CLIENT=@OLD_CHARACTER_SET_CLIENT */;
/*!40101 SET CHARACTER_SET_RESULTS=@OLD_CHARACTER_SET_RESULTS */;
/*!40101 SET COLLATION_CONNECTION=@OLD_COLLATION_CONNECTION */;
/*!40111 SET SQL_NOTES=@OLD_SQL_NOTES */;

-- Dump completed on 2023-02-22 19:23:07
