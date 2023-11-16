-- 1. Создать таблицу student с полями student_id serial, first_name varchar, last_name varchar, birthday date,
--phone varchar
CREATE TABLE student
(
	student_id serial,
	ferst_name varchar(30),
	last_name varchar(50),
	birthday date,
	phone varchar(20)
	CONSTRAINT student_id PRIMARY KEY
);

-- 2. Добавить в таблицу student колонку middle_name varchar
ALTER TABLE student ADD COLUMN middle_name varchar;

-- 3. Удалить колонку middle_name
ALTER TABLE student DROP COLUMN middle_name;

-- 4. Переименовать колонку birthday в birth_date
ALTER TABLE student RENAME COLUMN birthday TO birth_date;

-- 5. Изменить тип данных колонки phone на varchar(32)
ALTER TABLE student ALTER COLUMN phone SET DATA TYPE varchar(32);

-- 6. Вставить три любых записи с автогенерацией идентификатора
INSERT INTO student (ferst_name, last_name, birth_date, phone)
VALUES ('Алексей', 'Наумкин', '1990-10-05', '79807142415'),
       ('Тимур', 'Енилеев', '2000-08-19', '79106065599'),
       ('Марк', 'Харитонов', '2011-04-19', '79133961125');
-- 6.1 Исправление ошибки в столбце ferst_name на first_name
ALTER TABLE student RENAME COLUMN ferst_name TO first_name;

-- 7. Удалить все данные из таблицы со сбросом идентификатор в исходное состояние
TRUNCATE TABLE student RESTART IDENTITY;

