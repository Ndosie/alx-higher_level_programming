-- Lists all shows without genre
SELECT ts.title, tg.genre_id
FROM tv_shows AS ts LEFT JOIN tv_show_genres AS tg
ON ts.id = tg.show_id
WHERE tg.genre_id IS NULL
ORDER BY ts.title ASC, tg.genre_id ASC;
