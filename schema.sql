CREATE TABLE `survey` (
	`id` integer primary key,
	`name` text,
	`description` text,
	`created` text,
	`lastmodified` text,
	`deleted` text
);

CREATE TABLE 'question'(
	'id' integer primary key,
	'name' text, 
	'text' text,
	'order' integer, 
	'created' text,
	`lastmodified` text,
	`deleted` text
);


CREATE TABLE 'answer'(
	'id' integer primary key,
	'question_id' integer,
	'control_type' text,
	'description' text,
	'order' integer,
	'created' text,
	`lastmodified` text,
	`deleted` text
);


CREATE TABLE 'response'(
	'id' integer primary key,
	'question_id' integer,
	'answer_id' integer, 
	'free_text' text, 
	'created' text,
	`lastmodified` text,
	`deleted` text
);


CREATE TABLE 'user'(
	'id' integer primary key, 
	'ipp4' integer, 
	'created' text,
	`lastmodified` text,
	`deleted` text
);