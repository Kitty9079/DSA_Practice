WITH cte AS(
    SELECT
        Name ,
        Grade,
        Marks
    FROM Students
    LEFT JOIN Grades
        ON Students.marks BETWEEN Grades.Min_Mark AND Grades.Max_Mark
)

SELECT 
    CASE WHEN Grade BETWEEN 8 AND 10 THEN NAME
    ELSE NULL 
    END Nome ,
    Grade,
    Marks 
FROM cte 
ORDER BY Grade DESC,
    CASE
        WHEN Grade >= 8 THEN Nome 
        END ASC ;