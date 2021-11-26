-- phpMyAdmin SQL Dump
-- version 4.6.6deb5ubuntu0.5
-- https://www.phpmyadmin.net/
--
-- Хост: localhost:3306
-- Время создания: Ноя 26 2021 г., 14:11
-- Версия сервера: 5.7.36-0ubuntu0.18.04.1
-- Версия PHP: 7.2.24-0ubuntu0.18.04.10

SET SQL_MODE = "NO_AUTO_VALUE_ON_ZERO";
SET time_zone = "+00:00";


/*!40101 SET @OLD_CHARACTER_SET_CLIENT=@@CHARACTER_SET_CLIENT */;
/*!40101 SET @OLD_CHARACTER_SET_RESULTS=@@CHARACTER_SET_RESULTS */;
/*!40101 SET @OLD_COLLATION_CONNECTION=@@COLLATION_CONNECTION */;
/*!40101 SET NAMES utf8mb4 */;

--
-- База данных: `avagen`
--

-- --------------------------------------------------------

--
-- Структура таблицы `ava`
--

CREATE TABLE `ava` (
  `id` varchar(255) COLLATE utf8mb4_unicode_ci NOT NULL,
  `age` int(1) DEFAULT NULL,
  `sex` int(1) DEFAULT NULL
) ENGINE=InnoDB DEFAULT CHARSET=utf8mb4 COLLATE=utf8mb4_unicode_ci;

-- --------------------------------------------------------

--
-- Структура таблицы `ava_figure`
--

CREATE TABLE `ava_figure` (
  `ava_id` varchar(255) COLLATE utf8mb4_unicode_ci NOT NULL,
  `figure_id` int(11) NOT NULL,
  `fill` varchar(255) COLLATE utf8mb4_unicode_ci NOT NULL
) ENGINE=InnoDB DEFAULT CHARSET=utf8mb4 COLLATE=utf8mb4_unicode_ci;

-- --------------------------------------------------------

--
-- Структура таблицы `figure`
--

CREATE TABLE `figure` (
  `id` int(11) NOT NULL,
  `type` int(11) NOT NULL,
  `age` int(1) DEFAULT NULL,
  `sex` int(1) DEFAULT NULL,
  `rnd_fill` int(1) DEFAULT '0'
) ENGINE=InnoDB DEFAULT CHARSET=utf8mb4 COLLATE=utf8mb4_unicode_ci;

--
-- Дамп данных таблицы `figure`
--

INSERT INTO `figure` (`id`, `type`, `age`, `sex`, `rnd_fill`) VALUES
(1, 1, 25, 1, 0),
(2, 1, NULL, NULL, 0);

-- --------------------------------------------------------

--
-- Структура таблицы `fill`
--

CREATE TABLE `fill` (
  `id` int(11) NOT NULL,
  `value` varchar(255) COLLATE utf8mb4_unicode_ci NOT NULL
) ENGINE=InnoDB DEFAULT CHARSET=utf8mb4 COLLATE=utf8mb4_unicode_ci;

-- --------------------------------------------------------

--
-- Структура таблицы `path`
--

CREATE TABLE `path` (
  `id` int(11) NOT NULL,
  `figure_id` int(11) NOT NULL,
  `d` text COLLATE utf8mb4_unicode_ci NOT NULL,
  `priority` int(5) NOT NULL DEFAULT '1',
  `fill` varchar(255) COLLATE utf8mb4_unicode_ci NOT NULL,
  `extend_fill` int(1) NOT NULL,
  `status` int(1) NOT NULL
) ENGINE=InnoDB DEFAULT CHARSET=utf8mb4 COLLATE=utf8mb4_unicode_ci;

-- --------------------------------------------------------

--
-- Структура таблицы `type`
--

CREATE TABLE `type` (
  `id` int(11) NOT NULL,
  `slug` varchar(255) COLLATE utf8mb4_unicode_ci NOT NULL,
  `label` varchar(255) COLLATE utf8mb4_unicode_ci NOT NULL
) ENGINE=InnoDB DEFAULT CHARSET=utf8mb4 COLLATE=utf8mb4_unicode_ci;

--
-- Дамп данных таблицы `type`
--

INSERT INTO `type` (`id`, `slug`, `label`) VALUES
(1, 'face', 'Лицо');

--
-- Индексы сохранённых таблиц
--

--
-- Индексы таблицы `ava`
--
ALTER TABLE `ava`
  ADD PRIMARY KEY (`id`);

--
-- Индексы таблицы `figure`
--
ALTER TABLE `figure`
  ADD PRIMARY KEY (`id`);

--
-- Индексы таблицы `fill`
--
ALTER TABLE `fill`
  ADD PRIMARY KEY (`id`);

--
-- Индексы таблицы `path`
--
ALTER TABLE `path`
  ADD PRIMARY KEY (`id`);

--
-- Индексы таблицы `type`
--
ALTER TABLE `type`
  ADD PRIMARY KEY (`id`);

--
-- AUTO_INCREMENT для сохранённых таблиц
--

--
-- AUTO_INCREMENT для таблицы `figure`
--
ALTER TABLE `figure`
  MODIFY `id` int(11) NOT NULL AUTO_INCREMENT, AUTO_INCREMENT=3;
--
-- AUTO_INCREMENT для таблицы `fill`
--
ALTER TABLE `fill`
  MODIFY `id` int(11) NOT NULL AUTO_INCREMENT;
--
-- AUTO_INCREMENT для таблицы `path`
--
ALTER TABLE `path`
  MODIFY `id` int(11) NOT NULL AUTO_INCREMENT;
--
-- AUTO_INCREMENT для таблицы `type`
--
ALTER TABLE `type`
  MODIFY `id` int(11) NOT NULL AUTO_INCREMENT, AUTO_INCREMENT=2;
/*!40101 SET CHARACTER_SET_CLIENT=@OLD_CHARACTER_SET_CLIENT */;
/*!40101 SET CHARACTER_SET_RESULTS=@OLD_CHARACTER_SET_RESULTS */;
/*!40101 SET COLLATION_CONNECTION=@OLD_COLLATION_CONNECTION */;
