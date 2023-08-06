DROP DATABASE IF EXISTS memsql_demo;
CREATE DATABASE IF NOT EXISTS memsql_demo;

USE memsql_demo;

--
-- Table structure for table `region`
--
DROP TABLE IF EXISTS `region`;
CREATE ROWSTORE TABLE IF NOT EXISTS `region` (
  `regionkey` int(11) NOT NULL,
  `name` char(25) CHARACTER SET utf8 COLLATE utf8_general_ci NOT NULL,
  `comment` varchar(152) CHARACTER SET utf8 COLLATE utf8_general_ci NOT NULL,
  PRIMARY KEY (`regionkey`)
) AUTOSTATS_CARDINALITY_MODE=OFF AUTOSTATS_HISTOGRAM_MODE=OFF SQL_MODE='STRICT_ALL_TABLES';

INSERT INTO `region` VALUES (0,'AFRICA',' of the quickly ironic sheaves. furiously permanent pinto beans alongside of the furiously silent theodolites haggl'),(2,'ASIA','tructions wake furiously carefu'),(4,'MIDDLE EAST','tly across the blithely special foxes. furiously express pinto beans boost. bold deposits haggle quickly alo'),(1,'AMERICA','al pinto beans sleep fluffily i'),(3,'EUROPE','express packages. even deposits wake furiousl');

--
-- Table structure for table `nation`
--
DROP TABLE IF EXISTS `nation`;
CREATE ROWSTORE TABLE IF NOT EXISTS  `nation` (
  `nationkey` int(11) NOT NULL,
  `name` char(25) CHARACTER SET utf8 COLLATE utf8_general_ci NOT NULL,
  `regionkey` int(11) NOT NULL,
  `comment` varchar(152) CHARACTER SET utf8 COLLATE utf8_general_ci NOT NULL,
  PRIMARY KEY (`nationkey`),
  KEY `nation_fk1` (`regionkey`)
) AUTOSTATS_CARDINALITY_MODE=OFF AUTOSTATS_HISTOGRAM_MODE=OFF SQL_MODE='STRICT_ALL_TABLES';
INSERT INTO `nation` VALUES (0,'ALGERIA',0,'n dependencies lose blithely above the furiously sp'),(5,'ETHIOPIA',0,'ironic dependencies use careful'),(7,'GERMANY',3,'refully above the slyly final platelets. thinly ironic asy'),(15,'MOROCCO',0,'ns above the special, bold pinto beans wake slyly slyly regular packages! final instructio'),(20,'SAUDI ARABIA',4,'gainst the requests. even packages promise carefully accounts. carefully pendi'),(21,'VIETNAM',2,'notornis. furiously express grouches use blith'),(2,'BRAZIL',1,'l ideas nag alongside of the final, final requests-- slyly express foxes around the unusual packages must w'),(4,'EGYPT',4,' pending, bold instructions sleep across the express accounts. final theodolites sleep against the '),(8,'INDIA',2,'ously! quickly regular accounts wake idly across the slyly final '),(10,'IRAN',4,'uriously bold instructions. quickly final multipli'),(12,'JAPAN',2,' close dependencies are. carefully f'),(24,'UNITED STATES',1,'kages haggle quickly along the patterns. slyly regular packages affix slyly along the blithely final instructi'),(1,'ARGENTINA',1,'r the theodolites. regular platelets cajole carefully bold packages. careful'),(3,'CANADA',1,'fully pending pinto beans sleep furiously unusual accounts. deposits sleep quickly. furiously final r'),(6,'FRANCE',3,'the carefully permanent deposits. pend'),(9,'INDONESIA',2,'e carefully. quickly bold ideas across the sometimes pending accounts sleep along the furiously ironic pinto beans'),(11,'IRAQ',4,'egrate enticing, ironic theodolites. slyly even instructions affix'),(16,'MOZAMBIQUE',0,'y. final accounts across the evenly regular d'),(18,'CHINA',2,'gouts x-ray carefully above the carefully ironic asymptotes. blithely quick sheaves wake. q'),(19,'ROMANIA',3,'leep final pinto beans. slyly ironic gifts cajole slyly above the theodolites. bold, pending pinto beans mold c'),(22,'RUSSIA',3,'t instructions are fluffily. quickly ironic theodolites according to the slyly '),(13,'JORDAN',4,'egular warthogs cajole. bold, even notornis haggle furi'),(14,'KENYA',0,'ly regular asymptotes sleep according to the requests. daringly ironic ideas nag along the fu'),(17,'PERU',1,'quickly regular accounts carefully even accounts cajole slyly. quickly silent theodolites nod slyly unusu'),(23,'UNITED KINGDOM',3,'lithely regular ideas boost carefully. furiously ironic depen');


DROP TABLE IF EXISTS `customer`;
CREATE ROWSTORE TABLE IF NOT EXISTS  `customer` (
  `custkey` int(11) NOT NULL AUTO_INCREMENT,
  `name` varchar(25) CHARACTER SET utf8 COLLATE utf8_general_ci NOT NULL,
  `address` varchar(40) CHARACTER SET utf8 COLLATE utf8_general_ci NOT NULL,
  `nationkey` int(11) NOT NULL,
  `phone` char(15) CHARACTER SET utf8 COLLATE utf8_general_ci NOT NULL,
  `acctbal` decimal(15,2) NOT NULL,
  `mktsegment` char(10) CHARACTER SET utf8 COLLATE utf8_general_ci NOT NULL,
  `comment` varchar(117) CHARACTER SET utf8 COLLATE utf8_general_ci NOT NULL,
  PRIMARY KEY (`custkey`),
  KEY `customer_fk1` (`nationkey`)
) AUTOSTATS_CARDINALITY_MODE=OFF AUTOSTATS_HISTOGRAM_MODE=OFF SQL_MODE='STRICT_ALL_TABLES';

DROP TABLE IF EXISTS `orders`;
CREATE ROWSTORE TABLE IF NOT EXISTS  `orders` (
  `orderkey` bigint(20) NOT NULL AUTO_INCREMENT,
  `custkey` int(11) DEFAULT NULL,
  `orderstatus` char(1) CHARACTER SET utf8 COLLATE utf8_general_ci DEFAULT NULL,
  `totalprice` decimal(20,2) DEFAULT NULL,
  `orderdate` date DEFAULT NULL,
  `orderpriority` char(15) CHARACTER SET utf8 COLLATE utf8_general_ci DEFAULT NULL,
  `clerk` char(15) CHARACTER SET utf8 COLLATE utf8_general_ci DEFAULT NULL,
  `shippriority` int(11) DEFAULT NULL,
  `comment` varchar(79) CHARACTER SET utf8 COLLATE utf8_general_ci DEFAULT NULL,
  `created` timestamp NOT NULL DEFAULT CURRENT_TIMESTAMP,
  PRIMARY KEY (`orderkey`),
  KEY `orders_fk1` (`custkey`),
  KEY `orders_dt_idx` (`orderdate`),
  KEY `orders_crtd_dt_idx` (`created`)
) AUTOSTATS_CARDINALITY_MODE=OFF AUTOSTATS_HISTOGRAM_MODE=OFF SQL_MODE='STRICT_ALL_TABLES';

DROP TABLE IF EXISTS `part`;
CREATE ROWSTORE TABLE IF NOT EXISTS  `part` (
  `partkey` int(11) NOT NULL AUTO_INCREMENT,
  `name` varchar(55) CHARACTER SET utf8 COLLATE utf8_general_ci NOT NULL,
  `mfgr` char(25) CHARACTER SET utf8 COLLATE utf8_general_ci NOT NULL,
  `brand` char(10) CHARACTER SET utf8 COLLATE utf8_general_ci NOT NULL,
  `type` varchar(25) CHARACTER SET utf8 COLLATE utf8_general_ci NOT NULL,
  `size` int(11) NOT NULL,
  `container` char(10) CHARACTER SET utf8 COLLATE utf8_general_ci NOT NULL,
  `retailprice` decimal(15,2) NOT NULL,
  `comment` varchar(23) CHARACTER SET utf8 COLLATE utf8_general_ci NOT NULL,
  PRIMARY KEY (`partkey`)
) AUTOSTATS_CARDINALITY_MODE=OFF AUTOSTATS_HISTOGRAM_MODE=OFF SQL_MODE='STRICT_ALL_TABLES';

CREATE ROWSTORE TABLE IF NOT EXISTS  `supplier` (
  `suppkey` int(11) NOT NULL AUTO_INCREMENT,
  `name` char(25) CHARACTER SET utf8 COLLATE utf8_general_ci NOT NULL,
  `address` varchar(40) CHARACTER SET utf8 COLLATE utf8_general_ci NOT NULL,
  `nationkey` int(11) NOT NULL,
  `phone` char(15) CHARACTER SET utf8 COLLATE utf8_general_ci NOT NULL,
  `acctbal` decimal(15,2) NOT NULL,
  `comment` varchar(101) CHARACTER SET utf8 COLLATE utf8_general_ci NOT NULL,
  PRIMARY KEY (`suppkey`),
  KEY `supplier_fk1` (`nationkey`)
) AUTOSTATS_CARDINALITY_MODE=OFF AUTOSTATS_HISTOGRAM_MODE=OFF SQL_MODE='STRICT_ALL_TABLES';

CREATE ROWSTORE TABLE IF NOT EXISTS  `partsupp` (
  `partkey` int(11) NOT NULL,
  `suppkey` int(11) NOT NULL,
  `availqty` int(11) NOT NULL,
  `supplycost` decimal(15,2) NOT NULL,
  `comment` varchar(199) CHARACTER SET utf8 COLLATE utf8_general_ci NOT NULL,
  PRIMARY KEY (`partkey`,`suppkey`),
  KEY `partsupp_fk1` (`partkey`),
  KEY `partsupp_fk2` (`suppkey`)
) AUTOSTATS_CARDINALITY_MODE=OFF AUTOSTATS_HISTOGRAM_MODE=OFF SQL_MODE='STRICT_ALL_TABLES';

CREATE ROWSTORE TABLE IF NOT EXISTS  `lineitem` (
  `orderkey` bigint(20) NOT NULL DEFAULT '0',
  `partkey` int(11) DEFAULT NULL,
  `suppkey` int(11) DEFAULT NULL,
  `linenumber` int(11) NOT NULL DEFAULT '0',
  `quantity` decimal(20,2) DEFAULT NULL,
  `extendedprice` decimal(20,2) DEFAULT NULL,
  `discount` decimal(3,2) DEFAULT NULL,
  `tax` decimal(3,2) DEFAULT NULL,
  `returnflag` char(1) CHARACTER SET utf8 COLLATE utf8_general_ci DEFAULT NULL,
  `linestatus` char(1) CHARACTER SET utf8 COLLATE utf8_general_ci DEFAULT NULL,
  `shipdate` date DEFAULT NULL,
  `commitdate` date DEFAULT NULL,
  `receiptdate` date DEFAULT NULL,
  `shipinstruct` varchar(25) CHARACTER SET utf8 COLLATE utf8_general_ci DEFAULT NULL,
  `shipmode` varchar(10) CHARACTER SET utf8 COLLATE utf8_general_ci DEFAULT NULL,
  `comment` varchar(44) CHARACTER SET utf8 COLLATE utf8_general_ci DEFAULT NULL,
  `created` timestamp NOT NULL DEFAULT CURRENT_TIMESTAMP,
  PRIMARY KEY (`orderkey`,`linenumber`),
  KEY `li_shp_dt_idx` (`shipdate`),
  KEY `li_com_dt_idx` (`commitdate`),
  KEY `li_rcpt_dt_idx` (`receiptdate`),
  KEY `li_crtd_dt_idx` (`created`),
  KEY `lineitem_fk2` (`suppkey`),
  KEY `lineitem_fk4` (`partkey`),
  FOREIGN SHARD KEY (`orderkey`) REFERENCES `orders` (`orderkey`) 
) AUTOSTATS_CARDINALITY_MODE=OFF AUTOSTATS_HISTOGRAM_MODE=OFF SQL_MODE='STRICT_ALL_TABLES';


