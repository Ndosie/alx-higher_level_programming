-- Lists shows contained in a database
SELECT ts.title, tg.genre_id
FROM tv_shows AS ts, tv_show_genres AS tg
WHERE ts.id = tg.show_id
ORDER BY ts.title ASC, tg.genre_id ASC;
