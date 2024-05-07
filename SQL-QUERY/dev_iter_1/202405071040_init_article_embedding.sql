create table article
(
    `id`          int  primary key,
    `embedding` blob,
    `tags` json
);