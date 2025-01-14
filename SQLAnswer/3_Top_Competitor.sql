SELECT h.hacker_id, h.name 
FROM Hackers h
JOIN (
    SELECT s.hacker_id, count(*) AS full_score_count
    FROM Submissions s
    JOIN Challenges c ON c.challenge_id = s.challenge_id
    JOIN Difficulty d ON d.difficulty_level = c.difficulty_level
    WHERE s.score = d.score 
    GROUP BY s.hacker_id 
    HAVING COUNT(*) > 1 
    ) AS fs ON h.hacker_id = fs.hacker_id 
ORDER BY fs.full_score_count DESC,
         h.hacker_id ASC ;