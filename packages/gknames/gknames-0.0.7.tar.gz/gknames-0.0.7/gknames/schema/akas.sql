DROP TABLE `akas`;

CREATE TABLE `akas` (
  `id` int unsigned NOT NULL AUTO_INCREMENT,
  `event_id` int unsigned NOT NULL,
  `object_id` bigint unsigned NOT NULL,
  `aka` varchar(30),
  `ra` double NOT NULL,
  `decl` double NOT NULL,
  `survey_database` varchar(50) NOT NULL,
  `user_id` varchar(50) NOT NULL,
  `source_ip` varchar(20),
  `original_flag_date` DATE,
  `date_inserted` timestamp NOT NULL DEFAULT CURRENT_TIMESTAMP,
  `htm16ID` bigint unsigned NOT NULL,
  PRIMARY KEY `idx_id` (`id`),
  UNIQUE KEY `idx_object_id_survey_database` (`object_id`, `survey_database`),
  KEY `idx_htm16ID` (`htm16ID`),
  KEY `idx_aka` (`aka`)
) ENGINE=InnoDB
;
