-- Lists all genres of a show
SELECT g.name FROM tv_genres AS g
INNER JOIN tv_show_genres AS sg
ON g.id = sg.genre_id
INNER JOIN tv_shows AS s
ON s.id = sg.show_id
WHERE s.title = Dexter
ORDER BY g.name ASC;
