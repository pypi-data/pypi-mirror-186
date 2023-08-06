DROP TABLE `events`;

CREATE TABLE `events` (
  `id` int unsigned NOT NULL,
  `ra` double NOT NULL,
  `decl` double NOT NULL,
  `ra_original` double NOT NULL,
  `decl_original` double NOT NULL,
  `date_inserted` timestamp NOT NULL DEFAULT CURRENT_TIMESTAMP,
  `date_updated` datetime,
  `year` smallint unsigned NOT NULL,
  `base26suffix` varchar(20) NOT NULL,
  `htm16ID` bigint unsigned NOT NULL,
  PRIMARY KEY `idx_id` (`id`),
  UNIQUE KEY `idx_year_base26suffix` (`year`,`base26suffix`),
  KEY `idx_htm16ID` (`htm16ID`)
) ENGINE=InnoDB
;
